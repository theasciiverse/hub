**MANKIND BELIEVES IN YOU.**

"Right now you are earth's only hope to save it from alien invaders from space," says the README. "Make your job, and make it good, mankind believes in you..."

Rows of aliens march side to side and drop a step closer each time they reach the edge, bombing you as they come. Slide your gun along the bottom and shoot them down before they land. Four bunkers shelter you, and crumble with every hit. And now and then a UFO crosses the top of the screen, worth 500 points if you can lead your shot.

- **Points by the row**: 100, 150 and 200 points, more the higher they sit, and 500 for the UFO.
- **They get faster** as the block thins out and as the levels go by.
- **Ten skill levels**, from 0, which the game calls "NIGHTMARE", to 9, "May I play daddy?!"
- **A TOP 10 at last**: the high score table its authors wrote in 2003 and never released, finished, with a table for expert, normal and beginner play.

**DON'T LET THEM LAND.**

## Controls

- **Left** and **Right**, or **h** and **l**: move; hold the key down to
  move faster
- **Space** or **k**: fire
- **p**: pause, and again to go on
- **q**: quit
- **Space** on the title screen: start a game

## High scores

A score that makes the TOP 10 asks for your name after the game over
banner: type up to 8 letters and press **Enter**. The title screen shows
the table between its alien parades. Each skill level plays for its own
table: `-l 0` for the expert one, the default for the normal one, and
`-l 2` to `-l 9` for the beginner one. The table is kept in your own
folder (`~/.local/share/ninvaders/highscore`, or `%APPDATA%\ninvaders` on
Windows), so it survives updates.

## Options

- `-l 0` to `-l 9`: the skill level, from 0 (the game calls it "NIGHTMARE")
  to 9 ("May I play daddy?!"); 1 is the default
- `-gpl`: show the licence

## History

Thomas Dettbarn ("dettus") wrote nInvaders in 2002 with Alexander
Hollinger, Sebastian Gutsfeld and Matthias Thar, and code by Mike
Saarna; 0.1.1 (May 2003) added the title screen and a timer that made it
playable on more systems, and was the last release. Alexander Hollinger
and Sebastian Gutsfeld went on to add a high score table that summer,
which was never released; this edition has Debian's patches and brings
that table in, finished.

The Asciiverse runs the game in a loop instead of from a timer signal,
which makes it steadier and lets it run on Windows, and sends only what changes
to the terminal instead of repainting it 50 times a second. Each game now
plays out differently: the original never seeded its random numbers, so
every game was the same.
