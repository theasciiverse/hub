**MULTI-USER CLAY.**

Lera is Swedish for clay, and for mud. Pick a world from the list, press Enter, and you are standing in it: no config language to learn, no host and port to look up. Every MUD in the Asciiverse catalog is already there, with what kind of world it is and how long it has been running, and you can add any other world in a few keystrokes.

Once you are in, the screen takes care of itself. Colour comes through as the MUD intended it, in 16, 256 or millions of colours. Scroll back through the fight you just had and the screen splits, so the live text keeps running underneath. Your health and mana sit in the status line when the MUD sends them, and your password never shows on screen.

- **Every catalog MUD in one list**, filtered as you type, plus worlds of your own
- **Scrollback that splits**, with PageUp or the mouse wheel, so you never miss what is happening now
- **Command history** on Up and Down, and the usual line keys
- **Vitals in the status line** from GMCP, on the MUDs that send them
- **TLS** where the world offers it, and compression to keep things quick
- **A log of every session**, kept per world as plain text
- **Reconnect** with one key when the line drops

## Keys

- **Enter**: connect to the world, then send each line
- **Up**, **Down**: earlier commands
- **PageUp**, **PageDown** or the **mouse wheel**: scroll back; **Esc** returns to the live end
- **Shift+drag**: select text to copy
- **Ctrl+R**: reconnect; **Ctrl+D**: disconnect
- **Ctrl+N** in the list: add a world of your own
- **F1**: all the keys; **Ctrl+Q**: quit

From the command line: `lera <world-id>`, or `lera <host> <port> --tls` for anywhere at all.

## Credits

- Lera: Asciiverse
- License: MIT
