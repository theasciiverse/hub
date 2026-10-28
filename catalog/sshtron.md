**KEEP MOVING. LEAVE A WALL. BOX THEM IN.**

The grid is black. Your cycle is moving, and it is not going to stop.
Behind you it leaves a wall of light, and every other rider leaves one
too. Touch a wall, any wall, yours included, and you are gone: back at
once somewhere else on the grid with a score of zero and a fresh trail,
leaving a spot of your colour in the one you hit.

Your score climbs for every second you stay alive, and faster the more
riders there are. Box the others in, cut across their path, leave them
nowhere to turn. Seven colours fit in one arena: red, green, yellow,
blue, magenta, cyan and white.

SSHTron was built in about twenty hours at a hackathon, to be played
with nothing but `ssh`, and it still can be. Pick **Play** and you race
computer riders on a grid hosted on your own machine; anyone on your
network can ride in with `ssh -p 2022` and your address, or with
SSHTron's own **Join a friend**. **Play online** takes you to the
original public server at sshtron.zachlatta.com, where whoever else is
online that day shares the grid.

**Stay alive. Stay moving.**

## Controls

- **W A S D**, the **arrow keys** or **h j k l**: steer (also **z q s d**
  and **, a o e**)
- **Esc** or **Ctrl+C**: leave the game

In the menu, **Colour** asks for the colour you ride in; a computer rider
in it makes way for you.

## Options

- `-play`, `-online`, `-join host[:port]`: skip the menu
- `-color red`: ask for a colour
- `-bots N`: computer riders in each game (3, up to 6)
- `-demo`: watch the computer ride for you; any key ends it
- `-server`: run only the server, for others to join with `ssh -p 2022`

## Credits

- SSHTron: Zach Latta and Max Wofford, with Ali Yousuf and others
  ([github.com/zachlatta/sshtron](https://github.com/zachlatta/sshtron)),
  2016, written in Go at BrickHack 2
- Arrow keys and trail fixes: Yerlotic
  ([github.com/yerlotic/sshtron](https://github.com/yerlotic/sshtron))
- Asciiverse edition: the menu, the built-in SSH client, computer riders,
  games on the local network, and fixes for a server
  that could crash under load
- License: MIT
