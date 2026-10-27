A cryptogram, the puzzle from the Sunday paper. A saying is written in a
substitution cipher, every letter swapped for another, and you work out
the key. Put the cursor on a letter and type what you think it really
is: every copy of that letter changes at once, so one good guess lights
up the whole text. Short words and common letters are the way in.

Each game hides one of the maxims of François de La Rochefoucauld, the
17th century French moralist ("Self-love is the greatest of
flatterers"), in J. Hain Friswell's 1871 translation, 456 of them in
all, with a fresh key every time. When every letter is right, the game
says so.

## Controls

- **Arrow keys**, or **Ctrl-B**, **Ctrl-F**, **Ctrl-P**, **Ctrl-N**: move
  the cursor
- **A letter**: decode the letter under the cursor as that letter
- **\***: hint mode, which shows correctly decoded letters in bold
- **~**: quit

## Options

Started from a shell, `cgram file` makes a cryptogram of that file's
text instead of a maxim.

## History

David A. Holland wrote cgram around 2004 "for my own amusement", as he
put it when he added it to NetBSD in 2013; Roland Illig reworked it in
2020 and 2021. It takes its text from the fortune program, which the
Asciiverse does not ship, so this edition brings its own collection of
maxims from Project Gutenberg. It is part of BSD Games in the Asciiverse
catalog, under the BSD licence.
