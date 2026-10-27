Patterns made of plain characters scroll down the screen without end, a
new row every tenth of a second. Faint dots and colons rise into dense
blocks of D, # and @ wherever the noise is strongest. Each run starts from
a new random seed, so the landscape is never the same twice.

Started from a terminal, CLiAni picks its pattern from options; with none
it opens a menu to choose.

- **Flavours**: Voronoi (the default here), Perlin noise and cellular
  Voronoi
- **Effects**: scrolling, raining (the pattern shows only in falling
  streaks), zig-zag, and static
- **Characters**: any ten, from faint to dense

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
