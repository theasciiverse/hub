**ONE BIG SQUARE. ONE NARROW GAP. NINE PIECES IN THE WAY.**

HuaRongDao is an ancient Chinese sliding-block puzzle, and its author
put it best: "The rules are very easy to understand, but the game is not
so easy to solve."

Ten pieces fill a box four cells wide and five high, leaving just two
cells empty: a big square, four tall rectangles, one wide one and four
small squares. Slide them, one at a time and never over each other,
until the big square escapes through the gap in the middle of the bottom
edge.

- **Every step counts**: moving one piece, even round a corner, is one
  step, and the counter shows how few you can manage.
- **Undo and redo**: back out of dead ends step by step.
- **Bookmarks**: keep a position in a slot and come back to it later.
- **More layouts**: the classic one is built in; give others as a
  pattern on the command line.

**Free the big square. Then do it in fewer steps.**

## Controls

- **0** to **9**: select the piece with that number, then
  **arrow keys** (or **l r u d**) to move it one or two cells
- **u**: undo a step, **r**: redo it
- **b**: save a bookmark in a slot (a letter or digit), **l**: load one
- **Enter**: clear the prompt, **Ctrl-L**: redraw
- **q**: quit (asks first)

## Options

- `hrd <pattern>`: play another layout, one letter a cell and a dot
  after each row: Q the big square, T and B the top and bottom of a tall
  piece, L and R the left and right of the wide one, P a small square,
  `_` empty. The classic layout is `TQQT.BQQB.TLRT.BPPB.P__P.`

## Files

Bookmarks are kept in `~/.local/share/hrd`.

## History

Qingning Huo wrote hrd in 2004 and maintained it in Debian until 2005.
The Asciiverse edition has his Debian build fix, bookmarks in the
player's data folder, and fixes for a crash without a home folder and
for unchecked memory mapping.

## Credits

hrd is by Qingning Huo, under the GNU GPL version 2 or later.
