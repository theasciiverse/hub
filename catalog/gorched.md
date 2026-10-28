**TWO TANKS. ONE RANGE OF HILLS. FIRE!**

Two tanks face each other across procedurally generated hills, trees and
clouds. Turn your cannon, press Space to start charging, press it again
to fire, and watch the shell arc over the hills. Wherever it lands, the
ground blows out into a crater. Near misses chip away at the other
tank's armour; a direct hit can finish it. Land one and your tank says
so: "Yeeha !", "Take that !", "Rest in pieces !"

The last tank standing scores, the hills are swept away and the next
round starts on new ground. Between rounds, each player spends the
points they earned on Attack (bigger explosions, more shooting power) or
Defense (more armour).

- **Two players, one keyboard**: turn by turn, one shot each.
- **New terrain every round**: or replay the same rounds with `--seed`.
- **Fills your terminal**: with `--ascii-only` and `--low-color` for
  terminals that need them.

**Find the angle. Feel the power. Fire.**

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
