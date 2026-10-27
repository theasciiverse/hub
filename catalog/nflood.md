A board of 14 by 14 cells in six colours, and one simple move: pick a
colour, and the patch in the top left corner turns that colour, swallowing
every neighbouring cell that already had it. Keep picking until the whole
board is one colour. The fewer moves it takes, the better.

It sounds like there is nothing to it, but which colour to pick next is
a real choice: grab the colour with the most cells along your edge, or
the one that opens a path into the far corner. The panel shows your
moves, how much of the board is flooded, and your best game.

## Controls

- **1** to **6**: flood with that colour (the panel shows which is which)
- **Mouse**: click a colour in the panel, or any cell of the board, to
  flood with its colour
- **r**: a new board (or click "r: New Game")
- **c**: centre the board, or move it back to the corner
- **q**: quit

After "Congrats!", **r** plays another board and any other key quits.

## Options

- `-W <width>`, `-H <height>`: a board of another size (only the
  standard 14x14 counts for the best score)

## Files

The best score is kept in `~/.local/share/nflood` (`%APPDATA%\nflood` on
Windows). It starts at 25 before any game is won.

## History

Alexandre Dantas wrote nFlood, his terminal version of the Flood-It
puzzle, between 2011 and 2014, with Yu-Jie Lin adding mouse support,
custom board sizes and the best score. This edition has fixes so it
builds with current compilers and deals a different board each time it
starts, the best score in the player's data folder and shown as soon as
it is set, a working New Game click and a Windows build.

## Credits

nFlood is by Alexandre Dantas and Yu-Jie Lin, under the GNU GPL version
3 or later. Its option parser is TJ Holowaychuk's Commander (MIT).
