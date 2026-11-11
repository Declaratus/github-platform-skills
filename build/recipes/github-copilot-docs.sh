#!/usr/bin/env bash
# Resolve and validate a pinned snapshot before replacing good references.
set -euo pipefail
: "${REPO_ROOT:?REPO_ROOT must be set (invoke via build/build.sh)}"
exec "${PYTHON:-python3}" "$REPO_ROOT/build/lib/rebuild_copilot_docs.py" --repo-root "$REPO_ROOT" "$@"
