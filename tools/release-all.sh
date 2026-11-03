#!/bin/sh
# Re-runs the Asciiverse release workflow of every theasciiverse repo at its
# latest release tag, so the builds GitHub Actions refused while the org's
# billing was blocked (macOS, Linux aarch64) are filled in. Meant for launch
# day, after the repos are public (Actions is free for public repos).
#
#   sh hub/tools/release-all.sh            # dry run: shows what it would do
#   sh hub/tools/release-all.sh --run      # dispatches the workflows
#
# Each release workflow uploads with --clobber, so the locally built Linux
# x86_64 assets already attached are replaced and SHA256SUMS is regenerated.
# Repos with neither a release nor a tag, or no release workflow GitHub
# knows about, are listed at the end for a manual look.
set -eu
org=theasciiverse
run=no
[ "${1:-}" = "--run" ] && run=yes

skipped=""
for repo in $(gh repo list "$org" --limit 200 --json name --jq '.[].name'); do
  # the latest release's tag, or, for a repo whose tags never got a
  # release, its newest tag by version
  tag=$(gh release list -R "$org/$repo" --limit 1 --json tagName --jq '.[0].tagName // empty')
  [ -z "$tag" ] && tag=$(gh api "repos/$org/$repo/tags?per_page=100" --jq '.[].name' 2>/dev/null | sort -V | tail -1)
  if [ -z "$tag" ]; then
    skipped="$skipped\n  $repo: no release and no tag"
    continue
  fi
  wf=$(gh api "repos/$org/$repo/actions/workflows" \
    --jq '[.workflows[].path | select(test("(asciiverse-)?release\\.yml$"))][0] // empty')
  case "$wf" in
    */asciiverse-release.yml) wf=asciiverse-release.yml ;;
    */release.yml) wf=release.yml ;;
    *) skipped="$skipped\n  $repo ($tag): no release workflow registered"; continue ;;
  esac
  if [ "$run" = yes ]; then
    if gh workflow run "$wf" -R "$org/$repo" -f tag="$tag" 2>/dev/null; then
      echo "dispatched $repo $wf $tag"
    else
      skipped="$skipped\n  $repo ($tag): dispatch of $wf failed (no workflow_dispatch input 'tag'?)"
    fi
  else
    echo "would dispatch $repo $wf $tag"
  fi
done
[ -n "$skipped" ] && printf "\nNot dispatched:%b\n" "$skipped"
exit 0
