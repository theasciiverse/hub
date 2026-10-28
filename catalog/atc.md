**YOU'RE IN THE TOWER. THE PLANES DON'T STOP COMING.**

ATC "lets you try your hand at the nerve wracking duties of the air traffic
controller without endangering the lives of millions of travelers each
year." So says its manual, and it is right about the nerves.

Jets and prop planes appear at the edges of your radar and wait on the
runways, each with somewhere to be: out through one particular exit at 9000
feet, or down at one particular airport, facing the right way, at altitude
zero. You give every order by typing it (`atlab1`, `gtte4ab2`) while the
clock ticks and the next plane is already coming in.

Let two planes come within a square and a thousand feet of each other and
it's over. The same if one runs out of fuel, lands at the wrong airport,
leaves by the wrong exit or wanders out of your airspace. There is no
winning, only lasting: your score is the number of planes you brought home
safely.

- **Props and jets**: capital letters are props, lower case are jets, and
  the jets move twice as fast
- **Scenarios** from Easy and Novice to Killer, OHare and TicTacToe
- **A command line learned in minutes**: type `?` at any point to see
  what can come next
- **A BSD classic** by Ed James, 1986 and 1987

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
