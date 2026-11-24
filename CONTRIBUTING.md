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

## AI and other tools

Asciiverse is built with the help of AI assistants, and titles made with
them are welcome. We follow the Linux kernel's approach: tools may help,
and a person is accountable for the result.

- **A person stands behind every title.** Whoever submits a title has
  reviewed and tested it, understands how it works, can answer for it in a
  bug report, and has the right to distribute it. If you could not defend
  a part of it, do not submit that part.
- **Say where a tool did real work.** If an AI assistant or a generator
  wrote a meaningful part of the code, text or art, say so in the README
  or in the commits (an `Assisted-by:` or `Co-Authored-By:` line is
  enough). Spelling fixes, autocompletion and formatters do not count.
- **Original authors keep their credit.** A port or package of someone
  else's work credits and links them, keeps their code as they wrote it,
  and lists every change separately (`changes` in the manifest).
- **Reviewers decide how closely to look.** Every title goes through the
  checks above. Beyond that, each reviewer may handle a title made with
  much AI help as they see fit: review it like any other, ask for more
  testing, ask you to walk through how a part works, or review it later
  than hand-made work. Expect a closer look the more of a title was
  generated, and a submission that nobody can explain may be turned down
  without a detailed review.

Asciiverse's own titles work the same way: an assistant may write much of
a change, its commits say so, and a person reviews, tests and releases it.

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
