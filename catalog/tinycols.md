**THREE JEWELS AT A TIME. ONE NARROW WELL. KEEP IT CLEAR.**

A column of three jewels drops into a well six wide and thirteen deep.
Turn the column to shuffle its colours, slide it left or right, and let
it land. Three or more of a colour in a line, across, down or on either
diagonal, and they burst; the jewels above fall into the gap, and if
they make a new line, that bursts too, for more points each time round.

- **Chains pay**: every burst in a chain is worth more than the last, and
  every level multiplies it again.
- **It speeds up**: clear enough jewels and the next level drops them
  faster.
- **Three classes**: Novice with four colours, Amateur with five, Pro with
  six. Amateur is the default; `tinycols -c 1` or `-c 3` from a shell
  starts the others.
- **A best score for each class**, kept between games.
- **Watch the next column** in the box beside the well, and plan two
  moves ahead.

Rigel Di Scala wrote TinyCols in C and ncurses, and keeps it small on
purpose.

**Turn. Slide. Drop. Chain.**

## Controls

- **Left** and **Right**: move the column
- **Down**: drop it faster
- **Up** or **a**: turn the jewels upwards; **z**: turn them downwards
- **p**: pause; **q**: quit
- After a game: **r** to play again, **q** to quit

## Credits

- TinyCols: Rigel Di Scala ([github.com/zedr/tinycols](https://github.com/zedr/tinycols)),
  2022 on, written in C with ncurses
- License: BSD-3-Clause
