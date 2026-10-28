**FIFTY-TWO CARDS. SEVEN COLUMNS. ONE WAY HOME.**

The patience game everybody knows, laid out properly in your terminal:
real card frames drawn in Unicode, red and black suits (or four colours,
one for each suit, if you prefer), and a cursor you can drive with the
keyboard or the mouse.

Turn cards from the stock. Build down the seven columns in alternating
colours, uncovering the face-down cards as you go. Send every card up to
the four foundations, ace to king. Double-tap a card and, if there is a
place for it, it goes home by itself. Get them all up and solitty knows
you have won.

- **Keyboard or mouse**, click to pick up, click to put down
- **Pick up whole runs** or just the cards you want
- **Three passes through the stock** by default, or as many as you set
- **Your terminal's own background**, if you would rather keep it

**Deal. Build. Win.**

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
