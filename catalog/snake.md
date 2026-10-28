**GET RICH. GET OUT. DON'T GET EATEN.**

You are the red `@`. Somewhere on the field lies a `$`, and somewhere an
exit, `#`. And all the while a green snake is coming for you. Grab the
money and another `$` turns up; grab that one too. But as the manual
warns, "As you get richer, the snake gets hungrier."

You never stop moving: you keep going the way you last pointed, so every
turn is a plan. Walk out through the exit whenever your nerve gives out,
and the money is yours. Stay too long and it is the snake's: getting
eaten is worth nothing, and only players who escape make the high-score
table.

- **SPACE WARP!!!** throws you to a random spot when the snake has you
  cornered, at a price
- **A last chance:** if you are caught, a lucky match on the last digit
  of your winnings can still warp you free
- **Your choice of field:** the whole terminal, or a smaller one of the
  size you give it

**How greedy are you feeling?**

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
