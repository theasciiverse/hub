Naval combat in the days of wooden ships, from the 1770s to the end of
Napoleonic France. You command one man-of-war in a historical battle,
from single-ship duels such as Ranger against Drake to John Paul Jones
boarding the Serapis at Flamborough Head and full fleet actions: 31
scenarios in all. The computer captains the other ships.

Every turn you give your orders: how far to sail and when to turn, which
sails to set, when to fire your broadsides and with what shot, when to
grapple and board. The wind decides what is possible. Full sails make
you fast but get shredded by round shot, a ship that stops moving starts
to drift, and the captain who holds the weather gage usually wins.

Ships are shown as two characters for bow and stern, such as `a0` for
the first American ship. A capital letter means full sail is set, `!`
means the ship has struck its colours, `~` that it is sinking and `#`
that it is on fire.

## Controls

- **Arrow keys** or **j** and **k**: choose a scenario, ship and loads at the start; **Tab** or **Space** moves between the lists, **Enter** starts
- **m**: move, then a string of turns and moves such as `l3` (turn left, three ahead)
- **f**: fire broadsides, **l**: reload, **L**: unload to change shot
- **c**: change sails, **r**: repair
- **g**: grapple or let go, **u**: try to unfoul
- **b**: board an enemy ship, **B**: recall boarding parties
- **i**: the closest ship, **I**: all ships, **F**: find ships
- **C**: centre the view on your ship, **U**, **D**, **H**, **J**: move the view, **S**: follow your ship or not
- **Ctrl-L**: redraw, **q**: quit

The game's manual (`man sail`, also in the archive as `sail.6`) explains
movement, wind, shot types, boarding and every scenario in detail.

## History

Dave Riggle wrote the first Sail on a PDP-11/70 at Berkeley in the fall
of 1980, after Avalon Hill's board game Wooden Ships and Iron Men. Ed
Wang rewrote it almost from scratch in 1983, and Craig Leres made it
portable. It shipped with BSD Unix as a multi-player game for everyone
logged in to the same machine, with a separate driver program moving the
computer's ships.

In 2016 Mike Sharov rebuilt it for his bsd-games as a single-player
game: one program with its own computer captains, a new curses display
and the 31 scenarios built in. It is part of BSD Games in the Asciiverse
catalog.
