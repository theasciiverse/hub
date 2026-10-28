**THREE NEW CHIPS EVERY TURN. HOW LONG CAN YOU HOLD THEM OFF?**

The board is 9x9 and it is filling up. Every turn you fail to score, three more chips land at random: red, green, blue, yellow and purple, crowding your paths and closing the gaps you were saving. Your one weapon is a single move. Pick up a chip and send it to any free cell it can reach, sliding up, down, left and right around the others.

Line up five or more of one colour, across, down or diagonally, and they vanish. Better still, nothing new arrives: the move is yours again. Let the board fill and it is over.

- **Big clears pay big**: n chips cleared at once score n + n x (n - 5), so a line of six is worth 12, and two lines crossing at the last chip you drop are worth far more than two fives.
- **Chains pay too**: clear on turn after turn without letting new chips in, and each one adds a growing bonus, b x b for the b-th in a row after the first.
- **Keys or mouse**: arrow keys or h j k l and Space, or click a chip and then the cell to send it to.
- **Your best score**: kept between games and shown under the board while you play.

Plays in black and white too, with letters for the colours.

**One move. Five in a row. Don't let it fill.**

## Controls

- **Arrow keys** or **h**, **j**, **k**, **l**: move the cursor
- **Space**: pick up the chip under the cursor (it starts to jump), then
  put it down on a free cell
- **Mouse**: click a chip, then the cell to send it to
- **Ctrl+L**: redraw; **q**: quit (your score is saved)

## Options

- `-l`: list the high scores
- `-m b`: black and white, with letters for the colours
- `-w`, `-t`, `-c`, `-i`, `-n`, `-N`: board width and height, number of
  colours, line length, chips per turn and chips to start with (scores
  are only kept with the defaults)

## High scores

Your best score is kept in your own folder
(`~/.local/share/clines`), so it survives updates, and shows under the
board while you play.

## History

Pawel S. Veselov started Console Lines in 2002, after the classic Color
Lines, added mouse support (both the terminal's and GPM on the Linux
console) and scoring, and released 1.0.4 in October 2006 with resizing,
smaller terminals, black and white mode and saved high scores. His site
has since gone; ALT Linux and OpenBSD kept packaging it.

The Asciiverse edition keeps scores in your own folder, animates the
jumping chip without curses calls inside signal handlers, and makes sure the mouse keeps
working in terminal emulators.
