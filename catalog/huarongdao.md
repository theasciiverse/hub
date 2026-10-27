HuaRongDao is an old Chinese sliding-block puzzle. Ten pieces fill a box
four cells wide and five high, leaving two cells empty: a big square,
four tall rectangles, one wide one and four small squares. Slide
them, one at a time and never over each other, until the big square
reaches the gap in the middle of the bottom edge. The rules take a
minute to learn; the solution takes a good deal longer.

Moving one piece, even round a corner, counts as one step, and the step
counter shows how few you can manage. Undo and redo let you back out of
dead ends, and bookmarks keep a position to come back to.

This game ships one layout, the classic one. Other layouts can be
played by giving them as a pattern on the command line.

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
