**TWENTY-SIX LETTERS WALK INTO AN ARENA. ONE WALKS OUT.**

You are a letter: a bold capital on a floor of stone, and every other letter in the arena wants you gone. Throw fire at them. Leap out of the way of theirs. When the dust settles, the last one standing takes a point for every letter that fell, and a new arena opens for the next round.

Every fighter carries the same five spells, each on its own key, all paid for out of one bar of energy that fills back up as you go:

- **Fire ball**: flies where you face and bursts on the first thing it hits
- **Dash**: four cells in a blink, straight past whatever was about to hit you
- **Nova**: eight sparks burst out of you in every direction, murderous up close
- **Wall**: three cells of stone rise in front of you, and fire breaks on them
- **Mine**: left under your feet, bursting under the next enemy foot

Each spell has its own cooldown, so a duel is never just who shoots first. It is who runs dry first, who wastes the dash, who walks into the mine they watched being laid. And nobody hides for long: forty seconds in, the storm rolls in from the walls and swallows the arena ring by ring, pushing the survivors together until somebody wins.

A match rotates through five arenas: The Pit, Pillars, Crossroads, Ruins and Rings. Fight alone against up to seven computer players, Easy, Normal or Hard, who walk at your speed and pay the same costs you do, or host a game for friends on the local network and add bots to the fight. Want to watch first? `asciiarena --demo` hands every letter to the computer.

## Controls

- **W A S D** or the **arrow keys**: walk, and turn to face that way
- **Space** or **1**: Fire ball; **Q** or **2**: Dash; **E** or **3**: Nova
- **R** or **4**: Wall; **F** or **5**: Mine
- **Esc**: leave the match
- In the menu, the arrow keys choose and change, **Enter** goes

## Options

- `asciiarena solo`: straight into a match, with `--bots N`, `--level easy|normal|hard`, `--rounds N`, `--arena NAME` and `--character X`
- `asciiarena --demo`: the computer plays every letter, match after match
- `asciiarena client --host IP:PORT`: join a game on the local network
- `asciiarena server -p PLAYERS --bots N`: a server for the local network, without a screen

## History

Luis Enrique Muñoz Martín, lemunozm on GitHub, started AsciiArena in June 2020: a terminal deathmatch with a real client and server, so friends could fight over the network. In its first week he wrote the networking it needed, then moved it into a library of its own, message-io, which has since passed two hundred thousand downloads. The game grew a lobby where waiting letters wander about, an arena and a points system, in alpha releases through April 2021. Its README promised "a lot of skills with custom keys", but the full game waited, one fire ball and a network demo, until Asciiverse finished it in 2026 along the lines he had drawn: five spells, five arenas, the storm, rounds, and computer players to fight.

## Credits

- AsciiArena: Luis Enrique Muñoz Martín (lemunozm)
- Spells, arenas, storm and computer players: Asciiverse
- Networking: message-io by lemunozm
- License: Apache-2.0
