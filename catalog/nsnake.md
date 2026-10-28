**EAT. GROW. DON'T BITE YOURSELF.**

The snake game everyone played on their phone, now in your terminal. Steer the snake to the fruit; every fruit makes it longer, and longer makes it harder. Run into a wall or your own tail and it's over.

Arcade Mode is the classic, on an open board. Or pick one of 31 levels in Level Select: arenas, spirals, three hearts ("Cute, right?"), the word NSNAKE spelled out in walls ("How meta. Watch out for the letter K!"), and Tricky, which its author signs off with: "Let's see you survive on this baby. While it scrolls."

- **31 levels**, each with its own high score, and your own levels from plain text files.
- **Make it your game**: starting speed 1 to 10, how many fruits at once, board size, teleporting through the edges, random walls, and a board that scrolls under you. Scores are kept for every combination.
- **Every key remappable**, and colours and borders to taste.

**HOW LONG CAN YOU GET?**

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
