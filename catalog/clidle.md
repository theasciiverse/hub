Guess the hidden five-letter word in six tries. Type a word and press
Enter, and its letters turn colour one at a time: green for a letter in
the right place, yellow for a letter that is in the word somewhere else,
grey for a letter that is not in it at all. Only real words count.

Below the board, an on-screen keyboard colours each letter as you learn
about it, so you can see at a glance which letters are left. Every game
picks a new word at random, and a running score adds up how well you
do: 100 points for one guess, down to 50 for six.

clidle is a five-letter word-guessing game in the style of Wordle.

## Controls

- **a** to **z**: type a letter
- **Backspace**: clear the last letter
- **Enter**: check the guess; after a game, start the next one
- **Ctrl+R**: start a new word at any time
- **Esc** or **Ctrl+C**: quit

The on-screen keyboard needs a terminal of at least 58 columns by 30
rows.

## Options

- `-serve 0.0.0.0:1337`: run clidle as an SSH server, so others can play
  it with `ssh -p 1337 your-host`

## Credits

- clidle: Ajeet D'Souza
  ([github.com/ajeetdsouza/clidle](https://github.com/ajeetdsouza/clidle)),
  2022 on, written in Go with Charm's Bubble Tea and Lip Gloss
- Asciiverse edition: letters revealed one by one, Esc to quit, the
  score kept in view in a 30-row terminal, long messages fitted to narrow
  windows; written to be offered back upstream
- License: MIT
