**THE ROLE-PLAYING GAME THAT PLAYS ITSELF.**

Roll up a hero. Pick a race (Half Halfling? Land Squid? Talking Pony?) and a class (Ur-Paladin, Voodoo Princess, Battle-Felon, Fighter/Organist), roll the stats until you like them, and press **Sold!**. Then sit back. Your work here is done.

Your hero takes it from there. "Experiencing an enigmatic and foreboding night vision." Off on a long and dangerous journey. "Heading to the killing fields." Slaying Cub Scouts and Bugboars, looting their parts, "Heading to market to sell loot", "Negotiating purchase of better equipment", learning spells like Cone of Annoyance and Holy Batpole, gaining levels and working through quests and the acts of an epic plot, all as progress bars filling on their own.

pq2 is Nick Bollom's remake of Progress Quest, the send-up of level-grinding RPGs that Eric Fredricksen released in 2002, rebuilt in C++ with the same races, classes, monsters, spells and items. It is not the original, which you can still play at [progressquest.com](http://progressquest.com). Leave it running in a spare terminal and check in on your hero now and then; it only advances while it is open.

**THERE IS MUCH TO BE DONE. YOU ARE CHOSEN!**

## Controls

- **Up**, **Down** and **Enter**: the main menu; **Esc** quits
- On the character sheet: **Tab** or the arrow keys move between the
  fields, **Enter** picks one (a random name, the race and class lists,
  Roll, Unroll), letters and digits type a name, **Backspace** deletes,
  and **Sold!** starts the game; **Esc** goes back
- **F1** equipment, **F2** spells, **F3** inventory, **F4** plot, **F5**
  quests; **Up** and **Down** scroll a list, **Esc** closes it
- **p**: show or hide the percentages on the bars
- **-** and **+**: redraw faster or slower
- **Esc** on the game screen: save and quit

## Saving

The game saves to your data folder when the character is created, at
every new level, act and finished quest, and when you quit. To carry
on, choose Load Game, which lists your saved heroes, or start it from a
shell as `pq2 <name>`.

## History

Eric Fredricksen wrote Progress Quest for Windows in 2002 as a send-up
of the online role-playing games of the day, and has kept it going for
over twenty years, with a web version and online realms (Windows
version 6.4.4 came out in 2022). He
released it under the MIT licence. Nick Bollom began his cross-platform
remake in 2016, with Qt, GTK and ncurses editions; this is the ncurses
edition, with saved games in your data folder
and a few bugs fixed.

## Credits

- Progress Quest: [Eric Fredricksen](http://progressquest.com), MIT
- pq2: [Nick Bollom](https://github.com/nbollom/pq2), GPL-3.0
- Asciiverse edition: Asciiverse
