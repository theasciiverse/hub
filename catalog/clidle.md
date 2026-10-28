**FIVE LETTERS. SIX TRIES. ONE WORD.**

Type a guess, press Enter, and watch the letters turn, one at a time. Green: right letter, right place. Yellow: it's in there, but somewhere else. Grey: not in the word at all. Only real words count, so no cheating your way through the vowels.

Below the board, an on-screen keyboard colours every letter as you learn about it, so you can see at a glance what's left to try. Got it in three? That's 80 points. In one? A hundred, and bragging rights. Six squeaks home with 50, and it all adds up into a running score.

And you don't have to wait until tomorrow: every game picks a new word at random from 2,315 answers, with 12,972 words it accepts as guesses. Press Ctrl+R and there's another one.

- **Letters revealed one by one,** for that moment of suspense.
- **A running score** that keeps adding up, game after game.
- **Play it over SSH:** `clidle -serve` turns it into a server other people can connect to and play.

clidle is Ajeet D'Souza's five-letter word-guessing game in the style of Wordle.

**WHAT'S YOUR OPENING WORD?**

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
