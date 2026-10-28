**THE KLINGONS ARE INVADING. YOU HAVE ONE SHIP AND NOT MUCH TIME.**

Klingon warships are spreading across the galaxy. Starbases are calling for
help, inhabited star systems are under attack, and you have a limited number
of stardates to destroy every last invader. You command the Enterprise.

Warp between the quadrants, scan near and far, fight with phasers and photon
torpedoes, raise the shields, cloak, and dock at a starbase to refuel and
repair. Your bridge crew keep up a running commentary ("Chekov: But captain,
we are not adjacent to a starbase."), and there are novas, black holes,
tractor beams and a self-destruct sequence that asks for the password.

Get it wrong and the game has a long list of ways to tell you. "You ran into
the negative energy barrier." "You have burned up in a star." "Well, you
destroyed yourself, but it didn't do any good." Abandon ship and you are
"hereby put in charge of an antiquated but still functional ship, the Fairie
Queene." Win, and you may even be promoted.

It plays like a 1970s terminal session: type a command, read the result.
Nothing is on screen until you ask for it, so the scans are your eyes.

- **Eric Allman's original Trek**, written at Berkeley in 1976 and a BSD
  game ever since
- **Short, medium or long games**, at skill levels from novice to
  impossible
- **Every command can be shortened**, and `?` lists what each prompt
  accepts

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
