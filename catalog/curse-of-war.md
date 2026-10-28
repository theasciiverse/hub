**YOU DON'T COMMAND SOLDIERS. YOU COMMAND A NATION.**

Four countries start in the corners of a map of hexagons. You rule the green one. The other three want the whole map, and so do you.

There are no units to click on here. Your people are your army. They grow in your villages, towns and fortresses and spill out over the grassland, up to 499 to a tile, and where two countries' people meet, they fight. Plant a flag and your crowds drift toward it. Push a line of flags into enemy land and you have a front, fought over tile by tile. Surround a gold mine to take it, spend the gold on new cities, and outgrow them. Lose a city under siege and it burns down a size: fortress to town, town to village, and a village to nothing.

- **Real time, and fast**: speed it up, slow it down or pause while the fronts move.
- **Rivals with character**: every computer ruler fights in its own way.
- **Maps your way**: rectangles, rhombuses, or hexagons with room for six countries, any size, and a seed to replay the same map.
- **Friends on your local network**: one machine hosts, the others join.
- **Gentle to brutal**: five difficulty levels, and a choice of how fair the start is.

Start gently with `curseofwar -i4 -q1 -dee`: the strongest starting position against the easiest opponents.

**Plant your flag. Hold the line.**

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
