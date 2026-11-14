#!/usr/bin/env bash
# Resolve and validate a pinned snapshot of content/issues before replacing good references.
set -euo pipefail
: "${REPO_ROOT:?REPO_ROOT must be set (invoke via build/build.sh)}"
exec "${PYTHON:-python3}" "$REPO_ROOT/build/lib/rebuild_copilot_docs.py" --repo-root "$REPO_ROOT" \
  --plugin github-projects-issues-docs --content content/issues \
  --source build/projects-issues-docs-source.json "$@"
