# Asciiverse website: design

Status: first design mockup, 2026-10-10. Local only; deployment is the very
last step and not part of this. Run it with:

```bash
python3 dev/serve.py   # from this folder; no-cache, so the browser never shows stale files
# then open http://127.0.0.1:8765/
```

`data/catalog.json` is built by `dev/build_catalog.py` from the real
manifests and pages in `../../../store/code/asciiverse/hub/catalog/` plus
`dev/mock-titles.toml`, with faked release data. It has the same shape as
the `catalog.json` hub will generate (`hub/catalog/SCHEMA.md`), so the
pages are written against the real format from the start.

## Direction

Not a generic modern landing page. The references, studied 2026-10-10:

- **Steam client and store**: the structure. Dense, panelled, dark slate;
  top bar, sticky browse bar with search, a featured carousel with media
  left and facts right, capsule grids, and an app page with a big media
  area, a summary column, a "buy" box and a facts sidebar. Colors read from
  the installed client's own `steamui/css`: backgrounds `#0e141b` and
  `#23262e`, panels `#3d4450`, text `#dcdedf` / `#8b929a` / `#67707b`,
  accent blue `#1a9fff`, action green `#59bf40`.
- **itch.io**: the browsing. Tags everywhere, grid cards with title,
  one-liner, developer, genre and platform marks. Its `ascii` tag page
  shows how strong a grid of black terminal thumbnails looks.
- **16colo.rs**: monospace everywhere, the artwork is the only color. A
  title strip over each piece.
- **asciinema.org/explore**: cast tiles with title, author and duration.
- **Ratatui's showcase**: large terminal captures carry a page on their own.

Terminal Trove (terminaltrove.com) could not be viewed: it sits behind a
Cloudflare bot check.

## What that became

- **Darker than Steam.** Page `#0a0d11`, deep `#06080b`, panels `#10151b` to
  `#1d2530`. Steam's blue-slate pulled toward black.
