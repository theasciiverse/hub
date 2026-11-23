#!/usr/bin/env python3
"""Which catalog titles' upstreams have moved on since our build.

For every manifest whose [upstream] names a `git` repository, compares that
repository with our title repo (theasciiverse/<repo>):

- shared history (the usual case: our repo carries upstream's history and
  our changes on top): how many commits upstream has that our default
  branch does not, and upstream's tags newer than the point we built from;
- no shared history (a single-commit import, or a release tarball as our
  first commit): upstream's newest commit and tag with their dates, to
  check by hand;
- either repository unreadable: the reason.

Only commits are fetched (git's tree:0 filter: no trees, no files), into a
cache of bare repositories, so even long histories cost little and later
runs fetch only what is new. Nothing is ever merged: the report is for
choosing which titles to update, by hand, as their own jobs.

Usage, from the hub folder:
  python3 tools/upstream_report.py                  report to stdout
  python3 tools/upstream_report.py --out FILE       report to FILE
  python3 tools/upstream_report.py --only nethack crawl
Our repos are read over SSH (git@github.com:theasciiverse/...), as on beast;
OURS_URL=https://github.com/ reads them over HTTPS instead.
"""
import argparse
import concurrent.futures as cf
import datetime as dt
import os
import pathlib
import subprocess
import sys
import tomllib

HUB = pathlib.Path(__file__).resolve().parent.parent
CATALOG = HUB / "catalog"
CACHE = pathlib.Path(os.environ.get("XDG_CACHE_HOME", pathlib.Path.home() / ".cache")) / "asciiverse" / "upstream"
OURS_URL = os.environ.get("OURS_URL", "git@github.com:")
TIMEOUT = 900
ENV = dict(os.environ, GIT_TERMINAL_PROMPT="0", GIT_SSH_COMMAND=os.environ.get("GIT_SSH_COMMAND", "ssh -o BatchMode=yes"))


def git(repo, *args, check=True):
    p = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, timeout=TIMEOUT, env=ENV)
    if check and p.returncode:
        raise RuntimeError((p.stderr.strip().splitlines() or [f"git {args[0]} failed"])[-1])
    return p.stdout.strip()


def titles():
    """{repo: (git url, [title names])} for manifests with an upstream git."""
    out = {}
    for f in sorted(CATALOG.glob("*.toml")):
        t = tomllib.loads(f.read_text())
        up, repo = t.get("upstream") or {}, t.get("repo", "")
        if up.get("git") and repo.startswith("theasciiverse/"):
            url, names = out.setdefault(repo, (up["git"], []))
            names.append(t.get("title", f.stem))
    return out


def day(ts):
    return dt.datetime.fromtimestamp(int(ts), dt.timezone.utc).date().isoformat() if ts else "?"


def check(repo, url):
    name = repo.split("/", 1)[1]
    bare = CACHE / f"{name}.git"
    if not bare.exists():
        bare.mkdir(parents=True)
        git(bare, "init", "-q", "--bare")
    for remote, where in (("ours", f"{OURS_URL}{repo}.git"), ("up", url)):
        if git(bare, "remote", "get-url", remote, check=False) != where:
            git(bare, "remote", "remove", remote, check=False)
            git(bare, "remote", "add", remote, where)
    # our default branch
    head = git(bare, "ls-remote", "--symref", "ours", "HEAD").splitlines()
    branch = next((l.split()[1] for l in head if l.startswith("ref:")), "refs/heads/main").removeprefix("refs/heads/")
    git(bare, "fetch", "-q", "--filter=tree:0", "--no-tags", "--prune", "ours", f"+refs/heads/{branch}:refs/ours/head", "+refs/tags/*:refs/ours-tags/*")
    git(bare, "fetch", "-q", "--filter=tree:0", "--no-tags", "--prune", "up", "+HEAD:refs/up/head", "+refs/tags/*:refs/up-tags/*")
    ours, up = "refs/ours/head", "refs/up/head"
    up_ts, up_subject = git(bare, "log", "-1", "--format=%ct%x09%s", up).split("\t", 1)
    tags = []
    for line in git(bare, "for-each-ref", "--sort=-creatordate", "--format=%(refname:strip=2)\t%(creatordate:unix)\t%(*objectname)%(objectname)", "refs/up-tags").splitlines():
        tag, ts, sha = line.split("\t")
        tags.append((tag, int(ts or 0), sha[:40] if len(sha) == 80 else sha))
    base = git(bare, "merge-base", ours, up, check=False)
    r = {"repo": repo, "url": url, "branch": branch, "up_date": day(up_ts), "up_subject": up_subject}
    if not base:
        r["kind"] = "unlinked"
        r["newest_tag"] = (tags[0][0], day(tags[0][1])) if tags else None
        r["our_first"] = day(git(bare, "log", "--reverse", "--format=%ct", ours).splitlines()[0])
        return r
    r["behind"] = int(git(bare, "rev-list", "--count", f"{ours}..{up}"))
    r["base_date"] = day(git(bare, "log", "-1", "--format=%ct", base))
    r["base"] = base[:9]
    # an upstream tag is ours when our branch contains it, or when we
    # carry the same tag (or its "-patches" twin: a distribution's patches
    # applied one commit each, as with Debian's, rather than merged)
    our_tags = set(git(bare, "for-each-ref", "--format=%(refname:strip=2)", "refs/ours-tags").splitlines())
    base_ts = int(git(bare, "log", "-1", "--format=%ct", base))
    new = []
    for tag, ts, sha in tags:
        if tag in our_tags or f"{tag}-patches" in our_tags or ts <= base_ts:
            break  # tags come newest first; from here on we have them, or
            # they are older than what we built from (side branches)
        commit = git(bare, "rev-parse", "-q", "--verify", f"{sha}^{{commit}}", check=False)
        if not commit:
            continue
        ours_has = subprocess.run(["git", "-C", str(bare), "merge-base", "--is-ancestor", commit, ours], env=ENV, capture_output=True).returncode == 0
        if ours_has:
            break
        new.append((tag, day(ts)))
        if len(new) >= 3:
            break
    r["new_tags"] = new
    # a distribution's packaging repo moves with packaging work; only a new
    # version of it is news
    packaging = "salsa.debian.org" in url or r.get("remote") == "debian"
    r["kind"] = "moved" if new or (r["behind"] and not packaging) else "same"
    return r


