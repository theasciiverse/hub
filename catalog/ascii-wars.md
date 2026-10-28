**TEN BOSSES. EACH ONE A GLYPH WITH A GRUDGE.**

The Sentinel. The Hoarder. The Watcher. The Infernal Imp. The Spiral Beast.
The Guardian of Order. The Swarm King. The Celestial Tyrant. The Clockwork
Leviathan. And at the end of it all, The Chaos Reaper.

You fire at the boss whenever you move, and only then: standing still is
safe from nothing, so every dodge is an attack.

Each boss fights in phases, with names like Compound Interest, Thousand
Eyes, Supernova and Last Rites. It opens with its old attack, then starts to
move and brings out new ones: aimed fans, rings that turn into spirals,
shots raining from the top, walls with one gap, bullets that curve, speed
up, bounce off the edges or home in, and lasers that show as a dotted
line before they burn. Break a phase and every shot on screen turns into
points; break it without a scratch for a bonus.

Hold focus to move slowly through the tight spots, drop a bomb to clear
the shots round you, and brush past bullets to graze them for points and
the next bomb. A hit makes you blink for a moment; the sixth one ends it.

## Modes

- **Arcade**: all ten bosses in a row, with one score and your health
  carried from fight to fight
- **Practice**: any boss you have reached, with your best time
- **Classic**: the original game as it was, rule for rule
- Easy, Normal and Hard; a demo plays itself when the title is left alone

## Controls

- **Arrows** or **WASD**: move (and fire)
- **Shift**, **Z** or **J** (hold): focus
- **X**, **K** or **Space**: bomb
- **Esc** or **P**: pause; **M**: sound on and off
- **Enter**: choose; the mouse works in the menus
- Gamepad: stick or d-pad to move, **A** or a shoulder button to focus,
  **B** or **Y** to bomb, **Start** to pause

Best in a terminal that reports key releases (kitty, foot, WezTerm,
Ghostty, Alacritty, iTerm2 and others) or with a gamepad; elsewhere a
move runs on a little after the key is let go.

## Options

- `--level N`: start Arcade at boss N
- `--classic`: the original game
- `--demo`: watch the computer play
- `--mute`: no sound or music

## History

Carlos Alvarez made ASCII Wars! in Rust with the Bevy engine in January
2025: ten bosses drawn with a CP437 font in a graphical window, each
firing rings and aimed shots at a ship that fires back while it moves.
This edition brings it to the terminal and builds a fuller game around
it, with phases, moving bosses, new attacks, bombs, grazing, a score,
colour, sound and a chiptune for every boss. The original lives on
unchanged as Classic.

## Credits

- ASCII Wars!: Carlos Alvarez (VikingosTeam), 2025,
  [github.com/Alvarz/ascii-wars](https://github.com/Alvarz/ascii-wars)
- Terminal port, and the Arcade game built round the original: Asciiverse
- License: MIT
