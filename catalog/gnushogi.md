**NINE BY NINE. EVERY CAPTURE CHANGES SIDES.**

Shogi is chess as Japan plays it, and it never runs dry. The board is
nine squares by nine, the pieces are generals, silvers, lances and
knights, and anything you take is yours: it waits in your hand, and on
any later move you can drop it back onto the board as one of your own.
Reach the far ranks and most pieces promote. Checkmate the king and the
game is yours.

GNU Shogi sits across the board. It opens from a book of thousands of
known positions and searches on the clock you choose.

- **Ten time controls**: from 40 moves in 5 minutes to half an hour a
  move, or the whole game on one clock with a Fischer bonus.
- **A real opponent with a soft side**: ask for a `hint`, take moves back
  with `undo`, switch sides mid-game, or set a shallower `depth` for a
  gentler game.
- **Watch it think**: the depth of its search as it plays, and with `post`
  the line it expects.
- **Tsume mode**: set up a position with `edit` and let it hunt for a
  forced mate.
- **Keep your games**: `save` and `get` pick a game up where you left it.

Matthias Mutz built GNU Shogi in 1993 by teaching GNU Chess 4.0 the rules
of shogi, piece by piece; maintainers kept it going for twenty years
after.

**Take a piece. Drop it back. Close the net.**

## Controls

Type a move and press Enter, using the labels round the board (files 9
to 1, ranks a to i):

- **7g7f**: move the piece on 7g to 7f; **S6h**: the silver to 6h
- **2d2c+**: move and promote
- **P\*5e**: drop a pawn from your hand onto 5e
- **hint**, **undo**, **remove** (take back a whole move), **switch**
- **save**, **get**, **new**, **help** (every command), **quit**

## Credits

- GNU Shogi: Matthias Mutz (1993), after GNU Chess 4.0 by John Stanback
  and the Free Software Foundation; maintained by Mike Vanier, Luis Felipe
  Strano Moraes and Yann Dirson
  ([savannah.gnu.org/projects/gnushogi](https://savannah.gnu.org/projects/gnushogi/))
- License: GPL-3.0-or-later
