#!/usr/bin/env python3
"""Link-preview pictures: one PNG per title, its preview's still frame.

Renders each title's .cast at its thumbnail time with the site's own player,
font and palette (site/dev/frame.html, headless Chrome, like tools/frame.sh),
into public/t/<id>/poster.png, which tools/build_pages.py then names as the
page's og:image. Renders are kept in a cache folder by the cast's content
stamp (the ?v= in cast_url), so a deploy only renders new or changed casts;
the site workflow keeps that folder between runs.

  python3 tools/posters.py public [cache_dir]

Needs google-chrome. Serves site/ itself on 127.0.0.1:8790 while it runs.
"""
import json
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlparse, parse_qs

PORT, WIDTH, JOBS = 8790, 1200, 6
ROOT = Path(__file__).resolve().parent.parent


def render(cast_id, at, out):
    prof = tempfile.mkdtemp()
    try:
        subprocess.run(["google-chrome", "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        f"--user-data-dir={prof}", f"--window-size={WIDTH + 20},{WIDTH * 13 // 20}",
                        "--virtual-time-budget=5000", f"--screenshot={out}",
                        f"http://127.0.0.1:{PORT}/dev/frame.html?cast={cast_id}&t={at}&w={WIDTH}"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
    except subprocess.TimeoutExpired:
        pass
    finally:
        shutil.rmtree(prof, ignore_errors=True)
    return Path(out).exists() and Path(out).stat().st_size > 2000


def main(public, cache):
    public, cache = Path(public), Path(cache)
    cache.mkdir(parents=True, exist_ok=True)
    cat = json.loads((public / "data" / "catalog.json").read_text())
    titles = list(cat["titles"].values()) if isinstance(cat["titles"], dict) else cat["titles"]
    jobs = []
    for t in titles:
        cu = t.get("cast_url")
        if not cu:
            continue
        u = urlparse(cu)
        cast_id = Path(u.path).stem
        stamp = parse_qs(u.query).get("v", ["x"])[0]
        at = t.get("thumbnail_at", 5)
        key = cache / f"{cast_id}-{stamp}-{at}.png"
        jobs.append((t["id"], cast_id, at, key))
    todo = [j for j in jobs if not j[3].exists()]
    print(f"{len(jobs)} posters, {len(todo)} to render")
    server = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT), "--bind", "127.0.0.1"],
                              cwd=ROOT / "site", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        time.sleep(1)
        start = time.time()
        with ThreadPoolExecutor(JOBS) as pool:
            ok = list(pool.map(lambda j: render(j[1], j[2], str(j[3])), todo))
        print(f"rendered {sum(ok)} of {len(todo)} in {time.time() - start:.0f} s")
    finally:
        server.terminate()
    for tid, _, _, key in jobs:
        if key.exists():
            d = public / "t" / tid
            d.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(key, d / "poster.png")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "public", sys.argv[2] if len(sys.argv) > 2 else ".posters")
