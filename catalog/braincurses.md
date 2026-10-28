**FOUR COLOURS. TEN GUESSES. CRACK THE CODE.**

The computer has picked a secret: four colours in a row, from red, green,
yellow, blue, magenta and white, repeats allowed. You have ten tries to name
it exactly.

Every guess gets its answer in markers: a red X for each colour in the right
place, a white X for each right colour in the wrong place. They never say
which is which. Is it the yellow in the second slot, or the blue at the
end? Work it out, narrow it down, close in.

Donald Knuth showed that this classic code can always be cracked in five
guesses or fewer. You have ten. How hard can it be?

- **Classic code-breaking**: learned in a minute, played for years
- **Longer codes** of five or six colours, and anything from one to
  fifteen guesses
- **Play again** at a keystroke

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
