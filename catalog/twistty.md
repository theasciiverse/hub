**TWENTY-SIX LITTLE CUBES. SIX COLOURS. ONE TERMINAL.**

A real 3D cube floats in your terminal, and every face of it turns. Spin the whole thing around with the arrow keys, twist any face a quarter turn with a single letter, and watch the layer swing round in smooth animation. Then scramble it thirty turns deep and try to bring it home.

Twistty draws its cube the way a 3D game would, triangle by triangle, with depth and perspective, and then decides how your terminal should show it:

- **Half blocks, sextants and octants** in full 24-bit colour, picked to suit your terminal
- **Real pixels** in terminals that do graphics, such as kitty and Ghostty
- **Classic**: Benjamin Jones' original look, every cell matched to the ASCII character that best fits its shape, so the cube is built from letters and punctuation
- **Scramble with a seed**: type any word and get the same scramble every time, or leave it empty for a random one
- **Save and load** a cube in the middle of a solve
- **Space squares it up**: the cube swings to the nearest straight-on view

## Controls

- **f b l r u d**: turn the front, back, left, right, up or down face counterclockwise; **F B L R U D** (with Shift) turn it clockwise
- **Arrows**: turn the whole cube; **z** / **Z**: roll it
- **Space**: square the cube up to the view
- **v**: the next look (classic, half blocks, quadrants, sextants, octants, pixels; only those your terminal can show)
- **m** or **Esc**: the menu: Resume, Scramble, Save, Load, Exit

Faces are named as the cube faces you now, so **f** is always the side looking at you.

## Options

- `--view NAME`: start in a look: `classic`, `half`, `quadrant`, `sextant`, `octant` or `pixel`

## History

Benjamin Jones built this cube in 2019 on CAM, his own library for drawing pixels as coloured ASCII in curses' eight colours. This edition moves it onto notcurses, which gives it true colour (the orange and white faces were magenta and cyan before), finer block and pixel graphics, and a cube that is square whatever your font.

## Credits

- Twistty: Benjamin Jones (the cube and CAM)
- Drawn with notcurses by Nick Black and its contributors
- License: MIT
