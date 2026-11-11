#!/usr/bin/env python3
"""Stage and validate a pinned Copilot snapshot before publishing references.

Dependency imports happen before any cache or destination mutation. Publication
uses sibling renames with rollback on replacement failure, not delete/copy.
"""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import liquid
import yaml
from resolve_liquid import resolve_tree, site_context

INPUTS = ['content/copilot', 'data/variables', 'data/reusables', 'data/tables',
          'src/rest/lib', 'src/frame/middleware/context', 'src/versions/lib']
PLUGIN = 'plugins/github-copilot-docs/skills/github-copilot-docs'


def git(cache, *args, raw=False):
    output = subprocess.check_output(['git', '-c', 'core.longpaths=true', '-c',
                                   'core.autocrlf=false', '-c', 'core.eol=lf',
                                   '-C', str(cache), *args])
    return output if raw else output.decode('utf-8').strip()


def publish(stage, destination, backup):
    """Keep the previous tree until the validated replacement is in place."""
    existed = destination.exists()
    if existed:
        destination.rename(backup)
    try:
        stage.rename(destination)
    except BaseException:
        if existed:
            backup.rename(destination)
        raise


def rebuild(root, revision, upstream):
    if not re.fullmatch(r'[0-9a-f]{40}', revision):
        raise ValueError('Use a full immutable 40-character upstream commit SHA')
    cache = root / '.build-cache/github-copilot-docs'
    destination = root / PLUGIN / 'references'
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Serialize builds in this checkout. Never reuse another build's stage.
    lock = destination.parent / '.references-build-lock'
    lock.mkdir()
    try:
        cache.mkdir(parents=True, exist_ok=True)
        if not (cache / '.git').is_dir():
            git(cache, 'init')
            git(cache, 'remote', 'add', 'origin', upstream)
        if git(cache, 'remote', 'get-url', 'origin') != upstream:
            raise ValueError('Cache origin differs from requested upstream')
        git(cache, 'sparse-checkout', 'init', '--cone')
        git(cache, 'sparse-checkout', 'set', *INPUTS)
        git(cache, 'fetch', '--depth', '1', '--filter=blob:none', 'origin', revision)
        git(cache, 'checkout', '--detach', '--force', revision)
        if git(cache, 'rev-parse', 'HEAD') != revision:
            raise ValueError('Fetched upstream revision mismatch')
        context = site_context(cache)
        with tempfile.TemporaryDirectory(prefix='.references-stage-', dir=destination.parent) as temp:
            temp = Path(temp)
            stage = temp / 'references'
            shutil.copytree(cache / 'content/copilot', stage)
            # Exact Git object avoids platform checkout line-ending differences.
            (stage / 'LICENSE').write_bytes(git(cache, 'show', revision + ':LICENSE', raw=True))
            for path in stage.rglob('*'):
                if path.is_file() and path.suffix != '.md' and path.name != 'LICENSE':
                    path.unlink()
            resolve_tree(cache / 'data', stage, context)
            count = len(list(stage.rglob('*.md')))
            if not count:
                raise ValueError('Refusing an empty references snapshot')
            provenance = {
                'schema': 1, 'repository': upstream, 'revision': revision,
                'upstream_committed_at': git(cache, 'show', '-s', '--format=%cI', revision),
                'markdown_pages': count, 'source_inputs': INPUTS,
                'site_context': context,
                'site_context_sources': ['src/rest/lib/config.json',
                    'src/frame/middleware/context/context.ts', 'src/versions/lib/all-versions.ts'],
                'dependencies': {'PyYAML': yaml.__version__, 'python-liquid': liquid.__version__},
                'generator_sha256': {p.name: hashlib.sha256(p.read_bytes().replace(b'\r\n', b'\n')).hexdigest()
                                     for p in [Path(__file__), Path(__file__).with_name('resolve_liquid.py')]},
            }
            (stage / 'SOURCE.json').write_text(json.dumps(provenance, indent=2) + '\n', encoding='utf-8', newline='\n')
            publish(stage, destination, temp / 'previous')
        print(f'Built {count} Copilot markdown pages from {revision}')
    finally:
        lock.rmdir()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo-root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--revision', help='Full immutable upstream commit; defaults to build/copilot-docs-source.json')
    args = parser.parse_args()
    source = json.loads((args.repo_root / 'build/copilot-docs-source.json').read_text(encoding='utf-8'))
    rebuild(args.repo_root, args.revision or source['revision'], source['repository'])


if __name__ == '__main__':
    main()
