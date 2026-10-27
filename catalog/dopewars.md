You start in the Bronx with $2,000, a $5,500 debt to the loan shark that
grows every day, and a coat with room for 100 units. You have a month. Buy
drugs where they are cheap, jet to another part of New York, sell where
they are dear, and stay ahead of Officer Hardass and his deputies. Prices
crash and spike with the news on the street; guns, the bank and a bigger
coat are there if you can pay for them.

Play alone, or connect to a dopewars server and deal against other people,
who can trade with you, page you and tip off the cops about you.

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
