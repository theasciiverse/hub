You have crash-landed on an alien planet with a toxic atmosphere, so you
stay inside your robotic base and send robots out instead. You program
them in a small functional language: move, grab, build, scan, and later
loops, conditions, recursion and whole fleets of robots running their own
programs. Every resource they bring back lets you craft better devices,
which give your robots new abilities and new language features, which let
them gather more.

Start with the Tutorial from the main menu; it teaches the language one
idea at a time. Then try Classic or Creative games on a generated world, or
the challenges: Sokoban, mazes, Towers of Hanoi, ranching, bridge building
and more. Progress and achievements are saved automatically.

## Controls

- Type commands at the prompt and press **Enter** to run them, for example
  `move` or `build {move; grab}`; **Ctrl+C** or **Esc** stops a program
- **Alt+W**, **Alt+E**, **Alt+R**, **Alt+T**: focus the world, robot,
  prompt and info panels; the mouse works too
- **Arrow keys** or **h j k l**: scroll the world view
- **F1**: help, **F2**: robots, **F3**: recipes, **F4**: commands,
  **F5**: messages, **F6**: structures
- **Ctrl+G**: show the current goal
- **Ctrl+P**: pause, **Ctrl+X** and **Ctrl+Z**: double and halve the speed
- **Ctrl+Q**: quit

## Options

- `--scenario NAME`: start a scenario directly, e.g. `Tutorials/move`
- `--seed N`: world seed for generated worlds
- `--autoplay`: watch a scenario's built-in solution
- `--speed N`: starting game speed
- `swarm keybindings`: list every key binding

## History

Brent Yorgey started Swarm in 2021, written in Haskell with the Brick
terminal UI library, and it has grown into a community project with more
than thirty contributors. This edition has one small change: it
finds its data folder next to the program, so it runs straight
from the install folder.

## Credits

- Game: [Brent Yorgey and the Swarm contributors](https://swarm-game.github.io/)
- Asciiverse edition: Asciiverse
- License: BSD-3-Clause
