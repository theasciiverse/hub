**NO ROOMS. NO TREASURE. NO MONSTERS. JUST EACH OTHER.**

"The object of the game hunt is to kill off the other players." That's
the manual's whole pitch, and it's enough. Everyone on your network
drops into the same maze. Wander it, find the others, and shoot. Throw
grenades. Throw bombs: satchel charges, big bombs, even bigger bombs, all
the way up to the "very, very big bomb" and the biggest of all, if
you've saved the ammunition. Throw slime that oozes round the walls. Trip
mines, or defuse them for charges. Shoot down walls, and watch them grow
back.

You can only fire the way you're facing, and you can't see behind you.
Shots glance off diagonal walls and scatter through doors. Scan to see
where everyone is; cloak to hide from their scans. Every kill raises your
score, and when you die you can come straight back in.

Start Hunt and it looks for a game on your local network. If it finds
one, you join it (if it finds several, you pick); if there is none, it
starts a game on your machine for the others to find.

A word of warning from the original README: "hunt may be dangerous to
your health. "Arthritic pain" and "lack of circulation" in fingers have
been reported by hunt abusers."

**Find them. Face them. Fire.**

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
