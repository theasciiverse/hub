**TYPE. WATCH THE LINE. TYPE AGAIN.**

A handful of words sits in the middle of an empty screen. The clock starts with your first key, every letter turns right or wrong under your fingers, and the moment you land the last one thokr draws your whole run as a curve: where you flew, where you stumbled, and the words per minute, accuracy and steadiness it all adds up to.

Then **n** for a fresh set, or **r** to take the same words again and beat yourself.

- **Words or seconds**: a quick 15 words, a hundred, or a timed run where new words keep streaming in until the clock hits zero
- **Three word lists**: the 200, 1,000 or 10,000 most common English words, or whole sentences with full stops
- **A ghost to chase**: `--pace 70` sends a caret ahead of you at 70 words per minute
- **Death mode**: one wrong key and the run is over
- **Your own text**: type anything with `-p`
- **A history that grows**: every finished test adds a row to `log.csv`, ready for a spreadsheet or a script

## Controls

- Type the words; **Backspace** fixes a slip
- **←** starts the same test over, **→** brings a new one
- On the results: **r** to retry, **n** for a new test
- **Esc**: quit

## Options

- `-w N`: number of words (default 15)
- `-s SECONDS`: a timed test, words streaming until time runs out
- `-l english1k` or `-l english10k`: a bigger word list
- `-f N`: N sentences instead of words
- `-p "TEXT"`: your own prompt
- `--pace WPM`: race a ghost caret
- `-d`: death mode

## Credits

- thokr: [Colby Thomas](https://github.com/jrnxf/thokr) and contributors
- License: MIT
