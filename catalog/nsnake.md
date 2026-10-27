The snake game everyone played on their phone, in the terminal. Steer
the snake to the fruit; every fruit makes it longer and adds to the
score, and running into a wall or your own tail ends the game.

Arcade Mode is the classic game on an open board. Level Select has 31
mazes to play instead, from simple arenas to spirals, hearts and
letters, and each keeps its own high score. In Game Settings you set the
starting speed (1 to 10), how many fruits are on the board at once, the
board size, teleporting through the edges, random walls, and a board
that scrolls under you; scores are kept for each combination.

## Controls

- **Arrow keys**: steer the snake
- **p**: pause, **h**: help during a game
- **q**: quit at any time
- **Enter**: choose in the menus

Every key can be changed in the Controls menu, and colours and borders
in GUI Options.

## Levels

Levels are plain text files ending in `.nsnake`. Besides the 31 that
come with the game, nSnake reads your own from the `levels` folder in
its data folder (`~/.local/share/nsnake/levels`), where its settings
and scores are kept too.

## History

Alexandre Dantas wrote nSnake in C++ and ncurses from 2012 to 2014; it
is packaged by Debian, Fedora and others. This edition has a few fixes:
the bundled levels are found without copying them by hand, settings
follow `XDG_DATA_HOME`, and it builds for Windows.
