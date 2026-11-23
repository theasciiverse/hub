#!/usr/bin/env python3
"""Cuts the raw av session (dev/record_av_demo.py) into the Home banner's
reel: only the stretches where a search is complete and its title shows,
each opening with a full redraw of the screen at that moment, so the cuts
are clean although av only redraws what changes. Between searches the full
list (0verkill first) shows; that is cut out (David, 2026-11-23). Every
kept frame is then checked: if 0verkill shows anywhere, nothing is written.

  dev/cut_av_demo.py RAW.cast casts/av-demo.cast

Needs pyte (pip install pyte, in a virtual environment).
"""
import json, re, sys
import pyte

QUERIES = ["en prise", "ambassador", "angband", "bricks"]
SETTLE = 0.5      # seconds after a query is complete before keeping
TRIM_END = 0.15   # seconds dropped before the Esc that clears it
QUIT = 1.3        # seconds before the end the quit begins
SEARCH_ROW = 3

NAMES = {'black': 0, 'red': 1, 'green': 2, 'brown': 3, 'yellow': 3, 'blue': 4, 'magenta': 5, 'cyan': 6, 'white': 7}


def col(c, fg):
    if c == 'default':
        return '39' if fg else '49'
    if c in NAMES:
        return str((30 if fg else 40) + NAMES[c])
    if c.startswith('bright'):
        return str((90 if fg else 100) + NAMES.get(c[6:], 7))
    if len(c) == 6:
        return f"{'38' if fg else '48'};2;{int(c[0:2], 16)};{int(c[2:4], 16)};{int(c[4:6], 16)}"
    return '39' if fg else '49'


def snapshot(scr):
    out = ['\x1b[?25l\x1b[2J']
    for y in range(scr.lines):
        out.append(f'\x1b[{y + 1};1H')
        last = None
        for x in range(scr.columns):
            ch = scr.buffer[y][x]
            sgr = ';'.join(['0'] + (['1'] if ch.bold else []) + (['7'] if ch.reverse else []) + [col(ch.fg, True), col(ch.bg, False)])
            if sgr != last:
                out.append(f'\x1b[{sgr}m')
                last = sgr
            out.append(ch.data or ' ')
    out.append('\x1b[0m')
    return ''.join(out)


def query_shown(scr):
    """The complete query the search box shows, if it is one of ours."""
    # the text between "/ " and the search cursor, exactly one of ours
    m = re.search(r"/ ([^▏│]*)▏", scr.display[SEARCH_ROW])
    q = m.group(1).strip() if m else None
    return q if q in QUERIES else None


def main():
    raw, out = sys.argv[1], sys.argv[2]
    lines = open(raw).read().splitlines()
    head = json.loads(lines[0])
    events = [json.loads(l) for l in lines[1:]]
    cols, rows = head['term']['cols'], head['term']['rows']

    # pass 1: when each query is complete on screen
    scr = pyte.Screen(cols, rows)
    st = pyte.Stream(scr)
    t, spans, cur = 0.0, {}, None
    for d, k, data in events:
        t += d
        if k == 'o':
            st.feed(data)
        q = query_shown(scr)
        if q != cur:
            if cur:
                spans[cur][1] = t
            if q:
                spans.setdefault(q, [t, t])
                spans[q][0] = spans[q][0] if spans[q][1] > spans[q][0] else t
            cur = q
    # the last search is never cleared: it lasts until the quit (Ctrl-C,
    # then y to confirm, 1.1 s before the recording ends)
    if cur:
        spans[cur][1] = t - QUIT
    keep = []
    for q in QUERIES:
        if q not in spans:
            sys.exit(f"the raw session never shows the search {q!r}")
        a, b = spans[q]
        keep.append((a + SETTLE, b - TRIM_END))
    print("kept:", ", ".join(f"{q} {a:.1f}-{b:.1f}s" for q, (a, b) in zip(QUERIES, keep)))

    # pass 2: write the kept stretches, each opening with a full redraw
    scr = pyte.Screen(cols, rows)
    st = pyte.Stream(scr)
    t, outev, seg, prev = 0.0, [], 0, None
    for d, k, data in events:
        t += d
        if k == 'o':
            st.feed(data)
        if seg >= len(keep):
            break
        a, b = keep[seg]
        if prev is None and t >= a:
            outev.append([0.0 if not outev else 0.05, 'o', snapshot(scr)])
            prev = t
            continue
        if prev is not None:
            if t > b:
                seg += 1
                prev = None
                continue
            if k == 'o':
                outev.append([round(t - prev, 6), 'o', data])
                prev = t

    # check: replay what was written, every frame free of 0verkill
    scr = pyte.Screen(cols, rows)
    st = pyte.Stream(scr)
    for i, (d, k, data) in enumerate(outev):
        st.feed(data)
        if any('0verkill' in r for r in scr.display):
            sys.exit(f"0verkill shows in the cut at event {i}; nothing written")
    with open(out, 'w') as f:
        f.write(json.dumps(head) + '\n')
        for e in outev:
            f.write(json.dumps(e) + '\n')
    print(f"{out}: {len(outev)} events, {sum(e[0] for e in outev):.1f} s, no 0verkill")


if __name__ == '__main__':
    main()
