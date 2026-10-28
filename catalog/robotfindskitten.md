**YOU ARE ROBOT. YOUR JOB IS TO FIND KITTEN.**

This task is complicated by the existence of various things which are not kitten. Every one of them looks like a random character on the screen, just as kitten does, so robot must touch each thing to find out what it is. Perhaps "A stack of 7 inch floppies wobbles precariously." Perhaps "Some coconut crabs are milling about here." Perhaps "A wireframe model of a hot dog rotates in space here." There are 726 of them to meet, and only one kitten.

There is no score, no timer and no way to lose. The game ends when robotfindskitten.

**"YOU FOUND KITTEN! WAY TO GO, ROBOT!"**

## Controls

- **Arrow keys**, **hjkl** or the number pad: move robot; **yubn** (or
  **Home**, **PgUp**, **End**, **PgDn**) move diagonally
- **Ctrl-L**: redraw the screen
- **q** or **Ctrl-C**: give up

## Options

Started from a shell in its folder: `-n NUM` puts NUM things on the
screen (20 by default), `-s SEED` sets the layout, and `-f FILE` reads
the things from another list. Your own `.nki` files in
`~/.robotfindskitten` join the 726.

## History

In 1997 Peter A. Peterson II held a contest in his magazine Nerth Pork
for the best piece of art entitled "robotfindskitten". Leonard
Richardson submitted the winning (read: only) entry. This is the
canonical C version for terminals: Alexey Toptygin's 2004 to 2005 code,
merged by Eric S. Raymond in 2012 when he recovered the project's
history, and maintained since by Ryan Finnie, who moved it to Codeberg
in 2026. The game is upstream's, unchanged.

## Credits

- Game: Leonard Richardson and contributors
- C version: Alexey Toptygin, Eric S. Raymond, Ryan Finnie and contributors
- Windows console support: [PDCurses](https://pdcurses.org)
- Asciiverse edition: Asciiverse
- License: GPL-2.0-or-later
