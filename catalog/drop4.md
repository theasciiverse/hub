Shapes of four squares fall into a well one at a time. Move and turn
each one as it falls so they pack together: every row you complete
vanishes and the rows above drop down. When the stack reaches the top,
the game is over. The game speeds up as you go, and dropping a shape
early scores more.

## Controls

- **Left** and **Right**, or **j** and **l**: move
- **Up** or **k**: turn a quarter counterclockwise
- **Space** or **Down**: drop
- **>**: go faster
- **p**: pause
- **q**, **F10** or **End**: quit

## Options

Started from a shell, `drop4 5` starts at level 5. Levels go from 1 to
9; at level n the shapes fall n times a second.

## History

This is BSD's tetris, which Chris Torek and Darren F. Provine adapted
from a winning 1989 entry to the International Obfuscated C Code
Contest (UC Berkeley, 1992); Hubert Feyrer added the preview of the next shape in 1999. In
2016 Mike Sharov renamed it Drop4 for his bsd-games and changed its
look: a wider well, no animation when rows clear, and the score and
next shape on the right. The high score table is kept per player.
