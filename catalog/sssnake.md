**SMART. FAST. HUNGRY. IT CAN PLAY WITHOUT YOU.**

The snake game you know, drawn in solid blocks instead of letters: eat the
food, grow longer, don't run into yourself or the walls. Steer it with the
arrows, WASD or Vim keys, or try arcade mode, where every bite makes it
faster.

Then hand over the controls. In autopilot the snake hunts the food on its
own with A* or breadth-first search, and with `--try-hard` it plans ahead
so it never traps itself, curling round the board until it nearly fills
it. Turn the speed up and leave it running as a screensaver.

- **Four modes**: normal, arcade, autopilot and screensaver
- **Four looks**: fancy, full, ASCII and dots
- **Your board**: any size, walls that teleport you across, and random
  junk to steer round

**LET IT EAT.**

## Controls

- **Arrows**, **WASD** or **HJKL**: steer
- **Space**: pause; **Q**: quit
- Autopilot and screensaver: **+** and **-** change the speed; in the
  screensaver any other key quits

## Options

- `-m arcade`, `-m autopilot`, `-m screensaver`: the mode
- `-l full`, `-l ascii`, `-l dots`: the look
- `-s 15`: the speed, 1 to 20; `-x 30 -y 20`: the board size
- `-j 3`: junk on the board, 1 to 5; `-t`: teleport through the walls;
  `-z`: show the snake's size
- `--try-hard 1` or `2`: an autopilot that keeps itself alive;
  `--short-path=bfs`: breadth-first search instead of A*

## Credits

- sssnake: [AngelJumbo](https://github.com/AngelJumbo/sssnake)
- Autopilot solvers after chuyangliu's greedy snake solver
- License: MIT
