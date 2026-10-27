Fill the grid so that every row, every column and every smaller box
holds each symbol once. About half the cells start filled in, shown in
bold; a number that clashes with another is shown in red. The game ends
when every cell is filled by the rules, and asks whether to start a new
board.

Boards are not guaranteed to have only one solution: any filling that
follows the rules wins.

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