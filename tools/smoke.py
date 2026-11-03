#!/usr/bin/env python3
"""Smoke test: installs every title for this machine through av and starts
it, to show that it runs here. Made for GitHub's macOS, Windows and Linux
runners (.github/workflows/smoke.yml), and runs the same anywhere av does.

For each title the catalog offers for this machine's platform:

1. `av install <id>` must succeed (download, checksum, unpack);
2. `av play <id>` runs in a pseudo-terminal of at least 100x30 (more when
   the title asks for it) for a few seconds. It passes when it is still
   running then, or has exited cleanly, and has drawn something; it fails
   when it exits with an error or prints a loader error (a missing
   library, a binary for the wrong processor);
3. the title is stopped and uninstalled again.

MUDs (a connection, not a program) are left out. The result is a table on
stdout, also written to the job summary in GitHub Actions; the exit code is
1 when any title failed.

  python3 tools/smoke.py                 every title for this machine
  python3 tools/smoke.py tessera zork1   just these
Needs av on PATH. AV_CATALOG_URL works as for av itself. On Windows it
needs pywinpty (pip install pywinpty) for the pseudo-terminal.
"""
import json, os, platform, re, shutil, subprocess, sys, threading, time, urllib.request

RUN_FOR = float(os.environ.get("SMOKE_SECONDS", "4"))
CATALOG = os.environ.get("AV_CATALOG_URL", "https://asciiverse.sh/data/catalog.json")
WINDOWS = sys.platform == "win32"
LOADER = re.compile(
    r"error while loading shared libraries|cannot open shared object|GLIBC_[0-9.]+' not found"
    r"|dyld(\[\d+\])?: |Library not loaded|Bad CPU type|cannot execute binary|Exec format error"
    r"|is not a valid Win32 application|0xc000007b|was not found\. Reinstalling", re.I)
ANSI = re.compile(rb"\x1b\[[0-9;?<>=]*[ -/]*[@-~]|\x1b\][^\x07\x1b]*(\x07|\x1b\\)|\x1b[()][0-9A-Za-z]|\x1b.")


def targets():
    """Platform keys this machine runs, best first."""
    arch = {"amd64": "x86_64", "x86_64": "x86_64", "arm64": "aarch64", "aarch64": "aarch64"}[platform.machine().lower()]
    if sys.platform == "darwin":
        return [f"{arch}-apple-darwin"]
    if WINDOWS:
        return [f"{arch}-pc-windows-msvc", f"{arch}-pc-windows-gnu"]
    return [f"{arch}-unknown-linux-musl", f"{arch}-unknown-linux-gnu"]


def run_in_pty(cmd, cols, rows, seconds):
    """(still running, exit code or None, output bytes)."""
    if WINDOWS:
        from winpty import PtyProcess  # pywinpty
        p = PtyProcess.spawn(subprocess.list2cmdline(cmd), dimensions=(rows, cols))
        chunks = []

        def reader():
            while True:
                try:
                    chunks.append(p.read(4096).encode("utf-8", "replace"))
                except EOFError:
                    return
                except Exception:
                    return
        threading.Thread(target=reader, daemon=True).start()
        end = time.time() + seconds
        while time.time() < end and p.isalive():
            time.sleep(0.1)
        alive = p.isalive()
        code = None if alive else p.exitstatus
        if alive:
            p.terminate(force=True)
        time.sleep(0.3)
        return alive, code, b"".join(chunks)

    import fcntl, pty, select, signal, struct, termios
    pid, fd = pty.fork()
    if pid == 0:
        os.environ.update(TERM="xterm-256color", COLORTERM="truecolor", LANG="C.UTF-8")
        try:
            os.execvp(cmd[0], cmd)
        finally:
            os._exit(127)
    fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", rows, cols, 0, 0))
    out, end, code = [], time.time() + seconds, None
    while time.time() < end:
        r, _, _ = select.select([fd], [], [], 0.1)
        if r:
            try:
                data = os.read(fd, 65536)
            except OSError:
                data = b""
            if data:
                out.append(data)
                # answer a cursor position query, which some curses titles wait on
                if b"\x1b[6n" in data:
                    os.write(fd, b"\x1b[1;1R")
        done, status = os.waitpid(pid, os.WNOHANG)
        if done:
            code = os.waitstatus_to_exitcode(status)
            break
    alive = code is None
    if alive:
        for sig in (signal.SIGTERM, signal.SIGKILL):
            try:
                os.killpg(os.getpgid(pid), sig)
            except (ProcessLookupError, PermissionError):
                try:
                    os.kill(pid, sig)
                except ProcessLookupError:
                    pass
            time.sleep(0.5)
            if os.waitpid(pid, os.WNOHANG)[0]:
                break
    try:
        while select.select([fd], [], [], 0)[0]:
            data = os.read(fd, 65536)
            if not data:
                break
            out.append(data)
    except OSError:
        pass
    os.close(fd)
    return alive, code, b"".join(out)


def visible(output):
    return len(re.sub(rb"\s", b"", ANSI.sub(b"", output)))


def main():
    av = shutil.which("av")
    if not av:
        sys.exit("av is not on PATH")
    with urllib.request.urlopen(CATALOG, timeout=60) as r:
        catalog = json.load(r)
    mine = targets()
    wanted = set(sys.argv[1:])
    titles = [t for id_, t in sorted(catalog["titles"].items())
              if t.get("kind") != "mud" and (not wanted or id_ in wanted)
              and any(k in (t.get("platforms") or {}) for k in mine)]
    print(f"{len(titles)} titles for {', '.join(mine)}, av at {av}", flush=True)

    results = []
    for t in titles:
        id_ = t["id"]
        size = t.get("min_terminal") or {}
        cols, rows = max(100, size.get("cols", 0)), max(30, size.get("rows", 0))
        started = time.time()
        inst = subprocess.run([av, "install", id_], capture_output=True, text=True,
                              encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL)
        if inst.returncode:
            msg = (inst.stderr or inst.stdout).strip().splitlines()[-1:] or ["?"]
            results.append((id_, "FAIL", f"install: {msg[0][:120]}"))
        else:
            alive, code, out = run_in_pty([av, "play", id_], cols, rows, RUN_FOR)
            text = ANSI.sub(b"", out).decode("utf-8", "replace")
            if m := LOADER.search(text):
                line = next((l for l in text.splitlines() if m.group(0) in l), m.group(0))
                results.append((id_, "FAIL", f"loader: {line.strip()[:120]}"))
            elif not alive and code != 0:
                tail = " ".join(text.split())[-120:]
                results.append((id_, "FAIL", f"exit {code}: {tail}"))
            elif visible(out) < 10:
                results.append((id_, "FAIL", "drew nothing" + ("" if alive else f" (exit {code})")))
            else:
                results.append((id_, "ok", "running" if alive else "exited 0"))
            subprocess.run([av, "uninstall", id_], capture_output=True, stdin=subprocess.DEVNULL)
        print(f"{results[-1][1]:4}  {id_:28} {results[-1][2]}  ({time.time() - started:.0f}s)", flush=True)

    failed = [r for r in results if r[1] != "ok"]
    print(f"\n{len(results) - len(failed)} of {len(results)} ran on {mine[0]}")
    if summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(summary, "a", encoding="utf-8") as f:
            f.write(f"### {mine[0]}: {len(results) - len(failed)} of {len(results)} ran\n\n")
            if failed:
                f.write("| title | what happened |\n|---|---|\n")
                for id_, _, why in failed:
                    f.write(f"| {id_} | {why.replace('|', '/')} |\n")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
