"""Cuts START..END seconds out of an asciicast v3 recording. The clip opens
with one full redraw of the screen as it stood at START (from pyte), so a
program that only redraws what changes still shows a whole picture; then
the original events follow with their own timing.

  casttrim.py IN.cast OUT.cast START END

Needs pyte (pip install pyte, in a virtual environment). First used for
Brickspire's preview, cut from David playing (2026-11-23); checked by
replaying both and comparing every cell at five moments: identical."""
import json, sys, pyte
src, out, a, b = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
L = open(src).read().splitlines(); h = json.loads(L[0])
cols, rows = h['term']['cols'], h['term']['rows']
scr = pyte.Screen(cols, rows); st = pyte.Stream(scr)
NAMES = {'black':0,'red':1,'green':2,'brown':3,'yellow':3,'blue':4,'magenta':5,'cyan':6,'white':7}
def col(c, fg):
    if c == 'default': return '39' if fg else '49'
    if c in NAMES: return str((30 if fg else 40) + NAMES[c])
    if c.startswith('bright'):
        n = NAMES.get(c[6:], 7); return str((90 if fg else 100) + n)
    if len(c) == 6:
        r, g, bb = int(c[0:2],16), int(c[2:4],16), int(c[4:6],16)
        return f"{'38' if fg else '48'};2;{r};{g};{bb}"
    return '39' if fg else '49'
def snapshot():
    s = ['\x1b[?25l\x1b[2J']
    for y in range(rows):
        s.append(f'\x1b[{y+1};1H')
        last = None
        line = scr.buffer[y]
        for x in range(cols):
            ch = line[x]
            sgr = ';'.join(['0'] + (['1'] if ch.bold else []) + (['7'] if ch.reverse else []) + [col(ch.fg, True), col(ch.bg, False)])
            if sgr != last:
                s.append(f'\x1b[{sgr}m'); last = sgr
            s.append(ch.data or ' ')
    s.append('\x1b[0m')
    return ''.join(s)
t = 0.0; events = []; started = False; prev = a
for l in L[1:]:
    d, k, data = json.loads(l); t += d
    if not started:
        if k == 'o': st.feed(data)
        if t >= a:
            started = True
            events.append([0.0, 'o', snapshot()])
            prev = t
        continue
    if t > b: break
    events.append([round(t - prev, 6), k, data]); prev = t
with open(out, 'w') as f:
    f.write(json.dumps(h) + '\n')
    for e in events: f.write(json.dumps(e) + '\n')
print(f"{len(events)} events, {sum(e[0] for e in events):.1f} s")
