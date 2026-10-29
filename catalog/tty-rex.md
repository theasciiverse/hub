**NO INTERNET. NO PROBLEM. RUN.**

You know this dinosaur. It is the little T-Rex that waits on the browser's "No Internet" page, and now it runs in your terminal, drawn in Braille dots. Press Space and the road opens up. Jump the cacti. Past speed 8.5 the pterodactyls arrive, so duck. Every 700 points night falls. And it only ever gets faster.

Every rule, timing, sprite and sound comes from Chromium's own source, so it plays exactly the way you remember: hold jump for a higher leap, press down in mid-air to drop fast, and chase your own high score.

- **True to the pixel**: the original sprite art, every art pixel kept at the home scale
- **Fits anywhere**: from a 20x7 split pane to a big window; the dots get coarser or finer, the game doesn't change
- **Four looks**: Braille in your terminal's own colours, classic grey on white, coloured sprites, or colour blocks
- **Auto mode**: press **A** and he runs on his own, a strip of living scenery for the bottom of your tmux layout
- **Gamepad ready**: A jumps, B ducks, as in the original

## Controls

- **Space**, **Up**, **W** or **K**: jump (hold for a higher jump)
- **Down**, **S** or **J**: duck; in mid-air, drop fast
- **Enter**: run again after a crash (Space works too, after a moment)
- **P**: pause; **V**: next look; **A**: auto mode; **M**: mute
- **Q** or **Esc**: quit
- Gamepad: **A** jumps, **B** ducks, **Start** restarts after a crash and pauses otherwise, the D-pad's up and down jump and duck, **Select** toggles auto mode

Holding jump for a higher jump needs a terminal that reports key releases (the kitty keyboard protocol); elsewhere every jump is a full one.

## Credits

- The original game, its sprites and sounds: The Chromium Authors (BSD-3-Clause)
- Terminal version: Asciiverse
