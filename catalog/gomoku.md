**FIVE IN A ROW. IT'S WATCHING EVERY LINE.**

Gomoku is five in a row, the game played with stones on a Go board, and
here the board is 19 by 19 and your opponent is the computer. Take turns
placing stones. The first to get five in an unbroken line, across, down
or diagonally, wins.

Sounds simple. Then the computer starts building. It weighs every line of
five on the board for both sides, making threats of its own and blocking
yours, and an open three you leave alone soon becomes a line nobody can
stop. Win and it grumbles "Rats! you won". Lose and you'll read "Ha ha, I
won".

- **Cursor play**: steer with the arrows or hjkl, place with Space or
  Enter.
- **A coin toss to start**: the computer picks at random who goes first,
  and X always moves first.
- **Nothing slips past you**: each side in its own colour, and the last
  move of each side highlighted.

**Five stones. One line. Get there first.**

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
