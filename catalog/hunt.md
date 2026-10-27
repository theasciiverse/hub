A deathmatch in a maze for everyone on your network. There are no rooms,
treasures or monsters, only walls, doors, mines and the other players.
Wander the maze, find the others, and shoot them, throw grenades and
bombs, trip mines, and shoot down walls. The more players you kill before you
die, the better your score; when you die you can come straight back in.

Start Hunt and it looks for a game on your local network. If it finds
one, you join it (if it finds several, you pick); if there is none, it
starts a game on your machine for the others to find. Everyone who
starts Hunt on the same network ends up in the same maze.

## Controls

- **hjkl**: move left, down, up, right; **HJKL**: turn to face that way
- **f** or **1**: fire a bullet; **g** or **2**: throw a grenade; **F**,
  **G** and **3** to **0** and **@**: ever bigger bombs, each costing more
  ammunition
- **o**, **O**, **p**, **P**: throw slime
- **s**: scan for the other players, **c**: cloak against their scans
- **Ctrl-L**: redraw, **q**: quit

You can only fire the way you are facing.

## Options

Started from a shell: `hunt host` joins the game on that machine, `hunt
-q` lists the games on the network, `-m` joins as a spectator who
watches the whole maze, `-n name` sets your name and `-t digit` puts you
on a team.

## Network

Hunt finds games with a broadcast on UDP port 26740, and the game itself
runs over two TCP ports the server picks when it starts. If your
firewall asks, allow Hunt and its server, huntd, rather than a single
port.

## History

Conrad Huang, Ken Arnold and Greg Couch wrote Hunt at the University of
California, San Francisco's Computer Graphics Lab, and Berkeley
distributed it with 4BSD. The Asciiverse edition ports it to Linux and
macOS with its network play intact. It is part of BSD Games in the
Asciiverse catalog, under the BSD licence.
