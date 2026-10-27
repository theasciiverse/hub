The original Star Trek game of BSD Unix. The Klingons are invading the
Federation, and the Enterprise has a limited number of stardates to
destroy them. Warp between the quadrants of the galaxy, scan for enemies,
fight with phasers and photon torpedoes, and dock at starbases to refuel
and repair, while damage, novas, black holes and distress calls get in
the way.

It plays like a 1970s terminal session: you type a command, the computer
prints the result. Nothing is on screen until you ask for it, so the
scans are your eyes.

## Controls

Type a command and press Enter. Each command can be shortened to its
first letters, and anything the game needs that you leave out, it asks
for. `?` lists what it accepts at any prompt.

- `srscan` and `lrscan`: short and long range scans
- `move`: travel under warp power, at the factor set with `warp`;
  `impulse` for short hops
- `phasers` and `torpedo`: fight
- `shield up` or `shield down`, `cloak`
- `dock` and `undock` at a starbase, `rest` to repair
- `status`, `damages`, `computer` for charts and course calculations
- `dump` saves the game; answer `restart` to "What length game" to
  continue it
- `terminate` ends the game

At the start you choose the length (`short`, `medium`, `long`) and the
skill (`novice` to `impossible`).

## History

Eric Allman wrote Trek at UC Berkeley in 1976, and it was part of BSD's
games from then on. This edition comes from Kenji Rikitake's bsdtrek,
the FreeBSD and DragonFly BSD version made to build on Linux. The
Asciiverse fixes the build for current compilers and Windows, keeps the
saved game safe from updates, and makes restoring work again: it had
been broken on every current system.

The same game, without the Star Trek names and with the whole map always
on screen, is in the catalog as Space Pirate Hunt, from BSD Games.
