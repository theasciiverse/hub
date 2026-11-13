**TYPE REAL CODE. YOUR OWN, OR THE CATALOG'S.**

Typing tests hand you word lists. gittype hands you code: it reads the
source, picks out functions, structs, match arms and loops, and turns
each one into a challenge with its file and line numbers on top. The
indentation is skipped for you; the brackets, operators and odd
spacing are not.

Started from av, it types code from games in this catalog: Four in a
Row, av itself, TinyCols, Galaxis, blackjack, Zoridor, Intricacy and
robotfindskitten, each with its licence beside it. Start it inside a
project of your own and it types your code instead.

- **Live numbers**: words and characters per minute, accuracy, mistakes
  and your streak while you type.
- **Stages and a rank**: three challenges a session, a score for each,
  and a developer rank at the end, from "Hello World Newbie" up.
- **Five difficulties**: Easy short snippets to Wild, and Zen with no
  clock.
- **Records and analytics** of every session you have played.
- **Many languages**: Rust, TypeScript, JavaScript, Python, Go, Ruby,
  Swift, Kotlin, Java, PHP, C#, C, C++, Haskell, Dart, Scala, Zig, Elixir,
  Erlang.
- **Fifteen themes**, light and dark.

**Read it. Type it. Rank up.**

## Controls

- **Left** and **Right** (or **h** and **l**): choose the difficulty
- **Space**: start, and move on after each stage
- Type the code; **Enter** at the end of each line
- **Esc**: options during a challenge (skip it, three skips a session,
  or quit)
- **r**: records; **a**: analytics; **s**: settings; **i** or **?**: help

## Your own code

From a shell: `gittype` in a project folder, or `gittype path/to/project`.
`gittype --repo owner/name` clones a GitHub repository and plays that.

## Credits

- gittype: Yuji Ueki (unhappychoice) and contributors
  ([github.com/unhappychoice/gittype](https://github.com/unhappychoice/gittype)),
  2025 on, written in Rust with Ratatui and tree-sitter
- The code to type comes from the catalog games named above, each under
  its own licence (listed in `samples/README.md`)
- License: MIT
