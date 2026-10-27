Fluid in plain characters. Columns of water collapse and slosh, tea pours
out of a cup, water runs down rice terraces and through funnels, and an
hourglass empties, all computed live by a real fluid simulation and drawn
with slashes, dots and hashes, coloured by how dense the fluid is. The
first scene is the program's own source code, which melts into a puddle.

There are eighteen scenes, each playing for as long as it stays lively,
round and round. Warning: the picture changes quickly and may flicker on
some terminals.

## Controls

- **Any key**: quit

## Options

From a terminal, `ascii-fluid -m` shows the original black-and-white
version, `-t 20` gives every scene 20 seconds, `-l` lists the scenes, and
naming scenes plays only those (`ascii-fluid tanada clock`). A text file
of your own works as a scene too: `#` is a wall, any other character is
water.

## History

Yusuke Endoh wrote this for the International Obfuscated C Code Contest
in 2012, where it won "Most complex ASCII fluid". The whole simulator,
smoothed-particle hydrodynamics done in complex numbers, fits in 23
lines of C. The colour version came after the contest, at
the judges' suggestion. Asciiverse runs the entry as the IOCCC publishes
it, inside a small launcher that plays the scenes in turn and quits
on any key.

## Credits

- 2012/endoh1 by [Yusuke Endoh](https://github.com/mame/), from the [IOCCC](https://www.ioccc.org/2012/endoh1/index.html); clock scene by HAMANO Tsukasa, other scenes by the author and the IOCCC judges
- Copyright Landon Curt Noll, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) ([the IOCCC's summary](https://www.ioccc.org/license.html))
- Asciiverse edition: the launcher, scenes in turn, any key quits; changes listed in PATCHES.md
