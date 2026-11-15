**YOUR RIVALS THINK OUT LOUD. AND THEY HOLD GRUDGES.**

"I haven't forgotten turn 7."

That is the Grudge Holder talking, and it means it. Across the table sit three rivals, and every one of them is a small language model running right there on your own machine, with a personality you pick for it. The Aggressive one drives a hard bargain: "Everything has a price." The Builder builds and builds. The Chaos Agent does whatever seems funniest at the time: "Why not?" And the Grudge Holder remembers every stolen card, every blocked road, and exactly who put the robber on its wheat.

The island is a sweep of hexes, five resources and a robber lurking in the desert. Plant your first settlements and roads, then roll: every hex that comes up pays the settlements around it in wood, brick, sheep, wheat or ore. Push your roads to new ground, raise settlements on the corners and cities on the best of them, and buy development cards for knights, monopolies and hidden points. Wheel and deal across the table. First to ten points wins.

Want to know what they are plotting? Switch to the AI tab and read their reasoning as they make each move, and watch them weigh up the trade you just offered. For a quicker game, any seat can be the Computer instead, a sharp rule-based player that moves at once.

- **Five personalities** to sit across from: Balanced, Aggressive, Grudge Holder, Builder and Chaos Agent
- **Read their minds**: every rival's reasoning, live, in the AI tab
- **Real trading**: propose deals, weigh theirs, or go to the bank
- **Make your own rival**: write a personality, its style and its catchphrases, on the Personalities screen
- **The full race to ten**: roads, settlements, cities, development cards, the longest road and the largest army
- **The Computer**: an instant opponent for a fast game, or four of them to watch with `settl --demo`

**Settle in.**

## Controls

- **Arrow keys** or **h j k l**: move on the board, **n** and **p**: next
  and previous spot, **Enter**: confirm
- On your turn: **s** settlement, **r** road, **c** city, **d**
  development card, **b** bank trade, **t** propose a trade, **e** end turn
- **Tab**: switch the side panel between the game and the AI's reasoning
- **?**: help; **q**: back to the menu while the others play; **Ctrl+C**:
  quit. The game saves after every turn, and the menu offers to continue

## Setting up a game

On the New Game screen choose three or four players and each rival:
**Left** and **Right** step through the personalities, and one step past
the last is the Computer. Below that are the friendly robber (it leaves
players on two points or fewer alone), a fixed or random board, the model
size and how hard the models think.

The models come down the first time you play them, 292 MB for the fast
one and 1.2 GB for the smart one, with no account or key needed.

## History

Nathan Brake wrote settl at Mozilla.ai in the spring of 2026, in Rust and
Ratatui, to put small language models at a game table: no cloud, no keys,
just Mozilla's llamafile running PrismML's tiny Bonsai models right on
the player's machine, each one given a personality, a strategy and a few
catchphrases. The result is a board game where you can read your
opponents' minds, and still lose to them. In the Asciiverse it gained a
rule-based Computer player too, for the quick game.

## Credits

- settl: Nathan Brake, Mozilla.ai
- Language models: PrismML's Bonsai, run by Mozilla.ai's llamafile
- Computer player: Asciiverse
- License: Apache-2.0
