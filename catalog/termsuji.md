**BLACK MOVES FIRST. THE BOARD IS WAITING.**

Pull up a chair at a proper Go board: lines and star points on warm wood, black and white stones sitting right on the points, as big as your terminal can draw them. Across the table sits GNU Go, and it comes with the game. No account, no server, no waiting for an opponent to turn up. Just you, the stones and a patient adversary.

Pick your board: 9x9 for a quick, sharp fight, 19x19 for the full game. Pick your colour. Then pick how hard GNU Go should push back, from strength 1 to 10, and give Black up to nine handicap stones if you want a head start.

- **A board that looks like one**: wood, lines and star points; on a big terminal the points spread out and the stones become round discs
- **GNU Go built in**: it thinks while you study the board, marks the last stone played, and counts the game when both sides pass
- **Take it back**: **u** undoes your move and GNU Go's answer, as often as you like
- **Never lose a game in progress**: walk away mid-game and it is waiting under Continue, saved as an SGF file any Go program can open

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
