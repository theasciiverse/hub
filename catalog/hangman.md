**SEVEN WRONG GUESSES AND HE HANGS.**

The computer thinks of a word and shows you a dash for every letter.
Guess a letter. Right, and it fills in every place that letter appears.
Wrong, and another piece goes up on the gallows. Seven misses and the
figure is complete, and the screen tells you: "Sorry, the word was..."
Get there first and it's "You got it!"

Every word is at least six letters long, picked from 61,494 everyday
English and American words, and they keep coming, one after another.
Beside the gallows sits your average number of wrong guesses. Bring it
down.

- **One key per guess**: a to z; Space gives up on a word and moves on.
- **Its own dictionary**: no system word list needed.
- **Bring your own words**: from a shell, `-d` takes a word list and `-m`
  sets the shortest word length.

**Pick a letter. Any letter. Choose well.**

## Controls

- **a** to **z**: guess a letter
- **Space**: give up on this word and go to the next
- **Enter**: quit

## Options

Started from a shell, `-d` takes a different word list, one word per
line, and `-m` sets the shortest word length, as in `hangman -m 8`.

## History

Ken Arnold wrote Hangman for BSD Unix in 1983, and Mike Sharov cleaned
it up for modern curses in 2016 for his bsd-games, the modern Linux port
of the BSD games. Hangman is part of BSD Games in
the Asciiverse catalog, under the BSD licence.

The original reads the system's dictionary, which many computers no
longer have, so this edition comes with its own: 61,494 everyday English
and American words from SCOWL 2020.12.07, Kevin Atkinson's Spell Checker
Oriented Word Lists, used under SCOWL's permissive licence.
