#!/usr/bin/env python3
"""Stage and validate a pinned github/docs snapshot before publishing references.

Defaults build github-copilot-docs; --plugin/--content/--source reuse it for
another content/ section.

Dependency imports happen before any cache or destination mutation. Publication
uses same-filesystem renames with rollback on replacement failure, not delete/copy.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import liquid
import yaml
from resolve_liquid import resolve_tree, site_context

NAME = 'github-copilot-docs'
CONTENT = 'content/copilot'
SHARED_INPUTS = ['data/variables', 'data/reusables', 'data/tables',
                 'src/rest/lib', 'src/frame/middleware/context', 'src/versions/lib']
INPUTS = [CONTENT, *SHARED_INPUTS]
PLUGIN = f'plugins/{NAME}/skills/{NAME}'


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


FLAG_RE = re.compile(r'{%-?\s*(?:els)?ifversion\s+(.*?)-?%}')
FLAG_WORDS = {'or', 'and', 'not', 'fpt', 'ghec', 'ghes'}


def write_versions(stage, cache):
    """GHES releases and the feature flags the pages use, so agents can resolve version gates offline."""
    releases = (cache / 'src/versions/lib/enterprise-server-releases.ts').read_text(encoding='utf-8')
    supported = re.search(r"^export const supported = \[([^\]]*)\]", releases, re.M)
    candidate = re.search(r"^export const releaseCandidate = (?:'([0-9.]+)'|null)", releases, re.M)
    if not supported or not candidate:
        raise ValueError('Cannot read GHES releases from enterprise-server-releases.ts')
    supported = re.findall(r"'([0-9.]+)'", supported.group(1))
    used = set()
    for page in stage.rglob('*.md'):
        text = page.read_text(encoding='utf-8')
        for expr in FLAG_RE.findall(text):
            used.update(w for w in re.findall(r'[a-z][a-z0-9_-]*', expr) if w not in FLAG_WORDS)
        used.update(re.findall(r'^\s+feature:\s*[\'"]?([a-z0-9_-]+)', text, re.M))
    rows = []
    for flag in sorted(used):
        path = cache / 'data/features' / f'{flag}.yml'
        if not path.is_file():
            raise ValueError(f'Feature flag {flag} has no data/features entry')
        versions = (yaml.safe_load(path.read_text(encoding='utf-8')) or {}).get('versions') or {}
        rows.append(f"| `{flag}` | {', '.join(f'{k} `{v}`' for k, v in versions.items())} |")
    rc = candidate.group(1)
    (stage / 'VERSIONS.md').write_text(
        '# Versions at this snapshot\n\n'
        'Generated from upstream `src/versions/lib/enterprise-server-releases.ts` and `data/features/` '
        'at the pinned commit (see `SOURCE.json`).\n\n'
        f"## GitHub Enterprise Server releases\n\nSupported, newest first: {', '.join(supported)}.\n"
        + (f'Release candidate: {rc} (not yet generally available).\n' if rc else 'No release candidate.\n')
        + '\n## Feature flags used in these pages\n\n'
        '`{% ifversion <flag> %}` and `versions: feature: <flag>` text applies only to the versions listed. '
        '`fpt` is GitHub Free/Pro/Team, `ghec` is GitHub Enterprise Cloud, `ghes` is GitHub Enterprise Server.\n\n'
        '| Flag | Versions |\n|---|---|\n' + '\n'.join(rows) + '\n', encoding='utf-8', newline='\n')


def rebuild(root, revision, upstream, name=NAME, content=CONTENT, features=False):
    if not re.fullmatch(r'[0-9a-f]{40}', revision):
        raise ValueError('Use a full immutable 40-character upstream commit SHA')
    inputs = [content, *SHARED_INPUTS, *(['data/features'] if features else [])]
    cache = root / '.build-cache' / name
    destination = root / f'plugins/{name}/skills/{name}' / 'references'
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Corpora must never be staged inside the packaged plugin. An interrupted
    # process may leave this ignored workspace behind; do not adopt/delete it.
    workspace = root / '.build-cache' / f'{name}-staging'
    workspace.mkdir(parents=True, exist_ok=True)
    if workspace.stat().st_dev != destination.parent.stat().st_dev:
        raise ValueError('Build workspace and references must be on the same filesystem')
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
        git(cache, 'sparse-checkout', 'set', *inputs)
        git(cache, 'fetch', '--depth', '1', '--filter=blob:none', 'origin', revision)
        git(cache, 'checkout', '--detach', '--force', revision)
        if git(cache, 'rev-parse', 'HEAD') != revision:
            raise ValueError('Fetched upstream revision mismatch')
        context = site_context(cache)
        with tempfile.TemporaryDirectory(prefix='.references-stage-', dir=workspace) as temp:
            temp = Path(temp)
            (temp / 'BUILD.json').write_text(json.dumps({
                'pid': os.getpid(), 'destination': str(destination.resolve()),
                'revision': revision,
            }, indent=2) + '\n', encoding='utf-8', newline='\n')
            stage = temp / 'references'
            shutil.copytree(cache / content, stage)
            # Exact Git object avoids platform checkout line-ending differences.
            (stage / 'LICENSE').write_bytes(git(cache, 'show', revision + ':LICENSE', raw=True))
            for path in stage.rglob('*'):
                if path.is_file() and path.suffix != '.md' and path.name != 'LICENSE':
                    path.unlink()
            resolve_tree(cache / 'data', stage, context)
            count = len(list(stage.rglob('*.md')))
            if not count:
                raise ValueError('Refusing an empty references snapshot')
            if features:
                write_versions(stage, cache)
            provenance = {
                'schema': 1, 'repository': upstream, 'revision': revision,
                'upstream_committed_at': git(cache, 'show', '-s', '--format=%cI', revision),
                'markdown_pages': count, 'source_inputs': inputs,
                'site_context': context,
                'site_context_sources': ['src/rest/lib/config.json',
                    'src/frame/middleware/context/context.ts', 'src/versions/lib/all-versions.ts'],
                'dependencies': {'PyYAML': yaml.__version__, 'python-liquid': liquid.__version__},
                'generator_sha256': {p.name: hashlib.sha256(p.read_bytes().replace(b'\r\n', b'\n')).hexdigest()
                                     for p in [Path(__file__), Path(__file__).with_name('resolve_liquid.py')]},
            }
            (stage / 'SOURCE.json').write_text(json.dumps(provenance, indent=2) + '\n', encoding='utf-8', newline='\n')
            publish(stage, destination, temp / 'previous')
        print(f'Built {count} {name} markdown pages from {revision}')
    finally:
        lock.rmdir()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo-root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--revision', help='Full immutable upstream commit; defaults to the --source pin')
    parser.add_argument('--plugin', default=NAME, help='Plugin and skill name to publish into')
    parser.add_argument('--content', default=CONTENT, help='github/docs content folder to bundle')
    parser.add_argument('--source', default='build/copilot-docs-source.json', help='Pin file, relative to --repo-root')
    parser.add_argument('--features', action='store_true', help='Also write VERSIONS.md (GHES releases, feature flags)')
    args = parser.parse_args()
    source = json.loads((args.repo_root / args.source).read_text(encoding='utf-8'))
    rebuild(args.repo_root, args.revision or source['revision'], source['repository'],
            args.plugin, args.content, args.features)


if __name__ == '__main__':
    main()
