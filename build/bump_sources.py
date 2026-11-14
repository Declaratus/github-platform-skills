#!/usr/bin/env python3
"""Move each build/*-source.json pin to the upstream default branch head.

Prints one line per pin. With --summary, also writes a markdown summary with
compare links for the refresh PR body. Exits 0 whether or not anything moved.
"""
import argparse
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def remote_head(repository):
    output = subprocess.check_output(['git', 'ls-remote', repository, 'HEAD'], text=True)
    revision = output.split()[0]
    if not re.fullmatch(r'[0-9a-f]{40}', revision):
        raise ValueError(f'Unexpected ls-remote output for {repository}: {output!r}')
    return revision


def compare_url(repository, old, new):
    base = repository.removesuffix('.git')
    return f'{base}/compare/{old[:12]}...{new[:12]}'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--summary', type=Path)
    args = parser.parse_args()
    lines = []
    for pin in sorted((ROOT / 'build').glob('*-source.json')):
        source = json.loads(pin.read_text(encoding='utf-8'))
        old, new = source['revision'], remote_head(source['repository'])
        if old == new:
            print(f'{pin.name}: unchanged at {old[:12]}')
            continue
        source['revision'] = new
        pin.write_text(json.dumps(source, indent=2) + '\n', encoding='utf-8', newline='\n')
        print(f'{pin.name}: {old[:12]} -> {new[:12]}')
        lines.append(f'- `{pin.name}`: [{old[:12]}...{new[:12]}]({compare_url(source["repository"], old, new)})')
    if args.summary:
        body = '\n'.join(lines) if lines else 'No pins moved.'
        args.summary.parent.mkdir(parents=True, exist_ok=True)
        args.summary.write_text(body + '\n', encoding='utf-8', newline='\n')


if __name__ == '__main__':
    main()
