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
# On Linux, when the release has a package this machine can install (a .deb
# so far; an .rpm where dnf, zypper or yum is), it asks which way: that
# package (av in the applications menu, tab completion, and what titles
# need from the system; needs sudo), just av for you as above, or nothing.
# Running this again updates whichever it was.
# The package for the distribution comes first and is the default. Without
# a terminal to ask on, it installs for you only.
#
# Settings, all optional:
#   AV_INSTALL_DIR   where the av binary goes (default ~/.local/bin)
#   AV_DOWNLOAD_URL  folder holding the archives and SHA256SUMS
#                    (default https://asciiverse.sh/releases/av/latest)
#   AV_INSTALL       skip the questions, for scripts: user (just av, for
#                    you), deb or rpm (that package), package (the one
#                    for this system); a package needs root or sudo that
#                    asks no password when there is no terminal
#   NO_COLOR         plain text, no colors

set -eu

DOWNLOAD_URL="${AV_DOWNLOAD_URL:-https://asciiverse.sh/releases/av/latest}"
INSTALL_DIR="${AV_INSTALL_DIR:-$HOME/.local/bin}"
CHOICE="${AV_INSTALL:-}"

if [ -t 1 ] && [ -z "${NO_COLOR:-}" ]; then
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
    draw_bar "$({ wc -c <"$2"; } 2>/dev/null || echo 0)" "${total:-0}" "$(($(date +%s) - start))"
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

# ---- a package for this distribution ----

ask() { # question: yes unless the answer starts with n; no when there is no terminal to ask on
  (: </dev/tty) 2>/dev/null || return 1
  printf '  %s [Y/n] ' "$1" >/dev/tty
  read -r answer </dev/tty || return 1
  case "$answer" in [Nn]*) return 1 ;; esac
}

pkg_file() { # extension arch: this release's package for the machine, from SHA256SUMS
  awk '{ f = $2; sub(/^\*/, "", f); print f }' "$tmp/SHA256SUMS" | while read -r f; do
    case "$f" in av[_-]*"$2"*".$1") say "$f"; break ;; esac
  done
}

routes() { # the packages this machine could take, the suggested one first: "kind file" lines
  [ "$(uname -s)" = Linux ] || return 0
  ids=''
  [ -r /etc/os-release ] && ids=" $(. /etc/os-release && echo "${ID:-} ${ID_LIKE:-}") "
  case "$(uname -m)" in x86_64 | amd64) deb=amd64 rpm=x86_64 ;; *) deb=arm64 rpm=aarch64 ;; esac
  can_deb='' can_rpm=''
  command -v dpkg >/dev/null 2>&1 && can_deb=1
  { command -v dnf || command -v zypper || command -v yum; } >/dev/null 2>&1 && can_rpm=1
  case "$ids" in
    *" fedora "* | *" rhel "* | *" centos "* | *" suse "*) order="rpm deb" ;;
    *) order="deb rpm" ;;
  esac
  for k in $order; do
    f=''
    case "$k" in
      deb) [ -n "$can_deb" ] && f="$(pkg_file deb "$deb")" ;;
      rpm) [ -n "$can_rpm" ] && f="$(pkg_file rpm "$rpm")" ;;
    esac
    [ -n "$f" ] && say "$k $f"
  done
  return 0
}

from_package() { # the kind of package av is installed from, if any
  if command -v dpkg-query >/dev/null 2>&1 && dpkg-query -W -f='${Status}' av 2>/dev/null | grep -q 'ok installed'; then
    say deb
  elif command -v rpm >/dev/null 2>&1 && rpm -q av >/dev/null 2>&1; then
    say rpm
  fi
}

what() { # kind: what that package brings, for the menu
  case "$1" in
    deb | rpm) say "Asciiverse in your applications menu, tab completion, what titles need" ;;
  esac
}

