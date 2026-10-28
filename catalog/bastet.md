**THE GAME KNOWS WHICH BLOCK YOU NEED. IT IS NOT GOING TO GIVE IT TO YOU.**

"For people who enjoy swearing at their computer," wrote Federico Poloni,
here is Bastet.

Every other falling-blocks game picks the next block at random. Bastet
doesn't. It looks at your stack, tries every block in every place it could
go, and hands you the one that does you the least good. That deep gap you
left for the long straight piece? Bastet has seen it too. Clearing even a
few lines is an achievement, and a long game is a real one.

In the normal game you see the next block, and Bastet chooses the one after
it knowing you have seen it. The harder game takes the preview away,
"thus achieving," as the README puts it, "a higher level of bastardness."

- **An opponent, not a dice roll**: a chooser that picks the worst block
  it can find
- **Two games**, normal and harder, each with its own top ten
- **Classic scoring**: 100 points for one row, up to 800 for four at once,
  and every ten rows the blocks fall faster
- **Your keys**: every one can be changed in Customize keys

## Controls

- **Left**, **Right**: move the block
- **Down**: move it down one row
- **Space**: turn it clockwise, **Up**: turn it the other way
- **Enter**: drop it straight to the bottom
- **p**: pause
- **Ctrl+C**: quit at once (high scores already made are kept)

Every key can be changed in Customize keys.

## Files

Keys and high scores are kept in the player's data folder,
`~/.local/share/bastet` (`%APPDATA%\bastet` on Windows).

## History

Federico Poloni wrote Bastet; version 0.41 reached Slashdot in April
2005, and his 0.43 rewrite of 2009 split the chooser into the two games
above. It is packaged by Debian, Fedora and
others. This edition has Debian's fix for printing names, and fixes of
our own: Enter drops the
block as the documentation always said, scores and keys follow
`XDG_DATA_HOME` instead of needing a setgid binary, and it builds for Windows.
