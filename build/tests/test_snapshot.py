"""Offline bundle checks; source-semantic check also runs after a pinned rebuild."""
import json
import hashlib
import re
import subprocess
import sys
import unittest
from pathlib import Path

import yaml

from frontmatter_oracle import metadata_oracle

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'build/lib'))
import resolve_liquid as r

REFS = ROOT / 'plugins/github-copilot-docs/skills/github-copilot-docs/references'


class SnapshotTests(unittest.TestCase):
    def test_manifests_marketplace_and_skill_paths(self):
        marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
        for entry in marketplace['plugins']:
            plugin = ROOT / entry['source']
            self.assertEqual(json.loads((plugin / '.claude-plugin/plugin.json').read_text())['name'], entry['name'])
            self.assertTrue((plugin / 'skills' / entry['name'] / 'SKILL.md').is_file())

    def test_all_frontmatters_valid_and_page_count(self):
        source = json.loads((REFS / 'SOURCE.json').read_text())
        pages = list(REFS.rglob('*.md'))
        self.assertEqual(len(pages), source['markdown_pages'])
        self.assertEqual(len(pages), 568)
        for page in pages:
            with self.subTest(page=page.relative_to(REFS)):
                front = r.FRONT.match(page.read_text(encoding='utf-8'))
                self.assertIsNotNone(front)
                self.assertIn('title', yaml.safe_load(front[1]))

    def test_no_unresolved_build_constructs(self):
        for page in REFS.rglob('*.md'):
            with self.subTest(page=page.relative_to(REFS)):
                text = r.RAW.sub('', page.read_text(encoding='utf-8'))
                self.assertIsNone(r.DATA_TAG.search(text))
                self.assertIsNone(r.INDENTED_TAG.search(text))
                self.assertNotIn('{{ defaultRestApiVersion }}', text)
                self.assertNotRegex(text, r'{%\s*(?:for|assign)\b[^%]*\btables\.')

    def test_gating_and_attribution_retained(self):
        text = (REFS / 'copilot-on-ghes/about-copilot-on-ghes.md').read_text(encoding='utf-8')
        for expected in ['{% ifversion copilot-cli-ghes %}', '{% ifversion copilot-cli-ghes-ga %}', '3.22.3']:
            self.assertIn(expected, text)
        self.assertIn('Attribution', (REFS / 'LICENSE').read_text(encoding='utf-8'))

    def test_provenance_generator_hashes(self):
        source = json.loads((REFS / 'SOURCE.json').read_text())
        pin = json.loads((ROOT / 'build/copilot-docs-source.json').read_text())
        self.assertEqual(source['revision'], pin['revision'])
        for name, expected in source['generator_sha256'].items():
            content = (ROOT / 'build/lib' / name).read_bytes().replace(b'\r\n', b'\n')
            self.assertEqual(hashlib.sha256(content).hexdigest(), expected)

    def test_source_values_and_idempotence_against_pinned_upstream(self):
        upstream = ROOT / '.build-cache/github-copilot-docs'
        if not (upstream / '.git').exists():
            self.skipTest('Run the pinned rebuild first to populate source inputs')
        source = json.loads((REFS / 'SOURCE.json').read_text())
        revision = subprocess.check_output(['git', '-c', 'core.longpaths=true', '-C', str(upstream), 'rev-parse', 'HEAD'], text=True).strip()
        self.assertEqual(revision, source['revision'])
        variables = r.load_variables(upstream / 'data'); tables = r.load_tables(upstream / 'data')
        reusables = upstream / 'data/reusables'; context = r.site_context(upstream)
        # Expected values use a data-only oracle that never calls the renderer.
        oracle_variables = {p.stem: yaml.safe_load(p.read_text(encoding='utf-8')) or {}
                            for p in (upstream / 'data/variables').glob('*.yml')}
        for original in (upstream / 'content/copilot').rglob('*.md'):
            relative = original.relative_to(upstream / 'content/copilot')
            with self.subTest(page=relative):
                generated = (REFS / relative).read_text(encoding='utf-8')
                source_metadata = yaml.safe_load(r.FRONT.match(original.read_text(encoding='utf-8'))[1])
                actual_metadata = yaml.safe_load(r.FRONT.match(generated)[1])
                self.assertEqual(actual_metadata, metadata_oracle(source_metadata, oracle_variables, reusables))
                self.assertEqual(r.resolve(generated, variables, reusables, tables, context=context), generated)
        code = (upstream / 'data/reusables/copilot/java-int-snippet.md').read_text(encoding='utf-8').strip()
        expected = '   ' + code.replace('\n', '\n   ')
        examples = (REFS / 'how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions.md').read_text(encoding='utf-8')
        self.assertEqual(examples.count(expected), 3)
        api_relative = Path('how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-via-the-api.md')
        original = (upstream / 'content/copilot' / api_relative).read_text(encoding='utf-8')
        actual = (REFS / api_relative).read_text(encoding='utf-8')
        self.assertEqual(original.count('{{ defaultRestApiVersion }}'), 4)
        header = 'X-GitHub-Api-Version: ' + context['defaultRestApiVersion']
        self.assertEqual(actual.count(header), original.count(header) + 4)


if __name__ == '__main__':
    unittest.main()
