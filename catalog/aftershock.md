**THE GROUND IS STILL SHAKING. SOMETHING CAME UP WITH IT.**

Four runes hold the gate shut: the Rune of Blood, the Rune of Bone, the Rune of Mind and the Rune of Soul. Someone has scattered them across worlds that should never have been joined, and every one of those worlds has woken up.

You start in a hall of gates and walk into the dark. Through one: a sunken base where Chosen soldiers patrol the catwalks and Cyberhunters hum behind blast doors. Through another: a feudal castle where Carcosan Knights wait in the courtyard and Moon Rats leap from the rafters. Further on are flooded caves where Spine Eels circle in black water, Greek ruins split open, a reactor running too hot, a forest made of steel and a citadel of copper with something roaming its halls. Deathless Cultists shamble out of the crypts, Biohell Warriors charge, the Hollow lumber out of the deep, and the Servants of Nyarlathotep send their fire after you around corners.

Five episodes and close to thirty levels, every one with its doors, lifts, buttons, traps and secrets. Eight weapons, from a shotgun to a lightning gun. Thirteen arenas besides.

It is all drawn in your terminal, two pixels to a character in full colour, at whatever size your window is. Your health, armour and ammunition sit on a status line of real text, and the menus, messages and console are text too, so you can read them at a glance at 80 by 24.

**Find the runes. Keep moving.**

## Controls

- **Arrow keys** or **W A S D**: walk and turn; **,** and **.** step sideways
- **Ctrl**, **F** or **Enter**: fire; **Space**: jump, swim up
- **Shift**: walk slowly (you always run)
- **Page Up** and **Page Down**: look up and down; **End** or **V** looks ahead again
- **1** to **8**: weapons; **Q**, **[** and **]**: next and previous
- **Tab**: kills, secrets and time; **P**: pause
- **F6** and **F9**: quick save and load; **Esc**: menu; **F10**: quit

Your shots find what you face, so there is little need to aim up or down. It plays best in a terminal that reports key releases, such as Ghostty, kitty, WezTerm or foot.

## Options

- `--no-sound`: play silently
- `--video=sextant`: a finer picture, six pixels to a character; Options, Video, Picture switches it while you play

Settings and saved games are kept in `~/.local/state/aftershock`.

## History

In 1996 a small company in Texas released a first-person shooter whose engine drew true three-dimensional worlds in software, pixel by pixel, on an ordinary PC. Three years later id Software gave that engine's source to everyone under the GPL. Kevin Shanahan's TyrQuake kept its software renderer alive and sharp for two decades, and the libretro project made it a core any frontend could drive.

The worlds it drew were never free. In 2019 a group of artists, mappers and programmers set out to change that, and the LibreQuake project built a whole game from nothing: new monsters, new weapons, new sounds, new music and five episodes of new levels, free for anyone to play and share.

In 2026 Raul Dias turned the engine's pictures into characters with OmaQuake. Aftershock takes the last step: the free world in the free engine, in the terminal, with a picture made of half blocks and a status line, menus and messages made of words.

## Credits

- Engine: TyrQuake, Kevin Shanahan and contributors, from id Software's GPL source release; the libretro tyrquake core
- Terminal frontend: Aftershock's own, after OmaQuake by Raul Dias
- World, art, maps, sounds and music: the LibreQuake project and its contributors
- License: GPL-2.0-or-later (the program; GPL-3.0-or-later for a build with chafa), BSD-3-Clause (LibreQuake's art, maps, sounds and music)
