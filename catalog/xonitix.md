**ONE LINE. A HANDFUL OF DOTS. CLAIM MORE THAN HALF OF IT.**

Xonitix is a whole arcade game squeezed into a single line of your terminal. You are the little `_` sliding along it. Dots bounce back and forth at two speeds, rebounding off the ends and off every barrier you put down, so fast they blur. Press space and you drop a barrier where you stand. If every dot in your stretch of the line is on one side of you, the other side fills solid with `|` and every cell is worth a hundred points. If they are on both sides, you get a single wall that cuts the stretch in two, and the hunt for a clean side starts again.

Fill more than half the line and the level is yours: a fresh line, and one more dot than before. The catch is that a barrier dropped within a cell of a dot ends the game on the spot, so every press is a tiny gamble between greed and nerve. Wait for the dots to bounce away, slide to the gap, hit space and watch the line fill.

- **The old claim-the-field idea in one dimension**: fence off the enemies, take everything they cannot reach
- **A level a dot**: level one has one, level five has five, all crossing each other and stacking up as `:` when they meet
- **Walk anywhere**: you show as `L` when standing on your own barriers, and you can cross them freely to reach open ground
- **Score attack**: a hundred points a cell, the score climbing at the end of the line
- **Boss mode**: start it with `-s` and quitting wipes the line clean, as if you had been working all along

## Controls

- **Left** and **Right**: start sliding that way
- **Down**: stop
- **Space**: drop a barrier where you stand
- **q**: quit

## Options

- `-l <cells>`: play on a line of your chosen length (normally the terminal's width less 30)
- `-s`: boss mode, quitting leaves no trace on the screen
- `-h`: help

## History

Xonitix was born in Terminal Jam 2018 on itch.io, a jam for games that live in the computer terminal. Breno G. de Oliveira, who goes by wildgaru on itch and garu on GitHub, wrote it in a single file of plain C++ with no libraries at all, so the same few hundred lines built on Windows, Linux and macOS and ran as one small binary that worked straight out of the box. He took the classic game of fencing off enemies and claiming what is left, and asked how little screen it really needs. The answer was one line. He shared the source on GitHub that November, inviting anyone curious to see how it was made, and players on itch left their verdict in the comments: very clever, and it deserves to be in an arcade.

## Credits

- Xonitix: wildgaru (Breno G. de Oliveira), on [itch.io](https://wildgaru.itch.io/xonitix) and [GitHub](https://github.com/garu/Xonitix)
- License: MIT
