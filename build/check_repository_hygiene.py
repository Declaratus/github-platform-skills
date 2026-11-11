#!/usr/bin/env python3
"""Reject tracked generated artifacts, including files added with git add -f.

Uses the Git index, so run after staging intended changes. No dependencies or
network access. Intentional log input fixtures belong in build/tests/fixtures/.
"""
from pathlib import Path, PurePosixPath
import argparse
import subprocess
import sys


def artifact_reason(path: str) -> str | None:
    parts = PurePosixPath(path).parts
    lower = tuple(part.lower() for part in parts)
    if '.build-cache' in lower or '__pycache__' in lower:
        return 'generated cache'
    if path.lower().endswith(('.pyc', '.pyo', '.pyd')):
        return 'compiled Python output'
    if lower and lower[0] == 'test-evidence' and path != 'test-evidence/README.md':
        return 'raw evidence; keep only the curated summary here'
    if path.lower().endswith('.log') and parts[:3] != ('build', 'tests', 'fixtures'):
        return 'run log; use .build-cache (input fixtures have a dedicated directory)'
    return None


def tracked_artifacts(root: Path) -> list[tuple[str, str]]:
    paths = subprocess.check_output(['git', '-C', str(root), 'ls-files', '-z'])
    result = []
    for raw in paths.split(b'\0'):
        if raw:
            path = raw.decode('utf-8', errors='surrogateescape')
            reason = artifact_reason(path)
            if reason:
                result.append((path, reason))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo-root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        artifacts = tracked_artifacts(args.repo_root)
    except subprocess.CalledProcessError:
        print('Could not inspect the Git index.', file=sys.stderr)
        return 2
    if artifacts:
        print('Generated artifacts are staged/tracked. Keep raw output in .build-cache:', file=sys.stderr)
        for path, reason in artifacts:
            print(f'  {path}: {reason}', file=sys.stderr)
        return 1
    print('Repository hygiene passed: no tracked generated artifacts.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
