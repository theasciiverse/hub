**SOMETHING IN THE DARK FOREST HEARD THAT. WHICH WAY ARE YOU FACING?**

You start among the brown trunks and green thickets of the Dark Forest, a creek winding through it and a still pond, light breaking through the canopy in a few small clearings. Everywhere else is dark. You hear a rat before you see it. You see a wolf only as it turns toward you, a yellow **!** flashing over its head: it knows you are there.

Rhex is a roguelike on a grid of hexagons, and you have a front and a back. Turning is a move of its own, you see what lies ahead of you, and whatever reaches your back strikes twice as hard and twice as surely. So do you, if you get behind it. Every step, door and swing makes noise that travels through the trees, damped by thickets and stopped by trunks, and the creatures come to find out what made it.

Take the path onward and the forest gives way to the Dungeon: stone rooms lit by torches on the walls, closed doors, chests that open loudly and are sometimes empty, cave beetles in their armour and skeletons with short swords and bucklers. Then forest again, and Dungeon again, each harder than the last. Every level you leave is still there when you climb back, its creatures, its open chests and whatever you dropped.

- **Human, elf or dwarf**: the elf sees farthest in the dark, the dwarf hits hardest and runs longest
- **Light is a choice**: a hand lantern shows you the way, and shows you to everything else
- **Sound is a lure and a giveaway**: a whistle may bring them over; a club is easy to swing and loud to use
- **Charge** two hexes at a foe, if you have the stamina
- **No saving**: a run lasts as long as you do

## Controls

- **h l** or **Left Right**: turn; **k j** or **Up Down**: step forward or back
- Walk into a creature to attack, a door to open it, a thicket to cut it
- **H L**: strafe front-left or front-right without turning
- **c**: charge; **.**: wait; **o**: explore
- **> <**: take the passage you stand on; **G** then **>** or **<**: walk to one
- **,**: pick up, or open the chest or door in front of you
- **I**: inventory; **E**: equip or use; **D**: drop
- **x**: examine; **F2**: Vi keys; **?**: help; **Esc**: quit

## History

Dawid Ciężarkiewicz, dpc, started Rhex in January 2015 to sharpen his Rust on a hexagonal map, after an earlier try called Rustyhex, using his own hex2d library for the geometry. Within a month it had half-light, grues and noise; Demur Rumed, Christopher Serr and others joined in, and through 2016 it grew into the little curses roguelike of the old screenshots. Then it slept. In October 2026 dpc woke it up: ncurses gave way to Crossterm and Ratatui, and the game turned toward what he had always wanted, an atmospheric, scary roguelike where hiding, scouting, light and sound count for more than stats. The Dark Forest, its creek and thickets, chests, lanterns, whistles and creatures that notice you all arrived then. It is unfinished, as its author says, and very much playable.

## Credits

- Rhex: Dawid Ciężarkiewicz (dpc), with Demur Rumed, Christopher Serr and other contributors
- Built on hex2d, Crossterm and Ratatui
- License: MPL-2.0
