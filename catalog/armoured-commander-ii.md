You command a tank and its crew in one of ten campaigns of World War
II, from the invasion of Poland in September 1939 to the last weeks of
the war in Germany in April 1945. Fight for Germany, Poland, the Soviet
Union, Finland, France, the United Kingdom, the United States or
Canada, in tanks from the TKS tankette and the T-26 to the Char B1 bis,
the Panzer IV and the Sherman.

Each campaign is a calendar of combat days. Each day is a map of zones
to take and hold: travel, scout ahead, call in air and artillery
support, resupply, and deal with whatever the zone holds. Each
encounter is a battle on a hex map round your tank: spot the enemy,
give every crewman his orders, turn the turret, choose the shell, and
let the dice decide each to-hit, penetration and firepower roll, all of
them shown. Crewmen gain experience and skills, get wounded, spend time
in the field hospital and are replaced; refits bring new tanks. One
saved game per campaign, so several can run side by side.

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
