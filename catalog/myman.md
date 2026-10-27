Those scary ghosts are back, and they have mistaken you for their old
rival. Steer MyMan round the maze and eat every dot to clear it, while
four ghosts hunt you, each in its own way. Eat one of the big power
pellets in the corners and for a few seconds the ghosts turn and run,
and you can eat them for points. Fruit appears now and then for a bonus;
clear the maze and the next one is faster.

The maze scrolls to follow you, so it plays on any size of terminal.

## Controls

- **Arrow keys**, **hjkl** or the number pad (**4 2 8 6**): move; a turn
  pressed early is taken at the next opening
- **P** or **Esc**: pause
- **S**: sound on or off
- **C**: colour on or off
- **T**: save a screenshot, as HTML and text, in the myman folder of your
  data folder
- **?**: help, with the credits for every maze
- **Q**: quit

## Options

Started from a shell, MyMan takes options; `myman -h` lists them all.

- `-v VARIANT`: one of several hundred mazes, every one built in, among
  them `pacman`, `quackman`, and ones after old home-computer versions
  such as `paczx` (ZX Spectrum) and `pac64` (Commodore 64)
- `-z SIZE`: tile size, `small` (the default) or `big`, `huge` and more
- `-l NUM`: start with NUM lives

## History

Benjamin C. Wiley Sittler wrote MyMan on a dare on 28 June 1998, as 742
lines of C; colour and the small tiles came that December, and it grew
over the next twenty years into a game with hundreds of mazes that runs
on almost anything with a screen. Toru Iwatani's Pac-Man was the
inspiration.

This edition has the Termux and Fedora build fixes. Screenshots go to
your data folder rather than the game's own folder, and the attract
screen no longer leaves the ghosts' names behind on wide terminals.

## Credits

- Game: Benjamin C. Wiley Sittler
- Build fixes: Henrik Grimler (Termux), Jiri Vymazal (Fedora)
- Asciiverse edition: Asciiverse
- License: MIT
