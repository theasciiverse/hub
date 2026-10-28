**EIGHT WORMS. NO DESTINATION. NO HURRY.**

Eight worms crawl across the screen, each in its own colour and character, each with a head that looks different from its body. They turn at random, slide along the edges and cross each other's paths, and the ground behind them is wiped clean as they go. Nobody steers. Nobody wins. They just keep going, as they have on Unix screens since October 1980.

Leave them crawling on a spare terminal, or give them something to eat: from a terminal, `worms -f` covers the screen with WORM letters for them to graze on.

## Controls

- **Any key**: quit

## Options

From a terminal, `worms` takes more: `-n` sets the number of worms,
`-l 10` or `-l 5-40` their length, `-r` random lengths, `-t` a trail of
dots, `-f` a field of WORM letters for them to eat, `-d` the pause between
moves in milliseconds, and `-C` and `-H` colour and heads (Asciiverse
starts it with `-C -H -n 8`).

## History

Eric P. Scott wrote worms at Caltech High Energy Physics in October
1980, a Unix version of the DEC-2136 program of the same name, and it
has shipped with BSD Unix ever since. This edition quits on any key. It
is part of BSD Games in the Asciiverse catalog.

## Credits

- worms: Eric P. Scott, from [NetBSD's source tree](https://github.com/NetBSD/src/tree/trunk/games/worms)
- License: BSD-3-Clause, copyright The Regents of the University of California
