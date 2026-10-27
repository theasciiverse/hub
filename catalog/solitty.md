Klondike solitaire in your terminal: the classic seven-column patience
game, drawn with Unicode card frames and colored suits, played with the
keyboard or the mouse.

Turn cards from the stock, build down the seven columns in alternating
colors, and move every card up to the four foundations, ace to king.
solitty notices when you have won.

## Controls

- **Arrow keys** or **h j k l**: move the cursor
- **Space**: turn a card from the stock, flip a face-down card, or pick
  up a card and put it down where the cursor is
- **Space** twice on the same card: send it to a foundation if it fits
- **m** / **n**: while holding a column, take one more or one fewer card
- **M** / **N**: take every face-up card in the column, or only the top one
- **Esc**: put the held cards back
- **Left click**: pick up or put down; **right click**: cancel
- **q**: quit

## Options

- `--passes N`: how many times you may go through the stock (default 3)
- `--four-color-deck`: give each suit its own color
- `--no-background-color`: keep your terminal's own background

## History

solitty was written by Murilo Pereira, first released in 2017, and
developed through 2025. The Asciiverse edition adds a fairer
Fisher-Yates shuffle, a terminal that is restored properly when the
game is interrupted, and further fixes and tests.

## Credits

- Original game: [Murilo Pereira](http://murilopereira.com)
- Asciiverse edition: Asciiverse
- License: MIT
