Two sides take turns writing an S or an O in an empty square of a 5x6
board. Every S-O-S your letter completes in a straight line, across,
down or diagonally, scores you a point, and its letters take your
colour (green when both sides used them). Turns alternate whether you
scored or not. When the board is full, the higher score wins.

At the start the game asks who plays each side: by default you play
blue, which moves first, and the computer plays yellow. Two people can
share one keyboard, and the computer can play itself. Without `-p` the
computer starts out playing at random and adjusts after every game,
playing better after you win and worse after it wins.

## Controls

- **Arrow keys** or **hjkl**: move
- **S** or **O**: write that letter
- **Mouse**: left click writes S, right click writes O
- **F1** or **?**: help on the controls, **F2** or **!**: how to play
- **q** or **Esc**: quit

## Options

The command is `sos`.

- `-1 h` or `-1 c`: a human or the computer plays blue
- `-2 h` or `-2 c`: the same for yellow; either one skips the questions
- `-p 3`: a fixed strength for the computer, from 1 to 127
- `-n`: quit after one game instead of offering another

## History

SOS is one of the games abakh wrote for New BSD Games, a collection of
small curses games started in 2018 and named after the classic BSD games.
The collection is packaged by Debian, Ubuntu, openSUSE, Alpine, Nix,
Homebrew, FreeBSD and pkgsrc, and is in the AUR.