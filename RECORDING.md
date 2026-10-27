# Recording a catalog `.cast`

Every title in the catalog has one `.cast` recording. It is the title's
screenshot and its trailer at once: `av` plays it in the detail pane, draws a
still frame from it as a thumbnail, and the website embeds the same file with
`asciinema-player`. One recording, three uses, so every recording follows the
same fixed format.

## What does and does not matter

A `.cast` file stores the characters and escape codes the program printed,
with timing. It contains no pixels. So:

- **Your font, terminal emulator and OS do not affect the recording.** The
  viewer's own terminal font (or the website's) draws it later.
- **The terminal size, colors and character encoding do matter**, because
  the program decides what to draw based on them. Those are fixed below.

## The format

| Setting | Value |
|---|---|
| Size | **100x30** (columns x rows) for the preview; narrower is allowed, never taller (see below) |
| Format | asciicast v3, plain `.cast` (not `.zst`) |
| Recorder | asciinema 3.x |
| `TERM` | `xterm-256color` |
| `COLORTERM` | `truecolor` |
| Locale | UTF-8 (`LANG=C.UTF-8` or any `*.UTF-8`) |
| Idle limit | 2 seconds |
| Length | 20 to 60 seconds |
| Input capture | off (asciinema's default; do not pass `-I`) |
| Captured env | `TERM,COLORTERM,LANG` only |

100x30 fits every title surveyed on 2026-10-06 at its smallest playable
layout: solitty 57x28, sigpipe 71x24, prince-of-braille 70x25, entity 64x25,
panzer 48x18, and tetrix's six-player table.

**Colors:** `av` and the website play every cast with the Asciiverse
palette, ignoring any theme stored in the file, so all previews look
consistent. Titles that use 256-color or RGB colors keep their exact colors;
the palette only decides how the 16 basic colors look. (The palette itself is
not defined yet.)

## Tools

You record with the asciinema CLI, installed on your own machine. Asciiverse
does not ship it, and `av` does not need it: `av` has its own built-in player.

asciinema 3.x runs on Linux, macOS and FreeBSD; its README says Windows is
not supported. Windows developers will most likely need WSL; that has not
been tested yet.

## The command

Run in a terminal window at least 100x30:

```bash
TERM=xterm-256color COLORTERM=truecolor LANG=C.UTF-8 \
asciinema rec \
  --window-size 100x30 \
  --idle-time-limit 2 \
  --capture-env "TERM,COLORTERM,LANG" \
  --title "Solitty" \
  --command "solitty" \
  resources/solitty.cast
```

`--window-size` fixes the recorded size whatever your window is, but the
game also draws to your real window while you play, so a window of exactly
100x30 makes what you see match what is recorded.

For titles with a demo or attract mode, a scripted recording can add
`--headless`, which runs the program without using your terminal at all.
Headless sessions get no keyboard input, so it cannot be used for normal
gameplay.

Flags checked against asciinema 3.2.1's `src/cli.rs` on 2026-10-06. Its help
text mentions `--rec-env`, but the actual flag is `--capture-env`.

## What to record

- Show real gameplay within the first few seconds; skip long menus and
  loading.
- Pick a representative moment for the still frame and set its time as
  `media.thumbnail_at` in the manifest.
- Quit the program normally at the end so the recording ends with the
  terminal restored.
- No personal information on screen (usernames, paths, hostnames in a shell
  prompt). Recording the title directly with `--command` avoids showing a
  shell at all.
- No personal information in the file either. asciinema stores the
  `--command` string in the cast's header, so run the title by name with
  its folder on `PATH` or by a relative path (`--command "tf host port"`,
  not `--command "/home/you/..."`), and give it a throwaway `HOME` and a
  neutral player name (`USER=player`, `LOGNAME=player`). Games that print
  a path or score table show those too: check with
  `grep -l "/home/\|$(whoami)\|$(hostname)" *.cast` before publishing.
  (On 2026-10-13, 66 casts held a local path in their header, TinyFugue's
  showed one on screen and atc's score table showed the login name; all
  fixed.)

## Fonts, on the viewer's side

Titles that draw with Braille (U+2800 to U+28FF) or the Unicode 16 block
octants need a font that has those glyphs, both in a player's terminal and in
the website's web font. Declare them in the manifest's `requires.glyphs` so
`av` can warn.

## Titles whose best look is not 100x30

Settled 2026-10-10 from the first round of catalog recordings. Every
preview `av` plays is at most 100x30, because `av` draws it cell for cell.
Two ways to get there when 100x30 does not show a title at its best:

- **Narrower.** A tall game can record narrower than 100 columns, keeping
  30 rows. rusty-pinball draws its table at the terminal's width, so at
  56x30 far more of the table fits than at 100x30. `av` and the website show
  a narrower preview centred, with black at the sides.
- **Record big, crop to 100x30.** A game whose graphics need more room
  (moraen's 6-pixel tiles at 240x68, Ceres at 128x64 for 1:1 PICO-8 pixels,
  Calvary's full HUD) records at its own best size. The preview is then a
  100x30 window cut out of each frame: centred when the content fits,
  following the player when it does not, with the HUD row carried into the
  window. The manifest says how (`media.crop`, proposed in
  `catalog/SCHEMA.md`); hub's build does the cropping, and the website can
  also offer the full-size original. moraen's preview is the worked example.

Games that adapt to the window (most do) should simply record at 100x30:
cropping a bigger recording of them would only show part of the screen.

## Switching looks during the recording

If a title has several graphics modes (brickspire's pixel and pipe
graphics, tty-rex's five looks, moraen's pixel art and glyphs), switch
partway through, about a third and two thirds in, so viewers see each one.

## Still to settle

- **File size.** Games that redraw at 60 fps make large casts (92 MB raw for
  sleighride). Proposal: record normally; hub's build re-encodes every cast
  at a capped frame rate (25 to 30 fps keeps the look) and serves it
  compressed, with a size limit the build checks.
- **A clean environment.** The recording command should drop variables that
  identify the real terminal (`VTE_VERSION`, `TERM_PROGRAM` and similar), or
  a game may detect the recorder's terminal instead of the `xterm-256color`
  this spec promises.
- **asciinema version.** The command above needs asciinema 3.x; checked with
  3.2.1 on 2026-10-10 (all flags present, writes asciicast v3 with the
  `command`, `title` and captured `env` in the header). Distro packages may
  still be 2.x (Ubuntu's is 2.4.0), which writes asciicast v2 and takes
  different flags, so check `asciinema --version` first.
