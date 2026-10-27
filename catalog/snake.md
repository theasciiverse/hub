You are the red `@`. Somewhere on the field is a `$`, and somewhere an
exit, `#`. A green snake, `@` for its head and `s` for its body, hunts
you all the while. Grab the money, and a new `$` appears; the richer you
get, the hungrier the snake. Leave by the exit whenever you like to bank
your winnings, but getting eaten is worth nothing.

You keep moving in the direction you last chose, so plan your path
around the snake. When it has you cornered, a space warp throws you to a
random spot, at a price. If the snake does catch you, a lucky roll on
the last digit of your winnings can still warp you free.

## Controls

- **Arrow keys** or **hjkl**: change direction
- **w**: space warp, at a cost
- **q** or **F10**: quit

## Options

Started from a shell, `snake 40 20` plays on a field 40 wide and 20 high
instead of the whole terminal, and `snake -s` prints the high scores.

## History

Snake was written at UC Berkeley in 1980 and shipped with BSD Unix as one
of its "crt hack" games, made for the video terminals of the day. Mike Sharov
gave it a new chase algorithm and a longer, deadlier snake in 2016 for
his bsd-games, the modern Linux port. Only players who escape by the
exit make the high-score table.
