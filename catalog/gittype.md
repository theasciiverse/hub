**SHOW YOUR AI WHO'S BOSS.**

Typing tests hand you word lists. gittype hands you code. It reads real source, picks out the functions, structs, match arms and loops, and turns each one into a challenge, with its file and line numbers on top. The indentation is skipped for you; the brackets, operators, semicolons and odd spacing are not. Just you, your keyboard and somebody else's coding sins.

Started from av, you type code from games in this very catalog: Four in a Row, av itself, TinyCols, Galaxis, Blackjack, Zoridor, Intricacy and robotfindskitten, in Rust, C, Go, Zig and Haskell. Start it in a project of your own and you type your own code instead. Every session ends with a rank, and there are sixty-three of them to climb: from Hello World and Rubber Duck through Git Ninja, Kernel Hacker and Quantum Computer, all the way to the legends, Heisenbug, Blue Screen and, at the very top, Kernel Panic. How far can your fingers take you?

- **Live numbers:** words and characters per minute, accuracy, mistakes and your streak as you type
- **Sixty-three ranks,** each one with its own ASCII-art title
- **Five difficulties:** Easy short snippets, Normal, Hard, Wild chunks of any length, and Zen, a whole file
- **Records and analytics** of every session you have played
- **Twenty languages:** Rust, TypeScript, JavaScript, Python, Go, Ruby, Swift, Kotlin, Java, PHP, C#, C, C++, Haskell, Dart, Scala, Clojure, Zig, Elixir and Erlang
- **Fifteen themes,** light and dark

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

## History

Yuji Ueki (unhappychoice) started gittype at the end of August 2025 with a simple, cheeky question: why type word lists when you could type your own code? In little more than a year it has grown more than thirteen hundred of his commits, help from contributors, twenty languages, themes and a ladder of ranks, and it is still growing.

## Credits

- gittype: Yuji Ueki (unhappychoice) and contributors
  ([github.com/unhappychoice/gittype](https://github.com/unhappychoice/gittype)),
  2025 on, written in Rust with Ratatui and tree-sitter
- The code to type comes from the catalog games named above, each under
  its own licence (listed in `samples/README.md`)
- License: MIT
