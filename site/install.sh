#!/bin/sh
# Asciiverse: installs av, the terminal client, for the current user.
#
#   curl -fsSL https://asciiverse.sh/install.sh | sh
#   wget -qO- https://asciiverse.sh/install.sh | sh
#
# Downloads the av archive for this machine, checks it against SHA256SUMS,
# and puts the binary in ~/.local/bin (the same folder av links titles into).
# Nothing outside your home folder is touched, no sudo, no shell rc edits.
#
# Settings, all optional:
#   AV_INSTALL_DIR   where the av binary goes (default ~/.local/bin)
#   AV_DOWNLOAD_URL  folder holding the archives and SHA256SUMS
#                    (default https://asciiverse.sh/releases/av/latest)

set -eu

DOWNLOAD_URL="${AV_DOWNLOAD_URL:-https://asciiverse.sh/releases/av/latest}"
INSTALL_DIR="${AV_INSTALL_DIR:-$HOME/.local/bin}"

if [ -t 1 ]; then
  G="$(printf '\033[32m')"; A="$(printf '\033[33m')"; R="$(printf '\033[31m')"
  D="$(printf '\033[2m')"; B="$(printf '\033[1m')"; N="$(printf '\033[0m')"
else
  G=""; A=""; R=""; D=""; B=""; N=""
fi

say()  { printf '%s\n' "$*"; }
step() { printf '  %s%s%s\n' "$D" "$*" "$N"; }
die()  { printf '%serror:%s %s\n' "$R" "$N" "$*" >&2; exit 1; }

banner() {
  # green to amber like the site's wordmark, in terminals that say they have 24-bit color
  if [ -n "$N" ] && { [ "${COLORTERM:-}" = truecolor ] || [ "${COLORTERM:-}" = 24bit ]; }; then
    printf '  \033[38;2;127;220;94m▄\033[38;2;125;218;92m▀\033[38;2;123;216;91m█ \033[38;2;118;212;87m█\033[38;2;116;210;85m▀ \033[38;2;111;206;82m█\033[38;2;109;204;80m▀\033[38;2;107;202;78m▀ \033[38;2;103;198;75m█ \033[38;2;98;194;71m█ \033[38;2;100;190;67m█ \033[38;2;119;189;59m█ \033[38;2;137;187;51m█\033[38;2;146;186;47m▀\033[38;2;155;185;43m▀ \033[38;2;173;184;35m█\033[38;2;182;183;31m▀\033[38;2;191;182;27m█ \033[38;2;210;180;20m█\033[38;2;219;179;16m▀ \033[38;2;237;178;8m█\033[38;2;246;177;4m▀\033[38;2;255;176;0m▀\033[0m\n'
    printf '  \033[38;2;127;220;94m█\033[38;2;125;218;92m▀\033[38;2;123;216;91m█ \033[38;2;118;212;87m▄\033[38;2;116;210;85m█ \033[38;2;111;206;82m█\033[38;2;109;204;80m▄\033[38;2;107;202;78m▄ \033[38;2;103;198;75m█ \033[38;2;98;194;71m█ \033[38;2;100;190;67m▀\033[38;2;110;190;63m▄\033[38;2;119;189;59m▀ \033[38;2;137;187;51m█\033[38;2;146;186;47m█\033[38;2;155;185;43m▄ \033[38;2;173;184;35m█\033[38;2;182;183;31m▀\033[38;2;191;182;27m▄ \033[38;2;210;180;20m▄\033[38;2;219;179;16m█ \033[38;2;237;178;8m█\033[38;2;246;177;4m█\033[38;2;255;176;0m▄\033[0m\n'
  else
    printf '%s' "$G"
    say '  ▄▀█ █▀ █▀▀ █ █ █ █ █▀▀ █▀█ █▀ █▀▀'
    say '  █▀█ ▄█ █▄▄ █ █ ▀▄▀ ██▄ █▀▄ ▄█ ██▄'
    printf '%s' "$N"
  fi
  say "  ${A}Where text comes alive${N}"
  say ''
}

# ---- what machine is this ----

target() {
  os="$(uname -s)"
  arch="$(uname -m)"
  case "$arch" in
    x86_64 | amd64) arch=x86_64 ;;
    aarch64 | arm64) arch=aarch64 ;;
    *) die "no av build for the $arch processor yet" ;;
  esac
  case "$os" in
    Linux)
      # The static musl build runs on any distribution, whatever its libc.
      say "$arch-unknown-linux-musl" ;;
    Darwin)
      # A shell under Rosetta reports x86_64 on Apple silicon; the native build is better.
      if [ "$arch" = x86_64 ] && [ "$(sysctl -n sysctl.proc_translated 2>/dev/null || echo 0)" = 1 ]; then
        arch=aarch64
      fi
      say "$arch-apple-darwin" ;;
    MINGW* | MSYS* | CYGWIN*)
      die "on Windows, run this in PowerShell instead:  irm https://asciiverse.sh/install.ps1 | iex" ;;
    *) die "no av build for $os yet" ;;
  esac
}

# ---- tools ----

fetch() { # url file
  # HTTPS only, redirects included; a plain http AV_DOWNLOAD_URL is for local testing.
  case "$1" in https://*) strict=1 ;; *) strict= ;; esac
  if command -v curl >/dev/null 2>&1; then
    curl -fsSL ${strict:+--proto =https --tlsv1.2} -o "$2" "$1"
  elif command -v wget >/dev/null 2>&1; then
    wget -q ${strict:+--https-only} -O "$2" "$1"
  else
    die "needs curl or wget to download"
  fi
}

