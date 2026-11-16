**FIFTEEN HUNDRED METRES. FALLING. THE PAD IS THAT LITTLE STRIPE DOWN THERE.**

You come in high over the left edge of the moon, sliding sideways at 166 metres a second, and gravity has already started on you. Below lies a lunarscape drawn in line characters: a mesa, ridges, a cliff on the right with a narrow shaft cut into it, and eight landing pads, each marked with what it is worth, from 10 points out in the open to 50 at the bottom of that shaft.

Your module has three rockets. The left one shoves you right, the right one shoves you left, and the one underneath slows your fall. You never fire them directly: you pick a power level from **0** to **9**, from nothing through a whisper to full burn, then tell a rocket to run at it, and it keeps running until you say otherwise. Every second the moon takes its turn: thrust is applied, fuel burns, you drop, you drift, and a dotted trail marks where you have been.

Touch down on a pad at five metres a second or slower and you have landed. Any faster, or anywhere that is not a pad, and the man page puts it plainly: *fragmentation of the lander and loss of cabin pressure*. Land well and you score the pad, a bonus for the fuel you saved and a bonus for landings in a row. Then you go again, coming in faster, falling harder, with less in the tank, until the moon wins.

- **Real time, one second at a time**: plan your burns ahead, because the moon will not wait
- **Ten power levels** per rocket, from 0.01 to 20, for coarse braking and fine trimming
- **A high score table** of the ten best games

## Controls

- **0** to **9**: choose the power level
- **z**: run the left rocket at that power (pushes you right)
- **x**: run the vertical thrust at that power (slows your fall)
- **c**: run the right rocket at that power (pushes you left)
- **Space**: start, and go on after a landing
- **y** or **n**: another game, after the last crash

## History

In 1989 Stacey Campbell was working at HCR Corporation, the Toronto Unix house, and wrote Lander around one of the nifty new things in System V.3 curses: line drawing. It ran on HCR's own System V port to the VAX, on 386/ix and on BSD. On 1 May 1989 it went out over Usenet in comp.sources.games, volume 6, issue 70, with bug reports invited by UUCP to `{utzoo,utcsri,lsuc}!hcr!stacey`. Players wrote back, BSD readers sent patches, and in June a follow-up posting answered their questions about flying it.

Stacey kept no copy. Decades later he found his game again in a Usenet archive mirror, unpacked the shell archive, got it compiling on Linux and put it on GitHub, where in 2022 he added one last touch: a pause in the explosion to stand in for the time a 1989 machine took to work out its sines.

## Credits

- Lander: Stacey Campbell, HCR Corporation, 1989
- Asciiverse edition: Asciiverse
- License: GPL-2.0
