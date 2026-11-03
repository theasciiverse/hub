#!/bin/sh
# Makes the theasciiverse repos public that the catalog needs: every repo a
# manifest in catalog/ names as its repo, plus av and hub themselves. Other
# private repos in the org are listed and left as they are.
#
#   sh tools/go-public.sh          # dry run: shows what it would change
#   sh tools/go-public.sh --run    # makes them public
#
# Afterwards: sh tools/release-all.sh --run (releases for every title), then
# run hub's "site" workflow so the catalog picks them all up.
set -eu
export LC_ALL=C   # one byte order for sort and comm
org=theasciiverse
run=no
[ "${1:-}" = "--run" ] && run=yes
cd "$(dirname "$0")/.."

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
{ printf 'av\nhub\n'; grep -h '^repo *= *"theasciiverse/' catalog/*.toml | sed 's/.*theasciiverse\/\([^"]*\)".*/\1/'; } | sort -u > "$tmp/wanted"
gh repo list "$org" --limit 1000 --visibility private --json name --jq '.[].name' | sort -u > "$tmp/private"
flip=$(comm -12 "$tmp/private" "$tmp/wanted")
keep=$(comm -23 "$tmp/private" "$tmp/wanted")

n=0
for repo in $flip; do
  n=$((n + 1))
  if [ "$run" = yes ]; then
    gh repo edit "$org/$repo" --visibility public --accept-visibility-change-consequences >/dev/null && echo "public: $repo"
  else
    echo "would make public: $repo"
  fi
done
echo
echo "$n repos $( [ "$run" = yes ] && echo made || echo to make ) public."
[ -n "$keep" ] && printf 'Left private (no catalog title names them):\n%s\n' "$(printf '%s\n' "$keep" | sed 's/^/  /')"
exit 0
