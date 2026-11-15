**EAT THE SCREEN. EVERY NUMBER DECIDES HOW FAR.**

You are the @, standing in a field of numbers that fills the screen. Pick
any of eight directions and you munch your way along it: as many squares
as the first number you meet. Wherever you stop, the next number is
already waiting. As the game's own readme warns: "Beware! the length of
your next move is forced by the number you land on."

You can't leave the board, and you can't cross a square you've already
eaten. Paint yourself into a corner and that's it: when no move is left,
the game is over. Your score is every square you ate, shown beside it as
a share of the whole board.

- **One rule, eight directions**: learn it in a minute, then try to stop.
- **See your options**: press p and every move you can make lights up.
- **Every board is new**: a fresh field of numbers each game, and a
  fresh chance to clear more of it than last time.
- **High scores**: `greed -s` shows the best games.

**Greedy? Good. Now don't get stuck.**

## Controls

- **Arrow keys**, **h j k l y u b n** or the **numeric keypad**: move in any of eight directions
- **p**: show or hide the moves you can make
- **Ctrl+L**: redraw the screen
- **q**: quit

Moving eats as many squares in that direction as the first number you
meet. You cannot leave the board or cross a square you have already eaten;
when no move is left, the game ends. Your score is the number of squares
eaten.

## Options

- `-f`: fit the board to the terminal (av starts Greed this way)
- `-w N`, `-h N`: set the board's width and height
- `-p`: start with possible moves highlighted
- `-r N`: fixed random seed, for replaying the same board
- `-s`: show the high scores

## History

Nobody knows quite where Greed began. Matt Day wrote it in C for Unix and
took it up to version 3.0a in 1990, but he never claimed to have invented
it: "I once saw it on an IBM, and wrote it for Unix in C." It was probably
a DOS freeware game of the 1980s, yet no trace of that original has ever
turned up in the surviving archives. Then Matt dropped out of sight, and
by 1994 Eric S. Raymond had taken the game in. He has looked after it ever
since, for more than thirty years, and in 2026 he rebuilt it in Rust, so
the hungry @ munches on.

## Credits

- C version: Matt Day
- Maintainer and Rust port: [Eric S. Raymond](https://gitlab.com/esr/greed)
- Asciiverse edition: Asciiverse
- License: BSD-2-Clause
