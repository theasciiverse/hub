Night in a snowy forest. Snow drifts down at three depths, near flakes
fast and large, far ones faint. The wind comes and goes: a gust sweeps in
from one side, bends the spruces, shakes the snow off their branches in
clumps and lifts the snow off the open field in a low blizzard, laying it
down again behind the cabin and the trees, so the drifts grow and creep
downwind. Snow settles on the roof until it slides off.

A log cabin glows at its windows with smoke drifting from the chimney, a
spruce beside it is lit for Christmas, and above the mountains the stars
twinkle, the moon shines and a faint aurora moves. Every now and then a
sleigh crosses the sky.

The sound is made as it plays, nothing recorded: the wind in the trees
rises and falls with the gusts you see, whistles in the strongest, snow
thumps off the branches and the roof, an owl calls far off, and sleigh
bells ring while the sleigh is up.

## Controls

- **m**: sound off and on
- **Any other key**: quit

## Options

From a terminal: `silent-night --mute` starts quiet, `--no-sound` has no
sound at all, and `-s N` builds the same forest every time.

## Sound

On Linux the sound goes to PipeWire, PulseAudio or ALSA (through
`pw-cat`, `paplay` or `aplay`), or to `ffplay`, whichever is there; on
macOS and Windows to the default output. Without any of them it is a
silent night.

## Credits

- Silent Night: made by Asciiverse, 2026
- License: MIT
