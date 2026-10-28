**TWENTY-SIX LETTERS. EVERY ONE OF THEM WANTS YOU DEAD.**

This is Rogue as it was in 1981, the version that went out with BSD
Unix. The
guildmasters send you into the Dungeons of Doom with a mace and a bow;
your task is to find the Amulet of Yendor, somewhere below the 25th
level, and carry it back up into the light.

The alphabet is the monster manual. A is a giant ant, J a jackal, K a
kobold; further down wait the rust monster that eats your armour, the
floating eye you must never hit, the invisible stalker you cannot see,
the umber hulk, the xorn, the troll and, at the letter D, the dragon.
Potions, scrolls, rings and wands are unknown until you try them.

- **A new dungeon every game**, mapped only as you walk it
- **Death is final**, and your score is the gold you carry out
- **The headstone waits:** die and the game carves REST IN PEACE over
  your name; win and it tells you "Congratulations, you have made it to
  the light of day!"

**The original. Still merciless.**

## Controls

- **hjkl yubn**: move, the last four diagonally; with **Shift** run that
  way
- **f** and a direction: move until something turns up; **t**: throw,
  **p**: zap a wand in a direction, **z**: zap
- **i**: inventory, **d**: drop
- **e** eat, **q** quaff, **r** read, **w** wield, **W** wear, **T** take
  off armour, **P** put on and **R** remove a ring
- **s**: search for traps and secret doors, **space**: rest
- `>` and `<`: stairs down, and up once you carry the Amulet
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