def report(results, errors, names, skipped):
    moved = sorted((r for r in results if r["kind"] == "moved"), key=lambda r: (0 if r["new_tags"] else 1, -r["behind"]))
    unlinked = sorted((r for r in results if r["kind"] == "unlinked"), key=lambda r: r["up_date"], reverse=True)
    same = [r for r in results if r["kind"] == "same"]
    today = dt.date.today().isoformat()
    out = [f"# Upstream report, {today}", ""]
    out.append(f"{len(results) + len(errors)} title repos with an upstream git repository: "
               f"{len(moved)} have moved on, {len(same)} are where we built from, "
               f"{len(unlinked)} share no history with ours (check by hand), {len(errors)} could not be read."
               + (f" {skipped} more have no upstream git (archives, tarballs) and are not checked." if skipped else ""))
    out += ["", "Nothing is merged. Pick the updates worth taking; each is a job of its own: "
            "rebase our changes on upstream, test, release -av.N+1.", ""]

    def label(r):
        return f"**{', '.join(names[r['repo']])}** (`{r['repo']}`, {r['branch']})"

    if moved:
        out += ["## Moved on since our build", "", "New releases first, then by how far ahead upstream is.", ""]
        for r in moved:
            tags = "; new tags: " + ", ".join(f"{t} ({d})" for t, d in r["new_tags"]) if r["new_tags"] else ""
            out.append(f"- {label(r)}: {r['behind']} commits since ours ({r['base']}, {r['base_date']}); "
                       f"upstream last {r['up_date']}: \"{r['up_subject'][:70]}\"{tags}. {r['url']}")
        out.append("")
    if unlinked:
        out += ["## No shared history: check by hand", "",
                "Our repo starts from a tarball or a single-commit import, so commits cannot be counted. "
                "Newest upstream activity first.", ""]
        for r in unlinked:
            tag = f"; newest tag {r['newest_tag'][0]} ({r['newest_tag'][1]})" if r["newest_tag"] else ""
            out.append(f"- {label(r)}: upstream last {r['up_date']}: \"{r['up_subject'][:70]}\"{tag}; "
                       f"our history starts {r['our_first']}. {r['url']}")
        out.append("")
    if errors:
        out += ["## Could not be read", ""]
        for repo, why in sorted(errors.items()):
            out.append(f"- **{', '.join(names[repo])}** (`{repo}`): {why}")
        out.append("")
    if same:
        out += ["## Where we built from", "", ", ".join(sorted(n for r in same for n in names[r["repo"]])), ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", help="write the report here instead of stdout")
    ap.add_argument("--only", nargs="*", help="only these repos or title ids")
    ap.add_argument("--jobs", type=int, default=6)
    a = ap.parse_args()
    found = titles()
    total_up = sum(1 for f in CATALOG.glob("*.toml") if (tomllib.loads(f.read_text()).get("upstream")))
    if a.only:
        want = set(a.only)
        found = {r: v for r, v in found.items() if r.split("/", 1)[1] in want or any(n in want for n in v[1])}
    names = {r: v[1] for r, v in found.items()}
    results, errors = [], {}
    with cf.ThreadPoolExecutor(a.jobs) as ex:
        futs = {ex.submit(check, r, v[0]): r for r, v in found.items()}
        for f in cf.as_completed(futs):
            repo = futs[f]
            try:
                results.append(f.result())
            except Exception as e:
                errors[repo] = str(e)[:200]
            print(f"{len(results) + len(errors)}/{len(found)} {repo}", file=sys.stderr)
    skipped = 0 if a.only else max(0, total_up - sum(len(v) for v in names.values()))
    text = report(results, errors, names, skipped)
    if a.out:
        pathlib.Path(a.out).write_text(text + "\n")
    else:
        print(text)
    moved = sum(1 for r in results if r["kind"] == "moved")
    print(f"upstream report: {moved} moved on, {len(errors)} unreadable", file=sys.stderr)


if __name__ == "__main__":
    main()
