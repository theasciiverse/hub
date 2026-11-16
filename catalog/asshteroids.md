**THE ROCKS ARE FOR EVERYONE. SO IS YOUR SHIP.**

A little triangle wakes up blinking in a field of tumbling rocks, and it is not alone out here. Vesta is already shooting. Pallas is circling something big. Somewhere past the edge of the screen Juno is racking up points, and the board in the corner says so. Turn, burn, fire: a large rock cracks into two medium ones, a medium one into two small, and the small ones are the fast, nasty, valuable ones.

This is Asteroids with company. The field wraps around on itself, far bigger than your screen, and a map in the corner shows every ship in it. The rocks drift, bounce off each other and keep coming, and shots stop shots. Every other ship is a rival chasing the same rocks and the same top score, and any of them can turn its gun on you. A ship you shoot down is worth a thousand points. So are you.

- **Rocks**: 20 for a large one, 50 for a medium, 100 for a small
- **Ships**: 1000, whoever is flying them
- **Three lives**, three seconds of blinking safety after each, and your best score kept between games

The computer pilots are named for asteroids, Vesta, Pallas, Juno, Hygiea, Eros, Ida, Gaspra and Psyche, and they fly by the same keys you do: they pick the rock most likely to hit them, lead their shots, back off from a rock too close, and now and then come looking for you. And the moment the game starts, the field is open to your local network: the start screen shows the line, and a friend at another computer flies in with nothing but `ssh -p 2222` and your address. Their ship appears next to yours, name and all, and press **C** to talk.

**Clear the field. Then clear the board.**

## Controls

- **A** and **D**, the **left and right arrows** or **J** and **L**: turn
- **W**, the **up arrow** or **I**: thrust
- **U** and **O**: thrust while turning left or right
- **Space**: fire
- **C**: chat with everyone in the field; **Enter** sends, **Esc** closes
- **Space** or **Enter** after a crash: fly again; **Esc**: back to the start screen
- **Q**: quit

## Options

- `-bots N`: computer pilots in the field (3, up to 8)
- `-name NAME`: your name in the field (your login name otherwise)
- `-offline`: play without opening the field to the network
- `-join host[:port]`: fly into a friend's game (runs `ssh`)
- `-demo`: watch the computer fly your ship; any key ends it
- `-server`: only serve the field, for others to join with `ssh -p 2222`

## History

Tomas Zifcak started ASSHTEROIDS at the end of January 2026 with a single commit called "batman", and in the first week of February had the field shared: one Go server, one world, and anyone with ssh flying in it. Usernames, a respawn countdown, a minimap, a "killed by" on the death screen, scores and chat followed over the next weeks, and he put it online for anyone to join. The Asciiverse edition brings that field home: it plays right where you start it, with computer pilots so it is never empty, and your friends on the network one ssh away.

## Credits

- ASSHTEROIDS: Tomas Zifcak ([github.com/tomz197/asshteroids](https://github.com/tomz197/asshteroids))
- Asciiverse edition: computer pilots, playing and hosting from one program, the demo
- License: MIT
