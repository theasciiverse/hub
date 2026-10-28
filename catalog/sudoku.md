**FROM A 4x4 TO A 49x49. HOW BIG DARE YOU GO?**

You know the rules: fill the grid so that every row, every column and
every box holds each symbol exactly once. About half the cells start
filled in, in bold, and anything you write that clashes turns red. Fill
the last cell by the rules and the game cheers "Yay!! Wanna play
again?"

Then it gets interesting. Start it with a bigger box size and the
boards grow: 16x16, 25x25, all the way to 49x49, where the letters join
in as digits and a board will not fit on your screen without scrolling.
The generator does its honest best, though it warns you: "My algorithm
sucks, so you need to wait a bit."

- **Six sizes**, from 4x4 to 49x49
- **Hints** when you are stuck, a cell at a time
- **Mouse or keyboard**, whichever you like
- **Any valid filling wins**, even if it is not the one the generator
  had in mind

**Pick a size. Lose an evening.**

## Controls

- **Arrow keys**: move
- **1** to **9**: write a number; on boards bigger than 9x9 the letters
  from **a** on are symbols too
- **Enter**: step the number in the cell up by one
- **Space**: clear the cell
- **Mouse**: left click to step the number up, right click to clear
- **?**: hint, fills in the cell under the cursor (after showing the help)
- **r**: clear everything you wrote, **n**: a new board
- **F1**: help on the controls, **F2** or **!**: how to play
- **PgUp**, **PgDn**, **<** and **>**: scroll a board that does not fit
- **q** or **Esc**: quit

On the biggest boards some of these letters are symbols: **n** stops
working from 25x25, **q**, **r** and **Esc** from 36x36. **Q** always quits.

## Options

Started from a shell, Sudoku takes the size of the boxes:

- `-s 4` plays a 16x16 board; anything from `-s 2` (4x4) to `-s 7`
  (49x49) works, and the default is 3 (9x9)
- `-f` makes boards with a faster, cruder generator, which is always
  used from 25x25 up

## History

Sudoku is one of the games abakh wrote for New BSD Games, a collection of
small curses games started in 2018 and named after the classic BSD games.
The collection is packaged by Debian, Ubuntu, openSUSE, Alpine, Nix,
Homebrew, FreeBSD and pkgsrc, and is in the AUR.