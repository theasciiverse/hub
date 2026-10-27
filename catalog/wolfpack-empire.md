Empire is a war game played over the Internet since the 1980s. You run a
country on a shared world: explore the land around your capital, designate
sectors as farms, mines, factories and harbours, grow your population,
research technology, and build ships, planes and armies. Then deal with
your neighbours, who are real people, through trade, alliances,
telegrams and war. The world moves on whether you are logged in or not: updates
happen on a schedule, and a game runs for weeks.

This is the Empire client. It connects straight to Wolfpack Fever, the
game the Wolfpack team keeps running all year: no registration, grab a
country and go.

## Getting started

At the prompts, use one of the countries **1** to **8**, with the same
number as the password. Countries start in sanctuary, safe from attack;
the `break` command ends it, and breaking sanctuary counts as a promise to
play the game. Using more than one country is not allowed.

To look around first, log in as country `visitor` with any password and
read the message of the day (`motd`) and the newspaper (`newspaper`).

## Commands

Type commands at the `Command :` prompt. A few to start with:

- `nation`: your country at a glance
- `map #`: the map around you
- `census *`: your sectors
- `explore c 0,0 5 gh`: move 5 civilians from 0,0 west and claim land
  (directions `y u g j b n`, `h` to stop)
- `designate 2,0 m`: make a sector a mine
- `read`: your telegrams; `wire` for announcements, `newspaper` for the news
- `declare` and `relations`: alliances and war
- `info`: the built-in manual, and `info <command>` for any command
- `quit`: log out; your country stays in the game

## Options

- `empire COUNTRY PASSWORD`: log in without the prompts
- `-s host:port`: play on another Empire server
- `-u`: UTF-8 output
- `-2 file`: keep a log of the session

## History

Empire goes back to Peter Langston's game of the late 1970s and early
1980s. Dave Pare's reimplementation at UCSD in 1986 started the open line
of code, carried on through BSD Empire, KSU, Chainsaw and Empire 3 to
Wolfpack, who have developed it as Empire 4 since 1996. Wolfpack still hosts games and the code is still
developed.

This edition is the client, unchanged except that it connects to
Wolfpack Fever by default.

## Credits

- Empire: Peter Langston, Dave Pare, Jeff Bailey, Thomas Ruschak, Ken
  Stevens, Steve McClure, Markus Armbruster and [Wolfpack](http://www.wolfpackempire.com/)
- Asciiverse edition: Asciiverse
- License: GPL-3.0-or-later
