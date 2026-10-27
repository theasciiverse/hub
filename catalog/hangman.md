The computer thinks of a word and shows a dash for each letter. Guess
the letters one at a time: a right guess fills in every place that
letter appears, a wrong one adds a piece to the gallows. Seven wrong
guesses and the figure is hanged and the word revealed.

Words are at least six letters long. The game keeps playing word after
word, with your average number of wrong guesses for the current game
shown beside the gallows, so you can try to bring it down.

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
