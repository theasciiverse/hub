One of the oldest computer games there is. You are in a cave of twenty
rooms, each joined to three others by tunnels, and somewhere in it lives
the Wumpus. You cannot see it, but you can smell it up to two rooms
away. You can also feel the draft from a bottomless pit next door and
hear the bats that, disturbed, will carry you off to another part of the
cave.

Each turn you either move to a neighbouring room or shoot one of your
five crooked arrows, giving it a path of up to six rooms to fly
through. Hit the Wumpus and you win. Miss, and it may wake up and move;
give the arrow an impossible path and it flies off at random, maybe
straight back into you. Some tunnels only go one way.

## Controls

The game is typed: enter a command and press **Enter**.

- **m** and a room number, such as `m6`: move to that room
- **s** and a list of rooms, such as `s8 4`: shoot an arrow along that path
- **?**: the instructions
- **q**: quit

## Options

Started from a shell, wump builds other caves: `-r` sets the number of
rooms (20), `-t` the tunnels from each room (3), `-p` the pits (3), `-b`
the bat rooms (3) and `-a` the arrows (5), as in `wump -r 30 -a 3`.

## History

Hunt the Wumpus was first presented in the pages of People's Computer
Company in 1973. This version was written for BSD Unix by Dave Taylor of
Intuitive Systems in 1989, and Mike Sharov's bsd-games, the modern Linux
port, prints its instructions directly and highlights the important
words in bold.
