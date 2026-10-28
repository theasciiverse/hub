**THIS PROGRAM'S SOURCE CODE MELTS.**

It opens with its own C source on the screen. Then gravity switches on, and
the code slumps, slides and splashes into a puddle at the bottom of your
terminal.

That is Yusuke Endoh's ASCII Fluid: a real fluid simulation squeezed into a
few lines of C for the International Obfuscated C Code Contest. After the
source, the show goes on. A column of water collapses and sloshes, the
program "pours you a cup of tea", water runs down terraced rice fields and
through funnels, a water clock drains. Every frame is computed live and
drawn with slashes, dots and hashes, coloured by how dense the water is.

The contest judges opened their remarks with a round of Jeopardy: "A: An
obfuscated program that deals with complex numbers and produces animated
ASCII graphics. Q: What is a Mandelbrot simulator? Bzzzt!"

- **Eighteen scenes** in turn, each playing for as long as it stays lively
- **Bring your own water**: any text file is a scene, with `#` for a wall
  and anything else for water
- **Colour**, the version the author made at the judges' suggestion, or
  the original black and white

Warning: the picture changes quickly and may flicker on some terminals.

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
