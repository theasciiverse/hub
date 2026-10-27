The classic starfield: you are flying forward through space, and stars
stream out from the centre of the screen, faint and grey far away,
brightening to white as they rush past the edges. Below the sky sits a
small console with a frame counter and a command line, in the style of an
IRC client.

## Controls

- **Any key**: quit (while the command line is empty)
- **/**: start a command, then **Enter** to run it
- **Up** and **Down**: earlier commands
- **Esc** or **Ctrl+C**: quit at any time

## Commands

- `/sleep 10000`: the pause between frames in microseconds; higher is slower
- `/char *`: draw the stars with another character
- `/colormode mono` or `/colormode 256`: plain or shaded stars
- `/quit`: quit

## Options

From a terminal, `nstars -s '*'` sets the star character and `-c 256` (how
Asciiverse starts it) shades the stars; `-c mono` draws them plain.

## Credits

- stars and nstars: [Philip J Freeman](https://github.com/ph1l/stars)
- Asciiverse edition: any key quits, a memory fix and a Windows
  build
- License: GPL-3.0-or-later
