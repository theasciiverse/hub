A lifeform made of light creeps around the window: its body stretches and
contracts as it crawls along a path of circular arcs that never ends and
never repeats, glowing white along its spine and fading to blue and violet
at its edges. Leave it running and watch it coil.

Ternimal draws with half blocks in 24-bit colour, so the body is smooth at
twice the vertical resolution of the text.

## Controls

- **Any key**: quit

## Options

From a terminal, everything about the creature can be changed with
`name=value` arguments: `length=100 thickness=1,4,1,0,0 radius=6,12` makes
a long snake, `length=200 thickness=0,4,19,0,0` a swarm, `speed=` and
`fps=` set the pace, `gradient=0:#666600,0.5:#00ff00,1:#003300` the
colours, and `true_color=false` falls back to 256 colours. Without
`fit=true` it draws a 60 by 20 arena below the prompt, as the original
does. The README lists the examples and the source lists every parameter.

## Credits

- Ternimal: [Philipp Emanuel Weidmann](https://github.com/p-e-w/ternimal)
- Asciiverse edition: quits on any key, and fills the window with `fit=true`
- License: GPL-3.0-only
