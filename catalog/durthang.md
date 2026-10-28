**THE MUDS ARE STILL OUT THERE. WALK BACK IN.**

*"...stood the old castle of Durthang, now one of the many orc-holds that
clustered about the dale of Udûn."* Raimo Geisel named his MUD client
after a fortress in Tolkien's Mordor, and built it to be one: a single
terminal program that keeps every world you play and every character you
play there in one list. Pick one, press Enter, and you are through the
gate.

Inside, it does the chores so you can play. The map draws itself as you
walk, from the server's room data or from the "Exits:" lines it reads.
Your passwords go into your system's keyring, never into a config file.
Notes for each character sit right beside the action.

- **Automap**: a live ASCII map with you at the **@**, saved per server
- **Aliases and triggers**: type `k orc` for `kill orc`; highlight a line
  or answer it automatically when a pattern matches
- **Safe logins**: passwords in the Keychain, Credential Manager or Secret
  Service, never on disk in plain text
- **Plain TCP or TLS**, 16 and 256 colours, a 5,000 line scrollback,
  command history and copy mode
- **Sidebar** with the automap and a notes panel, toggled with **F3**

**Your characters are waiting. Reconnect.**

## Controls

- **Arrow keys**: move through servers and characters
- **Space**: expand or collapse a server
- **N**: add a server; **n**: add a character
- **Enter**: connect with the selected character
- **Ctrl+Q**: disconnect, back to the list
- **q**: quit

## Credits

- Durthang: [Raimo Geisel](https://github.com/Pommersche92/durthang)
- Asciiverse edition: packaging, and keyring stores for macOS and Windows
- License: GPL-3.0-only
