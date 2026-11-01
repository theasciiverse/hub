**THE SAME DUNGEON. FEWER CHORES. MORE SURPRISES.**

Down through the Dungeons of Doom, into Gehennom, and back out with the Amulet of Yendor: the quest is NetHack's. xNetHack sets out to "fix gameplay balance issues", "remove tedious and frustrating parts of the game" and "make uninteresting parts of the game more interesting", and it changes the game conservatively, deepening what is there rather than piling on more.

So that dagger might be silver, or glass. Armour comes in mithril, copper or bone. A crystal chest shows you what is inside and keeps it behind a lock no key can open. Gehennom's mazes are rebuilt around open caverns and themed rooms, and beneath Vlad's Tower there is a new level: a chasm of open air, home to vampires and a few demons.

Many of xNetHack's ideas have gone on to the official game. This is where they get tried first.

- **Object materials**: weapons, armour, boxes and amulets made of iron, silver, mithril, glass, bone and more, each with its own strengths
- **Crystal chests**: see-through, magically locked, with an extra item inside
- **A new Gehennom**: mazes rebuilt around open caverns and new special rooms
- **More themed rooms** throughout the dungeon
- **A tutorial** for first-timers, offered at the start

## Controls

- **hjkl yubn**: move, the last four diagonally; with **Shift**, run
- **F** and a direction: fight; **t**: throw, **z**: zap a wand
- **i**: inventory, **,**: pick up, **d**: drop
- **e** eat, **q** quaff, **r** read, **w** wield, **W** wear, **T**
  take off, **P** put on, **R** remove, **a** apply
- **o** and **c**: open and close doors; **s**: search; **.**: rest
- `>` and `<`: stairs down and up
- **#**: extended commands, such as `#pray`
- **?**: help, **;**: what is that symbol, **Ctrl-P**: earlier messages
- **S**: save and quit

## Saving and options

**S** saves the game to your data folder (`~/.local/share/xnethack`),
and starting xNetHack again carries on from there. Your options go in
`~/.xnethackrc`, or in `xnethackrc` in that folder, as `OPTIONS=` lines;
`OPTIONS=windowtype:curses` switches to the curses interface,
`OPTIONS=role:Valkyrie,name:Ada` skips the questions at the start, and
`OPTIONS=!tutorial` skips the tutorial offer. At the end of a game a
full account of it is written to `dumplog/` in the same folder.

## History

copperwater started xNetHack in 2017 as an "experimental" fork of
NetHack, a place to combine patches from the community and try new
ideas, and released it from 2018. It has followed the DevTeam ever
since: version 10.0, from May 2026, is built on NetHack 5.0.0. This
edition is built for Linux and macOS, keeping everything it writes in
your own data folder.

## Credits

- Game: copperwater and the xNetHack contributors, after NetHack by the
  NetHack DevTeam; object materials mostly from GruntHack
- Asciiverse edition: Asciiverse
- License: NetHack General Public License
