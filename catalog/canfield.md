Canfield is a solitaire played for money. Thirteen cards make
the stock; the first card of the foundation sets the base rank for all
four foundations, which build up by suit and wrap from king to ace. The
four tableau piles build down in alternate colours and move only as
whole piles, and an empty space is filled from the stock. Deal the
hand to the talon three at a time.

This version keeps the books. The deal costs $13, a look at
the game before buying it another $13, the rest of the game $26, and
every card on a foundation pays $5. Each run through the hand after the
first costs $5, card counting costs $1 a card, and time costs $1 a
minute. Your account carries over from game to game.

## Controls

Each move is two letters or digits, typed at the Move prompt:

- **s#** and **sf**: stock to tableau pile #, or to the foundation
- **t#** and **tf**: talon to a tableau pile, or to the foundation
- **##**: tableau pile to tableau pile
- **#f**: tableau pile to the foundation
- **ht**: deal the hand to the talon
- **c**: card counting on or off
- **b**: the betting account, **i**: the instructions, **x**: hide the box
- **q**: give up this game

## History

Steve Levine wrote Canfield at UC Berkeley (the copyright is from 1980).
Steve Feldman moved it to curses and debugged it, Kirk McKusick and
Mikey Olson added card counting, McKusick the betting, and Eric Allman
and McKusick cleaned up the interface. This edition keeps the betting account
in the player's own data folder rather than a system file. It is part
of BSD Games in the Asciiverse catalog, under the BSD licence.
