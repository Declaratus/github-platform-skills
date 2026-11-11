#!/usr/bin/env bash
# Recipe: refresh plugins/github-copilot-docs/skills/github-copilot-docs/references/
# from content/copilot in https://github.com/github/docs.
#
# Invoked by build/build.sh. Expects REPO_ROOT to point at the marketplace repo root.
# Never touches SKILL.md. Needs python3 with PyYAML for Liquid resolution.

set -euo pipefail

: "${REPO_ROOT:?REPO_ROOT must be set (invoke via build/build.sh)}"

PLUGIN="github-copilot-docs"
UPSTREAM="https://github.com/github/docs.git"
SPARSE=(content/copilot data/variables data/reusables)

CACHE="$REPO_ROOT/.build-cache/$PLUGIN"
DEST="$REPO_ROOT/plugins/$PLUGIN/skills/$PLUGIN/references"

# 1. Refresh upstream clone (shallow, blobless, sparse; github/docs is huge)
if [[ -d "$CACHE/.git" ]]; then
  echo "  → refresh $CACHE"
  git -C "$CACHE" sparse-checkout set "${SPARSE[@]}"
  git -C "$CACHE" fetch --depth 1 --filter=blob:none origin main --quiet
  git -C "$CACHE" reset --hard origin/main --quiet
else
  echo "  → clone $UPSTREAM (sparse)"
  rm -rf "$CACHE"
  git clone --depth 1 --filter=blob:none --sparse --quiet "$UPSTREAM" "$CACHE"
  git -C "$CACHE" sparse-checkout set "${SPARSE[@]}"
fi

# 2. Restage content/copilot
echo "  → stage references"
rm -rf "$DEST"
mkdir -p "$DEST"
cp -r "$CACHE/content/copilot/." "$DEST/"
cp    "$CACHE/LICENSE"             "$DEST/LICENSE"

# 3. Strip anything that isn't markdown (images, etc.)
find "$DEST" -type f ! -name '*.md' ! -name 'LICENSE' -delete

# 4. Resolve {% data %} variables and reusables so pages read as plain prose
python3 "$REPO_ROOT/build/lib/resolve_liquid.py" "$CACHE/data" "$DEST"

# 5. Report
MD_COUNT=$(find "$DEST" -name '*.md' | wc -l | tr -d ' ')
UPSTREAM_SHA=$(git -C "$CACHE" rev-parse --short HEAD)
echo "  ✓ $PLUGIN: $MD_COUNT markdown files, upstream $UPSTREAM_SHA"
