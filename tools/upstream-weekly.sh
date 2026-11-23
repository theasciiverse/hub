#!/bin/sh
# Weekly upstream report on beast: pulls hub's manifests and writes
# ../UPSTREAM-REPORT.md (the Asciiverse folder, beside the assignments),
# keeping last week's as UPSTREAM-REPORT.previous.md.
# Run by ~/.config/systemd/user/asciiverse-upstream.service (timer: Mondays).
set -eu
cd "$(dirname "$0")/.."
git pull -q --ff-only || true
out=../UPSTREAM-REPORT.md
[ -f "$out" ] && cp "$out" ../UPSTREAM-REPORT.previous.md
python3 tools/upstream_report.py --out "$out.new" 2>../upstream-report.log
mv "$out.new" "$out"
tail -1 ../upstream-report.log
