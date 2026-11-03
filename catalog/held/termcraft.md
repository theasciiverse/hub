**THE SUN IS GOING DOWN. YOU OWN NOTHING BUT YOUR FISTS.**

Punch a tree. Turn the wood into planks, the planks into a crafting table,
the table into a pickaxe. Dig into the hillside before the zombies come
out, light it with a torch, and listen for the creeper you did not see.
Termcraft is the whole survival loop of a block world, turned on its side
and drawn in terminal pixels: lit caves, rain and snow, rooms cut away so
you can see inside, and every creature with its own silhouette.

Then keep going. Smelt iron, find diamonds, raise a farm and breed the
animals that wander into it. Trade glances with villagers, raid dungeons,
build a portal of obsidian and step through into the Nether, where ghasts
spit fire and blazes guard the fortresses. Craft the Eyes of Ender, follow
them to the stronghold, and at the end of everything the Ender Dragon is
waiting.

You do not have to do it alone. One command hosts a world and drops you
into it; friends join from their own terminals, on the same network or
through SSH, up to eight players in all, with their own inventories,
shared building, chat and, if you leave it on, PvP.

Short on time? **Lantern Run** is a compact challenge route: cross a
broken trail, take back a ruin from its guards, raid the supply chest,
bridge the chasm and relight the signal.

## Controls

- **A** / **D** or **Left** / **Right**: walk; double-tap and hold to
  sprint (needs a terminal that reports key releases, such as kitty,
  Ghostty, foot or WezTerm)
- **W**, **Up** or **Space**: jump, swim up, climb ladders
- **Left mouse**: mine and attack; **right mouse**: place and use;
  **F**: use the block under the pointer
- **E**: inventory and crafting (the recipe book is on the left)
- **1** to **9**: hotbar; **V** / **Shift+V**: drop one or the stack
- **F4**: cycle the Detail, Overview and Wide views; **+** / **-**: zoom
- **T**: chat in co-op, commands in solo; **O**: settings (difficulty and
  game rules); **F3**: diagnostics
- **Q** or **Esc**: close a screen, or save and quit

The game autosaves. It plays at any size, best at 120x40 or larger.

## Options

- `termcraft trial`: play Lantern Run
- `termcraft host`: host a co-op world and play in it (**T** shows the
  address); friends run `termcraft client ADDRESS --player NAME`
- `termcraft join USER@HOST --player NAME`: join through an SSH account
- `termcraft world list`: your saved worlds; `termcraft world play ID`
  opens one

Everyone in a co-op game needs the same version. The full guides
(multiplayer, hosting, saves) are in the `docs` folder of the install.

## Credits

- Termcraft: Sebastian Pagel
  ([github.com/pagel-s/termcraft](https://github.com/pagel-s/termcraft)),
  2026, written in Rust
- License: AGPL-3.0-only
