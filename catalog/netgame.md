A grid of pipe pieces, scrambled: straights, corners, T junctions and
dead ends. The tile at the centre is the source, and everything joined to
it lights up green. Turn the tiles one by one until every piece is part
of a single network, with no loose ends and no loops. The count under the
board shows how many tiles are connected so far.

Lock a tile once you are sure of it, so a stray key cannot turn it again.
When the whole board lights up, press n for a fresh puzzle.

## Controls

- **Arrow keys**: move the cursor
- **Space** or **.**: turn the tile clockwise
- **,**: turn it anticlockwise
- **l** or **s**: lock or unlock the tile
- **n**: new puzzle
- **q** or **Ctrl+C**: quit

From a terminal, `netgame 15 20` plays on another size (2 to 99), and
`--wrapping` lets pipes run off one edge and back in at the other.

## Credits

- Netgame: [Ben Falconer](https://github.com/zed0/Netgame), under the MIT
  licence
- Asciiverse edition: wider tiles, n for a new puzzle, a clean exit on Ctrl+C, and a Windows build
