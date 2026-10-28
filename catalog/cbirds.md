**EIGHT HUNDRED BIRDS. THREE RULES. ONE FLOCK.**

A flock of birds in your terminal, drawn in braille: eight hundred boids
that keep their distance, match their neighbours and stay together, the
rules Craig Reynolds published in 1987. It opens by writing BOIDS in birds,
lets go, and flocks. Move the pointer into the flock and it scatters; leave
it alone for a minute and it starts moving its own sliders.

## Controls

- **q**: the flock flies off the top, and cbirds quits
- **h**: the panel of sliders: **b**/**B** boundary, **s**/**S**
  separation, **a**/**A** alignment, **t**/**T** turning, **p**/**P**
  perception, **v**/**V** speed (lowercase lowers, uppercase raises)
- **Space**: pause, **.** one frame
- **+** and **-**: more birds, fewer; **k** and **K**: a hawk more, one fewer
- **e**: tails; **Tab**: next preset; **0**: back to the defaults
- **Mouse**: the pointer scatters the flock

## Options

From a terminal: `--preset murmuration` for the starling look, `--hawks 2
--color ice`, `--flocks 3 --color ember`, `--3d` for a murmuration in three
dimensions, `--clock` or `--say "back in five"` to have the flock write,
`--matrix` for raining birds, `--render kitty` for real sprites in Kitty
or Ghostty, and `--screensaver` to quit on any key. `cbirds --help` lists
them all.

## Credits

- cbirds: [Alessandro Palliccia](https://github.com/clainstone/cbirds), after
  Craig Reynolds' boids (SIGGRAPH 1987)
- Asciiverse edition: upstream's program unchanged, built static for
  Linux and for macOS
- License: MIT
