**NAVIGATE THE BALL INTO THE AT-SIGN!**

That is all level 1 asks, and it sounds easy. Your red ball never stops rolling. An arrow key sends it off one way and it keeps going until you send it another, or until it hits something, and everything on the screen that is not empty space is a wall: the borders, the boxes, the giant letters, every star and every word of the level's own text. Touch any of it and you lose a life and roll again from the start.

Every crash leaves a `0` where your ball last rolled, and a `0` is an extra life for whoever rolls over it, so the corners that beat you slowly fill up with spare lives. Each level hands you a pile of points that drains every moment you play, and every press of an arrow costs 77 more: the quickest line with the fewest turns wins.

Eleven levels, each a plain page of text. Roll past the game's own name in letters of X, through a maze folded inside itself, across a field of stars with one narrow staircase cut through, into a grid of walls built from the very `O`s your ball is made of, and up the layers of a network stack to the last level, where the goal is the at-sign in THE AMBASSAD@R 0F PAIN. Finish it and the game says "Well done!". Lose the last life and it says "Sucker!".

## Controls

- **Arrow keys**: send the ball up, down, left or right
- **q**: quit

## Options

- `aop level.txt ...`: play your own levels, in order. A level is 24 lines of 80 characters: `%` is the start, `@` the goal, `0` an extra life, anything else a wall; `levels/empty-level.txt` is a blank one to draw in.

## History

The whole game is 64 lines of C, and every one of them is still here as written. Claire Wolf once told Raffael Himmelreich that C64 programmers wrote games like her *Power Ballon* in under a hundred lines, and that on a modern Unix it would take twice that. Raffael wrote this one in 97 lines to prove otherwise. Claire sent it back almost at once, squeezed to 64. They put it out in 2004, six versions between January and April, with an open invitation: design new levels, add nifty features, as long as the code stays at 64 lines or fewer. The file's last line still says it: "Yup - This are 64 lines of C code. ;-)"

## Credits

- Ambassador of Pain: Raffael Himmelreich and Claire Wolf, on [GitHub](https://github.com/hit-sys/Ambassador-Of-Pain)
- License: GNU GPL version 3
