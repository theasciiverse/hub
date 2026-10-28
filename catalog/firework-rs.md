**THE SHOW NEVER ENDS. TURN OUT THE LIGHTS.**

Bang. A burst of sparks blooms in the corner of your terminal, sparks
arcing out, slowing, drooping under their own weight and fading as they
fall. Then another, over there. Then three at once. It never stops, and
it never repeats: every firework picks its own spot, its own moment and
its own palette, and a bigger window gets a bigger show.

Wayoung7 built firework-rs as a little particle engine in Rust, with real
gravity and air resistance on every spark, and the colours are hand-picked:
reds and golds, deep sea greens, ice blues, pastel pinks and lilacs, eight
palettes in all.

- **Endless and random**: no two minutes alike, as long as you leave it
  running
- **Fills any window**: from a corner of the screen to a wall-sized
  terminal, the number of bursts grows with the space
- **Five designed shows** too, from the command line, and a colour fade
  for black backgrounds

**Pour a drink. Press any key when the party's over.**

## Controls

- **Any key**: quit

## Options

From a terminal, `firework -d 0` to `firework -d 4` play five designed
shows (add `-l` to loop one), `-g` fades the sparks through a colour
gradient (best on a black background), `--fps` sets the frame rate from 5
to 30, and `--cjk` suits fonts with wide characters.

## Credits

- firework-rs: [Wayoung7](https://github.com/Wayoung7/firework-rs), the
  crate and its `firework` demo
- Asciiverse edition: any key quits
- License: MIT
