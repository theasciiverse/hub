**IT IS STRONGER THAN ANY HUMAN WHO EVER PLAYED. YOUR MOVE.**

Stockfish comes in the box, ready the moment you start: no setup, no engine to hunt down. At full strength it is far stronger than any human player. Feeling less heroic? Turn it down to one of four easier levels and work your way up.

This is chess with a proper board. On a big terminal the pieces are drawn large in block characters; on a smaller one, in chess symbols. Move with the arrow keys or the mouse, or just type it: `e4`, `Nf3`, `O-O`. The move history and captured pieces sit beside the board, so you always know who's winning, and why.

- **Stockfish at five strengths,** from Easy to full power, or any other UCI engine you point it at.
- **Two players:** share one keyboard, or host and join across your local network.
- **Lichess, from the terminal:** sign in and seek a game, join a friend's by its code, pick up your ongoing games, or solve rated Lichess puzzles.
- **Clocks** from UltraBullet to Classical, or none at all.
- **Save, load and replay:** load a PGN file and step through any game, move by move.
- **Skins:** press `s` and the board changes its look.

**WHITE TO PLAY.**

## Controls

- **Arrow keys**: move the cursor; **Enter** or **Space**: pick up a
  piece, then put it down
- **m**: type a move in chess notation (`e4`, `Nf3`, `O-O`)
- **Esc**: put the piece back; **s**: change the board's look
- **?**: help with every key; **q**: quit
- In the menus: **Up** and **Down** to choose, **Enter** to go on

## Options

- `--difficulty easy`, `medium`, `hard` or `magnus`: the computer's
  strength for Play Bot
- `-e <path>`: use another UCI chess engine instead of the bundled
  Stockfish
- `-l <token>`: a Lichess API token, for playing on Lichess
- `--no-sound`: no move sounds (macOS and Windows; this build has none on
  Linux)

## Credits

- chess-tui: Thomas Mauran and contributors
  ([github.com/thomas-mauran/chess-tui](https://github.com/thomas-mauran/chess-tui)),
  2023 on, written in Rust with Ratatui
- Stockfish 11: the Stockfish developers
  ([stockfishchess.org](https://stockfishchess.org)), GPL-3.0-or-later,
  shipped beside chess-tui with its licence and source
- Asciiverse edition: Stockfish included and found without any setting
- License: MIT (chess-tui), GPL-3.0-or-later (Stockfish)
