**THE GHOSTS DON'T USE VIM. YOU DO.**

Every level is a maze of words. Your cursor has to pass over every letter until the whole maze turns green, while red ghosts close in. Walls can't be walked through, but vim's motions jump over them: **w** to the next word, **$** to the end of the line, **gg** to the top. Step on a **~** and you lose a life.

It's the friendliest way there is to get vim's motions into your fingers, and a tense little maze game besides.

- **Ten levels**, from a gentle first maze to word-filled labyrinths
- **Real vim motions**: words, WORDs, line ends, line numbers
- **A life back** after levels 0, 3, 6 and 9; after level 9 it starts again with faster ghosts
- **Two speeds**: hard by default, or `pacvim n` for slower ghosts

## Controls

- **h j k l**: left, down, up, right
- **w** / **W**: forward to the next word or WORD
- **e** / **E**: forward to the end of a word or WORD
- **b** / **B**: back to the start of a word or WORD
- **0** / **$**: start or end of the line; **^**: first word on the line
- **gg** or **1G**: first line; **G**: last line; a number then **G**: that line
- **Enter**: start a level; **q**: quit (**Esc** too, on the screen before each level)

## Options

- `pacvim N`: start at level N (0 to 9)
- `pacvim n` or `pacvim h`: normal or hard ghosts; `pacvim 4 n` combines them

## Credits

- PacVim: [Jamal Moon](https://github.com/jmoon018/PacVim) and contributors
- License: LGPL-3.0-or-later
