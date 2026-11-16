**FIND THE END. THE CLOCK IS ALREADY WATCHING.**

The moment you take your first step, the timer starts. Ahead of you runs a corridor of olive walls and amber floor, shaded and lit in true colour, every bit of it drawn in your terminal one character cell at a time. Somewhere in this maze, maybe three floors up, is the end. Get there. Then get there faster.

TermTrack is a first-person 3D platformer. You walk, you turn, you look up at the floor above you and wonder how to reach it. A **half wall** is a step you can jump onto, and from its top the next floor is in reach. **Holes** drop away into the floor below, or into nothing at all. **Spikes** end the run on touch. And here and there waits an **angry pixel**: a small red cube that wakes when it sees you and flies straight at you, only a little slower than you can run.

The levels stack floor on floor, so a route is never just left or right. In the second level you cross the bottom floor, hop down a line of pillars along its edge, climb to the middle floor and up again to a row of lonely stepping stones floating over the drop, then fall back down to the end. **M** shows you a map of the floor you are on, when you are lost.

Every finished run is kept, and **L** in the menu shows your best times. A level is a plain text file of eight characters, so you can draw your own maze in any editor and run it, then race it.

## Controls

- **W A S D**: move
- **arrow keys**: turn, and look up and down
- **Space**: jump
- **M**: the map of this floor
- **R**: start the level again
- **E** or **Esc**: leave the level; **Q**: quit
- In the menu: **Up** and **Down** choose, **Enter** plays, **L** shows your best times

## Your own levels

Write a text file: **S** start, **E** end, **X** wall, **x** half wall, **v** spike, **.** floor, a space for a hole, **e** an angry pixel. A line with only **sep** begins the floor above. Put your files in a folder and run `termtrack <folder>`.

## History

TageDan and abbfelarb started TermTrack in August 2024 with a pitch of a few lines: easy to install, light, easy to mod, your own tracks for replayability, and a 3D game in the terminal, which would make it one of a kind. They wrote the renderer from scratch in Rust, every cell of the screen traced against the level's triangles on all cores and shaded by which way each face turns, and by the end of September they had a speedrunning game with an online leaderboard. 1.0 came out on 7 October. In 2025 they began moving it from reading the desktop's keyboard to reading the terminal's own keys. This edition finishes that move, so it plays in any terminal, and keeps your times on your own computer.

## Credits

- TermTrack: the TermTrack team, TageDan and abbfelarb
- Title art made with patorjk.com's Text to ASCII Art Generator
- Asciiverse edition: Asciiverse
- License: MIT
