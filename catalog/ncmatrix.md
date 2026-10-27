The falling green code of The Matrix, as CMatrix has drawn it in
terminals since 1999, with one thing more: your computer's network
traffic falls in it too. Every packet sent and received since the last
moment is painted into the rain as a bold run, red for what goes out and
magenta for what comes in, so a download pours magenta down the screen
and a quiet machine rains plain green.

## Controls

- **Any key**: quit (Asciiverse starts it in screensaver mode)

## Options

From a terminal, `ncmatrix` without `-s` takes keys while it runs: `N`
turns the network display off and on, `a` asynchronous scroll, `b` and
`B` bold, `0` to `9` the speed, `! @ # $ % ^ &` the colour, `p` pause,
`q` quit. `-I wlan0` (or `en0` on a Mac, `Wi-Fi` on Windows) shows one
interface only, `-T` and `-R` change the traffic colours, `-c` uses
Japanese characters. `ncmatrix -h` lists them all.

## Credits

- CMatrix: [Chris Allegretta, Abishek V Ashok and contributors](https://github.com/abishekvashok/cmatrix)
- Network display: Thomas Bloedorn, NCMatrix 1.0 (2005)
- Asciiverse edition: the network display carried over to CMatrix
  and fixed, traffic read on macOS and Windows too, quits cleanly
  on SIGTERM and SIGHUP
- License: GPL-3.0-or-later
