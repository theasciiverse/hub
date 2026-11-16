**GIVE IT A SONG. IT GIVES YOU A FIGHT.**

Cascade listens to music the way you do. Hand it any song you own and it hears where the drums hit, where the melody leaps, how fast the beat is going, and a few seconds later that song is pouring down five lanes at you as a chart nobody wrote by hand. Your favourite album, the track you've had on repeat all week, your own band's demo: every one of them becomes a level.

And it plays like a proper rhythm game. Notes fall as soft half-block glow toward the line, and every Perfect throws sparks and splits the colours for a heartbeat. The starfield behind the highway warps into streaks when the song gets loud, so the chorus really does feel faster than the verse. Chords come at you two and three at once, long notes want holding, and on Hard and Expert a held note can slide across to another lane before it lets you go.

Nine songs are waiting the first time you start, so you can play straight away: songs from Bellbeat, the Asciiverse's own rhythm game, all written for it. From the bright bell of *Hello, World* through the *Segfault March* in 2/4, the *Waltz for a Spinning Disk* in 3/4 and *Five Nines* in 5/4, to *Escape Sequence*, *Kernel Panic* and, at 172 beats a minute, *SIGTERM*.

- **Any song becomes a chart.** Press **I** on the song list and give it an MP3, FLAC, Ogg or WAV file; Cascade finds the tempo and the beat itself and builds Easy, Medium, Hard and Expert, each with a star rating.
- **Four modifiers** to raise the stakes: Hidden, Flashlight, Sudden Death and Perfect Only, each combination with its own best score.
- **Practice mode** loops any stretch of a song, from a quarter speed up to double, until that one run is in your fingers.
- **Race your own ghost.** Every run is recorded, and any past one can ride along beside you as markers on the highway.
- **Results that tell you why:** a timing histogram, accuracy across the whole song, whether you rush or drag, and the lane you keep missing.
- **Twelve achievements,** from First Steps to Untouchable, plus a stats screen with a month of accuracy and play at a glance.
- **Five colour themes,** Classic, Neon, Mono, Sunset and Ocean, or paint your own.
- **Calibrate once** by tapping along to a metronome, and every note lands where you hear it.

## Controls

- **D F Space J K**: the five lanes (hold them for long notes)
- **Esc**: pause; **Q** while paused: back to the song list
- On the song list: **↑ ↓** (or **K J**) choose, **Enter** play, **Tab** difficulty, **/** search, **S** sort, **M** modifiers, **P** practice, **I** add a song, **R** rename, **X** delete
- **Settings** on the main menu: note speed, volume, sound offset, health, drain mode, hold notes, theme and calibration

Long notes are held for real in terminals that report key releases (kitty, WezTerm, foot, Alacritty); elsewhere they are tapped.

## Options

- `cascade add FILE-OR-FOLDER`: add songs, a whole folder at once
- `cascade play SONG --hard --mods hd,sd`: straight into a song (`--easy`, `--medium`, `--expert`; `--section 1:30-2:00 --speed 0.7` to practise)
- `cascade history` and `cascade replay RUN`: race a past run as a ghost
- `cascade stats` and `cascade achievements`: your record, in the shell

## History

Gleb Matsko started Cascade on 15 April 2026 around the promise still at the top of its page: a terminal rhythm game that plays any song you throw at it. Within its first week it had modifiers, achievements, practice mode and a stats dashboard; by May, share packages for swapping charts with friends and replay ghosts to race. In October came the release he called honest timing: the analysis now stamps every note where the sound truly starts, and judging and drawing run on the audio's own clock, so a hit that sounds right is judged right.

## Credits

- Cascade: Gleb Matsko, MIT or Apache-2.0
- The nine songs: from Bellbeat, written for it and played by its synthesiser (Asciiverse, MIT)
