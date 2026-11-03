#!/usr/bin/env python3
"""Download counts for every catalog title, from its GitHub releases.

av installs and updates a title by downloading that title's release file,
so each install or update adds one to that file's count. GitHub keeps only
running totals; save the output now and then to see change over time.

Usage, from the hub folder (needs the gh CLI, signed in):
  python3 tools/downloads.py            table, most downloaded first
  python3 tools/downloads.py --csv      one row per title and file, for saving
  python3 tools/downloads.py --platforms  totals per platform, with system
                                          packages and documents apart
"""
import json, re, subprocess, sys, tomllib
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

CATALOG = Path(__file__).resolve().parent.parent / "catalog"
SKIP = re.compile(r"SHA256SUMS|\.sig$|\.asc$")


def titles():
    for p in sorted(CATALOG.glob("*.toml")):
        t = tomllib.loads(p.read_text())
        if t.get("repo"):
            yield t.get("id", p.stem), t["repo"]


def releases(repo):
    # one release per line, with only the fields needed
    out = subprocess.run(["gh", "api", "--paginate", f"repos/{repo}/releases?per_page=100", "--jq",
                          ".[] | {tag_name, assets: [.assets[] | {name, download_count}]}"],
                         capture_output=True, text=True)
    if out.returncode:
        return None
    return [json.loads(line) for line in out.stdout.splitlines() if line.strip()]


def platform(name):
    """The platform an archive is for (what av downloads), or the kind of
    file for system packages and documents, which people fetch directly."""
    ext = name.rsplit(".", 1)[-1].lower()
    if ext in ("deb", "rpm", "apk"):
        return f"package .{ext}"
    if ext in ("pdf", "txt", "md"):
        return "document"
    for key in ("x86_64-unknown-linux", "aarch64-unknown-linux", "x86_64-apple", "aarch64-apple",
                "x86_64-pc-windows", "aarch64-pc-windows"):
        if key in name:
            return key.replace("-unknown", "").replace("-pc", "").replace("apple", "macos")
    return "other"


def main():
    args = set(sys.argv[1:])
    todo = list(titles())
    with ThreadPoolExecutor(8) as pool:
        got = list(pool.map(lambda t: (t, releases(t[1])), todo))
    rows, missing = [], []
    for (tid, repo), rel in got:
        if rel is None:
            missing.append(tid)
            continue
        for r in rel:
            for a in r.get("assets", []):
                if not SKIP.search(a["name"]):
                    rows.append((tid, r["tag_name"], a["name"], a["download_count"]))
    if "--csv" in args:
        print("title,tag,file,downloads")
        for row in rows:
            print(",".join(map(str, row)))
    elif "--platforms" in args:
        per = Counter()
        for _, _, name, n in rows:
            per[platform(name)] += n
        for k, n in per.most_common():
            print(f"{n:8}  {k}")
    else:
        per = Counter()
        for tid, tag, _, n in rows:
            per[tid] += n
        for tid, _ in todo:
            per.setdefault(tid, 0)
        print(f"{'downloads':>9}  title")
        for tid, n in per.most_common():
            print(f"{n:9}  {tid}")
        print(f"{sum(per.values()):9}  in all, {len(per)} titles")
    if missing:
        print(f"could not read releases for: {', '.join(missing)}", file=sys.stderr)


if __name__ == "__main__":
    main()
