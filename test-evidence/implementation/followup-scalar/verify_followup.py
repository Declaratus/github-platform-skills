"""Compare frozen/candidate metadata with the independent permanent oracle."""
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import types
import unittest

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'build/tests'))
sys.path.insert(0, str(ROOT / 'build/lib'))
import yaml
from frontmatter_oracle import metadata_oracle
import test_resolver

FROZEN = 'f4db74d994b2efaa51d70fb92b6458402e8f59c2'
SUB = 'plugins/github-copilot-docs/skills/github-copilot-docs/references'
UP = ROOT / '.build-cache/github-copilot-docs'
PIN = '7c3387d3b513ed43ea26c9b2e4c0e1b12234c010'
checks = []
def git(*args):
    return subprocess.check_output(['git', '-c', 'core.longpaths=true', *args], cwd=ROOT).decode('utf-8').replace('\r\n', '\n')
def check(name, expected, actual):
    checks.append(dict(id=name, expected=expected, actual=actual, status='PASS' if expected == actual else 'FAIL',
                       command='python test-evidence/implementation/followup-scalar/verify_followup.py'))
    assert expected == actual, checks[-1]

def front(text):
    return yaml.safe_load(re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)[1])

check('upstream-pin', PIN, git('-C', str(UP), 'rev-parse', 'HEAD').strip())
variables = {p.stem: yaml.safe_load(p.read_text(encoding='utf-8')) or {} for p in (UP / 'data/variables').glob('*.yml')}
frozen_mismatches, candidate_mismatches, body_changes = [], [], []
pages = list((UP / 'content/copilot').rglob('*.md'))
for source in pages:
    relative = source.relative_to(UP / 'content/copilot').as_posix()
    expected = metadata_oracle(front(source.read_text(encoding='utf-8')), variables, UP / 'data/reusables')
    frozen = git('show', FROZEN + ':' + SUB + '/' + relative)
    candidate = (ROOT / SUB / relative).read_text(encoding='utf-8')
    for text, mismatches in [(frozen, frozen_mismatches), (candidate, candidate_mismatches)]:
        actual = front(text)
        if actual != expected:
            mismatches.append(dict(page=relative, expected=expected, actual=actual))
    split = lambda text: re.split(r'\A---\r?\n.*?\r?\n---(?:\r?\n|$)', text, maxsplit=1, flags=re.S)[1]
    if split(frozen) != split(candidate):
        body_changes.append(relative)
check('oracle-page-count', 568, len(pages))
check('oracle-reproduces-frozen-defect', ['concepts/customizations/plugins.md'], [m['page'] for m in frozen_mismatches])
check('candidate-independent-metadata-oracle', [], candidate_mismatches)
check('all-bodies-preserved-vs-frozen', [], body_changes)
(OUT / 'frozen-oracle-mismatches.json').write_text(json.dumps(frozen_mismatches, indent=2, ensure_ascii=False), encoding='utf-8', newline='\n')

# Execute the same literal regression assertions against the untouched frozen
# implementation in memory. This never checks out or modifies old source.
frozen_module = types.ModuleType('frozen_resolver')
exec(compile(git('show', FROZEN + ':build/lib/resolve_liquid.py'), '<frozen resolver>', 'exec'), frozen_module.__dict__)
saved = test_resolver.r
test_resolver.r = frozen_module
names = ['test_frontmatter_multiline_reusable_has_no_body_padding',
         'test_frontmatter_preserves_existing_scalar_whitespace',
         'test_frontmatter_and_body_use_distinct_continuation_rules']
stream = io.StringIO()
try:
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(unittest.TestSuite(test_resolver.ResolverTests(n) for n in names))
finally:
    test_resolver.r = saved
(OUT / 'before-fix-regressions.log').write_text('\n'.join(line.rstrip() for line in stream.getvalue().splitlines()) + '\n', encoding='utf-8', newline='\n')
check('frozen-literal-regressions-fail', [3, 4, 0], [result.testsRun, len(result.failures), len(result.errors)])
(OUT / 'followup-results.json').write_text(json.dumps(checks, indent=2), encoding='utf-8', newline='\n')
print(json.dumps(checks, indent=2))
