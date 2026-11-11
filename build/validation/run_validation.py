"""Local implementation validation. Fail nonzero; retain commands and outcomes."""
from pathlib import Path
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
from output_paths import output_directory

label = sys.argv[1] if len(sys.argv) > 1 else 'implementation'
E = output_directory(ROOT, label)
REFS = ROOT / 'plugins/github-copilot-docs/skills/github-copilot-docs/references'
PIN = '7c3387d3b513ed43ea26c9b2e4c0e1b12234c010'
BASE = '875c75bc9c8bbf9f010e16633ef0c25475a3e1b3'
checks = []


def record(name, expected, actual, command):
    passed = actual == expected
    def brief(value):
        if isinstance(value, dict) and len(value) > 100 and all(isinstance(v, str) and re.fullmatch('[0-9a-f]{64}', v) for v in value.values()):
            return {'files': len(value), 'sha256_inventory': hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()}
        return value
    entry = dict(id=name, status='PASS' if passed else 'FAIL',
                 expected=brief(expected), actual=brief(actual), command=command)
    checks.append(entry)
    (E / 'validation-results.json').write_text(json.dumps(checks, indent=2), encoding='utf-8', newline='\n')
    if entry['status'] == 'FAIL':
        raise AssertionError(entry)


def command(name, argv, expected=0, env=None):
    process = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True, encoding='utf-8', errors='replace')
    (E / (name + '.log')).write_text(process.stdout + process.stderr, encoding='utf-8', newline='\n')
    record(name, expected, process.returncode, argv)
    return process


def inventory(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file()}


command('repository-hygiene', [sys.executable, 'build/check_repository_hygiene.py'])
command('pinned-rebuild', [sys.executable, 'build/lib/rebuild_copilot_docs.py', '--revision', PIN])
first = inventory(REFS)
command('pinned-repeat', [sys.executable, 'build/lib/rebuild_copilot_docs.py', '--revision', PIN])
record('repeat-byte-idempotence', first, inventory(REFS), 'SHA-256 inventory before/after second pinned rebuild')

# The real cold and refresh entry points, not just a mocked fetch or fixture.
cold = ROOT / ('.build-cache/validation-cold-root' + ('-' + label if label else ''))
if cold.exists():
    raise AssertionError('Cold validation root already exists; preserve it and choose a fresh directory')
(cold / 'build').mkdir(parents=True)
shutil.copyfile(ROOT / 'build/copilot-docs-source.json', cold / 'build/copilot-docs-source.json')
command('cold-pinned-rebuild', [sys.executable, 'build/lib/rebuild_copilot_docs.py', '--repo-root', str(cold)])
record('cold-byte-equivalence', first, inventory(cold / 'plugins/github-copilot-docs/skills/github-copilot-docs/references'), 'SHA-256 full cold build vs existing-cache build')
command('cold-cache-refresh', [sys.executable, 'build/lib/rebuild_copilot_docs.py', '--repo-root', str(cold)])
record('refresh-byte-equivalence', first, inventory(cold / 'plugins/github-copilot-docs/skills/github-copilot-docs/references'), 'SHA-256 refresh vs cold build')
command('real-missing-dependencies', [sys.executable, '-S', 'build/lib/rebuild_copilot_docs.py'], expected=1)
record('real-failure-preserves-568-pages', first, inventory(REFS), 'SHA-256 full previous references after actual import failure')

bash = 'C:/Program Files/Git/bin/bash.exe' if os.name == 'nt' else shutil.which('bash')
command('bash-dispatcher-syntax', [bash, '-n', 'build/build.sh'])
command('bash-recipe-syntax', [bash, '-n', 'build/recipes/github-copilot-docs.sh'])
environment = dict(os.environ, PYTHON=sys.executable.replace('\\', '/'))
command('shell-pinned-rebuild', [bash, 'build/build.sh', 'github-copilot-docs', '--revision', PIN], env=environment)
record('shell-byte-equivalence', first, inventory(REFS), 'SHA-256 shell supported pinned path vs Python path')
command('marketplace-validation', ['claude', 'plugin', 'validate', '.'])
command('plugin-validation', ['claude', 'plugin', 'validate', './plugins/github-copilot-docs'])
command('diff-whitespace', ['git', '-c', 'core.longpaths=true', '-c', 'core.autocrlf=false', 'diff', '--check'])

