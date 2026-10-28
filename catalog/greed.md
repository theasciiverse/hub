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
- **The whole window**: av starts Greed fitted to your terminal, so a
  big window means a big feast.
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

Matt Day wrote the C version and released it up to 3.0a in 1990; it
probably goes back to a DOS game of the 1980s. Eric S. Raymond took over
maintenance and has kept it going since, porting it to Rust in 2026.

## Credits

- C version: Matt Day
- Maintainer and Rust port: [Eric S. Raymond](https://gitlab.com/esr/greed)
- Asciiverse edition: Asciiverse
- License: BSD-2-Clause
