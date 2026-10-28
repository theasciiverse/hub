**THE MUDS ARE STILL OUT THERE. HERE'S YOUR WAY IN.**

Text worlds full of quests, guilds and other players, still running on
servers across the internet. Blightmud is a modern way to reach them from
your terminal: a MUD client written in Rust by Linus Probert, a long-time
TinyFugue user who wanted one of his own.

Connect, and everything a serious MUD player wants is there. Triggers,
aliases, timers and keybindings, a status bar you can shape and whole
plugins, all in Lua. It speaks the protocols modern MUDs use to send
structured data (GMCP, MSDP and MSSP), connects over TLS, plays a MUD's
music and sound effects, spellchecks what you type, splits the screen when
you scroll back, and has a screen reader mode.

- **Lua for everything**: triggers, aliases, timers, keybindings, the
  status bar, plugins
- **Saved servers**: `/add_server` once, then `/connect <name>`
- **Screen reader friendly**, with a mode of its own
- **The manual inside**: `/help` and its topics

## Getting started

- `blightmud --connect <host>:<port>`: connect straight away
- `/connect <host> <port>`: connect from inside Blightmud
- `/help`: the built-in manual
- `/quit`: quit

## Credits

- Blightmud: Linus Probert and contributors
- Asciiverse edition: builds and packaging, no code changes
- License: GPL-3.0
