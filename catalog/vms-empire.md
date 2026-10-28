**TWO EMPERORS. ONE WORLD. ONLY ROOM FOR ONE.**

A full-scale war between you and the computer, on a randomly generated world of continents and oceans. As the game's own README puts it: "Naturally, there is only room for one, so the object of the game is to destroy the other."

You start with a single city and a map you have never seen. Cities build armies, fighters, patrol boats, destroyers, submarines, troop transports, carriers, battleships and satellites. Explore. Take the unclaimed cities before the enemy does. Ship your armies across the sea and destroy the other side. The computer plays by exactly the same rules.

The game saves itself every 10 turns and picks up where you left off the next time you start it.

- **Every arm of war**: nine kinds of piece on land, at sea, in the air and in orbit
- **A new world every game**: choose how much of it is water, how smooth the coasts are and how big the map
- **A fair fight**: the computer gets no extra rules, only the ones you have
- **The ancestor**: in its maintainer's words, "the ancestor of all the multiplayer 4X simulations out there, including Civilization and Master of Orion"

## Controls

Keys work in upper or lower case. **h** shows help for the mode you are in,
and **Ctrl+L** redraws the screen.

In command mode, between rounds:

- **a**: automove, the normal way to play a round
- **z**: the whole world, zoomed out
- **s**: save the game
- **q**: quit

In move mode, when the cursor sits on one of your pieces:

- **q w e / a d / z x c** or the **arrow keys**: move one square
- **Space**: leave the piece where it is
- **y**: send an army to attack the nearest target by itself
- **g**: explore unknown territory
- **s**: sentry, park a piece until something comes near
- **b**: change what a city builds
- **o**: go back to command mode after this round

## Options

- `-w N`: percentage of the world that is water, 10 to 90 (default 70)
- `-s N`: how smooth the coastlines are (default 5)
- `-g WxH`: world size
- `-t`: wrap the map round at the edges
- `-d N`: how long, in milliseconds, each message stays at the top of the screen (default 2000)
- `-S N`: autosave every N turns (default 10)
- `-f file`: use another save file

## History

Walter Bright wrote Empire in the early 1970s as a student at Caltech. It
spread to DEC's VAX/VMS, which gave it the name VMS Empire; Craig Leres
added terminal support and Ed James converted parts to C with curses. In
1987 Chuck Simmons at Amdahl rewrote it completely in C with a new
computer strategy, pieces and map generator, and Eric S. Raymond has
maintained it since around 1990, adding colour in 1994. Its line leads
to Civilization (1990) and Master of Orion (1993).

This edition adds a small patch that lets it build and save games on
Windows.

## Credits

- Original game: Walter Bright
- C version: Chuck Simmons
- Maintainer: [Eric S. Raymond](http://www.catb.org/~esr/vms-empire/)
- Windows console support: [PDCurses](https://pdcurses.org)
- Asciiverse edition: Asciiverse
- License: GPL-2.0-or-later
