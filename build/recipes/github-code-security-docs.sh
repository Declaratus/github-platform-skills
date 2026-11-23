#!/usr/bin/env bash
# Resolve and validate a pinned snapshot of content/code-security before replacing good references.
set -euo pipefail
: "${REPO_ROOT:?REPO_ROOT must be set (invoke via build/build.sh)}"
exec "${PYTHON:-python3}" "$REPO_ROOT/build/lib/rebuild_copilot_docs.py" --repo-root "$REPO_ROOT" \
  --plugin github-code-security-docs --content content/code-security \
  --source build/code-security-docs-source.json "$@"
