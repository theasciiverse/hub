Each side starts with 12 men. Men move one square diagonally forward;
a man that reaches the far side becomes a king (**K**), which moves
diagonally both ways. You capture by jumping over an enemy piece, and
can capture several in one turn with a chain of jumps. If you can jump,
you must. A side wins when the other cannot move, and 50 turns without
any gain for either side is a draw.

At the start the game asks who plays each side: by default you play
black, shown in red, which moves first, and the computer plays white.
Two people can share one keyboard, and the computer can play itself.
Without `-p` the computer starts out weak, so a beginner can win the
first game, and after that it adjusts to how well you play.

## Controls

- **Arrow keys**, **hjkl** or **wasd**: move
- **Enter**: on your piece, pick it up; on a free square, move it there.
  In a chain of jumps, pick the same piece up again for each jump
- **Mouse**: click instead of Enter
- **F1** or **?**: help on the controls, **F2** or **!**: how to play
- **q** or **Esc**: resign

## Options

- `-1 h` or `-1 c`: a human or the computer plays black
- `-2 h` or `-2 c`: the same for white; either one skips the questions
- `-p 3`: a fixed strength for the computer, from 1 to 127
- `-n`: quit after one game instead of offering a rematch

## History

Checkers is one of the games abakh wrote for New BSD Games, a collection
of small curses games started in 2018 and named after the classic BSD
games. The collection is packaged by Debian, Ubuntu, openSUSE, Alpine,
Nix, Homebrew, FreeBSD and pkgsrc, and is in the AUR.