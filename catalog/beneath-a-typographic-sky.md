**UNION CITY. REBUILT IN TYPE.**

Robert Foster grew up in the Gap, the wasteland outside Union City, until security men came for him and his helicopter came down in the city. Now he is on the run in a vast city of soaring tower blocks, with only Joey, a talking robot circuit board, for company, and he wants to know why they took him. The answers are somewhere in the towers, and somewhere inside LINC, the computer that runs the city.

This is Revolution Software's Beneath a Steel Sky, the whole game, in your terminal. Every pixel of Dave Gibbons' art becomes a dot of a Braille character, so Union City is rebuilt out of type, and everything the game says is set in your terminal's own font. The speech, effects and AdLib music play as they did in 1994.

- **The whole game**, from the factory where Foster lands to the very end
- **Dave Gibbons' art in Braille dots**, or in half blocks or quadrants: F2
  switches
- **Full speech and the AdLib soundtrack**, as in 1994
- **Subtitles in seven languages**, picked up from your system

## Controls

- **Left click**: look at something
- **Right click**: use it, take it, talk, or walk through an exit
- **Pointer to the top edge**: the inventory; click an item to hold it, then right click it onto something
- **F5** or **q**: options, save, restore, subtitles and speech, language, restart, quit
- **Esc**: skip the intro or a cut scene; **.** skips a line of speech
- **p**: pause; **F2**: Braille, half blocks or quadrants; **Ctrl+F**: fast mode

The intro plays the first time; after that a start menu offers Continue, which picks up where you quit. Saves go to `~/.local/share/typographic-sky`.

## Options

- `--skip-intro`: start a new game at once
- `--mute`: no sound
- `--game-font`: the game's own pixel fonts instead of type, for very large terminals

The game starts in your system's language when it has it (English, German, French, Swedish, Italian, Portuguese or Spanish subtitles; the speech is English) and remembers the one you choose in F5.

## History

Revolution Software released Beneath a Steel Sky in 1994 for MS-DOS and the Amiga, and gave it away as freeware in 2003. ScummVM brought it to modern systems from Revolution's own source. This edition runs the unmodified CD version's data in a Rust port of ScummVM's engine and draws it in a terminal.

## Credits

- Beneath a Steel Sky: Revolution Software, 1994; directed by Charles Cecil; art and characters by Dave Gibbons; written and scored by Dave Cummins; programmed by David Sykes, Tony Warriner and James Long
- Game content (C) Revolution Software Ltd, freeware: free to share, never to be sold
- The sky engine: Robert Goeffringmann, Oliver Kiehl, Joost Peters and the ScummVM team (GPL-3.0-or-later)
- AdLib music: Nuked-OPL3 by Nuke.YKT, in Tony Gies' Rust port (LGPL-2.1-or-later)
- Asciiverse edition: Asciiverse, GPL-3.0-or-later
