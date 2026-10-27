Rogue as it was in 1981, the version that reached BSD Unix. You go down
through the Dungeons of Doom, a new map of rooms and corridors on every
level, to find the Amulet of Yendor somewhere below the 20th and bring
it back. Twenty-six monsters, one for each letter, wait on the way;
potions, scrolls, rings and wands are unknown until you try them. Death
is final, and your score is the gold you carry out.

## Controls

- **hjkl yubn**: move, the last four diagonally; with **Shift** run that
  way
- **f** and a direction: move until something turns up; **t**: throw,
  **p**: zap a wand in a direction, **z**: zap
- **i**: inventory, **d**: drop
- **e** eat, **q** quaff, **r** read, **w** wield, **W** wear, **T** take
  off armour, **P** put on and **R** remove a ring
- **s**: search for traps and secret doors, **space**: rest
- `>`: stairs down
- **?**: all the commands, **/**: what a symbol is
- **S**: save and quit, **Q**: quit

## Saving

**S** saves the game to your data folder. To carry on, start it from a
shell as `rogue36 -r`; a saved game is deleted once it is restored.

## History

Michael Toy and Glenn Wichman prototyped Rogue at UC Santa Cruz in
1980, and with Ken Arnold made the 1981 version 3.6, which reached BSD
Unix (it is in the reconstructed 4.1BSD release). Nicholas J. Kisseberth (Yendor) restored it for modern systems
in the Roguelike Restoration Project, releases 3.6.1 to 3.6.5, and keeps
it at rogueforge. This edition keeps its files in your data folder and
fixes a table overflow at
the start of every game and saved games that never restored. It is part
of the Roguelike Restoration Project in the Asciiverse catalog, next to
NetBSD's Rogue, a later clone of 5.3.

## Credits

Michael Toy, Glenn Wichman and Ken Arnold; restoration by Nicholas J.
Kisseberth. BSD licence.
