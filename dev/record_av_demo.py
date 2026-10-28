# Records casts/av-demo.cast, the av session in the Home banner: av driven
# by scripted keys under asciinema 3, at 128x40 (av's own target size),
# against the dev catalog, with a throwaway HOME so real av state is untouched.
#
#   python3 -m http.server 8765 --bind 127.0.0.1      # in the site folder, for the catalog
#   python3 dev/record_av_demo.py casts/av-demo.cast "$(mktemp -d)"
#
# av is taken from a release build in the av folder beside hub.
import os, pty, sys, time, select, struct, fcntl, termios
out, home = sys.argv[1], sys.argv[2]
env = dict(os.environ, HOME=home, XDG_DATA_HOME=home+"/.local/share", XDG_CACHE_HOME=home+"/.cache",
           XDG_CONFIG_HOME=home+"/.config", TERM="xterm-256color", COLORTERM="truecolor", LANG="C.UTF-8",
           AV_CATALOG_URL="http://127.0.0.1:8765/data/catalog.json")
env["PATH"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../av/target/release") + os.pathsep + env["PATH"]
pid, fd = pty.fork()
if pid == 0:
    os.execvpe("asciinema", ["asciinema", "rec", "--overwrite", "-q", "-i", "2",
        "--capture-env", "TERM,COLORTERM,LANG", "-c", "av", out], env)
fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", 40, 128, 0, 0))
def pump(sec):
    end = time.time() + sec
    while time.time() < end:
        r, _, _ = select.select([fd], [], [], 0.05)
        if r:
            try: os.read(fd, 65536)
            except OSError: return
DOWN, UP = b"\x1b[B", b"\x1b[A"
# Every title on screen stays for at least 3.5 s: Page Down jumps ten titles
# in one move, single steps only go between neighbours, and the search is
# typed quickly so only one title shows (the second letter settles it).
PGDN = b"\x1b[6~"
script = [(5.0, None), (0.1, PGDN), (4.5, None), (0.1, DOWN), (4.0, None), (0.1, DOWN), (5.0, None),
          (0.1, b"s"), (0.15, b"l"), (6.0, None), (0.3, b"\x03"), (0.8, b"y")]
for wait, key in script:
    pump(wait)
    if key: os.write(fd, key)
pump(2)
try: os.kill(pid, 15)
except ProcessLookupError: pass