choose() { # list of "kind file" lines: sets kind and pkg, or kind to user, remove or exit
  n=0
  say "  How would you like to install av?"
  say ''
  printf '%s\n' "$1" | while read -r k f; do
    [ -n "$k" ] || continue
    n=$((n + 1))
    if [ "$k" = "$have" ]; then
      printf '    %s%d%s  update the .%s package%s  (needs sudo)\n' "$B" "$n" "$N" "$k" "$([ "$n" = 1 ] && echo ', suggested')"
    else
      printf '    %s%d%s  the .%s package%s  (needs sudo)\n' "$B" "$n" "$N" "$k" "$([ "$n" = 1 ] && echo ', suggested')"
    fi
    printf '       %s%s%s\n' "$D" "$(what "$k")" "$N"
  done
  count="$(printf '%s\n' "$1" | grep -c .)"
  private=''
  [ -f "$INSTALL_DIR/av" ] && private=1
  printf '    %s%d%s  %sjust av, for you only  (no sudo)\n' "$B" $((count + 1)) "$N" "$([ -n "$private" ] && echo 'update ')"
  if [ -n "$have" ]; then
    printf '       %s%s/av, which would start instead of the .%s%s\n' "$D" "$INSTALL_DIR" "$have" "$N"
  else
    printf '       %s%s/av, nothing else%s\n' "$D" "$INSTALL_DIR" "$N"
  fi
  last=$((count + 2))
  if [ -n "$private" ]; then
    # the private copy can go: then the package starts, or av is uninstalled for this user
    printf '    %s%d%s  remove the av in %s\n' "$B" "$last" "$N" "$INSTALL_DIR"
    if [ -n "$have" ]; then
      printf '       %sit starts instead of the .%s; without it, the .%s does%s\n' "$D" "$have" "$have" "$N"
    else
      printf '       %suninstalls av for you; saves, settings and installed titles stay%s\n' "$D" "$N"
    fi
    last=$((last + 1))
  fi
  printf '    %s%d%s  exit, nothing installed\n' "$B" "$last" "$N"
  say ''
  while :; do
    printf '  Choose 1 to %d [1]: ' "$last" >/dev/tty
    read -r answer </dev/tty || answer=$last
    case "${answer:-1}" in
      *[!0-9]*) continue ;;
    esac
    c=${answer:-1}
    if [ "$c" -ge 1 ] && [ "$c" -le "$count" ]; then
      line="$(printf '%s\n' "$1" | sed -n "${c}p")"
      kind="${line%% *}" pkg="${line#* }"
      return
    elif [ "$c" -eq $((count + 1)) ]; then
      kind='user'
      return
    elif [ -n "$private" ] && [ "$c" -eq $((count + 2)) ]; then
      kind='remove'
      return
    elif [ "$c" -eq "$last" ]; then
      kind='exit'
      return
    fi
  done
}

pick() { # highest number: a choice from 1 to it, 1 when Enter is pressed
  while :; do
    printf '  Choose 1 to %d [1]: ' "$1" >/dev/tty
    read -r answer </dev/tty || answer=$1
    case "${answer:-1}" in *[!0-9]*) continue ;; esac
    if [ "${answer:-1}" -ge 1 ] && [ "${answer:-1}" -le "$1" ]; then
      say "${answer:-1}"
      return
    fi
  done
}

# install_pkg: 0 installed; 1 it could not, so offer av for the user; 2 the
# user picked av for themselves instead; 3 the user chose to stop
install_pkg() {
  if [ "$(id -u)" = 0 ]; then
    sudo=''
  elif ! command -v sudo >/dev/null 2>&1; then
    say "  ${A}There is no sudo here${N}, so the .$kind can't be installed."
    return 1
  elif ! (: </dev/tty) 2>/dev/null; then
    # no terminal to type a password on: only sudo that asks none will do
    sudo=sudo
    if ! sudo -n true 2>/dev/null; then
      say "  ${A}sudo wants a password and there is no terminal to type it on${N}, so the .$kind was not installed."
      return 1
    fi
  else
    sudo=sudo
    # the password now, before anything is downloaded
    while ! sudo -v </dev/tty; do
      say ''
      say "  ${A}sudo did not let this account in.${N}"
      say "    ${B}1${N}  try sudo again"
      say "    ${B}2${N}  just av, for you only  (no sudo)"
      say "    ${B}3${N}  exit, nothing installed"
      case "$(pick 3)" in
        2) return 2 ;;
        3) return 3 ;;
      esac
    done
  fi
  fetch_bar "$DOWNLOAD_URL/$pkg" "$tmp/$pkg" || die "could not download $DOWNLOAD_URL/$pkg"
  verify "$pkg"
  # the package manager may read it as its own user
  chmod 755 "$tmp" && chmod 644 "$tmp/$pkg"
  # it asks on the terminal when there is one
  input=/dev/null
  (: </dev/tty) 2>/dev/null && input=/dev/tty
  step "installing $pkg"
  if [ "$kind" = deb ]; then
    if command -v apt-get >/dev/null 2>&1; then
      # a fresh system is often updating in the background: wait for it
      $sudo apt-get install -y -o DPkg::Lock::Timeout=300 "$tmp/$pkg" <"$input"
    else
      $sudo dpkg -i "$tmp/$pkg" <"$input"
    fi
  elif command -v dnf >/dev/null 2>&1; then
    $sudo dnf install -y "$tmp/$pkg" <"$input"
  elif command -v zypper >/dev/null 2>&1; then
    $sudo zypper --non-interactive install --allow-unsigned-rpm "$tmp/$pkg" <"$input"
  else
    $sudo rpm -U "$tmp/$pkg" <"$input"
  fi || {
    say "  ${A}The package manager did not install $pkg.${N}"
    return 1
  }
  # a copy from an earlier run of this script would start instead of the package
  if [ -f "$INSTALL_DIR/av" ] && [ -z "$CHOICE" ] && ask "Remove the av in $INSTALL_DIR, which would start instead of the package?"; then
    rm -f "$INSTALL_DIR/av"
  fi
  say ''
  say "  Done. Asciiverse is in your applications menu, or type ${B}${G}av${N} to open the catalog."
}

