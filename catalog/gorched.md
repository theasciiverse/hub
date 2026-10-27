Two tanks face each other across a range of procedurally generated hills,
trees and clouds. Take turns setting your cannon's angle and charging up
your shot, watch the shell's arc, and blow craters in the landscape until
one of you lands a hit. The winner scores, the hills are swept away and the
next round starts on new terrain.

Two players share one keyboard. Between rounds each player spends the
points they earned on Attack (bigger explosions, more shooting power) or
Defense (more armour).

## Controls

- **Left** and **Right**: turn the cannon
- **Space**: start charging; press again to fire at the power shown
- **s**: score board
- **a**: player attributes
- **h**: help
- **Ctrl+R**: restart the round
- **Ctrl+N**: skip to the next round
- **Ctrl+C**: quit

In the score and attributes windows, **Tab** moves between buttons and
**Enter** presses one.

## Options

- `--seed N`: replay the same sequence of rounds
- `--width N`, `--height N`: set the world size instead of filling the terminal
- `--ascii-only`: draw the tanks with plain ASCII, if you see question marks
- `--low-color`: use only the 8 basic colors, if the colors look wrong
- `--fps N`: lower the frame rate to save CPU

## History

Ján Čabala wrote Gorched in Go in 2020 as a homage to Scorched Earth,
Wendell Hicken's 1991 DOS artillery game, and has kept releasing it since.

## Credits

- Game: [Ján Čabala (zladovan)](https://github.com/zladovan/gorched)
- Engine: [termloop](https://github.com/JoelOtter/termloop) by Joel Auterson, terrain from [opensimplex-go](https://github.com/ojrac/opensimplex-go)
- Asciiverse edition: Asciiverse
- License: MIT
