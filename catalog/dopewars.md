**YOU OWE THE LOAN SHARK $5,500. YOU HAVE ONE MONTH.**

You start in the Bronx with $2,000 in your pocket, a coat with room
for 100 units, and a debt that gets bigger every single day. The streets
of New York are your stock exchange. Buy where it's cheap, take the subway
to Manhattan, Brooklyn, Coney Island or Staten Island, and sell where it's
dear. Then do it again. Faster.

The market never sits still. "The Marrakesh Express has arrived!" and
hashish is dirt cheap. "Cops made a big bust! Prices are outrageous!" and
you'd better be holding. Officer Hardass and his deputies are on your
tail, the bank, the gun shop and a bigger coat all cost money you haven't
made yet, and the lady next to you on the subway has opinions: "Does your
mother know you're a dope dealer?"

- **The classic trading game**: eight boroughs and neighbourhoods, a
  dozen goods, prices that crash and spike on the news from the street
- **Run or fight**: when the cops catch up, flee, or shoot it out if you
  bought a gun
- **Deal against real people**: connect to a dopewars server, pick one
  from the public server list, or run your own; trade with other dealers,
  page them, or tip off the cops about them
- **Antique mode**: play it as close to John E. Dell's original Drug Wars
  as it gets

**Pay off the shark. Get rich. Don't get caught.**

## Controls

Each screen tells you which keys it takes. In the market:

- **b**: buy, **s**: sell
- **j**: jet to another part of town
- **l**: list players or high scores
- **g**: give money or drugs to another player (online)
- **q**: quit

When the cops catch up with you, **r** runs and **f** fights, if you have a
gun.

## Options

- `-n`: single player, without the server menu
- `-o host`: connect to a dopewars server, `-p port` (default 7902)
- `-s`: run a public server, `-S` a private one
- `-c`: add a computer player to a server
- `-a`: "antique" mode, as close to the original Drug Wars as possible
- `-P name`: your dealer's name
- `-b`: no colours

High scores are kept in `~/.local/state/dopewars.sco`.

## History

John E. Dell's Drug Wars was an MS-DOS game; Ben Webb rewrote it as
dopewars for Unix and Windows from 1998, adding networked multiplayer, a
metaserver listing public servers, and a configurable everything.

The Asciiverse edition is the text-mode client and server only, with two
small changes: high scores
go in your own state folder, and the static build finds your system's
certificates to reach the metaserver.

## Credits

- Original game: John E. Dell (Drug Wars)
- dopewars: [Ben Webb](https://dopewars.sourceforge.io/) and contributors
- Asciiverse edition: Asciiverse
- License: GPL-2.0-or-later
