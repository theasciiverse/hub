**FOUR DIMENSIONS. TWENTY MINES. EIGHTY NEIGHBOURS PER CELL.**

You know Minesweeper: a number says how many mines touch a cell. Here the
field runs along x, y, z and w, drawn as a grid of grids, and a cell
touches everything one step away in any of the four directions at once:
up to 80 neighbours. Move the cursor and every cell it reaches lights up,
so you can see the shape of a 4D neighbourhood before you trust a number.

- **Delta mode** (on by default): each number counts only the mines not
  yet flagged around it, so solved areas fall to zero.
- **Sweep mode**: a flagged mine is swept away. Flag wrong and the game is
  over.
- **Marks**: tag a group of cells and see how the mines in their reach
  overlap; a way to learn 4D tactics, not a way around them.
- **Any size you like**: `-d 6 6 3 3 -m 40`, or `-d 16 16 1 1 -m 40` for
  the classic flat game.

**SWEEP SIDEWAYS.**

## Controls

- **Arrows** or **H J K L**: move in x and y; **A D**: move in z;
  **W S**: move in w. Hold **Shift** to jump to the edge
- **Space**: uncover; **M** or **E**: flag; **Shift+M**: flag every
  covered cell around the cursor; **F**: find a zero and open it
- **X**: mark; **Shift+X**: uncover the obvious marked cells;
  **Alt+X**: flag them; **Ctrl+X**: clear the marks
- **U**: delta mode; **Shift+U**: sweep mode; **I**: info box
- **N**: new game; **R**: retry; **G**: give up; **P**: pause
- **C**: controls; **O**: settings; **Q** or **Esc**: quit

## Options

- `-d X Y Z W`: field size; `-m N`: mines; `-s N -r f`: a fixed seed
- `-cm t`: play with the mouse (left uncovers, right flags)
- Ctrl+O saves the game; start with the file's name to load it

## Credits

- minesweeper_4d: [itabesamesa](https://github.com/itabesamesa/minesweeper_4d_rs)
- Asciiverse edition: starts without a config file of your own
- License: MIT
