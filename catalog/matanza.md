**-=> KABOOM ! Vega is destroyed by Orion . . .**

Your ship sits in the middle of the screen, a smear of ASCII art that
turns into a ship the moment it moves. Turn, thrust, let it coast: this
is space, and you keep the speed you build. Letters at the edge of the
screen point to the other ships, small while they are far, capitals as
they close in, and an asterisk when it is time to open fire. Then the
dots between you fill with bullets, an asteroid tumbles through, and
someone gets a missile in the wing.

Everything in Matanza is a real picture, rotated through sixty-four
angles and drawn into characters as it flies, so the bigger your window,
the finer the battle. Every ship has five lives; lose them and you are
sent out of the game, to the server's cheerful commentary.

Play against computer ships here, or open the game to your network:
friends join with Matanza's own **Join a friend**, or with nothing but
`ssh -p 2022` and your address, and each one who joins takes the place
of a computer ship.

## Controls

- **Left**, **Right** (or **h**, **l**): turn
- **Up** (or **k**): thrust; **Down** (or **j**): brake
- **Space**: fire; **b** fires backwards
- **n**: small missile (seven); **m**: missile (two)
- **+**, **-**: zoom in and out
- **[**, **]**: watch the battle from another ship
- **Enter**: say something to everyone
- **w**, **z**: who is playing, and the scores
- **p**: pause the universe, for everyone
- **q**: quit (**y** to confirm); **Q** quits at once

At the start, press Enter through the opening, take the name you are
offered or type your own (up to eight letters), and press Enter.

## Options

- `--play`, `--host`, `--join host[:port]`: skip the menu
- `--ships N`: computer ships (3, up to 8)
- `--server`: host on the network without playing

## History

Alejandro Forero Cuervo released Matanza on 4 September 2000, a game of
the Freaks Unidos at bachue.com, written as a literate program in Donald
Knuth's CWEB. It was played over telnet: one machine ran the server and
everyone typed `telnet yourhost 7993`. "Currently, the only way to play
is through telnet. That's correct, telnet," said its README, which also
asked you to say it right: *Matanga*. It promised computer-controlled
ships one day, and a protocol so programs could fly them. Debian took the
game up in 2004 and its games team has kept it building ever since;
bachue.com lives on in the
[Wayback Machine](https://web.archive.org/web/20071226080243/http://bachue.com/matanza/).
This edition keeps that battle and gives it the computer ships it was
waiting for, with SSH in place of telnet.

## Credits

- Matanza: Alejandro Forero Cuervo, Freaks Unidos, 2000 to 2003
- Debian packaging and fixes: Polkan Alexis Garcia Rodriguez, Frank
  Lichtenheld, Peter Pentchev, Bart Martens, Nobuhiro Iwamatsu, Boris
  Pek, Patrice Duroux, Alexandre Detiste and the Debian Games Team
- Asciiverse edition: computer ships, the menu, play over SSH on the
  local network, and fixes for today's terminals
- License: GPL-2.0 or later
