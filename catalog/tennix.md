**HOLD IT... HOLD IT... NOW LET GO!**

The crowd goes quiet. The umpire leans forward in the high chair. The ball hangs beside you, waiting to be served, and your power bar is empty. Press the hit key and hold it: the bar climbs, your racket tilts back, and the whole stadium can see what is coming. Let go, and the ball cracks across the net. Too timid and it floats over for your opponent to punish. Too greedy and it sails long, the umpire throws up his arms, and the line reads **out!**

Across the net waits Carl Van Court, the computer, who never gets tired. Or a friend on the same keyboard. Every point is a duel of timing:

- **The power bar** fills while you hold and drains the moment you let go, so let go just as the ball arrives
- **The racket** sends the ball where it meets it: dead centre and it flies straight, off the frame and it angles for the side lines, and maybe past them
- **Three strokes**: the plain drive, the **topspin** that loops high and drops in, and the **smash** that goes like a bullet
- **Every call made**: *net!*, *out!*, *fault!*, *volley!*, and the bitter *did not catch the ball*, then the umpire points to the winner and the crowd applauds

Then take it on tour. Pick your venue on a map of the world where night is really falling: red clay in Paris with rain in the air, ryegrass in a London drizzle, a hard court in New York under thick fog, Melbourne, Kitzbühel, Beijing, or a tiny club with thirty seats on the edge of the Atlantic in the Hebrides. Play a city after dark and the match is lit by floodlights. Matches go to best of five sets, six games by two or seven, deuce and advantage in every game; best of three or a single set when time is short.

## Controls

- **Player 1**: **Up/Down** move, **Space** hit, **Left** topspin, **Right** smash; or **W/S**, **D**, **E**, **F**
- **Player 2**: **O/L** move, **K** hit, **I** topspin, **J** smash
- **Gamepad**: stick or cross to move, **A** hit, **B** or **Y** topspin, **X** smash, **Start** pause
- **P**: pause; **M**: sound; **Esc**: back to the menu, where the match waits to be resumed

In terminals that report key releases you hold and let go; in the others, tap the hit key to wind up and tap again to swing.

## Options

- `--demo`: the computer plays itself, venue after venue
- `--venue N`: start the demo at venue 1 to 7
- `--sets N`: sets to win, 3, 2 or 1
- `--night`, `--day`: floodlights or daylight, whatever the clock says
- `--mute`: start with the sound off

## History

Thomas Perl wrote Tennix! in 2003, a little tennis game at 320 by 200. On the 10th of May 2007 he ported it to SDL at twice the size, and then he kept going: an umpire in the chair, rain, fog and floodlit night matches in 2008, and in February 2009 the power bar and a world map of the four great tournaments, with night falling on it as it falls on the real cities. Tennix ran on Linux, Windows, Mac OS X and Nokia's Maemo internet tablets, learned to play against Python robots, and in 2011 became the Classic Championship Tour. It moved to SDL2 in 2023 and was still being served in August 2026. This edition is his game ported from C, the match checked against his code tick for tick, drawn in half blocks for the terminal.

## Credits

- Tennix!: Thomas Perl, code, graphics, sounds and idea
- Some sound effects based on data from the Freesound Project
- World map outline from Vardion's public domain BlankMap-World
- Terminal edition: Asciiverse
- License: GPL-2.0-or-later
