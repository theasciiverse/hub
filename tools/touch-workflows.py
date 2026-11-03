#!/usr/bin/env python3
"""Makes GitHub register a repo's release workflow that it never picked up.

Workflows pushed while the org's Actions were blocked (October 2026) were
never registered: the Actions tab says "No workflows found" although the
file is there, and an empty commit does not help. A commit that changes the
file does. For each repo named, this adds one header comment to its release
workflow on the default branch (through the GitHub API, so no local clone
is needed), then starts that workflow for the repo's newest tag.

  python3 tools/touch-workflows.py csol zoridor ...
"""
import base64, json, subprocess, sys, time

ORG = "theasciiverse"
HEAD = "# Asciiverse release workflow (tag v* or run by hand with a tag)\n"
MESSAGE = ("release.yml: a header line, so GitHub reads the workflow again\n\n"
           "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>")


def gh(*args, data=None):
    r = subprocess.run(["gh", *args], capture_output=True, text=True, input=data)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def newest_tag(repo):
    _, out, _ = gh("api", f"repos/{ORG}/{repo}/tags?per_page=100", "--jq", ".[].name")
    tags = out.split()
    if not tags:
        return None
    r = subprocess.run(["sort", "-V"], input="\n".join(tags), capture_output=True, text=True)
    return r.stdout.split()[-1]


for repo in sys.argv[1:]:
    _, branch, _ = gh("api", f"repos/{ORG}/{repo}", "--jq", ".default_branch")
    path = meta = None
    for p in (".github/workflows/release.yml", ".github/workflows/asciiverse-release.yml"):
        code, out, _ = gh("api", f"repos/{ORG}/{repo}/contents/{p}?ref={branch}")
        if code == 0:
            path, meta = p, json.loads(out)
            break
    if not path:
        print(f"{repo}: no release workflow on {branch}")
        continue
    text = base64.b64decode(meta["content"]).decode()
    if not text.startswith(HEAD):
        body = json.dumps({"message": MESSAGE, "branch": branch, "sha": meta["sha"],
                           "content": base64.b64encode((HEAD + text).encode()).decode()})
        code, _, err = gh("api", "-X", "PUT", f"repos/{ORG}/{repo}/contents/{path}", "--input", "-", data=body)
        if code:
            print(f"{repo}: edit FAILED: {err[:150]}")
            continue
    # GitHub registers it within seconds of the push
    name = path.rsplit("/", 1)[1]
    for _ in range(10):
        _, n, _ = gh("api", f"repos/{ORG}/{repo}/actions/workflows", "--jq", ".total_count")
        if n not in ("", "0"):
            break
        time.sleep(3)
    tag = newest_tag(repo)
    if not tag:
        print(f"{repo}: workflow registered, no tag to build")
        continue
    code, _, err = gh("workflow", "run", name, "-R", f"{ORG}/{repo}", "-f", f"tag={tag}")
    print(f"{repo}: {'release started for ' + tag if code == 0 else 'workflow edited; start FAILED: ' + err[:150]}")
