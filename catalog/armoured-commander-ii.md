**SEPTEMBER 1939. ONE TANK. ONE CREW. SIX YEARS OF WAR AHEAD.**

Climb into the commander's hatch. In front of you lies the whole war in
Europe, from the invasion of Poland to the last weeks in Germany, and a tank
that may not be up to it. Drive a Polish TKS tankette or a 7TP into the
September Campaign. Defend Finland in the Winter War with "one of the few
tanks in the Finnish armed forces". Cross into France in 1940 for Germany,
or hold the line for France or Britain in a Char B1 bis or a Cruiser. Or
roll a Sherman across Europe in Patton's Best and Canada's Best.

Each day of a campaign is a map of zones to take and hold: scout ahead, call
in the artillery and the aircraft, resupply before the ammunition runs dry.
Each battle is a hex map round your tank: spot the enemy before he spots
you, give every crewman his orders, turn the turret, choose the shell, and
watch the dice decide every hit, every penetration, every kill. Nothing is
hidden.

Your crew are people. They gain experience and skills, earn nicknames, get
wounded, spend weeks in the field hospital and come back, or don't. Refits
bring new tanks.

- **Ten campaigns, 1939 to 1945**, for Germany, Poland, the Soviet Union,
  Finland, France, the United Kingdom, the United States and Canada
- **Tanks from the TKS and the T-26** to the Char B1 bis, the Panzer IV and
  the Sherman
- **Every roll on screen**: to-hit, penetration and firepower, all shown
- **Gregory Adam Scott's art, sounds and theme tune**, laid out for the
  terminal, the maps growing with a bigger window
- **One save per campaign**, so several wars can run side by side

## Controls

- In battle: **W/S** choose a crewman, **A/D** change his order,
  **H** open or close his hatch, **F** the crewman's menu;
  **Space** ends the phase
- Moving: **W/S** forward or reverse, **A/D** pivot, **H** try for a
  hull-down position, **R** reposition
- Shooting: **W/S** choose a weapon, **A/D** choose a target, **Q/E**
  turn the turret, **C** change the shell, **R** use the ready rack,
  **F** fire; **Enter** goes on after each roll
- **Tab** in battle: your tank in full
- On the day map: **1** to **4** for Supply, Crew, Travel and Group;
  **Q E A D Z C** choose a direction, **Enter** move, **R** recon,
  **W** wait or defend, **I** abandon the tank
- On the calendar: **1** to **4** for the day's mission, crew and tank,
  journal and field hospital; **Enter** starts the day
- **Esc**: the game menu with sound, volume, message pause and keyboard
  layout (QWERTY, AZERTY, QWERTZ, Dvorak), and Save and Quit

## Options

- `--battle [campaign]`: straight into one battle with a fresh tank and
  crew, to try the battle rules (nothing is saved); campaigns are named
  as `poland_campaign`, `pattons_best`, `winter_war_finland` and so on
- `--art`: browse the game's pictures

## History

Gregory Adam Scott made Armoured Commander II in Python 3 and libtcod
between 2016 and 2020 as free software, the sequel to his Armoured
Commander; later versions went to Steam. This edition ports the free
version to Rust and Ratatui: the same rules,
campaigns, art, sounds and theme tune, with every screen laid out for a
terminal of 100x30 and the maps growing with a bigger one. Its README
lists the few places where it plays or looks different.

## Credits

- Armoured Commander II: Gregory Adam Scott, 2016 to 2020
  ([github.com/sudasana/armcom2](https://github.com/sudasana/armcom2))
- Terminal port: Asciiverse
- License: GPL-3.0-or-later
