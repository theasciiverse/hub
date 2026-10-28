#!/usr/bin/env python3
"""Record one MUD's greeting as casts/<id>.cast at the catalog's 100x30
(hub/RECORDING.md), through dev/mud_greet.py, under asciinema 3.
Usage: record_mud.py id host port [tls|plain] [seconds] [encoding]
MUD_COLS=80 records narrower, for DOS ANSI art drawn to wrap at 80 columns."""
import os, pty, sys, time, select, struct, fcntl, termios
here = os.path.dirname(os.path.abspath(__file__))
mid, host, port = sys.argv[1:4]
tls = sys.argv[4] if len(sys.argv) > 4 else "plain"
secs = sys.argv[5] if len(sys.argv) > 5 else "12"
enc = sys.argv[6] if len(sys.argv) > 6 else ""
out = os.path.join(here, "..", "casts", f"{mid}.cast")
env = dict(os.environ, TERM="xterm-256color", COLORTERM="truecolor", LANG="C.UTF-8")
pid, fd = pty.fork()
if pid == 0:
    os.execvpe("asciinema", ["asciinema", "rec", "--overwrite", "-q", "-i", "2", "--capture-env", "TERM,COLORTERM,LANG",
        "-c", f"python3 -I {here}/mud_greet.py {host} {port} {tls} {secs} {enc}".strip(), out], env)
fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", 30, int(os.environ.get("MUD_COLS", 100)), 0, 0))
while True:
    r, _, _ = select.select([fd], [], [], 0.2)
    if r:
        try:
            if not os.read(fd, 65536): break
        except OSError: break
    if os.waitpid(pid, os.WNOHANG)[0]: break
