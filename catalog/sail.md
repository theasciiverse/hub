**RUN OUT THE GUNS, CAPTAIN.**

You hold a commission in the Sail Navy and a wooden warship under your
feet. Every turn you give the orders: how far to sail and when to come
about, which sails to set, when to "let loose the terrible destruction"
of your broadsides (the manual's words) with round, double, chain or
grape shot, and when to throw out the grapples and board. The computer
captains everything else on the water.

The wind decides what is possible. Full sail makes you fast, until round
shot shreds it. A ship that stops moving drifts. And as every captain of
the day knew, whoever holds the weather gage usually wins.

- **31 battles** from the 1770s to the fall of Napoleon: Ranger against
  Drake, John Paul Jones boarding the Serapis at Flamborough Head,
  Constitution against Guerriere, and full fleet actions
- **A few that history forgot:** the Curse of the Flying Dutchman, the
  South Pacific aboard the USS Scurvy (crew rating: mutinous), and a
  Battle of Midway fought by Enterprise and Akagi under canvas
- **Every ship on one screen**, two letters for bow and stern: capitals
  under full sail, `!` when she has struck her colours, `~` sinking,
  `#` on fire

**Clear for action.**

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
