Backgammon as it came with BSD Unix: you play White against the
computer, or two players share the keyboard. The board is redrawn in
place after every move, the computer offers and takes doubles, and a
game can be saved and picked up later.

New to the game? Answer yes when it asks whether you want the rules:
teachgammon explains backgammon section by section and then plays a
practice game with you, move by move.

## Controls

At your colour's prompt:

- **Space** or **Enter**: roll the dice
- **d**: double
- **r** or **Ctrl+L**: redraw the board
- **s**: save the game, **q**: quit

At the Move prompt, type your moves and press **Enter**:

- **8-5**: move a man from point 8 to point 5
- **13/4**: move a man on point 13 by a roll of 4
- separate moves with commas or spaces: `8-5,6-5`
- **b** is the bar and **h** is home: `b-20`, `3-h`

## Options

- `-w` or `-r`: play White or Red against the computer, skipping the
  questions; `-b`: two players
- `backgammon <name>`: pick up the game saved under that name

## History

Alan Char wrote backgammon and its tutorial at UC Berkeley (the
copyright is from 1980), and it shipped with BSD Unix from then on. This
edition keeps saved games in the player's own data folder. One fix changes
how the computer plays: when it judged whether a lone man of yours could
be hit, it looked at the wrong squares, past the end of the board. It is
part of BSD Games in the Asciiverse catalog, under the BSD licence.
