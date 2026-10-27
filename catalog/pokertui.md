Five bots, ten thousand chips each, and one seat with your name on it.
Every hand you get two cards, a felt full of pods, and a rail that does
the arithmetic for you: your chance to win right now, the pot odds on the
call, and a blunt verdict on whether calling is worth it.

The bots are not all alike. One is tight and aggressive, one calls
anything, one bluffs more than it should, and one is a rock that only
moves with a monster. They remember how often you fold, and they lean on
you when you do. The game ends when one player has every chip on the
table. Make it you.

Tired of bots? `pokertui-server` comes in the box: start a room and your
friends join it over the network.

## Controls

- **F**: fold; **C**: check or call; **R**: raise; **A**: all-in
- **Up** and **Down**: change the bet size; **Enter**: confirm
- Any key after a hand: deal the next one
- **S**: settings (table size, blinds, bot speed, the odds rail);
  **Q**: quit

## Options

- `--join <host:port> --name <name>`: sit down at a network table
- `pokertui-server --seats 4`: host a table (port 4000; `--buy-in`,
  `--small-blind`, `--big-blind`, `--turn-secs` set the game)

## Credits

- pokertui: Aleksandr Babarika
  ([github.com/AlexAlexBabarika/pokertui](https://github.com/AlexAlexBabarika/pokertui)),
  2026, written in Rust with Ratatui
- Asciiverse edition: fits 100x30, smarter bots, no freeze on a short
  stack, Windows settings saved
- License: MIT or Apache-2.0
