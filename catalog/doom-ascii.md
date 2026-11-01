**THE ENGINE THAT DEFINED THE FIRST-PERSON SHOOTER, IN YOUR TERMINAL.**

The engine of the 1993 first-person shooter runs in your terminal: the real thing, with its doors, lifts, secrets and monsters, drawn in full colour two pixels to a character, and with its music and sound effects. It plays **Freedoom**, a complete free replacement for the original game's levels, monsters, sounds and music, so there is nothing else to buy or find.

Two games come with it:

- **Freedoom: Phase 1**: four episodes in the style of the original
- **Freedoom: Phase 2**: one long campaign of 32 levels, with the double-barrelled shotgun

The bigger your terminal window, the sharper the picture. It plays best in a terminal that reports key releases, such as Ghostty, kitty, WezTerm or foot: movement is then exact, and Ctrl, Shift and Alt work as fire, run and strafe.

## Controls

- **Arrow keys**: move and turn
- **,** and **.**: strafe left and right
- **Space**: fire; **E**: use doors and switches; **]**: run
- **1** to **7**: weapons; **Tab**: map
- **Esc**: menu, to load, save and quit
- Gamepad, on Linux: left stick to move and strafe, right stick to turn,
  **RT** fires, **LT** runs, **A** uses doors and switches, **LB** and
  **RB** change weapons, **Back** shows the map, **Start** opens the menu;
  in menus the d-pad or stick moves, **A** chooses and **B** goes back.
  A game saved from the pad is named after its level

## Options

- `-iwad freedoom2.wad`: play Phase 2
- `-skill 1` to `-skill 5`, `-warp E M` (or `-warp M` in Phase 2): start where you like
- `-nosound`, `-nomusic`: play quietly
- `-chars ascii`, `-chars block` or `-chars braille`: doom-ascii's own looks

Settings and saved games are kept in `~/.local/share/doom-ascii`, where `.default.cfg` holds the key bindings.

## History

id Software released its engine's source in 1997. Chocolate Doom keeps it faithful to the original, doomgeneric made it easy to port, and doom-ascii brought it to the terminal. This edition adds the sound effects and the music, played through an emulated OPL synthesiser as a 1990s sound card would, exact key releases, gamepads, and the half-block picture.

## Credits

- doom-ascii: Wojciech Graj
- Engine: id Software, Chocolate Doom (Simon Howard and contributors), doomgeneric (ozkl)
- OPL3 emulation: Nuked OPL3, Alexey Khokholov
- Freedoom: the Freedoom project
- License: GPL-2.0-or-later (the engine), BSD-3-Clause (Freedoom)
