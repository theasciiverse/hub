#!/bin/sh
# frame.sh CAST_ID SECONDS OUT.png [WIDTH_PX]: render one frame of
# site/casts/<id>.cast with the site's player, font and palette
# (needs the dev server: python3 -m http.server 8765 in site/).
W=${4:-800}
P=$(mktemp -d)
timeout 40 google-chrome --headless=new --disable-gpu --hide-scrollbars --user-data-dir="$P" \
  --window-size=$((W+20)),$((W*13/20)) --virtual-time-budget=5000 --screenshot="$3" \
  "http://127.0.0.1:8765/dev/frame.html?cast=$1&t=$2&w=$W" >/dev/null 2>&1
rm -rf "$P"
