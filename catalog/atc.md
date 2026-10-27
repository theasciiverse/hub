You are the air traffic controller. Planes enter the radar from the
edges and take off from the airports, and each one has a destination: an
exit on the edge, which it must leave through at 9000 feet, or an
airport, where it must land facing the right way at altitude zero. You
give every order by typing it, while the clock keeps ticking.

The game ends when a plane runs out of fuel, leaves by the wrong way, or
comes next to another plane at the same height. There is no winning,
only lasting longer: the score is the number of planes you brought home
safely.

Prop planes are capital letters and jets lower case, with their altitude
beside them in thousands of feet. Jets move every tick, props every
other tick.

## Controls

A command is a plane's letter, then what it should do, then Enter. Type
`?` at any point to see what can come next, and Backspace to take back
the last part.

- **a** and a number: climb or descend to that altitude in thousands of
  feet; **a+** and **a-** (or **ac** and **ad**) change it by that much.
  At an airport, climbing means take off
- **t** and a direction: turn to that heading, with **w e d c x z a q**
  for 0, 45, 90 and so on round to 315 degrees; **tl** and **tr** turn 45
  degrees left or right, **tL** and **tR** 90
- **tta**, **ttb**, **tte** and a number: turn towards that airport,
  beacon or exit
- **c**: circle, clockwise; **cl** circles the other way
- **ab** and a number, after a turn or circle: wait until the plane
  reaches that beacon
- **m**, **u**, **i**: mark, unmark or ignore a plane on the radar
- **Enter** on its own, or **Space**: let time pass
- **Ctrl-L**: redraw the screen

From the manual: `atlab1` turns plane A left at beacon 1, `gtte4ab2`
turns plane G towards exit 4 at beacon 2, `ma+2` climbs plane M by 2000
feet, and `stq` turns plane S to 315 degrees.

## Options

Started from a shell, `atc -l` lists the scenarios (Default, Atlantis,
Killer, OHare, TicTacToe, Easy and more) and `atc Killer` plays one;
`atc -s` shows the scores.

## History

Ed James wrote ATC in 1986 and 1987 and contributed it to UC Berkeley,
where it became one of BSD's games. This edition is Mike Sharov's bsd-games, which compiled the
scenarios into the program and redrew the screen with curses.
