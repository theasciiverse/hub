**LET'S KICK SOME ASCII.**

Asciicker is a real 3D world made of characters. Hills rise in blocks of
green and dotted grass, pines stand in dark teal stacks, a grey boulder
the size of a house sits by the path, and when you press Q or E the whole
island swings around you, mountains, lake, fences and all. Nothing is
painted on: it is a terrain and mesh renderer that happens to draw with
CP437 instead of pixels.

You wake on a forest path with two armoured companions who follow you
wherever you go. From there the island is yours: wander up the slopes,
jump the rocks, meet the bands of armed strangers, and pick up what you
find. Giant's maces and hammers, an alpha sword, a crossbow, a flail,
light and heavy armour, helmets and shields, unidentified rings in four
colours, meat, eggs and water. Equip a weapon and Enter swings it. Drink
the grey potion and you are riding a wolf; drink the gold one and it is a
giant bee.

Be warned that this is a concept, not a finished adventure: Marcin
Sokalski (Gumix, of ASCII Patrol) built it as a showcase of what ASCII 3D
can do, and the world has more to explore than to accomplish. As a piece
of terminal engineering it is astonishing.

For the curious, it is also scriptable: open the chat with Tab, start a
line with a backslash, and the rest runs as JavaScript against the game,
with `ak.getPos()` and friends.

## Controls

- **Arrow keys** or **WASD**: walk
- **Q** / **E**: turn the view
- **Space**: jump
- **Enter**: attack (with a weapon equipped)
- **I**: open and close the inventory; **1** to **9** pick up the item
  shown under you, **0** drops the highlighted one
- **Tab**: chat; Tab again sends it (a line starting with `\` runs as
  script)
- **Esc** (or **\\**): the game menu (video, sound, controls, main
  menu, exit); Esc again closes it
- A gamepad works too (checked with an Xbox 360 pad)
- Mouse: hold the left button toward where you want to walk, right
  button to jump, drag with the right button to turn the view

In terminals with the kitty keyboard protocol (kitty, Ghostty, foot,
WezTerm) held keys walk and turn smoothly; elsewhere a held key is
followed through its key repeat, so walking starts after your keyboard's
repeat delay. **H** or **?** shows the keys in the game, and the menu's
Controls has a page for the keyboard and one for the mouse.

## Credits

- Asciicker: Marcin Sokalski (Gumix),
  [github.com/msokalski/asciicker](https://github.com/msokalski/asciicker),
  2019 to 2024, C++; [asciicker.com](https://asciicker.com)
- QuickJS-ng by Fabrice Bellard, Charlie Gordon and the QuickJS-ng
  authors (MIT); miniaudio by David Reid (public domain or MIT-0);
  stb_vorbis by Sean Barrett (public domain)
- License: MIT
