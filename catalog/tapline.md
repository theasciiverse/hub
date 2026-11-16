**THE MELODY IS IN YOUR FINGERS.**

Notes come falling down the lanes, you hit each one as it crosses the line, and every hit makes a sound: not a click, but *that* note of the song. This is a keysound game, the way the arcade rhythm machines do it. The band plays along underneath, and the melody is yours to play. Hit everything and the tune rings out whole; drop a note and you can hear exactly where it went missing.

Eight songs from Bellbeat come with it, turned into keysound charts. *Hello, World* chimes on a bell, *Segfault March* stomps along in two, *Waltz for a Spinning Disk* turns in three, *Null Pointer Samba* plucks and sways, *Carriage Return* and *Escape Sequence* drive hard, and then *Kernel Panic* and, at 172 beats a minute, *SIGTERM*. Every song has two charts: on **4 keys** you play the notes on the beat and the band fills in the rest, and on **7 keys** the whole melody is yours, spread across the keyboard the way it climbs and falls.

Then there are tapline's own eight charts, from *First Steps* to *Final Cascade* at 175 beats a minute, where streams, jacks and staircases come at you on all seven keys.

- **Every hit plays its note.** Miss it and the song has a hole in it.
- **PERFECT, GREAT, GOOD or MISS** on every note, a combo counter and a gauge that has to be at 80% when the song ends to CLEAR it
- **Long notes** to hold, and let go of on time where your terminal reports key releases
- **Your best score, accuracy and combo** on every chart, compared after every run
- **A chart selector** with live search across titles and artists, and a filter by number of lanes
- **Bring more:** drop BMS and bmson charts into the songs folder in tapline's state folder, with their keysounds, background music and pictures. 4, 5 and 7 keys, scratch lanes, nine-button PMS and double-play charts all play.

## Controls

- **S D F Space J K L**: the seven lanes; **S D K L** on four lanes
- **Esc** or **Q**: stop playing
- In the selector: **↑ ↓** (or **j k**) move, **/** search, **l** number of lanes, **c** clear, **Enter** play, **Esc** quit

## Options

- `--autoplay`: watch a chart play itself
- `--auto-ks` and `--audio-lead-ms MS`: keep the sound in step on slow audio systems
- `--no-audio`: play silently

## History

Yuji Ueki (unhappychoice), who also made gittype, started tapline on 9 July 2026 as a simple four-lane rhythm game that read BMS charts, the open chart format of the keysound games, and wrote eight charts for it that same day. In November 2026 he came back to it in a rush of nearly four hundred commits, and it grew into a full keysound player: scratch lanes, nine-button charts, judgement windows and a clear gauge, chart pictures drawn in half blocks, and the newer bmson format. In the Asciiverse it plays Bellbeat's songs too, the band on the backing and every note of the melody under your fingers.

## Credits

- tapline and its eight charts: Yuji Ueki (unhappychoice)
  ([github.com/unhappychoice/tapline](https://github.com/unhappychoice/tapline)),
  MIT
- The Bellbeat songs: Asciiverse, written for Bellbeat
  ([github.com/theasciiverse/bellbeat](https://github.com/theasciiverse/bellbeat)),
  MIT
