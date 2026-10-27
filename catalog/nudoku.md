Sudoku on the classic 9x9 board: fill every row, column and 3x3 box
with the numbers 1 to 9, each once. nudoku makes a new puzzle each
time, easy, normal or hard, and keeps out of the way: move around the
board, type numbers into the empty cells, and ask it to check your work
whenever you like.

When you are stuck, a hint fills in one cell for you, and the count of
hints used is shown when you finish. Marks light up every copy of the
number under the cursor, which makes it easy to see where a number can
still go. Mistakes can be deleted or undone, and a game in progress can
be saved and picked up again later.

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
