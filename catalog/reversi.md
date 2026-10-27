Black (X) and white (O) take turns putting a disc on the 8x8 board. A
disc has to trap at least one line of the other side's discs between
itself and another disc of yours, across, down or diagonally, and every
trapped disc turns over to your side. A side that cannot move is skipped;
when neither can, the side with more discs wins.

At the start the game asks who plays each side: by default the computer
plays white and you play black, which moves first. Two people can share
one keyboard, and the computer can play itself. Without `-p` the
computer starts out playing at random and adjusts after every game,
playing better after you win and worse after it wins.

## Controls

- **Arrow keys**, **hjkl** or **wasd**: move
- **Enter**: put your disc
- **Mouse**: click to put your disc
- **F1** or **?**: help on the controls, **F2** or **!**: how to play
- **q** or **Esc**: resign

## Options

- `-1 h` or `-1 c`: a human or the computer plays white
- `-2 h` or `-2 c`: the same for black; either one skips the questions
- `-p 3`: a fixed strength for the computer, from 1 to 127
- `-n`: quit after one game instead of offering another

## History

Reversi is one of the games abakh wrote for New BSD Games, a collection of
small curses games started in 2018 and named after the classic BSD games.
The collection is packaged by Debian, Ubuntu, openSUSE, Alpine, Nix,
Homebrew, FreeBSD and pkgsrc, and is in the AUR.