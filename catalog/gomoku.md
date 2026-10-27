Gomoku is five in a row, the game played with stones on a Go board, here
against the computer on a 19 by 19 grid. Take turns placing
stones; the first to get five in an unbroken line, across, down or
diagonally, wins.

The computer picks at random who starts, and X always moves first. It
weighs every line of five on the board for both sides, building threats
of its own and blocking yours, so an open three left alone soon becomes
a line that cannot be stopped. Your stones and its stones
are in different colours, and the last move of each side is highlighted
so you can see what just happened.

## Controls

- **Arrow keys** or **hjkl**: move the cursor
- **Space** or **Enter**: place your stone
- **q** or **F10**: end the game

## History

Ralph Campbell wrote Gomoku for BSD Unix in 1994, building the board
display on goref, a program by Peter Langston. Its computer player looks
for combinations of threats in every direction.

Mike Sharov reworked Gomoku in 2016 for his bsd-games, the modern Linux
port of the BSD games: a boxed board centred in
the terminal, moves chosen with the cursor instead of typed coordinates,
and colour for each side. Gomoku is part of BSD Games in the Asciiverse
catalog, under the BSD licence.
