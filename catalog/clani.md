**AN ENDLESS LANDSCAPE OF NOISE. NEVER THE SAME TWICE.**

Patterns made of plain characters roll down the screen without end, a new row every tenth of a second. Faint dots and colons swell into dense banks of D, # and @ wherever the noise runs strongest, then thin out again. Every run starts from a new random seed, so the landscape you see has never been seen before.

Ryan Huth made CLiAni for "some cool scrolling patterns and other animation effects", and, in his words, "just something I work on by the side for fun". It shows.

- **Three flavours:** Voronoi (the one av starts), Perlin noise and cellular Voronoi.
- **Four effects:** scrolling, raining (the pattern shows only in falling streaks), zig-zag, and static.
- **Your own characters:** up to ten, from faint to dense.
- **Make your choice:** started from a terminal with no options, it opens a menu to pick from.

**SIT BACK AND WATCH IT ROLL.**

## Controls

- **Any key**: quit

From a terminal: `clani -f cell -e raining` picks the flavour and effect,
`-s 42` a fixed seed, `-c " .oO@"` your own characters, and `clani` on its
own opens the menu (arrows, Enter, F1 to leave). `clani -h` lists the
options.

## Credits

- CLiAni: [Ryan Huth](https://github.com/hu-ry/CLiAni), resize handling by
  Sergeant-Salz
- Asciiverse edition: options that start an animation at once, any key to
  quit, current ncurses, and bug fixes
- License: GPL-3.0-only
