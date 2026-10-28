**NINE ROWS. NINE COLUMNS. NINE BOXES. ONE OF EACH.**

Fill every row, column and 3x3 box with the numbers 1 to 9, each exactly once. nudoku deals you a fresh puzzle every time, easy, normal or hard, and then stays out of your way: move around the board, type numbers into the empty cells, and ask it to check your work whenever you like. "Correct so far"? Keep going.

- **Marks** light up every copy of the number under the cursor, so you can see at a glance where a 7 can still go.
- **Hints** when you are stuck: one cell filled in for you, and the count shown when you finish.
- **Undo, save and come back later**: a game in progress picks up where you left it.
- **Your own puzzles**: give one as a line of 81 characters.
- **Help in nine more languages**, from German and Japanese to Georgian and Vietnamese (Linux builds).

**JUST ONE MORE PUZZLE.**

## Controls

- **h j k l** or the **arrow keys**: move
- **1** to **9**: put a number in the cell, **x**, **Delete** or
  **Backspace** to clear it
- **u**: undo
- **c**: check the board so far
- **H**: a hint
- **m**: marks on or off
- **N**: a new puzzle
- **S**: show the solution
- **G**: save the game
- **r**: redraw
- **Q** or **Escape**: quit

## Options

- `-d easy`, `-d normal`, `-d hard`: the difficulty (easy unless given)
- `-r`: resume the saved game
- `-c`: no colours
- `-s <81 characters>`: play a puzzle of your own, given as one line of
  digits with `.` for the empty cells; `-o` prints a new one that way

The help text is translated into German, Spanish, French, Japanese,
Georgian, Russian, Turkish, Ukrainian and Vietnamese, chosen from your
language settings (Linux builds).

## Files

The saved game is kept in `~/.local/state/nudoku` (`%LOCALAPPDATA%\nudoku`
on Windows).

## History

Michael Vetter started nudoku in 2014 and has kept it going since, with
translations from contributors; it is packaged by Debian and many
others. This edition has the translations found beside the program,
saving that works in a fresh home folder, and a Windows build. The
optional export of puzzles to PDF and PNG is not included.

## Credits

nudoku is by Michael Vetter and contributors, under the GNU GPL version
3 or later.
