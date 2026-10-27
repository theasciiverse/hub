Go, the board game, in the terminal, on a board that looks like one:
lines and star points on wood, black and white stones on the points, as
big as the terminal allows. Play GNU Go, which comes with the game, on a
9x9, 13x13 or 19x19 board, as Black or White, at any of its ten
strengths, with up to nine handicap stones for Black.

GNU Go thinks while you look at the board, a cursor shows where you are
and the last stone played is marked. Take back a move whenever you like.
Two passes end the game and GNU Go counts it. Leave in the middle and the
game is waiting under Continue the next time, saved as an SGF file that
any Go program can open.

## Controls

- **Arrow keys**: move the cursor; **Enter**: play a stone there
- **p**: pass; **u**: take back your move and GNU Go's answer
- **t**: change the board's look; **q**: back to the menu (the game is
  saved)
- **n**: a new game once the game is over
- In the menus: **Up**, **Down** or **Tab** to choose, **Enter** to go on

## Credits

- termsuji: lvank ([github.com/lvank/termsuji](https://github.com/lvank/termsuji)),
  2022, written in Go with tview and tcell
- GNU Go 3.9.1: the GNU Go authors
  ([gnu.org/software/gnugo](https://www.gnu.org/software/gnugo/)),
  GPL-3.0-or-later, shipped beside termsuji with its licence and source
- Asciiverse edition: play against GNU Go, saved games and the classic
  board
- License: MIT (termsuji), GPL-3.0-or-later (GNU Go)
