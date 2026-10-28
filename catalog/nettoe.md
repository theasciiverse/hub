**THREE IN A ROW. HOW HARD CAN IT BE?**

Noughts and crosses, the game everyone knows, with three ways to play it: against the computer at one of three levels, against a friend sharing your keyboard, or against a friend on another machine over the network. A running score is kept for as long as you both keep saying yes to one more game.

How hard can it be? That depends on the level. Weak is easily fooled. Normal goes for its own wins first. Better checks every winning and blocking move, and you will have to set a real trap to beat it.

- **Head to head over the network**: one of you hosts, the other types in the address, and you play direct, with no server in between.
- **Its own little history**: written in 2000 and 2001 by Gabriele Giorgetti, in Debian since 2001, and taken over in 2009 by Mats Erik Andersson, who added the hardest computer level.

**YOUR MOVE.**

## Controls

Moves and menus are typed and confirmed with **Enter**:

- **a1** to **c3**: your move, row (a, b, c) then column (1, 2, 3), as the
  coordinate grid beside the board shows
- the number of a menu item, or **q** to go back or quit
- **y** or **n** after a game: play again or not

## Playing over the network

One of you hosts: choose Two players over network, then Host the game,
and type a name. The screen lists this machine's addresses; tell your
friend one of them. Your friend chooses Connect to host and types that
address or the host's name. The game uses TCP port 7501, so the host's
firewall has to let it in; on a home network that usually means nothing
at all. Play is direct between the two machines, there is no server in
between.

## Options

- `-4`, `-6`: IPv4 or IPv6 only (both by default)
- `-nb`: no beeps; `-nc`: no colours

## History

Gabriele Giorgetti wrote netToe in 2000 and 2001, adding colours in 1.1.0
(July 2001); Debian has carried it since June 2001 (1.0.5). Mats Erik Andersson took it over in 2009 and added the
harder computer level, IPv6 and terminfo support, releasing 1.5.1 in March
2014, the last version.

The Asciiverse edition adds three fixes: the host screen now lists the
addresses a friend can actually connect to (it used to suggest 127.0.1.1
on many systems), colours no longer turn the screen bright red on
256-colour terminals when they reset, and prompts appear in the static
Linux build.