# ---- the download bar ----

size_of() { # url: the server's Content-Length, empty when it does not say
  if command -v curl >/dev/null 2>&1; then
    curl -fsIL "$1" 2>/dev/null
  else
    wget -q -S --spider "$1" 2>&1
  fi | tr -d '\r' | awk 'tolower($1) == "content-length:" { n = $2 } END { if (n > 0) print n }'
}

draw_bar() { # done total seconds
  # green blocks with eighth-steps on a faint track, then percent, size, speed and time left
  awk -v d="$1" -v t="$2" -v e="$3" -v g="$G" -v f="$D" -v a="$A" -v n="$N" '
    function h(x) {
      if (x < 1000) return sprintf("%d B", x)
      if (x < 1000000) return sprintf("%.0f kB", x / 1000)
      if (x < 1000000000) return sprintf("%.1f MB", x / 1000000)
      return sprintf("%.2f GB", x / 1000000000)
    }
    BEGIN {
      w = 30; split("▏ ▎ ▍ ▌ ▋ ▊ ▉", part, " ")
      rate = ""
      if (e >= 1) {
        s = d / e; rate = "  " h(s) "/s"
        if (t > d && s > 0) { left = int((t - d) / s + 0.999); rate = rate "  " (left < 60 ? left " s" : int(left / 60) " min") " left" }
      }
      if (t > 0) {
        if (d > t) d = t
        e8 = int(d * w * 8 / t); full = int(e8 / 8); r = e8 % 8
        bar = ""; for (i = 0; i < full; i++) bar = bar "█"
        used = full; if (r > 0 && full < w) { bar = bar part[r]; used++ }
        track = ""; for (i = used; i < w; i++) track = track "─"
        printf "\r\033[K  %s%s%s%s%s %3d%%  %s / %s%s%s", g, bar, f, track, a, int(d * 100 / t), h(d), h(t), rate, n
      } else {
        printf "\r\033[K  %s%s%s%s", a, h(d), rate, n
      }
    }'
}

fetch_bar() { # url file
  # Without a terminal the download stays quiet, as before.
  if [ ! -t 1 ]; then fetch "$1" "$2"; return; fi
  total="$(size_of "$1" || true)"
  fetch "$1" "$2" &
  pid=$!
  start="$(date +%s)"
  while kill -0 "$pid" 2>/dev/null; do
    draw_bar "$(wc -c <"$2" 2>/dev/null || echo 0)" "${total:-0}" "$(($(date +%s) - start))"
    sleep 0.1 2>/dev/null || sleep 1
  done
  if wait "$pid"; then
    draw_bar "$(wc -c <"$2")" "${total:-0}" "$(($(date +%s) - start))"
    printf '\n'
  else
    printf '\n'
    return 1
  fi
}

sha256() { # file
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$1" | cut -d' ' -f1
  elif command -v shasum >/dev/null 2>&1; then
    shasum -a 256 "$1" | cut -d' ' -f1
  elif command -v openssl >/dev/null 2>&1; then
    openssl dgst -sha256 "$1" | sed 's/^.*= *//'
  else
    die "needs sha256sum, shasum or openssl to check the download"
  fi
}

# ---- install ----

main() {
  banner
  command -v tar >/dev/null 2>&1 || die "needs tar to unpack"

  t="$(target)"
  archive="av-$t.tar.gz"

  tmp="$(mktemp -d 2>/dev/null || mktemp -d -t av-install)"
  trap 'rm -rf "$tmp"' EXIT INT TERM

  step "fetching av ($t)"
  fetch "$DOWNLOAD_URL/SHA256SUMS" "$tmp/SHA256SUMS" || die "could not download $DOWNLOAD_URL/SHA256SUMS"
  fetch_bar "$DOWNLOAD_URL/$archive" "$tmp/$archive" || die "could not download $DOWNLOAD_URL/$archive"

  want="$(awk -v f="$archive" '$2 == f || $2 == "*" f { print $1 }' "$tmp/SHA256SUMS")"
  [ -n "$want" ] || die "SHA256SUMS has no line for $archive"
  got="$(sha256 "$tmp/$archive")"
  [ "$want" = "$got" ] || die "checksum mismatch for $archive (expected $want, got $got); nothing installed"
  step "sha256 ${G}ok${N}"

  mkdir -p "$tmp/x"
  tar -xzf "$tmp/$archive" -C "$tmp/x"
  [ -f "$tmp/x/av" ] || die "$archive does not contain av"

  mkdir -p "$INSTALL_DIR"
  # Copy then rename, so a running av is never left half-written.
  cp "$tmp/x/av" "$INSTALL_DIR/.av.new"
  chmod 755 "$INSTALL_DIR/.av.new"
  mv -f "$INSTALL_DIR/.av.new" "$INSTALL_DIR/av"
  step "installed to $INSTALL_DIR/av"
  say ''

  case ":${PATH}:" in
    *":$INSTALL_DIR:"*)
      say "  Done. Type ${B}${G}av${N} to open the catalog." ;;
    *)
      say "  Done, but ${A}$INSTALL_DIR is not on your PATH${N} yet."
      say "  Add this line to your shell's startup file (~/.bashrc, ~/.zshrc, ...):"
      say ''
      say "    export PATH=\"$INSTALL_DIR:\$PATH\""
      say ''
      say "  then open a new terminal and type ${B}${G}av${N}." ;;
  esac
}

# Everything runs from here, so a download cut off halfway runs nothing.
main "$@"
