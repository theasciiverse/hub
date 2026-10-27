Cribbage for one player against the computer. Each hand you are dealt
six cards and lay two away into the crib, which belongs to the dealer.
Then the two of you take turns laying cards and calling the count,
scoring for fifteens, pairs, runs and reaching 31, and finally each hand
is counted with the turned-up starter card. The pegs on the board keep
the score.

A game here is played to 61 points, once round the board, and a match
ends after seven games, with a skunk counting as two. The computer
counts both hands, and waits before the show so you can count yours
first.

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
