**FIFTEEN-TWO, FIFTEEN-FOUR, AND A PAIR IS SIX.**

Pull up a chair. The computer has shuffled, the pegs are in the board, and it wants a game. Six cards each: lay two away into the crib, and remember whose crib it is before you throw, because it belongs to the dealer. Then the play: you take turns laying cards and calling the count, pegging for fifteens, pairs, runs and 31, and saying "go" when you can't. Then the show, where every hand is counted with the starter card and the dealer counts the crib as well. Turn up a jack, and the dealer gets one for "his heels".

- **A quick game**: once round the board, first to 61.
- **A seven-game match**: and a skunk, winning before your opponent reaches 31, counts as two games.
- **No arithmetic homework**: the computer counts both hands and the crib, shows the breakdown (fifteens, pairs, runs, flushes, nobs) and waits before the show so you can count yours first.
- **No fault points**: you can only make legal plays, and when one card is all you can play, it plays itself.
- **Real suits**: hearts, spades, diamonds and clubs as card symbols in a UTF-8 terminal.

**"I get one for his heels." Make it pay for that.**

## Controls

- **Left** and **Right**, or **j** and **k**: choose a card
- **Space** or **Enter**: discard or play the chosen card, and go on
  after a pause
- **q** or **F10**: quit

Cards that would take the count past 31 are skipped, and when only one
card can be played it is played for you.

## History

Cribbage was one of the early BSD games: Earl T. Cohen wrote the game
logic and Ken Arnold added the screen interface (UC Berkeley, 1980).
Mike Sharov replaced it with a rewrite of his own in 2016 for his
bsd-games, and has since fixed its scoring of pairs, runs and flushes
and taught the computer to avoid easy fifteens for its opponent. Suits
show as card symbols in a UTF-8 terminal.
