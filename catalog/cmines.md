Clear the minefield without stepping on a mine. Every square you open
tells you how many of its eight neighbours hide mines; flag the ones you
are sure of and open the rest. The first square you open is never a
mine.

Three fields come ready: Beginner (8x8, 10 mines), Intermediate (16x16,
40 mines) and Expert (16x30, 99 mines), each with its own best time. Add
your own to the setup file, or start with one by name: `cmines Expert`.

When a number already has all its mines flagged, Return (or both mouse
buttons) opens all its other neighbours at once, the quick way through a
field.

## Controls

- **Arrow keys** or **h j k l**: move; **H J K L**: move by three
- **Space** or **left click**: open a square
- **.** (dot) or **right click**: flag a mine
- **Return** or **middle click**: open the neighbours of a number
- **p**: peek at a square
- **?**: help and the best times
- **n**: new game; **b**, **i**, **e**: Beginner, Intermediate, Expert
  (between games); **q**: give up the game; **Q**: quit

## Options

- `-t`: keep the timer running on screen
- `-e`: show the game's mood as an emoticon
- `-s FILE`: use another setup file

## Credits

- cmines: Brian Raiter ([muppetlabs.com/~breadbox](https://www.muppetlabs.com/~breadbox/software/cgames.html)),
  2000 to 2020, written in C with curses; part of his cgames
- License: GPL-2.0-or-later
