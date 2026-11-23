**NOBODY ON CONAMARA STATION IS SUPPOSED TO BE RACING THE WORK ROVERS. EVERYBODY IS.**

Under the ice of Europa, with Jupiter filling the long window on the
upper deck, the night shift has a league. You get a Mule: a squat
ice-crawler with two drive tracks, a gyro, eight sensor slots, two weapon
mounts and a logic board. You do not drive it. You wire it. Sensors feel the world, logic decides, the
tracks move, and then you let go and watch what you built try its best.

Every part is a box on your bench, and every wire finds its own way
round them. Press Tab while your rover runs and the whole bench lights
up, each wire glowing with the signal running through it: there is the
ranger's number dropping under 3, there is the compare flipping on,
there go the tracks easing off for the corner. Out in the arena your
rover slides across the ice in Braille, its sensor beams feeling ahead
and its trail curling behind.

## The night league

On your first night, Ines, who runs the league from a paper notebook,
pushes a rover into your hands. Seven nights later you are under the dome
at midnight, facing a matte black rover nobody will admit to wiring. In
between come Hana and her stopwatch, Oskar who is always faster, Sami and
the meltwater, and Ruben from comms, who fights in the boiler room and
sends his daughter forty-minute messages about it.

- **Ring Hall Run**: one lap of the lower deck, past the laundry and the
  pump columns, eight checkpoints in order. Homer, waiting in your
  garage, does it at a steady trot. Hana from hydroponics keeps the
  stopwatch, and she knows how much faster it can go. Full power just
  slides you into the walls
- **The Cold Stores**: aisles of frozen seed racks that all look alike,
  and one hatch out. Your compass knows exactly where the hatch is. It
  knows nothing about the shelves in between
- **The Puck**: a circle scraped on the pump room floor, a bucket of
  meltwater to make it slick, and Tumbler, Sami's rover, which has never
  been pushed out by a newcomer
- **Sparks in the Boiler Room**: the first battle, among the pipes,
  against Ruben's Sprocket
- **The Long Window**: Hana's second course, under Jupiter, with a hairpin
  round the stores lift
- **Laundry Night**: Kettle, which keeps its distance, faces you and keeps
  firing
- **Lights Out in the Dome**: Nightjar, which presses in when you are weak
  and backs away when it is

Every rover goes into battle with 100 charge, and at 0 it stalls where it
stands. Each challenge has three stars, for the time on the wall or the
charge you still have, and every one of them is in reach with the parts
you have.

## The parts

- **Sensors**: a bumper that feels a touch, a whisker that feels what is
  near, a ranger that measures the way ahead, a compass that knows your
  heading or the way to the beacon, a radar that finds the nearest rover
  through walls, and a gauge for your own charge
- **Logic**: AND, OR, NOT, compare, timer, toggle, counter, memory and a
  number
- **Drive**: a left track and a right track, each with forward and back,
  and a gyro that spins the rover on the spot
- **Weapons**: a pellet gun that fires frozen pellets off the nose, and a
  lobber that throws slush over walls to the range you wire into it

Every rover is a small text file you can copy to a friend or open in an
editor, and the arena is exact: the same wiring always gives the same
run, on any machine.

## When the wiring grows up

Press **L** and your wiring turns into Lua: a line or two per part, in the
order the wiring runs, driving exactly as the wiring did. Open it in your
editor, change anything, run it again, and watch what it prints beside the
arena. Or start a rover in plain Lua from nothing and give `tick()` your
own ideas. Scripts can feel, think and drive, and nothing else: no files,
no system, and a budget of instructions every tick.

## Bring your own language

Any program can drive a rover. Icewire writes its readings as plain text
lines sixty times a second and reads back lines like `tracks 0.8 0.8`
and `fire`, so a bot can be a shell script, a Python program or anything
else that reads a line and prints one. Two come with the game: Shellby,
in plain shell, and Dodger, in Python, who weaves and lobs and beats
Kettle. Then pit them all against each other in a tournament with nobody
watching, and watch the best matches again as replays.

## Controls

- **Arrows** or **hjkl**: move about the bench; **Tab** jumps from part to part
- **a** or **Enter**: add a part; **Enter** sets a part's mount, mode or value
- **w**: wire from the part under the cursor, then **Enter** on the part it feeds
- **m** moves a part, **x** removes a part or wire, **u** undoes
- **L** compiles the wiring to Lua; on a Lua rover **e** opens the script
  in your editor
- **r**: run the rover; **c** picks the next challenge
- In the arena: **Space** pauses, **.** steps one tick, **f** goes faster,
  **Tab** shows the live bench, **Esc** stops so you can rewire
- The mouse works too: drag parts, click an output to start a wire,
  right-click to remove
- **?** shows every key, **p** opens the parts library
- **Watch and learn** on the title screen: a rover wired in front of you,
  key by key, and run three times; Space pauses, the arrows step, and at
  the end Enter keeps it
- The league on the title screen plays the season night by night; free
  play opens every challenge
- **B** in the garage makes a bot rover; `icewire --tournament dodger
  kettle nightjar` runs a tournament, and `icewire --replay FILE` watches
  a match again

## Credits

Made by Asciiverse, from David Sandquist's design. MIT licence.
