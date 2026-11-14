#!/usr/bin/env python3
"""Scripted asciicast v3 recorder for catalog previews: run a program in a
pty of a fixed size, feed it timed keys, write a .cast.

usage: castrec.py OUT.cast CWD SCRIPT -- CMD [ARGS...]
Size: CAST_COLS / CAST_ROWS environment variables (default 100x30).
SCRIPT is a ;-separated list of steps:
  w1.5              wait 1.5 s
  k<name>           send a key (up down left right enter space esc tab bs,
                    sup sdown sleft sright for Shift+arrows, or a literal char)
  r<n>:<key>:<gap>  repeat key n times with gap seconds between
  s<text>           send text literally (no ';' inside)
  m<click|right|move|up|down>,<col>,<row>  SGR mouse left click, right
                    click, pointer move or wheel at a 1-based cell
  m<press|drag|release>,<col>,<row>[,<button>]  hold a button down, move
                    with it held, let it go (button 0 left, 1 middle,
                    2 right; default 0), for programs that act while a
                    button is held

The program runs with the terminal identity of the spec (TERM=xterm-256color,
COLORTERM=truecolor, UTF-8), without variables that identify the real
terminal, with audio pointed nowhere, stderr discarded and USER/LOGNAME set to
"player", so recordings do not depend on, or show, the recording machine.
"""
import codecs, fcntl, json, os, pty, select, signal, struct, sys, termios, time

KEYS = {"up": "\x1b[A", "down": "\x1b[B", "right": "\x1b[C", "left": "\x1b[D",
        "enter": "\r", "space": " ", "esc": "\x1b", "tab": "\t", "bs": "\x7f",
        "sup": "\x1b[1;2A", "sdown": "\x1b[1;2B", "sright": "\x1b[1;2C", "sleft": "\x1b[1;2D"}

def main():
    out, cwd, script = sys.argv[1:4]
    cmd = sys.argv[sys.argv.index("--") + 1:]
    cols, rows = int(os.environ.get("CAST_COLS", 100)), int(os.environ.get("CAST_ROWS", 30))
    # drop variables that identify the real terminal, so games see only TERM
    base = {k: v for k, v in os.environ.items()
            if not k.startswith(("VTE_", "TERM_PROGRAM", "KITTY_", "WEZTERM_", "KONSOLE_", "ALACRITTY_", "WT_"))}
    env = dict(base, TERM="xterm-256color", COLORTERM="truecolor", LANG="C.UTF-8",
               LC_ALL="C.UTF-8", COLUMNS=str(cols), LINES=str(rows),
               PULSE_SERVER="unix:/nonexistent", PIPEWIRE_REMOTE="/nonexistent",
               SDL_AUDIODRIVER="dummy",
               # high-score tables print the user name; keep real names out of casts
               USER="player", LOGNAME="player")
    pid, fd = pty.fork()
    if pid == 0:
        # stderr would land in the recording (audio library warnings and the like)
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, 2)
        os.chdir(cwd)
        os.execvpe(cmd[0], cmd, env)
    fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", rows, cols, 0, 0))
    start = time.time()
    events, last = [], 0.0
    dec = codecs.getincrementaldecoder("utf-8")("replace")

    def pump(until):
        nonlocal last
        while True:
            left = until - time.time()
            if left <= 0:
                return True
            r, _, _ = select.select([fd], [], [], min(left, 0.05))
            if r:
                try:
                    data = os.read(fd, 65536)
                except OSError:
                    return False
                if not data:
                    return False
                now = time.time() - start
                events.append([round(now - last, 6), "o", dec.decode(data)])
                last = now
                # answer cursor position queries so TUIs don't stall
                if b"\x1b[6n" in data:
                    os.write(fd, b"\x1b[1;1R")
                # notcurses waits for the reply to its closing device
                # attributes query; answer as a VT220 with colour, and give
                # the text area in pixels as a nominal 10x20 cell
                if b"\x1b[14t" in data:
                    os.write(fd, f"\x1b[4;{rows * 20};{cols * 10}t".encode())
                if b"\x1b[c" in data:
                    os.write(fd, b"\x1b[?62;22c")

    alive = True
    for step in [s.strip() for s in script.split(";") if s.strip()]:
        if not alive:
            break
        kind, arg = step[0], step[1:]
        if kind == "w":
            alive = pump(time.time() + float(arg))
        elif kind == "k":
            os.write(fd, KEYS.get(arg, arg).encode())
            alive = pump(time.time() + 0.02)
        elif kind == "m":
            what, x, y, *rest = arg.split(",")
            b = int(rest[0]) if rest else 0
            if what == "press":
                os.write(fd, f"\x1b[<{b};{x};{y}M".encode())
            elif what == "drag":
                os.write(fd, f"\x1b[<{32 + b};{x};{y}M".encode())
            elif what == "release":
                os.write(fd, f"\x1b[<{b};{x};{y}m".encode())
            elif what == "click":
                os.write(fd, f"\x1b[<0;{x};{y}M\x1b[<0;{x};{y}m".encode())
            elif what == "right":
                os.write(fd, f"\x1b[<2;{x};{y}M\x1b[<2;{x};{y}m".encode())
            elif what == "move":
                os.write(fd, f"\x1b[<35;{x};{y}M".encode())
            else:
                os.write(fd, f"\x1b[<{64 if what == 'up' else 65};{x};{y}M".encode())
            alive = pump(time.time() + 0.03)
        elif kind == "s":
            os.write(fd, arg.encode())
        elif kind == "r":
            n, key, gap = arg.split(":")
            for _ in range(int(n)):
                os.write(fd, KEYS.get(key, key).encode())
                alive = pump(time.time() + float(gap))
                if not alive:
                    break
    if alive:
        pump(time.time() + 1.0)
        try:
            os.kill(pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        pump(time.time() + 0.5)
    try:
        _, status = os.waitpid(pid, 0)
    except ChildProcessError:
        status = 0
    header = {"version": 3, "term": {"cols": cols, "rows": rows, "type": "xterm-256color"},
              "timestamp": int(start), "idle_time_limit": 2,
              "env": {"TERM": "xterm-256color", "COLORTERM": "truecolor", "LANG": "C.UTF-8"}}
    with open(out, "w") as f:
        f.write(json.dumps(header) + "\n")
        for e in events:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
        f.write(json.dumps([0.1, "x", str(os.waitstatus_to_exitcode(status) if status else 0)]) + "\n")
    print(f"{out}: {len(events)} events, {time.time()-start:.1f}s, exit {status}")

main()
