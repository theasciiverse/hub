**CLEAR THE BOARD. EVERY LAST BLOCK.**

Five hundred and twelve blocks in four colours. Pick two or more of one colour touching side by side and they vanish; everything above falls into the gap, and an empty column closes up from the right. A group of n blocks scores (n-1) squared, so two blocks earn a single point and twenty earn 361. The whole art is in the order: take the small groups that join big ones together, keep building the colour you are saving, and never strand one lonely block of a colour that can no longer be cleared.

Josh Williams made his SameGame to be driven like vi. Move with `hjkl` and a count (`12l`, `5j`), clear with `x` or `dd`, and speak to it in `:`commands. Every move can be undone with `u` and redone with `r`, all the way back to the first. Save a game by name with `:w` and open it again with `:e`; `:q` refuses, vi style, while there are unsaved changes. When a game ends, it plays itself back to you, the board filling up and emptying again move by move.

- **Easy boards** where one colour turns up far more often, with `:easy`
- **Reverse gravity**: `:revgrav on` and the blocks fall up
- **Any board up to 64 by 64** with `:setw` and `:seth`, each size with its own highscore
- **God mode** fills the board with a single colour, and, as the history puts it, still counts on the highscore "because it's for cheaters"
- **A settings script**: put any `:`commands in `.samerc` and they run at every start

## Controls

- **h j k l** or the **arrow keys**: move; a number first moves that far
- **x**, **dd** or **Enter**: clear the group under the cursor
- **Mouse**: click a block to light up its group, click the group again to clear it
- **u** / **r**: undo / redo
- **n**: a new board
- **:w** *name*: save, **:e** *name*: open, **:x**: save and quit
- **:q**: quit, **:q!**: quit without saving

## Options

- `--easy`, `--hard`, `--god`: the difficulty
- `--reverse-gravity`: blocks fall upward
- `--width n`, `--height n`: the board's size

## History

Josh Williams wrote same over 2015, from a first board in March to undo, redo, highscores, saved games, the end-of-game replay and a small scripting language by the autumn, with a plan to let scripts one day teach the computer to find the best solution to a puzzle.

## Credits

- SameGame: Josh Williams (jodawill), on [GitHub](https://github.com/jodawill/same)
- License: GNU GPL version 2