with (E / 'unittest.log').open('w', encoding='utf-8', newline='\n') as stream:
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(unittest.defaultTestLoader.discover(str(ROOT / 'build/tests')))
suite = dict(tests=result.testsRun, failures=[t.id() for t, _ in result.failures],
             errors=[t.id() for t, _ in result.errors], skipped=[t.id() for t, _ in result.skipped])
(E / 'unittest-results.json').write_text(json.dumps(suite, indent=2), encoding='utf-8', newline='\n')
record('full-permanent-suite', {'success': True, 'skips': 0},
       {'success': result.wasSuccessful(), 'skips': len(result.skipped)},
       'python -m unittest discover -s build/tests -v (same discovery executed with JSON summary)')

# Compare immutable original Git blobs, not CRLF-converted working-tree files.
prefix = 'plugins/github-copilot-docs/skills/github-copilot-docs/references/'
lines = subprocess.check_output(['git', 'ls-tree', '-r', BASE, '--', prefix], cwd=ROOT).decode().splitlines()
entries = [(s.split('\t')[0].split()[2], s.split('\t')[1]) for s in lines]
blobs = subprocess.run(['git', 'cat-file', '--batch'], cwd=ROOT,
                       input=('\n'.join(x[0] for x in entries) + '\n').encode(), capture_output=True, check=True)
data = io.BytesIO(blobs.stdout)
changed = []; same = []; body_changes = []; old_invalid = []
import yaml
for sha, path in entries:
    size = int(data.readline().split()[2]); old = data.read(size); data.read(1)
    new = (ROOT / path).read_bytes(); relative = path.removeprefix(prefix)
    (same if old == new else changed).append(relative)
    if path.endswith('.md'):
        source = old.decode('utf-8'); generated = new.decode('utf-8')
        a = re.split(r'^---\s*$', source, maxsplit=2, flags=re.M)
        b = re.split(r'^---\s*$', generated, maxsplit=2, flags=re.M)
        if a[2] != b[2]:
            body_changes.append(relative)
        try:
            yaml.safe_load(a[1])
        except yaml.YAMLError:
            old_invalid.append(relative)
        yaml.safe_load(b[1])
comparison = dict(original_files=len(entries), unchanged=same, changed=changed,
                  markdown_changed=sum(p.endswith('.md') for p in changed),
                  markdown_preserved=sum(p.endswith('.md') for p in same),
                  body_changes=body_changes, original_invalid_yaml=old_invalid,
                  new_files=sorted(set(first) - {p.removeprefix(prefix) for _, p in entries}))
(E / 'corpus-comparison.json').write_text(json.dumps(comparison, indent=2), encoding='utf-8', newline='\n')
expected_bodies = ['how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions.md',
                   'how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-via-the-api.md']
record('only-intended-body-changes', expected_bodies, body_changes, 'Git blob comparison splitting frontmatter/body for all 568 pages')
record('license-unchanged', True, 'LICENSE' in same, 'Byte comparison of license against original Git blob')
record('original-15-YAML-errors-repaired', 15, len(old_invalid), 'Parse old metadata to identify 15 old errors; all new metadata parsed above')
record('no-page-additions-removals', [568, ['SOURCE.json']],
       [len(list(REFS.rglob('*.md'))), comparison['new_files']], 'Compare original tree paths with regenerated tree')
record('postvalidation-no-staging-debris', [],
       [p.name for p in REFS.parent.iterdir() if p.name.startswith('.references-stage-') or p.name == '.references-build-lock']
       + [p.name for p in (ROOT / '.build-cache/github-copilot-docs-staging').glob('.references-stage-*')],
       'List sibling build locks/staging directories after successful and failed runs')
print(json.dumps({'checks': len(checks), 'suite': suite,
                  'corpus_markdown_preserved': comparison['markdown_preserved'],
                  'corpus_markdown_changed': comparison['markdown_changed']}, indent=2))
