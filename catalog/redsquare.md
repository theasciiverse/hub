A puzzle played in Conway's Game of Life. The board is full of white
cells, **#**, that live, die and are born by Life's rules, and you move
a red square of four cells through them. Life moves on a generation
every time you press a key, or by itself after a short wait.

Red cells live by the same rules, and a cell that is born or survives
takes the colour of most of its neighbours, so when your square touches
other cells it starts reactions that can spread red, **O**, or wipe it
out. Once the square has come apart you cannot move it, until a new red
square with nothing around it forms somewhere and you take control of
that one.

You clear a level by catching the X, which wanders around the board, in
your square for two turns in a row, or by having red cells outnumber
the white ones until no white cell is left. You lose when no red cell is
left. A few set levels come first, then random ones. When the board
settles down for long, the game scatters new red and white cells over
it.

The board is 50 by 35 and wraps around at every edge; on a terminal
shorter than 42 rows it scrolls to follow your square.

## Controls

- **Arrow keys**, **hjkl** or **wasd**: move the square
- **p**: pause
- **F1** or **?**: help on the controls, **F2** or **!**: how to play
- **q** or **Esc**: quit

## History

Redsquare is one of the games abakh wrote for New BSD Games, a collection
of small curses games started in 2018 and named after the classic BSD
games. The collection is packaged by Debian, Ubuntu, openSUSE, Alpine,
Nix, Homebrew, FreeBSD and pkgsrc, and is in the AUR.