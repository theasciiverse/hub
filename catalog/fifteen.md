The classic sliding puzzle. Fifteen numbered tiles sit in a four by four
frame with one gap, shuffled. Slide tiles into the gap until they are in
order again, 1 to 9 and then a to f, with the gap in the bottom right
corner. A tile turns green when it is in its right place.

Put the cursor on a tile in the same row or column as the gap and press
Enter: that tile moves toward the gap, and so do all the tiles between
them, so a whole line can move in one go.

## Controls

- **Arrow keys**, **hjkl** or **wasd**: move the cursor
- **Enter**: slide
- **Mouse**: click a tile to slide it
- **F1** or **?**: help on the controls, **F2** or **!**: how to play
- **q** or **Esc**: quit

## Options

Started from a shell, Fifteen takes the size of the board, from 3 to 7:

- `fifteen -s 5`: a five by five board; past 9 the tiles carry letters,
  lower case and then upper case
- `-n`: do not ask to play again after a solved board

## History

Fifteen is one of the games abakh wrote for New BSD Games, a collection of
small curses games started in 2018 and named after the classic BSD games.
The collection is packaged by Debian, Ubuntu, openSUSE, Alpine, Nix,
Homebrew, FreeBSD and pkgsrc, and is in the AUR.