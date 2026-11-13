#!/usr/bin/env python3
"""Builds catalog.json from hub/catalog (catalog/SCHEMA.md).

Every manifest (<id>.toml) and page (<id>.md) is merged with its release
data and written as one catalog.json, which av and the website read:

- release.source = "github": the newest published release of the title's
  repo that holds an archive for it (<id>-<target>.tar.gz or .zip), its
  SHA256SUMS, and the notes of its latest releases as news;
- release.source = "direct": the files written in the manifest, each
  downloaded and checked against its sha256;
- MUDs: no release, only the world's address;
- every title's preview from site/casts/<id>.cast, with its length and a
  version stamp taken from its contents.
- every title's `added` date: the day its manifest first came into the
  hub's git history (a manifest not committed yet counts as added today),
  which the FRESH! badge reads.

A title whose release cannot be read this time keeps its entry from the
previous catalog (--previous), so a GitHub hiccup never drops it. Manifests
that do not parse, ids that do not match their file, and pages outside the
Markdown subset fail the build.

Needs only Python 3.11 or newer. Set GITHUB_TOKEN (in Actions it is
there; locally `GITHUB_TOKEN=$(gh auth token)`) for the GitHub API.

  python3 tools/build_catalog.py --out site/data/catalog.json
  python3 tools/build_catalog.py --out public/data/catalog.json \\
      --previous https://asciiverse.sh/data/catalog.json
"""
import argparse, getpass, hashlib, json, os, pathlib, re, subprocess, sys, tomllib
import urllib.error, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

HUB = pathlib.Path(__file__).resolve().parent.parent
CATALOG = HUB / "catalog"
CASTS = HUB / "site" / "casts"
API = "https://api.github.com"
KINDS = {"game", "program", "movie", "mud", "adventure", "art"}
NEWS = 3
TARGET = r"(?:x86_64|aarch64|i686|armv7|riscv64gc)-[a-z0-9_]+-[a-z0-9_]+(?:-[a-z0-9_]+)?"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

warnings = []


def warn(msg):
    warnings.append(msg)
    print(f"warning: {msg}", file=sys.stderr)


# ---------------------------------------------------------------- http

class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


_plain = urllib.request.build_opener(_NoRedirect)


