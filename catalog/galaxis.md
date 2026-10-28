**FOUR LIFEBOATS. ONE STARFIELD. THE AIR IS RUNNING OUT.**

A crippled interstellar liner has cast four lifeboats adrift in a
starfield of 20 by 9 squares, and you can't see a single one of them.
What you can do is drop probes. Each probe looks out along all eight
compass directions and tells you in how many of them it sees a lifeboat
(only the nearest boat in each direction counts). Land a probe right on
a boat and the screen says it plainly: "You found a lifeboat!"

Your orders, straight from the rules: find them "as quickly as possible,
before the stranded passengers run out of oxygen!" Every probe is a try,
and the tries are counted.

- **Pure deduction**: once the boats are placed there is no luck left,
  only counts, crossing rays and the squares they rule out.
- **See where it looks**: the eight rays from the cursor are highlighted,
  so you know exactly which squares a probe would search.
- **It does the bookkeeping**: mark the squares you've ruled out, and once
  every boat a probe counted has turned up, the rest of its rays are
  marked for you. Asking an old probe again can mark more, and costs no
  try.
- **Keys or mouse**: arrows, vi keys or the number pad, or click to mark
  and double-click to probe.

Christian Franz made Galaxis as Macintosh freeware; Eric S. Raymond
cloned it for curses in 1994 and still maintains it. His version, he
says, "compensates by automating away some of the game's simpler
deductions."

**Drop a probe. Read the count. Bring them home.**

## Controls

- **Arrow keys**, **h j k l y u b n** or the **number pad**: move (the
  field wraps round)
- **p**: drop a probe, or ask an old probe again
- **Space**: mark a square as empty, or unmark it
- **o**: turn the ray highlighting off or on
- **Mouse**: click to mark, double-click to drop a probe
- **?**: the rules; **q**: give up and see where the boats were

## Credits

- Galaxis: Eric S. Raymond ([gitlab.com/esr/galaxis](https://gitlab.com/esr/galaxis)),
  1994 on, written in C with curses
- After Christian Franz's freeware Galaxis for the Macintosh
- License: BSD-2-Clause