start_now() { # binary: offer to open av right away, said how big the terminal should be
  [ -z "$CHOICE" ] || return 0
  (: </dev/tty) 2>/dev/null || return 0
  size="$(stty size </dev/tty 2>/dev/null || true)"
  rows="${size% *}" cols="${size#* }"
  if [ -n "$size" ] && { [ "$cols" -lt 128 ] || [ "$rows" -lt 40 ]; }; then
    say ''
    say "  This terminal is ${cols}x${rows}. av is made for 128x40 or more, where each title's"
    say "  preview shows in full; a bigger window or a smaller font gets you there."
  fi
  ask "Start av now?" || return 0
  # exec ends this script, so clean up first
  rm -rf "$tmp"
  trap - EXIT INT TERM
  exec "$1" </dev/tty
}

startup_file() { # where this user's shell takes a PATH line, written as shown to them
  # shellcheck disable=SC2088
  case "${SHELL:+${SHELL##*/}}" in
    zsh) say "~/.zshrc" ;;
    bash) if [ "$(uname -s)" = Darwin ]; then say "~/.bash_profile"; else say "~/.bashrc"; fi ;;
    *) say "~/.profile" ;;
  esac
}

verify() { # file in $tmp, against its line in SHA256SUMS
  want="$(awk -v f="$1" '$2 == f || $2 == "*" f { print $1 }' "$tmp/SHA256SUMS")"
  [ -n "$want" ] || die "SHA256SUMS has no line for $1"
  got="$(sha256 "$tmp/$1")"
  [ "$want" = "$got" ] || die "checksum mismatch for $1 (expected $want, got $got); nothing installed"
  step "sha256 ${G}ok${N}"
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

  list="$(routes)"
  have="$(from_package)"
  if [ -n "$CHOICE" ]; then
    case "$CHOICE" in
      user) step "installing for this user only" ;;
      deb | rpm | package)
        line="$(printf '%s\n' "$list" | awk -v k="$CHOICE" 'NF && (k == "package" || $1 == k) { print; exit }')"
        [ -n "$line" ] || die "AV_INSTALL=$CHOICE, but this release has no such package this machine can install"
        kind="${line%% *}" pkg="${line#* }"
        install_pkg || die "the .$kind was not installed"
        return ;;
      *) die "AV_INSTALL is user, deb, rpm or package, not \"$CHOICE\"" ;;
    esac
  elif [ -n "$list" ] && (: </dev/tty) 2>/dev/null; then
    choose "$list"
    case "$kind" in
      exit) say ''; say "  Nothing installed."; return ;;
      remove)
        rm -f "$INSTALL_DIR/av"
        say ''
        if [ -n "$have" ]; then
          say "  Removed $INSTALL_DIR/av. Typing ${B}${G}av${N} now starts the .$have."
        else
          say "  Removed $INSTALL_DIR/av."
        fi
        return ;;
      user) step "installing for this user only" ;;
      *)
        if install_pkg; then
          start_now /usr/bin/av
          return
        else
          case $? in
            1) ask "Install just av, for you only, instead (no sudo)?" || { say ''; say "  Nothing installed."; return; } ;;
            3) say ''; say "  Nothing installed."; return ;;
          esac
        fi
        step "installing for this user only" ;;
    esac
  elif [ -n "$have" ]; then
    # no terminal to ask on: never hide the package behind a second copy
    say "  av is installed as a .$have package, so nothing was put in $INSTALL_DIR."
    say "  Run this again in a terminal to update it."
    [ -f "$INSTALL_DIR/av" ] && say "  The av in $INSTALL_DIR starts instead of it; run this in a terminal to remove it."
    return
  elif [ -n "$list" ]; then
    say "  There is a .${list%% *} for your system: Asciiverse in the applications menu and"
    say "  tab completion. Run this again in a terminal to choose it."
    step "installing for this user only"
  fi

  fetch_bar "$DOWNLOAD_URL/$archive" "$tmp/$archive" || die "could not download $DOWNLOAD_URL/$archive"
  verify "$archive"

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

  short="$(printf '%s' "$INSTALL_DIR" | sed "s|^$HOME/|~/|")"
  case ":${PATH}:" in
    *":$INSTALL_DIR:"*)
      say "  Done. Type ${B}${G}av${N} to open the catalog." ;;
    *)
      if [ "$INSTALL_DIR" = "$HOME/.local/bin" ] && grep -qs '\.local/bin' "$HOME/.profile" "$HOME/.bash_profile" "$HOME/.bash_login" "$HOME/.zprofile"; then
        # Debian and Ubuntu's ~/.profile adds the folder at login, if it existed then
        say "  Done. Your login adds $short to your PATH, so once you have logged out"
        say "  and back in, typing ${B}${G}av${N} opens the catalog."
      elif [ "${SHELL:+${SHELL##*/}}" = fish ]; then
        say "  Done. To start it by typing ${B}${G}av${N}, run this once:"
        say ''
        say "    fish_add_path $short"
      else
        say "  Done. To start it by typing ${B}${G}av${N}, add this line to $(startup_file)"
        say "  and open a new terminal:"
        say ''
        say "    export PATH=\"$short:\$PATH\""
      fi
      say ''
      say "  Until then, start it with ${B}${G}$short/av${N}" ;;
  esac
  start_now "$INSTALL_DIR/av"
}

# Everything runs from here, so a download cut off halfway runs nothing.
main "$@"
