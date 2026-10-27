NetHack's big variant. You go down through the Dungeons of Doom for the
Amulet of Yendor, as in NetHack, but the dungeon has more in it: Angband
style towns, the Ruins of Moria, a black market, an Advent Calendar
portal, Sheol, an icy branch of Gehennom, the Convict role, and many
smaller changes that make each game less predictable and harder. New
players can press **T** at the start for a tutorial.

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

**S** saves the game to your data folder (`~/.local/share/unnethack`),
and starting UnNetHack again carries on from there. Your options go in
`~/.unnethackrc`, or in `unnethackrc` in that folder, as `OPTIONS=` lines;
`OPTIONS=windowtype:curses` switches to the curses interface, and
`OPTIONS=role:Valkyrie,name:Freya` skips the questions at the start.

## History

UnNetHack is Patric Mueller's fork of NetHack 3.4.3, started in January
2009, meant to show "how NetHack would look today if the DevTeam didn't
stop releasing". It gathered patches from the NetHack community and its
own new levels and branches, and it is played on public servers. This
edition is built for Linux and macOS, keeping
everything it writes in your own data folder. The succubus and incubus
seduction scene is left out, with upstream's own build option.

## Credits

- Game: Patric Mueller and the UnNetHack contributors, after NetHack by
  the NetHack DevTeam
- Asciiverse edition: Asciiverse
- License: NetHack General Public License
