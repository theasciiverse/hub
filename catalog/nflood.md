**ONE CORNER. SIX COLOURS. CAN YOU BEAT 25?**

A 14 by 14 board in six colours, and your patch starts in the top left corner. Pick a colour, and your patch turns that colour, swallowing every neighbouring cell that already had it. Pick again. And again. Keep going until the whole board is one colour. The fewer moves it takes, the better.

It sounds like there is nothing to it. Then you start counting. Grab the colour with the most cells along your edge, or the one that opens a road into the far corner?

- **One key per colour**, 1 to 6, or click a colour in the panel, or any cell on the board.
- **A best score to beat**, kept for the standard board. Before your first win, it stands at 25 moves.
- **Bigger or smaller boards** from a terminal, just for fun.

**DROWN THE BOARD.**

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