def fetch(url, accept="application/vnd.github+json", auth=True):
    """The body of url. GitHub's token goes only to api.github.com; an
    asset download redirects to a storage host, which is fetched without
    it (that host refuses a second credential)."""
    for _ in range(5):
        req = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": "asciiverse-hub"})
        if auth and TOKEN and urllib.parse.urlsplit(url).hostname == "api.github.com":
            req.add_header("Authorization", f"Bearer {TOKEN}")
        try:
            with _plain.open(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (301, 302, 303, 307, 308) and e.headers.get("Location"):
                url = urllib.parse.urljoin(url, e.headers["Location"])
                continue
            raise
    raise RuntimeError(f"too many redirects for {url}")


def api(path):
    return json.loads(fetch(f"{API}/{path}"))


# ---------------------------------------------------------------- pages

PAGE_RULES = [
    (re.compile(r"^# ", re.M), "a # heading (the title comes from the manifest)"),
    (re.compile(r"!\[[^\]]*\]\("), "an image"),
    (re.compile(r"^\s*(```|~~~)", re.M), "a fenced code block"),
    (re.compile(r"^\s*\|.*\|\s*$", re.M), "a table"),
    (re.compile(r"</?[A-Za-z][A-Za-z0-9-]*(\s[^>]*)?/?>"), "raw HTML"),
    (re.compile(r"\]\((?!https?://)[^)]*\)"), "a link that is not http(s)"),
]


def page_problems(text):
    # inline code may show anything, so it is left out of the checks
    bare = re.sub(r"`[^`\n]*`", "``", text)
    return [what for rx, what in PAGE_RULES if rx.search(bare)]


# ---------------------------------------------------------------- casts

LEAKS = re.compile(r"/home/|/Users/|/tmp/claude|\b%s\b" % re.escape(getpass.getuser().lower()))


def cast_info(id_):
    """(cast_url, duration) of site/casts/<id>.cast, or None. A cast that
    names a home folder or the builder's login is refused (RECORDING.md)."""
    path = CASTS / f"{id_}.cast"
    if not path.is_file():
        return None
    data = path.read_bytes()
    text = data.decode("utf-8", "replace")
    if (m := LEAKS.search(text)) and getpass.getuser() not in ("runner", "root"):
        raise ValueError(f"its cast contains {m.group(0)!r}; re-record it (RECORDING.md)")
    if m := re.search(r"/home/|/Users/|/tmp/claude", text):
        raise ValueError(f"its cast contains {m.group(0)!r}; re-record it (RECORDING.md)")
    lines = text.splitlines()
    head = json.loads(lines[0])
    v3, idle = head.get("version") == 3, head.get("idle_time_limit", 2.0)
    total = prev = 0.0
    for line in lines[1:]:
        if line.strip():
            t = json.loads(line)[0]
            total += min(t if v3 else t - prev, idle)
            prev = t
    stamp = hashlib.sha256(data).hexdigest()[:12]
    return f"/casts/{id_}.cast?v={stamp}", round(total, 1)


# ---------------------------------------------------------------- releases

_releases = {}


def releases(repo):
    """The repo's published releases, newest first (cached: a collection's
    titles share one repo)."""
    if repo not in _releases:
        rel = api(f"repos/{repo}/releases?per_page=30")
        rel = [r for r in rel if not r.get("draft") and not r.get("prerelease")]
        rel.sort(key=lambda r: r.get("published_at") or "", reverse=True)
        _releases[repo] = rel
    return _releases[repo]


_sums = {}


def sha256sums(asset):
    if asset["id"] not in _sums:
        body = fetch(asset["url"], accept="application/octet-stream").decode()
        sums = {}
        for line in body.splitlines():
            parts = line.split()
            if len(parts) == 2:
                sums[parts[1].lstrip("*")] = parts[0].lower()
        _sums[asset["id"]] = sums
    return _sums[asset["id"]]


def archives(release, id_):
    """{target: asset} of id_'s archives in a release."""
    rx = re.compile(rf"^{re.escape(id_)}-({TARGET})\.(?:tar\.gz|zip)$")
    out = {}
    for a in release.get("assets", []):
        if m := rx.match(a["name"]):
            out[m.group(1)] = a
    return out


def github_release(t):
    rels = [r for r in releases(t["repo"]) if archives(r, t["id"])]
    if not rels:
        raise ValueError(f"no release of {t['repo']} holds an archive named {t['id']}-<target>")
    r = rels[0]
    sums_asset = next((a for a in r["assets"] if a["name"] == "SHA256SUMS"), None)
    if not sums_asset:
        raise ValueError(f"{t['repo']} {r['tag_name']} has no SHA256SUMS")
    sums = sha256sums(sums_asset)
    platforms = {}
    for target, a in sorted(archives(r, t["id"]).items()):
        if a["name"] not in sums:
            warn(f"{t['id']}: {a['name']} is not in SHA256SUMS of {r['tag_name']}, left out")
            continue
        platforms[target] = {"url": a["browser_download_url"], "sha256": sums[a["name"]], "size": a["size"]}
    if not platforms:
        raise ValueError(f"{t['repo']} {r['tag_name']}: no archive is listed in SHA256SUMS")
    version = re.sub(r"^v(?=\d)", "", r["tag_name"])
    news = [{"version": re.sub(r"^v(?=\d)", "", x["tag_name"]),
             "date": (x.get("published_at") or "")[:10],
             "notes": (x.get("body") or "").strip()} for x in rels[:NEWS]]
    return {"version": version, "updated_at": r.get("published_at"), "platforms": platforms, "news": news}


def direct_release(t):
    rel = t["release"]
    platforms = {}
    for target, p in rel.get("platforms", {}).items():
        data = fetch(p["url"], accept="*/*", auth=False)
        got = hashlib.sha256(data).hexdigest()
        if got != p["sha256"].lower():
            raise ValueError(f"{target}: {p['url']} has sha256 {got}, the manifest says {p['sha256']}")
        platforms[target] = {"url": p["url"], "sha256": got, "size": len(data)}
    news = []
    if url := rel.get("notes_url"):
        try:
            body = fetch(url, accept="text/markdown, text/plain", auth=False).decode()
            if not page_problems(body) and not body.lstrip().startswith("<"):
                news = [{"version": rel["version"], "date": "", "notes": body.strip()}]
        except Exception as e:
            warn(f"{t['id']}: notes_url not read ({e})")
    return {"version": rel["version"], "updated_at": rel.get("updated_at"), "platforms": platforms, "news": news}


def av_entry():
    """The catalog's "av" entry: av's newest published release, if any."""
    try:
        rels = [r for r in api("repos/theasciiverse/av/releases?per_page=5")
                if not r.get("draft") and not r.get("prerelease")]
    except Exception as e:
        warn(f"av's releases not read ({e})")
        return None
    if not rels:
        return None
    r = max(rels, key=lambda r: r.get("published_at") or "")
    return {"version": re.sub(r"^v(?=\d)", "", r["tag_name"]),
            "date": (r.get("published_at") or "")[:10], "notes": (r.get("body") or "").strip()}


# ---------------------------------------------------------------- manifests

def load_manifests():
    titles, errors = {}, []
    for path in sorted(CATALOG.glob("*.toml")):
        if path.name == "collections.toml":
            continue
        try:
            t = tomllib.loads(path.read_text())
        except tomllib.TOMLDecodeError as e:
            errors.append(f"{path.name}: {e}")
            continue
        id_ = t.get("id")
        if id_ != path.stem:
            errors.append(f"{path.name}: id {id_!r} does not match the file name")
            continue
        if t.get("kind") not in KINDS:
            errors.append(f"{id_}: kind {t.get('kind')!r} is not one of {sorted(KINDS)}")
            continue
        page = path.with_suffix(".md")
        t["page"] = page.read_text() if page.exists() else ""
        if bad := page_problems(t["page"]):
            errors.append(f"{id_}.md uses {', '.join(bad)} (SCHEMA.md, Page)")
        if "system_deps" in t.get("requires", {}):
            t["system_deps"] = t["requires"].pop("system_deps")
        if t["kind"] != "mud":
            src = t.get("release", {}).get("source")
            if src not in ("github", "direct"):
                errors.append(f"{id_}: release.source must be github or direct")
            elif src == "github" and not t.get("repo"):
                errors.append(f"{id_}: release.source = \"github\" needs repo")
        titles[id_] = t
    return titles, errors



def added_dates():
    """Maps each id to the ISO date its manifest was first committed.

    One git log over catalog/*.toml, newest first, so the last date seen for
    a file is the earliest. Empty when git or the history is not there (a
    shallow checkout would give every title the day of the newest commit).
    """
    try:
        if subprocess.run(["git", "rev-parse", "--is-shallow-repository"], cwd=HUB,
                          capture_output=True, text=True, check=True).stdout.strip() == "true":
            warn("shallow git checkout: no added dates (fetch-depth: 0 in the workflow)")
            return {}
        log = subprocess.run(["git", "log", "--diff-filter=A", "--format=%x00%cs",
                              "--name-only", "--", "catalog/*.toml"], cwd=HUB,
                             capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError) as e:
        warn(f"no added dates ({e})")
        return {}
    dates, day = {}, None
    for line in log.splitlines():
        if line.startswith("\0"):
            day = line[1:]
        elif line.strip() and day:
            dates[pathlib.PurePosixPath(line.strip()).stem] = day
    return dates


def build_one(t, previous):
    id_ = t["id"]
    try:
        if c := cast_info(id_):
            t["cast_url"], t["duration"] = c
        elif t["kind"] != "mud":
            warn(f"{id_}: no cast in site/casts, left out")
            return None
        if "media" in t:
            t["thumbnail_at"] = t["media"].get("thumbnail_at", 5.0)
        if t["kind"] == "mud":
            return t
        rel = github_release(t) if t["release"]["source"] == "github" else direct_release(t)
        t.update(rel)
        return t
    except Exception as e:
        old = previous.get(id_)
        if old:
            warn(f"{id_}: {e}; kept from the previous catalog ({old.get('version')})")
            return old
        warn(f"{id_}: {e}; left out")
        return None


def load_previous(where):
    if not where:
        return {}
    try:
        if re.match(r"https?://", where):
            data = fetch(where, accept="application/json", auth=False)
        else:
            data = pathlib.Path(where).read_bytes()
        return json.loads(data).get("titles", {})
    except Exception as e:
        warn(f"previous catalog not read ({e})")
        return {}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", required=True, help="where to write catalog.json")
    ap.add_argument("--previous", help="the last published catalog.json, a path or URL")
    ap.add_argument("--only", nargs="*", help="build just these ids (for testing)")
    args = ap.parse_args()

    titles, errors = load_manifests()
    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        sys.exit(1)
    if args.only:
        titles = {k: v for k, v in titles.items() if k in args.only}
    previous = load_previous(args.previous)

    with ThreadPoolExecutor(8) as pool:
        # titles of one repo run in the same worker order, so the cache helps
        built = list(pool.map(lambda t: build_one(t, previous), titles.values()))
    out = {t["id"]: t for t in built if t}
    if dates := added_dates():
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        for id_, t in out.items():
            t["added"] = dates.get(id_, today)

    cols = CATALOG / "collections.toml"
    catalog = {
        "schema_version": 1,
        "catalog_generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "collections": tomllib.loads(cols.read_text()) if cols.exists() else {},
        "titles": dict(sorted(out.items())),
    }
    if av := av_entry():
        catalog["av"] = av
    dest = pathlib.Path(args.out)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(catalog, indent=1, ensure_ascii=False))
    print(f"{len(out)} titles of {len(titles)} written to {dest}, {len(warnings)} warnings")

    if summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(summary, "a") as f:
            f.write(f"### Catalog\n\n{len(out)} titles of {len(titles)}.\n\n")
            if warnings:
                f.write("Warnings:\n\n" + "".join(f"- {w}\n" for w in warnings))
    if not out:
        sys.exit(1)


if __name__ == "__main__":
    main()
