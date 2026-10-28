**THE LETTERS ARE FALLING. SPELL FAST.**

Letters drop one at a time into a pit ten columns wide. Steer each one
left or right and let it land so that it spells words with the letters
around it: across or up and down, forwards or backwards, never
diagonally. A word of four letters or more scores and vanishes, and the
letters above fall into the gap. Palindromes count twice. The letters
fall faster as you find more words, and the game ends when the pit is
full.

- **Rare letters pay**: letter scores and how often each letter turns up
  come from the dictionary itself.
- **Blanks**: now and then a blank falls; press the letter you want it to
  be before it lands, or the game picks one for you.
- **Pit empty bonus!**: clear the whole pit and it pays extra.
- **English or French**: Lexter picks its dictionary from your language;
  `lexter -d fr` or `lexter -d en` chooses for yourself.

**Catch a letter. Make a word. Make room.**

## Controls

- **Left** and **Right**: move the letter
- **Down**: lower it a row; **Space**: drop it
- a letter key: what a falling blank should be
- **P**: pause; **H**: help; **L**: letter scores and chances;
  **W**: the words found so far
- **S**: save a screenshot as text; **Q**: quit

The keys are capital letters: **P**, **H**, **L**, **W**, **S** and **Q**
with Shift, so lowercase letters stay free for blanks.

## High scores

The table keeps the best 20 games, with each dictionary getting an equal
share. It lives in your own folder (`~/.local/share/lexter/scores`), so it
survives updates; `lexter -s` prints it.

## History

Mark Pulford started Lexter in 1998 and released it in February 2001, with
1.0.3 that March as the last version. It came with an English and a
French dictionary and was built to take others: any plain list of words
makes a new game.

The Asciiverse edition keeps scores and screenshots in your own folder,
stops a spurious
dictionary error at start, and shows the French dictionary's accented
letters properly on today's UTF-8 terminals.
