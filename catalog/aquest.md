You're a jolly little ship dingus which shoots around a rather abstract
landscape collecting little gem thingies, while avoiding mines. Pick up
every crystal on the level and the gate at the top opens; fly out through
it to the next one. Fifty levels, each with more crystals, more mines, a
narrower gate, and from level 33 a gate that won't keep still.

Every level has a par time, counting down in the corner. Beat it and
each second left is worth 500 points; overstay it and the whole game
starts to speed up. An extra ship comes every 15,000 points on the first
levels, every 100,000 later.

Your ship steers by thrust and drifts on when you let go, so brake before
the wall: on every difficulty but Wimp, the wall is as deadly as a mine.
Your shots fly the way you do, as fast as you do. Enemies come in through
the side gates, eighteen kinds of them: Grungers wander, Zippos curve,
Zingers and Snipes shoot, Miners lay mines, Meebies follow you,
Retaliators fire back when they die, Tribblers burst into five, Clusters
into fifteen shots, and the Repulsor shoves you away. Catch a Supercrystal
for a power-up (Shield, AimedFire, RapidFire, MultiFire, AssFire,
HeavyFire or Bounce; a banner says what you got and what it does, and the
status bar shows all seven, lit while they last), and keep a smart bomb
for the moment it all goes wrong.

The game is the original, rule for rule: the same physics, levels, enemies
and sounds, and Mark Mackey's sprites drawn in Braille dots and half
blocks, cell by cell, so even a small terminal shows them in fine detail
and full colour; at full size, his own status bar.

## Controls

- **Arrows**, **WASD** or the numpad: thrust
- **Space** or **Enter**: fire (hold it with RapidFire)
- **Shift**, **Z** or numpad **5**: brake
- **B** or **X**: smart bomb
- **P**: pause; **Esc**: quit the game; **V**: graphics (Mixed, Blocks
  or Braille); **M**: sound
- Mouse: move to thrust, left button fires, right bombs, middle brakes
- Gamepad: stick or d-pad to thrust, **A** fires, **B** bombs, **X** or a
  shoulder brakes, **Start** pauses

Best in a terminal that reports key releases (kitty, foot, WezTerm,
Ghostty, Alacritty, iTerm2 and others), with the mouse or with a gamepad;
elsewhere a held key stutters until the terminal's repeats start.

## Options

- `--mixed`, `--blocks`, `--braille`: how to draw
- `--demo`: watch the built-in demo
- `--record FILE`, `--play FILE`: record and play back demos in the
  original `xquest.dmo` format
- `--difficulty N`: 0 Wimp to 4 Inhuman
- `--mute`: no sound

## History

Mark Mackey wrote XQuest in Turbo Pascal for DOS, a Mode X game at
320x240, and released it as shareware from 1994 to 1996. Make it to
Inhuman, the manual promised, and he'd send you a UUencoded GIF of a
tenner.

Thirty years on, David, who played it as shareware in the mid-90s, ported
version 1.3 to C and SDL2 as xquest-sdl. AQuest
carries that port's game logic over to the terminal line by line: a demo
recorded in either one plays back in the other, frame for frame. The Hall
of Fame and the demos keep the original file formats.

## Credits

- **XQuest**: Mark Mackey, 1994 to 1996
- **xquest-sdl**: David, the C and SDL2 port this edition is built on
- **AQuest**: the terminal edition, for Asciiverse

Free to play and share, never sold.
