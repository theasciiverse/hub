# hub

The Asciiverse catalog and website. It plays the itch.io role (browsable,
tag-driven discovery) to `av`'s Steam role (library and launcher). Named
`site` until 2026-10-06; renamed because it is the central catalog repo, not
just the website.

Status: no code yet. Will become its own repo (`theasciiverse/hub`, not
created yet).

## What lives here

```
hub/
├── catalog/
│   ├── SCHEMA.md       # manifest format and generated catalog.json
│   ├── <id>.toml       # one hand-written manifest per title (solitty.toml is the worked example)
│   └── <id>.md         # the title's store page, a small Markdown subset (solitty.md is the worked example)
├── CONTRIBUTING.md     # how outside developers add their games
├── RECORDING.md        # the fixed .cast format (100x30) every title records to
└── (to come) catalog generator, GitHub Action, website
```

## What it does

- **Catalog build:** a GitHub Action merges every manifest with release data
  (GitHub Releases, or the `direct` URLs in the manifest), verifies
  checksums, and publishes `catalog.json` to Cloudflare Pages. Runs every 6
  hours and on every merge.
- **Submissions:** outside developers add titles by PR, per
  `CONTRIBUTING.md`. Reviewed by hand.
- **Website:** served from the same Pages project, reads the same
  `catalog.json`, embeds each title's `.cast` with `asciinema-player`
  (asciicast v3 support since player 3.10, poster frame via
  `poster="npt:..."`).

Content stays in each title's own repo or host (binaries, `.cast` files);
`hub` holds pointers, manifests and the generated catalog.

## Not designed yet

- The website itself: pages, navigation, browsing and discovery in a
  browser.
- The Asciiverse color palette used for cast playback (shared with `av`).
- A web font with Braille and block-octant coverage for the website player.
- Donation page / platform (see `../ORGandFunding.md`).

See `../av/CLAUDE.md` for the client side and the full list of open
questions.
