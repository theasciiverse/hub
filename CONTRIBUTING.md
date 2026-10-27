# Adding your game to Asciiverse

Asciiverse is a home for text-mode and terminal games and programs. If you
have made one, you are invited to add it to the catalog, so people can find,
install and launch it through `av`, the Asciiverse terminal client.

Asciiverse launches as a free catalog funded by donations: every title is
free to download and play, and you are welcome to link your own donation
page from your title's entry. Paid titles are planned for later; that is
not designed yet.

## What fits

- It runs in a terminal: a TUI, a text game, an ASCII-art animation, a
  terminal utility.
- It runs from a downloadable archive without admin rights or an installer.
- It keeps its saves and settings outside its own install directory (in the
  user's normal config/data directories), because an update replaces the
  install directory's contents.
- You have the right to distribute it.
- It has no sexual content (this applies to MUDs too).

**Open or closed source are both welcome.** `av` only downloads and launches
your program; it does not link with it, and its own license does not affect
yours.

## What you provide

1. **Builds** for one or more platforms: `<id>-<target-triple>.tar.gz` for
   Linux and macOS, `<id>-<target-triple>.zip` for Windows, plus their sha256
   checksums. Static (`musl`) Linux builds are preferred where possible.
   Hosting can be either:
   - **GitHub Releases** on a public repo, with a `SHA256SUMS` file
     attached. New releases are picked up automatically.
   - **Any public HTTPS URL** (your own site, another forge, a storage
     bucket). URLs and checksums go into your manifest, so each update is a
     small PR here.
2. **A manifest**, `catalog/<id>.toml`, described in `catalog/SCHEMA.md`.
   `catalog/solitty.toml` is a worked example.
   Its `provenance` says where the title comes from and who made it; if it
   is a port or a package of someone else's work, `[upstream]` links to the
   original project and `changes` to the list of what you changed.
3. **A page**, `catalog/<id>.md`: your title's store page text (what it
   is, controls, credits) in the small Markdown subset described in
   `catalog/SCHEMA.md`. `catalog/solitty.md` is a worked example.
4. **One `.cast` recording**, made as described in `RECORDING.md`. It is your
   title's screenshot and trailer in `av` and on the website.

## How to submit

Three ways in, all with the same review:

- **The form:** open an issue with the "Submit a title" form
  (`.github/ISSUE_TEMPLATE/submit-title.yml`). It asks what the title is,
  who made it, where the downloads are, its licence and what it needs; we
  write the manifest and page from it. No git needed.
- **Email:** the same details to submit@asciiverse.sh, for anyone without a
  GitHub account.
- **A pull request**, for developers who know git, as below.

To recommend someone else's title, use the "Suggest a title" form
(`.github/ISSUE_TEMPLATE/suggest-title.yml`).

For a pull request: open one adding `catalog/<id>.toml` and `catalog/<id>.md`. In the description, say:

- what the title is and who made it,
- whether it uses the network, and for what,
- anything it needs from the system (libraries, mouse support, a font with
  Braille, a minimum terminal size).

## What review checks

- The manifest and page are valid and the archives download and match their checksums.
- The title installs, launches and quits cleanly through `av` on at least one
  listed platform.
- The `.cast` follows `RECORDING.md`.
- The provenance is right: the original authors are credited and linked.
- Nothing harmful: no undisclosed network use, nothing written outside the
  user's own directories, no bundled malware or miners.

Once merged, the title appears in `catalog.json` on its next build (every 6
hours, or right after the merge).

## Why checksums matter

`av` checks every download against the sha256 in the reviewed catalog before
installing it. If an archive changes after review, the checksum no longer
matches and `av` refuses to install it. That is what lets players trust
binaries from many different developers.

## Not decided yet

- Whether updates to titles hosted on GitHub Releases go live automatically
  for every developer, or whether new outside developers start with
  reviewed updates (pinned versions) until they are established.
- Content guidelines beyond "nothing harmful".
