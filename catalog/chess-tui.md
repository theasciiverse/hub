Chess in the terminal, with a proper board: large pieces drawn in block
characters on a big enough terminal, chess symbols on a smaller one.
Play against Stockfish, which comes with the game, at full strength or at
one of four easier levels; play a friend on the same keyboard, or over
the network; or sign in to Lichess and play people online.

Choose a clock from bullet to classical, or none. Move with the cursor
keys or the mouse, or type a move in chess notation. The move history and
the captured pieces sit beside the board, and a game can be saved, loaded
from a PGN file and stepped through.

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
