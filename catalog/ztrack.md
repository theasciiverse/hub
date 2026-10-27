Get as far as you can down an endless three-lane road full of stupid but
dangerous traffic. You score more the faster you go, and the top speed is
150 mph. Run into the back of a car, or swerve into a lane that is
occupied, and you lose one of your three cars.

You see the road from behind the wheel, over your bonnet. Cars level with
you are out of sight, but your wing mirrors light up with a blob when a lane
beside you is taken, so check them before you change lanes.

You don't hold a pedal: you set a mode. Accel keeps speeding up, decel keeps
slowing down, and cruise holds your speed exactly.

## Controls

- **Up** or **q**: accel mode
- **Down** or **a**: decel mode
- **Space** or **Tab**: cruise at the current speed
- **Left** or **o**: move left a lane
- **Right** or **p**: move right a lane
- **Esc** or **X**: end the game

On the title screen, **Space** starts a game and **Esc** or **q** quits.
The high score lasts until you quit.

## History

Russell Marks wrote Ztrack 1.0 in October 1995, loosely after a Casio
LCD driving game he remembered as "Turbo Drive", and put it in the public
domain; it was uploaded to sunsite.unc.edu (now ibiblio) in 1996. FreeBSD still
carries it in its ports collection.

This edition reads the keyboard through curses rather than straight from
the terminal device. That makes the cursor keys steer (in the original they
ended the game) and lets the game run in the Windows console. It also fixes
an out-of-bounds read when drawing the title logo. The gameplay is
unchanged.

## Credits

- Game: Russell Marks
- Windows console support: [PDCurses](https://pdcurses.org)
- Asciiverse edition: Asciiverse
- License: public domain
