A falling-blocks game where the game is against you. Every other one
picks the next block at random; Bastet looks at your stack, tries every
block in every place it could go, and hands you the one that does you
the least good. Waiting for the long straight piece to fill a deep
gap is a plan that does not work here. Clearing even a few lines is an
achievement, and a long game is a real one.

Rows clear when they are full, as you would expect: 100 points for one
row, 300 for two, 500 for three and 800 for four at once. Every ten
rows the level goes up and the blocks fall faster.

There are two games. The normal one shows the next block, and Bastet
picks the block after that knowing you have seen it. The harder one
has no preview at all, and the chooser is tuned for that. Each has its
own top ten.

## Controls

- **Left**, **Right**: move the block
- **Down**: move it down one row
- **Space**: turn it clockwise, **Up**: turn it the other way
- **Enter**: drop it straight to the bottom
- **p**: pause
- **Ctrl+C**: quit at once (high scores already made are kept)

Every key can be changed in Customize keys.

## Files

Keys and high scores are kept in the player's data folder,
`~/.local/share/bastet` (`%APPDATA%\bastet` on Windows).

## History

Federico Poloni wrote Bastet; version 0.41 reached Slashdot in April
2005, and his 0.43 rewrite of 2009 split the chooser into the two games
above. It is packaged by Debian, Fedora and
others. This edition has Debian's fix for printing names, and fixes of
our own: Enter drops the
block as the documentation always said, scores and keys follow
`XDG_DATA_HOME` instead of needing a setgid binary, and it builds for Windows.
