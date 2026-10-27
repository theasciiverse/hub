A fast real-time strategy game on a map of hexagons, where you never
command a single soldier. Four countries start in the corners; you rule the
green one and win by conquering the whole map.

Your people are your army. They grow in villages, towns and fortresses and
spill out over the grassland around them. Plant flags and they gather
there; push a line of flags into enemy land and your crowds will fight
theirs tile by tile. Surround a gold mine to own it, and spend the gold on
new cities. The game plays out like a war of fronts and supply lines, and
the computer rulers each fight with their own personality.

Start gently with `curseofwar -i4 -q1 -dee`: the strongest starting
position against the easiest opponents.

## Controls

- **Arrow keys** or **h j k l**: move the cursor
- **Space**: add or remove a flag
- **r** or **v**: build a village, then grow it into a town and a fortress (160, 240 and 320 gold)
- **x**: remove all your flags
- **c**: remove half of your flags
- **f** and **s**: speed up and slow down
- **p**: pause
- **q**: quit, after confirming with **y**

Keys are lowercase; with Caps Lock on only **q** works.

Your flags show as a white **P** on the right of a tile, computer flags as
an **x** on the left. Dots and colons on grassland show how many people live
there.

## Options

- `-W N`, `-H N`: map width and height (default 21)
- `-S rect`, `-S rhombus`, `-S hex`: map shape; hex maps hold six countries
- `-l N`: number of countries
- `-i 0` to `-i 4`: how unequal the starting positions are
- `-q N`: start in the best (1) or a worse position
- `-r`: completely random start
- `-d ee`, `e`, `n`, `h`, `hh`: computer difficulty, easiest to hardest
- `-s sss` to `-s fff`: game speed
- `-R N`: map seed, to replay the same map
- `-T`: show the population timeline
- `-E N`: host a game for N players over the network (UDP port 19140)
- `-C address`: join a hosted game

## History

Alexey Nikolaev released Curse of War in 2013 and developed it in the open
on GitHub, where others contributed fixes until 2021; Debian, Ubuntu and
other distributions have packaged it ever since. It also has an SDL
graphical version, which is not part of this edition.

## Credits

- Game: [Alexey Nikolaev](https://a-nikolaev.github.io/curseofwar/), with contributions from the [curseofwar](https://github.com/a-nikolaev/curseofwar) community
- Asciiverse edition: Asciiverse
- License: GPL-3.0-or-later
