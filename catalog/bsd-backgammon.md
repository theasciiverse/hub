**ROLL THE DICE. THE COMPUTER HAS ITS EYE ON THE DOUBLING CUBE.**

Backgammon as it came with BSD Unix in 1980. You play White, the computer
plays Red, and the board is redrawn in place after every move. The computer
offers doubles and takes them, and it is watching for any man you leave on
his own. Win big enough and the game says so: "Backgammon!"

Two players can share the keyboard instead, and a game can be saved and
picked up later.

New to the game? Answer yes when it asks whether you want the rules.
Teachgammon, its built-in tutor, explains backgammon section by section and
then plays a practice game with you, move by move.

- **You against the computer**, or two players on one keyboard
- **The doubling cube**, offered and accepted by the computer
- **Teachgammon**, the tutorial that teaches the rules
- **Saved games** to come back to

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
