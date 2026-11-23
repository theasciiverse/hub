# Records casts/av-demo.cast, the av session in the Home banner: av driven
# by scripted keys under asciinema 3, at 128x40 (av's own target size),
# against the live catalog (AV_CATALOG_URL overrides it), with a throwaway
# HOME so real av state is untouched. Re-recorded 2026-11-23: four searches
# in turn, En Prise (David's pick for the opening), Ambassador of Pain,
# Angband and Brickspire, whose preview (David playing) av starts just
# before the tower turns; then cut with dev/cut_av_demo.py.
#
#   python3 dev/record_av_demo.py /tmp/av-demo-raw.cast "$(mktemp -d)"
#   dev/cut_av_demo.py /tmp/av-demo-raw.cast casts/av-demo.cast   (needs pyte)
#
# av is taken from a release build in the av folder beside hub.
import os, pty, sys, time, select, struct, fcntl, termios
out, home = sys.argv[1], sys.argv[2]
env = dict(os.environ, HOME=home, XDG_DATA_HOME=home+"/.local/share", XDG_CACHE_HOME=home+"/.cache",
           XDG_CONFIG_HOME=home+"/.config", TERM="xterm-256color", COLORTERM="truecolor", LANG="C.UTF-8",
           AV_CATALOG_URL=os.environ.get("AV_CATALOG_URL", "https://asciiverse.sh/data/catalog.json"))
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
# Each title is found by its own search, typed quickly, and held; Esc
# between searches clears it (the full list, 0verkill first, shows then,
# and is cut out afterwards by dev/cut_av_demo.py, which keeps only the
# stretches where a search is complete: David, 2026-11-23, no 0verkill and
# no jumping about the list). "bricks" leaves Brickspire only (Bricktick
# shares "brick"); av starts its preview a little before the still, so
# the floor clears and the tower turns to the Spire.
def find(words, hold):
    return [(0.1, b"/")] + [(0.1, bytes([c])) for c in words.encode()] + [(hold, None), (0.1, b"\x1b")]
# The welcome a first run shows appears after about 3 s; Space closes it
# (the arrows do not, and a letter would be eaten by it).
script = [(3.5, None), (0.1, b" ")] + find("en prise", 8.0) + find("ambassador", 6.0) + find("angband", 6.0) \
    + find("bricks", 16.0)[:-1] + [(0.3, b"\x03"), (0.8, b"y")]
for wait, key in script:
    pump(wait)
    if key: os.write(fd, key)
pump(2)
try: os.kill(pid, 15)
except ProcessLookupError: pass
