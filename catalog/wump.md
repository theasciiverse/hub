**SOMETHING IN THIS CAVE SMELLS TERRIBLE. AND IT'S HUNGRY.**

One of the oldest computer games there is. You are in a cave of twenty rooms, each joined to three others by tunnels, and somewhere in it lives the evil Wumpus. You cannot see it. But you can smell it: `*sniff* (I can smell the evil Wumpus nearby!)`. You can feel the draft from a bottomless pit next door: `*whoosh*`. And you can hear the bats that, if you blunder in, will carry you off to another part of the cave: `*rustle* *rustle*`.

Your quiver holds five "custom super anti-evil Wumpus arrows", and they are crooked: you tell each one which rooms to fly through, up to six. Hit the Wumpus and you win. Miss, and it may wake up and move, maybe right into your room. Give an arrow an impossible path and it flies off at random, maybe straight back into you. Some tunnels only go one way.

Walk into the wrong room and the game will tell you all about it: "Much to the delight of the Wumpus, you walked right into his mouth, making you one of the easiest dinners he's ever had!" Or you fall into a pit, and "have a lot of time to reflect on this error as you fall many miles to the core of the earth."

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
