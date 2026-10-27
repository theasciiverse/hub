#!/usr/bin/env python3
"""Build data/catalog.json for the design mockup.

Stands in for hub's catalog generator: real manifests and pages from
hub/catalog/ (<id>.toml + <id>.md), plus mock titles from dev/mock-titles.toml
for games that have no manifest yet. Release data (version, platforms, sizes)
is faked here; the real generator reads it from GitHub Releases.

Mockup-only fields, not in SCHEMA.md: featured (carousel order), old and new
(the OLD! and NEW! banners, manual curation), duration (cast length, computed here).
"""
import getpass, hashlib, io, json, pathlib, re, sys, tarfile, tomllib

SITE = pathlib.Path(__file__).resolve().parent.parent
HUB = SITE.parent / "catalog"
MOCK = SITE / "dev" / "mock-titles.toml"
GAMES = SITE.parent.parent / "games"
RELEASES = SITE / "dev-releases"
TARGET = "x86_64-unknown-linux-gnu"

def local_binary(t):
    """The game's binary if it is built on this machine."""
    name = (t.get("exec") or {}).get("game") or t["id"]
    dirs = [GAMES / t["id"], GAMES / t["id"].replace("-", " ")]
    for d in dirs:
        for c in (d / "target" / "release" / name, d / name, d / "src" / name):
            if c.is_file() and c.stat().st_mode & 0o111:
                return c, name, d
    return None

def release_dir(t):
    """dev-releases/<id>/, or dev-releases/<repo name>/ when one release holds
    several titles (theasciiverse/zork: zork1, zork2, zork3)."""
    for name in (t["id"], (t.get("repo") or "").split("/")[-1]):
        if name and (RELEASES / name / "SHA256SUMS").exists():
            return RELEASES / name
    return None

def release_info(t):
    """version and updated_at of a downloaded release, from release.json next
    to its SHA256SUMS ({"version": ..., "updated_at": ...})."""
    d = release_dir(t)
    f = d / "release.json" if d else None
    return json.loads(f.read_text()) if f and f.exists() else {}

def real_release(t):
    """A downloaded GitHub release in dev-releases/<id>/ (archives plus
    SHA256SUMS), served as is: the same files and checksums av would get
    from the real release, read the way hub's generator will read them."""
    d = release_dir(t)
    if not d:
        return {}
    sums = d / "SHA256SUMS"
    out = {}
    for line in sums.read_text().splitlines():
        sha, name = line.split()
        name = name.lstrip("*")
        for ext in (".tar.gz", ".zip"):
            if name.startswith(t["id"] + "-") and name.endswith(ext):
                target = name[len(t["id"]) + 1:-len(ext)]
                out[target] = {"url": f"/dev-releases/{d.name}/{name}", "sha256": sha, "size": (d / name).stat().st_size}
    return out

def dev_release(t):
    """Package a locally built binary as a real archive with a real sha256,
    served by the dev server, so av can test installs end to end."""
    found = local_binary(t)
    if not found:
        return {}
    path, name, root = found
    RELEASES.mkdir(exist_ok=True)
    out = RELEASES / f"{t['id']}-{TARGET}.tar.gz"
    if not out.exists() or out.stat().st_mtime < max([path.stat().st_mtime] + [(root / e).stat().st_mtime for e in t.get("dev_extra", [])]):
        buf = io.BytesIO()
        with tarfile.open(fileobj=buf, mode="w:gz") as tar:
            info = tar.gettarinfo(str(path), arcname=name)
            info.uid = info.gid = 0
            info.uname = info.gname = ""
            with open(path, "rb") as f:
                tar.addfile(info, f)
            # data the game reads relative to its working directory (av runs
            # titles from their install dir), e.g. robotfindskitten's nki/
            def anon(x):
                x.uid = x.gid = 0
                x.uname = x.gname = ""
                return x
            for extra in t.get("dev_extra", []):
                tar.add(str(root / extra), arcname=extra, recursive=True, filter=anon)
        out.write_bytes(buf.getvalue())
    data = out.read_bytes()
    return {TARGET: {"url": f"/dev-releases/{out.name}", "sha256": hashlib.sha256(data).hexdigest(), "size": len(data)}}

