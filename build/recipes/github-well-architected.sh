#!/usr/bin/env bash
# Recipe: refresh plugins/github-well-architected/skills/github-well-architected/references/
# from https://github.com/github/github-well-architected.
#
# Invoked by build/build.sh. Expects REPO_ROOT to point at the marketplace repo root.
# Never touches SKILL.md.

set -euo pipefail

: "${REPO_ROOT:?REPO_ROOT must be set (invoke via build/build.sh)}"

PLUGIN="github-well-architected"
UPSTREAM="https://github.com/github/github-well-architected.git"

CACHE="$REPO_ROOT/.build-cache/$PLUGIN"
DEST="$REPO_ROOT/plugins/$PLUGIN/skills/$PLUGIN/references"

# 1. Refresh upstream clone (shallow)
if [[ -d "$CACHE/.git" ]]; then
  echo "  → refresh $CACHE"
  git -C "$CACHE" fetch --depth 1 origin main --quiet
  git -C "$CACHE" reset --hard origin/main --quiet
else
  echo "  → clone $UPSTREAM"
  rm -rf "$CACHE"
  git clone --depth 1 --quiet "$UPSTREAM" "$CACHE"
fi

# 2. Restage curated markdown
echo "  → stage references"
rm -rf "$DEST"
mkdir -p "$DEST"
cp    "$CACHE/charter.md"                 "$DEST/charter.md"
cp    "$CACHE/docs/framework-overview.md" "$DEST/framework-overview.md"
cp    "$CACHE/docs/taxonomies.md"         "$DEST/taxonomies.md"
cp -r "$CACHE/content/library"            "$DEST/library"

# 3. Drop release notes (timestamped changelog, low signal as skill content)
rm -rf "$DEST/library/overview/release-notes"

# 4. Strip binary assets (skills don't load them; they only bloat the repo)
find "$DEST" -type f \( \
    -name '*.png'  -o -name '*.jpg' -o -name '*.jpeg' \
 -o -name '*.gif'  -o -name '*.webp' \
 -o -name '*.pdf' \
\) -delete

# 5. Report
MD_COUNT=$(find "$DEST" -name '*.md' | wc -l | tr -d ' ')
UPSTREAM_SHA=$(git -C "$CACHE" rev-parse --short HEAD)
echo "  ✓ $PLUGIN: $MD_COUNT markdown files, upstream $UPSTREAM_SHA"
