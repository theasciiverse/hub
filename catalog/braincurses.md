The computer picks a secret code of four colours, repeats allowed, from
red, green, yellow, blue, magenta and white. You have ten guesses to find
it. After each guess, markers tell you how close you came: a red X for
every colour in the right place, a white X for every right colour in the
wrong place. The markers are always listed reds first, so they never say
which of your colours earned them.

Work it out from the answers; the secret is shown when you crack it or
run out of guesses.

## Controls

- **r g y b m w**: type a colour (red, green, yellow, blue, magenta,
  white); the guess is scored once every place has a colour
- **Left**, **Right**, **Backspace**: move back and change a guess
- **y** or **Enter** after a game: play again; **n** stops
- **q**: quit

## Options

- `braincurses -c 5` or `-c 6`: a longer code
- `braincurses -g 12`: the number of guesses (1 to 15)

## Credits

- braincurses: [Brian Derr](https://github.com/bderrly/braincurses), under
  the GPL version 2
- Asciiverse edition: q to quit, the
  result kept on screen, fixes for 5 and 6 colour codes and incomplete
  guesses, and a Windows build
