Angband for many players. You create a character, set out from the town,
and go down into the dungeon below, level after level, towards Morgoth,
Lord of Darkness, a hundred levels deep. Everything is a letter on the map:
you are the `@`, monsters are letters of their own, and the numbers in town
are the shops' doors. Races run from Hobbits and Ents to Dragons and
Hydras, classes from Warriors and Mages to Necromancers and Shapechangers.

PWMAngband is always a server and a client. Started from Asciiverse, it runs
a private server on your machine and connects you to it: the world and your
characters are kept for the next time, and friends on your network can join
the same world. The first time, you choose an account name and password;
they protect your characters on that server.

## Controls

- **Arrow keys** or **1** to **9**: walk (diagonals on 1, 3, 7 and 9);
  walking into a shop's number goes inside, **Escape** leaves
- **<** and **>**: stairs, **R**: rest, **,**: stay still
- **i**: inventory, **e**: equipment, **g**: pick up, **d**: drop
- **w**: wear or wield, **q**: quaff, **r**: read, **E**: eat,
  **f**: fire, **m**: cast a spell
- **l**: look, **M**: map of the level
- **:**: chat with other players
- **?**: help, **Ctrl-X**: save and quit (**Q** and **Ctrl-C** retire the
  character for good)

## Playing online

`pwmangband-play <host> [port]` joins a server elsewhere (the default port
is 18346), and `pwmangband-play --list` shows the servers listed on the
mangband.org metaserver. A server must run the same version.
On 17 October 2026 none on the list did: it showed MAngband servers and one
older PWMAngband 1.4.0 server, which did not answer, and the servers named in
PWMAngband's own manual no longer exist.

## History

Angband goes back to 1990, to Umoria and to VMS Moria (1985). MAngband
made it a game for many players, and PWMAngband carries that on: it is
based on Angband 4.2 and MAngband 1.5, and the MAngband and PWMAngband
developers maintain it on GitHub. This edition has only its curses
client, with your files kept in your own data folder.

## Credits

- Game: the MAngband and PWMAngband developers (draconisPW and others), after
  Angband by Ben Harrison, Robert Alan Koeneke and James E. Wilson
- Asciiverse edition: Asciiverse
- License: GPL-2.0 (or the Angband licence)
