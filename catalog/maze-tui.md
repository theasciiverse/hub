**EVERY MAZE TELLS YOU HOW IT WAS MADE.**

Watch a maze being carved, wall by wall, and then watch it being solved.
Maze TUI animates the classic maze algorithms in your terminal: a
randomized depth-first search tunnelling ahead and backing out of dead
ends, Prim's maze spreading like frost, Kruskal's joining scattered
pieces, Eller's sweeping row by row, Wilson's loop-erased random walks,
recursive division splitting open floor into rooms. Then the solvers move
in, several threads at once, each painting its own colour as it races for
the finish, gathers every prize or hunts for the corners.

Every animation is a timeline. Pause it, slow it to a crawl or speed it
up, step forward and back one change at a time, or run the whole thing in
reverse and watch the maze unbuild itself. Press **i** while it plays and
a page explains the algorithm on screen.

Leave it at the home screen and a new random maze builds and solves itself
behind the menu, over and over.

**Pick an algorithm and watch it think.**

## Controls

- **Enter**: a random maze, or the one your flags describe
- **Space**: pause and play
- **<** and **>**: slower and faster
- **Left** and **Right**: step back or forward, and set the direction
- **i**: about the algorithm on screen
- **Up** and **Down**: scroll the help or the algorithm page
- **Esc**: back to the home screen, and quit from there; **Ctrl+C** quits
  from anywhere

## Flags

Type them on the home screen, in any order, then press Enter. Anything
left out is chosen for you.

- `-b`: the builder: `rdfs`, `hunt-kill`, `kruskal`, `prim`, `eller`,
  `wilson`, `wilson-walls`, `fractal`, `grid` or `arena`
- `-s`: the solver: depth-first, randomized depth-first, flood fill or
  breadth-first, each as `-hunt`, `-gather` or `-corner` (for example
  `bfs-gather`), or `distance` and `runs` to paint the maze by path
  length
- `-m`: shortcuts through the middle: `cross` or `x`
- `-w`: the walls: `mini`, `sharp`, `round`, `doubles`, `bold`,
  `contrast`, `half` or `spikes`

For example `-b wilson -s bfs-hunt -w round`, or `-b fractal -s distance`.

## Credits

- Maze TUI: [Alex G. Lopez](https://github.com/agl-alexglopez/maze-tui);
  his [wiki](https://github.com/agl-alexglopez/maze-tui/wiki) covers every
  algorithm
- License: MIT
