**AA PRESENTS... BB. A REAL DEMO, MADE OF NOTHING BUT LETTERS.**

The screen fills with a hex dump while BB "precalculates data". Then two
giant letter Bs fly in from opposite corners, and the boasts arrive one
word at a time: 100 % ANSI C. PORTABLE DEMO. FULL SVGA TEXT MODE.
DEVELOPED UNDER LINUX!!!?

For seven minutes it does not let up. Fire and plasma, tunnels and moiré
patterns, a snowfall, a 3D torus turning in shaded
ASCII, a dive through a fractal borrowed from XaoS, and greetings to
Future Crew, Triton and Cascada. Each of the four authors gets a portrait
and a life story typed out beside it: "1993 - Became a linux extremist",
"1997 - Removed Windows 95 to make space for aalib". "STILL WATCHING BB?"
it asks early on. "GREAT. NOW IT'S A GREAT TIME TO FILL IN YOUR
REGISTRATION CARD." The credits roll past in letters a screen high, and
at the end you can page through the AA project's own story: three goals,
the third being to force IBM to start manufacturing MDA cards again.

It is all drawn by AAlib, the ASCII art library the same people wrote,
with bold and dim for the brightest and darkest parts, and it plays three
Scream Tracker songs by FK underneath.

**Turn the sound up and watch.**

## Controls

- **s** or **Backspace**: on to the next part
- **q** or **Esc**: quit
- In the end text: **Space** or **Down** for the next page, **Up** for
  the one before, **1**, **2** and **3** to change the song

## Options

From a terminal, `bb -loop` plays the demo again and again, `bb 2` starts
at the second half, `bb 3` at the end text, and `bb -nosound` plays it in
silence. `bb --help` lists AAlib's own options, such as `-extended` for
the full character set.

## History

Four friends from Tabor in the Czech Republic made BB in 1997, the AA
project's showcase for AAlib, which Jan Hubicka had pulled out of a tool
he wrote to turn a penguin logo into ASCII art for an old Hercules
monitor. They kept polishing it until 2001. Debian has carried it since
1998, looked after by Michael Bramer, Uwe Hermann and Axel Beckert, so
it never stopped running.

## Credits

- Filip Kupsa (FK): the music
- Jan Hubicka (HH): AAlib, the intro, fire, greetings, photos, the XaoS
  zoom, the timing system and the outro
- Mojmir Svoboda (MS): the 3D engine
- Kamil Toman (KT): the sound engine and synchronisation, plasma, texts,
  titles, stars and snow
- Debian's patches: Uwe Hermann, Axel Beckert and others
- Asciiverse edition: the music starts with the demo and plays on every
  system, found beside the program
- License: GPL-2.0-or-later
