Five objects turn in 3D, drawn as wireframes in dots, colons and
backticks that pack two lines of the picture into every row of text: a
cube, a pyramid, a desk, an X-wing fighter and the letters IOCCC, which
sway back and forth so they can be read. Each object tumbles about one
axis after another for a while, then the next takes its place.

## Controls

- **Any key**: quit

## Options

From a terminal, `ioccc-chaos -t 20` gives every object 20 seconds, `-l`
lists them, and naming objects shows only those (`ioccc-chaos xwing`). A
data file of your own in the entry's format works too.

## History

Alan De Smet wrote chaos for the International Obfuscated C Code Contest
in 1998, his first entry, and won "Best object orientation". Left alone,
the original turns its object about one axis; its keys turn and zoom it
by hand. Asciiverse runs the entry as the IOCCC publishes it, inside a
small launcher that sends it those keys to tumble each object, shows the
five in turn and quits on any key.

## Credits

- 1998/chaos by [Alan De Smet](http://www.highprogrammer.com/alan/), from the [IOCCC](https://www.ioccc.org/1998/chaos/index.html)
- Copyright Landon Curt Noll, licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) ([the IOCCC's summary](https://www.ioccc.org/license.html))
- Asciiverse edition: the launcher, objects in turn, tumbling, any key quits; changes listed in PATCHES.md
