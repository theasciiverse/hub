Chroma is an abstract puzzle game. Each level is a maze of walls, dots,
arrows and bombs with stars scattered through it, and you have two
player pieces. Collect every star, then leave through the door. It
starts simple enough to pick up at once, and gets hard enough to tax
anyone.

The pieces are not explained. Arrows slide the way they point whenever
there is room, and a moving one can crush a player piece; bombs, circles
and dots have rules of their own, and part of the game is finding out
exactly how they behave and set each other off. The first
six levels of each set bring the pieces in one by one. Later levels
need both player pieces working together.

There are 21 levels in two sets, nine for beginners and twelve for
experts, and they can be played in any order. Mistakes cost nothing:
undo goes back as far as you like, and redo plays it forward again.
Positions can be saved and loaded, and a saved solution replays move by
move. A level editor lets you build and test your own, and Chroma can
also play levels from the similar games XOR and Enigma.

## Controls

- **Arrow keys**: move the active player piece
- **Space** or **Enter**: swap to the other player piece
- **Delete**, **Backspace** or **U**: undo a move
- **Insert** or **Y**: redo
- **F**: let everything moving come to rest at once
- **P**: pause
- **Escape**: the game menu (save, load, replay, revert, display
  options, leave the level)

Keys can be changed under Display Options. In the editor, Page Up and
Page Down choose a piece and Space places it.

## Files

Saved and solved positions, levels under construction and the display
options are kept in `~/.local/share/chroma` (`%APPDATA%\chroma` on
Windows). Exported levels and solutions go to your home folder.

## History

Amf released Chroma in 2010 with a graphical SDL version and this
terminal one, and kept it going until version 1.21 in November 2025;
there is also a browser version and a port to the BBC Micro. It is
packaged by Debian. The Asciiverse edition is the terminal version, with
the levels found beside the program and saved positions in the player's
data folder.

## Credits

Chroma is by Amf (level7.org.uk), under the GNU GPL version 2 or later.
