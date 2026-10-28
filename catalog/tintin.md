**THE KICKIN TICKIN DIKUMUD CLIENT.**

That is what the name stands for: (T)he K(I)cki(N) (T)ickin D(I)kumud Clie(N)t. Since Peter Unold's TinTin III in 1992, it has been the client MUD players reach for when they want the game to work for them. Connect to any MUD on the internet with one command, then teach it your habits.

Hungry? `#action {You are hungry} {get bread bag;eat bread}` and you need never starve again. Tired of typing? One alias runs a dozen commands. Lost? The mapper draws every room you walk through, and walks you back.

Fair warning, from its own manual: "TinTin++ doesn't baby sit." You get the keys to everything.

- **Actions, aliases and substitutions**: react to anything the MUD sends, with up to 99 wildcards or full PCRE patterns
- **A scripting language**: variables, lists, loops and maths, all in its own `#` commands
- **The mapper**: rooms and exits drawn as you explore, and `#map run` to speedwalk across them
- **Several sessions at once**, a split screen for input and output, and TLS with `#ssl`

## Getting started

- `#session <name> <host> <port>`: connect, for example `#session bat batmud.bat.org 23`
- `#help`: the built-in manual
- `#end`: quit

## Credits

- TinTin++: Peter Unold, Bill Reis and Igor van den Hoven
- Asciiverse edition: static builds and packaging, no code changes
- License: GPL-3.0-or-later