- **Accents per the Asciiverse design rules:** phosphor green for every
  action (Steam's green buy button becomes the `av install` line), amber
  for highlights, links and the OLD! banner. No Steam blue.
- **Every preview is a black terminal tile.** The casts are the capsule
  art, the screenshots and the trailer. Tiles show the still frame at
  `thumbnail_at` and play on hover. Faint scanlines over tiles only.
- **Type:** IBM Plex Mono for the brand, navigation, headings and labels;
  IBM Plex Sans for reading text. Both from the IBM terminal lineage, and
  both OFL. Section heads are prompt-styled (`> FEATURED`, `## CONTROLS`).
- **Wordmark:** hand-lettered in half-block characters, green to amber, with
  the slogan **Where text comes alive** under it (chosen by David
  2026-10-10; no prior use found in a web search, not a trademark search).
- **Free at launch, paid later.** The "buy" box is "Get <title>" with a
  FREE mark, the `av install <id>` line and direct archive links. Paid
  titles are intended later (2026-10-10), so the box keeps a place where a
  price could go instead of the FREE mark.

## Pages

Top row, one page each (David, 2026-10-12): **Catalog** (`index.html`),
**Get av** (`get-av.html`: the one-line installer, what it does, where
things go, update and uninstall), **History** (`history.html`), **Submit a
title** (`submit.html`, the website form of `hub/CONTRIBUTING.md` and
`RECORDING.md`). The catalog page no longer carries the av box. "About"
left the row.

Catalog row under it (David, 2026-10-12): **Home** (`index.html`: featured
carousel, then a shelf per branch: six games, the three oldest MUDs, and
Programs and Movies as "coming"), **Games** (`games.html`: OLD! and new
grids, then all games), **MUDs** (`muds.html`), **Programs**
(`programs.html`) and **Movies** (`movies.html`), the last two empty until
titles of that kind exist. "Tags" left the row.

**Text adventures** (David, 2026-10-12) became their own category, between
Games and MUDs: Home, Games, Text adventures, MUDs, Programs, Movies
(`adventures.html`). Like the MUD page: an explainer, then interpreters
(Frotz, Glulxe, FrobTADS, ScottFree; facts from Debian 13 and each project,
only checked platforms listed) above the stories, which are `kind =
"adventure"` titles naming the interpreter they need. Zork I to III
(MIT since 2025) are in, each a package with its own Frotz build inside,
so a story installs and plays with no separate interpreter; the start line
reads "pick a story", and Home has a Text adventures shelf. Frotz itself is
also listed on Programs, under an Interpreters group. Next: Colossal Cave
(Open Adventure, BSD) and a curated set of IF Archive games with clear
licences.

Home layout, after Steam's store front (2026-10-12): the featured carousel
with the neighbouring titles' front pictures dimmed and cut off either
side, arrows over them, dots below, advancing every 10 s and holding still
under the pointer or focus; then **topic shelves**, one row of five
capsules each that scrolls a page at a time with arrows and page marks
(`shelf()` in `js/site.js`): OLD! classics, originals and homages, puzzle,
platformers, play together, action and arcade, picked from genre and
topics. Then MUDs, then Programs and Movies.

**Banner** (2026-10-12): Home opens with "Take back your terminal." beside
a terminal window playing `casts/av-demo.cast` (drawn as GNOME Terminal's header bar, not macOS, David 2026-10-12), a real av session recorded
by `dev/record_av_demo.py` (24.5 s, 0.84 MB gzipped; every title stays at least 3.5 s, nothing flashes past; it is large
because av plays each title's preview in its detail pane). It says up front
that everything on the page runs in a terminal, because the previews do not
look like one. The menu row has more air (Oh My Zsh's as reference) and the
catalog row under it is larger, with the current page boxed in green.

**Library pages** (2026-10-12): Games, MUDs, Programs and Movies use Steam's
library layout (`library()` in `js/site.js`): a sidebar with Home, a filter
and every title A to Z, and a main pane with shelves (arrows top right) or,
when a title is picked, that title's page in the pane (recording, install
line, facts, link to its store page `title.html`). The pick lives in the
URL hash (`games.html#sleighride`). MUDs have no recordings, so their cards
and pages are their age, theme and name in type. Programs and Movies are
empty until such titles exist.

**MUDs and security** (2026-10-12): the MUD library lists clients (Lera,
and any later one) above the worlds. Each world's page offers Lera
(`lera <id>`), openssl when the world has a TLS port, and telnet, and says
plainly whether the connection is encrypted. Lera uses TLS by itself when
the catalog gives `connect.tls_port`; telnet never encrypts. Of the six
worlds, only BatMUD offers TLS (port 2022, checked 2026-10-12: certificate
verified, game answers); for the other five none was found by probing the
usual ports or searching their pages.

**30 MUDs and their pictures** (2026-10-12): 24 more MUDs went in, each one
answering with its greeting that day, facts from each game's own site.
Encrypted: BatMUD 2022, Dune MUD 6788, MorgenGrauen 4712, StickMUD 7670,
UNItopia 992, Merentha 10001. A MUD's preview and front picture is its own
greeting screen, recorded without logging in by `dev/record_mud.py` (through
`dev/mud_greet.py`, which refuses every telnet option). DOS ANSI art is
decoded from CP437 and recorded at 80 columns (`MUD_COLS=80`), as for
DurisMUD. MorgenGrauen sends a stray HTTP redirect before its greeting; it
is trimmed from the cast.

**Front picture:** a title's front picture (Steam's capsule art) is the
still frame of its own recording at `thumbnail_at` (David, 2026-10-12: "just
a screenshot from the asciinema recording"). No separate art is made; to
change a front picture, change `thumbnail_at`.

## Cast playback

- `asciinema-player` 3.17.0 (Apache-2.0), vendored in `vendor/`.
- **Palette:** `.asciinema-player-theme-asciiverse` in `css/site.css`, the
  16 basic colors every cast plays with. `av` must use the same 16 values.
  Green is a felt green (`#3e9b4f`) because solitty paints its whole table
  with basic green; the default neon green looked harsh there.
- **Font:** Iosevka Term 34.9.0 (OFL-1.1), subset to Latin (with
  Extended-B), Greek, Cyrillic, U+2000 to U+2BFF (punctuation, arrows,
  maths, technical, box drawing, blocks, shapes, symbols), Powerline, and
  both legacy computing blocks in full (U+1FB00 to U+1FBFF and Unicode 16's
  U+1CC00 to U+1CEBF, octants included), about 168 KB per weight
  (`fonts/`; the full TTFs are in `fonts/src/` for re-cutting). Widened
  2026-10-10 after tty-rex's preview showed missing-glyph boxes for
  U+1CEA0 to U+1CEAB and Ohm's Workshop used the ohm sign; every cast is
  checked against the subset (a fontTools cmap check). Chosen
  2026-10-10 after checking the cmaps of 18 candidates: it is the only
  narrow text font with full Braille, octant, sextant and card-suit
  coverage. The player draws block elements and sextants itself; Braille
  and octants come from the font.
- **Players are created only once attached and visible** (they size from
  their container, and off-screen casts should not load).

## Open

- Production build: static pages generated from `catalog.json` (for links
  and search engines) instead of rendering in the browser. Generator not
  chosen.
- Thumbnails: a live player per tile is heavy for a big catalog. Option:
  hub renders each still frame to SVG at catalog build time.
- `featured`, `old` and `duration` are mockup-only fields; `old` and
  `featured` need a home in hub (manual curation, per SCHEMA.md).
- How `av` itself is installed: a one-line installer, Oh My Zsh style
  (2026-10-12). `install.sh` (POSIX sh, curl or wget) and `install.ps1`
  (`irm ... | iex`) sit at the site root, so the lines are
  `curl -fsSL https://asciiverse.sh/install.sh | sh` and
  `irm https://asciiverse.sh/install.ps1 | iex`. They fetch
  `av-<target>.tar.gz` (Windows: `.zip`) and `SHA256SUMS` from
  `https://asciiverse.sh/releases/av/latest/`, check the sha256, and put
  `av` in `~/.local/bin` (Windows: `%LOCALAPPDATA%\Asciiverse\bin`, added to
  the user PATH). Targets: `{x86_64,aarch64}-unknown-linux-musl`,
  `{x86_64,aarch64}-apple-darwin`, `{x86_64,aarch64}-pc-windows-msvc`.
  Still to do: building and publishing those archives (av has no release
  workflow yet). Test locally with `AV_DOWNLOAD_URL=http://...` pointing at
  a folder of archives; `install.ps1` has not been run on Windows yet.

## Where it comes from (2026-10-13)

Every installable title shows a "Where it comes from" box: on its store page
under the Get box, and at the foot of its library pane. It holds the
manifest's `provenance` text (who made it, where our copy comes from, what
Asciiverse changed) and three links: the original project (`upstream.url`),
our source (`repo`) and our changes (`changes`, a path in `repo`; labelled
Provenance when it is a story's README). `provenance()` in `js/site.js`
draws it; av shows the same block above the page in its detail pane.

## Art & Demos (2026-10-13)

`art.html` lists kind `art`: demos and effects (art in motion; tarts is the
first) and, later, still ANSI and ASCII art collections. One category, so
neither half starts out empty; it can be split if art collections grow.
It has a tab between Programs and Movies and an "Art & Demos" shelf on the home page under
Text adventures. The store page's subnav tab and breadcrumb now follow the
title's kind (they were always Games).
