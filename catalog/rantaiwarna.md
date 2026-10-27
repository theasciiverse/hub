The board starts full of elements in four colours. Pick any group of
two or more touching elements of the same colour and they vanish; the
elements above fall into the gap, and when a whole column empties, the
columns to its right slide over. The game is over when no group of two
is left.

A group of n elements scores (n - 1) squared, so two at a time earns
almost nothing and twenty at once earns 361. Clearing the board
completely adds a bonus of 1000. The trick is to leave the small groups
alone until the colours around them have run together into big ones.
The best ten scores are kept for each board size and number of colours.

## Controls

- **Arrow keys** or **h j k l**: move the cursor
- **Space** or **Enter**: remove the group under the cursor
- **Left mouse button**: remove the group you click
- **n**: a new game
- **i**: the high score table, **H**: help, **a**: back to the game
- **Ctrl+L**: redraw
- **q**: quit

## Options

- `-c <colours>`: two to five colours (four unless given)
- `-w <width>`, `-h <height>`: the board's size, at least 5 by 5 (20 by
  10 unless given)

## Files

High scores are kept in `~/.local/share/rantaiwarna`.

## History

SameGame goes back to Chain Shot!, a 1985 game by Kuniaki Moribe. Guido
Berhoerster wrote rantaiwarna in 2014 for any curses that follows the
X/Open standard, from ncurses to the native curses of Solaris and
NetBSD, and kept it in a Mercurial repository until 2016. This edition
has its history rebuilt in git, the high scores moved to the player's
data folder, and a terminal that starts too small now waiting to grow
instead of quitting.

## Credits

rantaiwarna is by Guido Berhoerster, under the MIT licence.
