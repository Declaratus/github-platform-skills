#!/usr/bin/env bash
# Recipe: refresh plugins/github-well-architected/skills/github-well-architected/references/
# from the revision pinned in build/well-architected-source.json.
#
# Invoked by build/build.sh. Expects REPO_ROOT to point at the marketplace repo root.
# Never touches SKILL.md.

set -euo pipefail

: "${REPO_ROOT:?REPO_ROOT must be set (invoke via build/build.sh)}"
PY="${PYTHON:-python3}"

PLUGIN="github-well-architected"
PIN="$REPO_ROOT/build/well-architected-source.json"
UPSTREAM=$("$PY" -c 'import json,sys; print(json.load(open(sys.argv[1]))["repository"])' "$PIN")
REVISION=$("$PY" -c 'import json,sys; print(json.load(open(sys.argv[1]))["revision"])' "$PIN")
[[ "$REVISION" =~ ^[0-9a-f]{40}$ ]] || { echo "ERROR: $PIN needs a full 40-character commit SHA" >&2; exit 1; }

CACHE="$REPO_ROOT/.build-cache/$PLUGIN"
DEST="$REPO_ROOT/plugins/$PLUGIN/skills/$PLUGIN/references"

# 1. Fetch exactly the pinned revision (shallow)
if [[ ! -d "$CACHE/.git" ]] || [[ "$(git -C "$CACHE" remote get-url origin)" != "$UPSTREAM" ]]; then
  echo "  → init $CACHE"
  rm -rf "$CACHE"
  git init --quiet "$CACHE"
  git -C "$CACHE" remote add origin "$UPSTREAM"
fi
echo "  → fetch ${REVISION:0:12}"
git -C "$CACHE" fetch --depth 1 --quiet origin "$REVISION"
git -C "$CACHE" checkout --detach --force --quiet "$REVISION"
[[ "$(git -C "$CACHE" rev-parse HEAD)" == "$REVISION" ]] || { echo "ERROR: fetched revision mismatch" >&2; exit 1; }

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

# 5. Provenance
MD_COUNT=$(find "$DEST" -name '*.md' | wc -l | tr -d ' ')
[[ "$MD_COUNT" -gt 0 ]] || { echo "ERROR: refusing an empty references snapshot" >&2; exit 1; }
COMMITTED_AT=$(git -C "$CACHE" show -s --format=%cI "$REVISION")
"$PY" - "$DEST/SOURCE.json" "$UPSTREAM" "$REVISION" "$COMMITTED_AT" "$MD_COUNT" <<'EOF'
import json, sys
out, repo, rev, when, count = sys.argv[1:]
with open(out, 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'schema': 1, 'repository': repo, 'revision': rev,
               'upstream_committed_at': when, 'markdown_pages': int(count)}, f, indent=2)
    f.write('\n')
EOF

echo "  ✓ $PLUGIN: $MD_COUNT markdown files, upstream ${REVISION:0:12}"