# A cast must not carry anything about the machine it was recorded on:
# asciinema stores the command it ran in the header, and games print paths
# and login names. A cast with a home path, the scratch folder or this
# user's login name (as a lower-case word) is refused, not published.
LEAKS = re.compile(r"/home/|/Users/|/tmp/claude|\b%s\b" % re.escape(getpass.getuser().lower()))

def cast_leak(path):
    m = LEAKS.search(path.read_text(errors="replace"))
    return m and m.group(0)

def cast_duration(path):
    total, idle = 0.0, 2.0
    with open(path) as f:
        head = json.loads(f.readline())
        v3 = head.get("version") == 3
        idle = head.get("idle_time_limit", idle)
        prev = 0.0
        for line in f:
            if not line.strip():
                continue
            t = json.loads(line)[0]
            gap = t if v3 else t - prev
            prev = t
            total += min(gap, idle)
    return round(total, 1)

def fake_release(t):
    tri = ["x86_64-unknown-linux-musl", "aarch64-apple-darwin", "x86_64-pc-windows-msvc"]
    if t.get("system_deps"):
        tri = ["x86_64-unknown-linux-gnu", "aarch64-apple-darwin"]
    ext = lambda x: "zip" if "windows" in x else "tar.gz"
    return {x: {"url": f"https://example.invalid/{t['id']}-{x}.{ext(x)}", "sha256": "0" * 64,
                "size": 900_000 + 37_000 * len(t["id"])} for x in tri}

def main():
    titles = {}
    for toml in sorted(HUB.glob("*.toml")):
        if toml.name == "collections.toml":
            continue
        t = tomllib.loads(toml.read_text())
        md = toml.with_suffix(".md")
        t["page"] = md.read_text() if md.exists() else ""
        titles[t["id"]] = t
    if MOCK.exists():
        for t in tomllib.loads(MOCK.read_text()).get("title", []):
            titles.setdefault(t["id"], {}).update({k: v for k, v in t.items() if k not in titles.get(t["id"], {}) or k in ("featured", "old", "new")})
    out = {}
    for id_, t in titles.items():
        cast = SITE / "casts" / f"{id_}.cast"
        if t.get("kind") == "mud":
            # a world on someone's server: no release; its cast is its greeting screen
            if cast.exists():
                t["cast_url"] = f"/casts/{id_}.cast?v={int(cast.stat().st_mtime)}"
            out[id_] = t
            continue
        if not cast.exists():
            print(f"skip {id_}: no cast", file=sys.stderr)
            continue
        if leak := cast_leak(cast):
            print(f"REFUSED {id_}: its cast contains {leak!r}, re-record it (hub/RECORDING.md)", file=sys.stderr)
            continue
        for k, v in release_info(t).items():
            t.setdefault(k, v)
        t.setdefault("version", "0.1.0")
        t.setdefault("updated_at", "2026-10-10T00:00:00Z")
        t["thumbnail_at"] = t.get("media", {}).get("thumbnail_at", t.get("thumbnail_at", 5.0))
        # version stamp, so av and browsers fetch a re-recorded cast instead of a cached one
        # (hub's generator should use a hash of the cast)
        t["cast_url"] = f"/casts/{id_}.cast?v={int(cast.stat().st_mtime)}"
        t["duration"] = cast_duration(cast)
        t["platforms"] = real_release(t) or dev_release(t) or fake_release(t)
        out[id_] = t
    cols = HUB / "collections.toml"
    collections = tomllib.loads(cols.read_text()) if cols.exists() else {}
    (SITE / "data").mkdir(exist_ok=True)
    (SITE / "data" / "catalog.json").write_text(json.dumps(
        {"schema_version": 1, "catalog_generated_at": "2026-10-10T00:00:00Z",
         "collections": collections, "titles": out},
        indent=1, ensure_ascii=False))
    print(f"{len(out)} titles")

main()
