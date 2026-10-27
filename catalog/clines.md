The Lines game in your terminal. Coloured chips appear on a 9x9 board
three at a time. Each turn you move one chip to any free cell it can
reach by sliding up, down, left and right around the others. Line up
five or more of the same colour, across, down or diagonally, and they
vanish, and you get another move before new chips arrive. When the board
is full, the game is over.

Every chip removed scores a point, and longer or crossing lines score
more: n chips removed at once score n + n x (n - 5). Clearing on several
turns in a row adds a growing bonus, b x b for the b-th such turn after
the first.

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
