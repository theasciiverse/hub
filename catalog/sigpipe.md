**THE DATA IS COMING. LAY PIPE. FAST.**

A process has started. Somewhere on the board, `cat` is about to start writing, and its data has nowhere to go. Yet.

You have seconds. Grab pieces from the queue and slam them down across the grid: straights, corners, crossovers, tees. Then the countdown hits zero, the modem chirps, and the green data starts creeping down your pipe, one segment at a time, each one a note higher than the last...

Keep laying. Stay ahead of it. Because the moment it reaches an open end, it's all over:

`cat: write error: Broken pipe`
`[exit 141]`

- **Loop it!** Send the stream back through a crossover for +500. Five loops in one level? That's a 5000 bonus.
- **Split it!** A tee sends the data down both arms at once, and suddenly you're racing two fronts.
- **Buffers** soak up the flow, **valves** let data through one way only, and the `nul` sink swallows whatever you feed it.
- **Press F when you're feeling brave:** fast flow, double points.
- **Endless levels,** each one longer, faster and more cramped than the last.
- **Versus on the local network:** race a rival on an identical board, and every three segments you pipe locks a cell on theirs.

Pause and you're `[1]+ Stopped`. Pass and it's `[exit 0]`. Fail and... well, you know the signal. **DON'T BREAK THE PIPE.**

## Controls

- **Arrow keys**, **W A S D** or **H J K L**: move the cursor
- **Enter** or **Space**: lay the next piece (or replace one, at a small cost)
- **Mouse**: point and click to lay
- **F**: fast flow (during the countdown, starts the data at once)
- **P**: pause, **M**: sound on or off, **Esc**: back, **Q**: quit
- On the title: **V** hosts a versus match, **C** joins one
- **Gamepad**: d-pad moves, bottom button lays, left or top button or right trigger for fast flow, Start pauses

SIGPIPE fits an 80x24 terminal. At 144 columns or wider, your rival's board shows live beside yours in versus.

## Options

- `--level N`: start at level N
- `--mute`: no sound

## Credits

- Game: Asciiverse
- Sound synthesised in the game
- Networking: iroh
