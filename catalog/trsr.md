**THE TREASURE IS DOWN THERE. GET TO IT FIRST.**

Minesweeper, turned around, for two. Treasure lies hidden under the field, and two sides, Percent (**%**) and Square (**#**), take turns opening cells. A cell without treasure shows how many of its eight neighbours hold some, found or not, and a cell with none around opens its neighbours too. Strike treasure and you score it and dig again, a few times in a row at most. Find more than half of it and you win; there is always an odd number of treasures, so there is no draw.

In the game's own words: *Like Mines but you need to find stuff instead of avoiding them. Try to trick the AI into doing useless stuff.*

At the start it asks who plays each side. Press **Enter** twice to play Percent against the computer, which plays Square; you go first. Press **Enter** and then **h** for two players taking turns at one keyboard, or **c** and then **Enter** to watch the computer play both sides.

## Controls

- **Arrow keys**, **hjkl** or **wasd**: move
- **Enter**: dig the cell
- **Mouse**: click to dig
- **PgUp**, **PgDn**, **<**, **>**: scroll a field bigger than the
  terminal
- **F1** or **?**: help on the controls, **F2** or **!**: how to play
- **q** or **Esc**: quit; at the end, **y** plays again and **n** or
  **q** quits

## Field size

Started from a shell, Treasure takes the size and the amount of
treasure, for example `trsr -w 30 -l 20 -m 75`: `-w` is the width,
`-l` the length (height) and `-m` the number of treasures; without `-m`
an eighth of the cells hold one. The default field is 15 by 15, or 20
by 15 on a terminal narrower than 45 columns.

## History

Treasure is one of the games abakh wrote for New BSD Games, a collection
of small curses games started in 2018 and named after the classic BSD
games.
