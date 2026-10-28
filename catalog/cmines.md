**ONE WRONG STEP AND IT'S OVER.**

Somewhere under this grid are 99 mines. Every square you open tells you how many of its eight neighbours hide one, and from those numbers, and nothing else, you work out where it is safe to step. Flag the mines you are sure of. Open the rest. The clock is running.

The first square you open is never a mine, so the opening move is free. After that, it's all you.

- **Three classic fields**: Beginner (8x8, 10 mines), Intermediate (16x16, 40 mines) and Expert (16x30, 99 mines), each with its own best time. Write your own into the setup file, or start one by name: `cmines Expert`.
- **Chording**: when a number has all its mines flagged, Return (or the middle mouse button) opens all its other neighbours in one go. That is how the fast times are made.
- **A peek when you're truly stuck**: **p** looks under one square, but a game with a peek in it can't set a best time.
- **A face to keep you company**: with `-e`, a little emoticon shows the game's mood, from :-) to B-).
- **Keys or mouse**: arrow keys or h j k l, or click.

**Beginner is a warm-up. Expert is a war.**

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
