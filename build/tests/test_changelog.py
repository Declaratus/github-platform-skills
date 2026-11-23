import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'lib'))
import build_changelog as c

CONFIG = {'api': 'https://example.test/wp/v2', 'lookback_days': 30,
          'plugins': {'demo': {'title': 'Demo', 'labels': ['account-management'], 'match': 'budget'}}}


def entry(date, title, types=(1,)):
    return {'date_gmt': f'{date}T12:00:00', 'link': f'https://github.blog/changelog/{date}-x',
            'title': {'rendered': title}, 'excerpt': {'rendered': '<p>body</p>'}, 'type': list(types)}


class ChangelogTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.skill = self.root / 'plugins/demo/skills/demo'
        (self.skill / 'references').mkdir(parents=True)
        (self.skill / 'references/SOURCE.json').write_text(
            json.dumps({'upstream_committed_at': '2026-11-13T15:26:07-08:00'}), encoding='utf-8')
        self.urls = []

    def fake_get(self, rows):
        def get(url):
            self.urls.append(url)
            if '/label?' in url:
                return [{'id': 7, 'slug': 'account-management'}], 1
            if '/type?' in url:
                return [{'id': 1, 'slug': 'new-releases'}, {'id': 2, 'slug': 'improvements'},
                        {'id': 3, 'slug': 'deprecations'}], 1
            return rows, 1
        return get

    def run_build(self, rows):
        with patch.object(c, 'get', self.fake_get(rows)):
            c.build(self.root, CONFIG, 'demo', datetime(2026, 11, 23, tzinfo=timezone.utc))
        return (self.skill / 'changelog.md').read_text(encoding='utf-8')

    def test_window_filter_and_render(self):
        out = self.run_build([entry('2026-11-16', 'Budget limit &amp; more', (2,)),
                              entry('2026-11-10', 'Unrelated audit log change')])
        changelogs = next(u for u in self.urls if '/changelogs?' in u)
        self.assertIn('after=2026-10-14T00%3A00%3A00', changelogs)
        self.assertIn('label=7', changelogs)
        self.assertIn('| 2026-11-16 | Improvement | [Budget limit & more]', out)
        self.assertNotIn('Unrelated', out)
        self.assertIn('covers 2026-10-14 to 2026-11-23', out)
        self.assertIn('label/account-management/feed/', out)

    def test_refuses_empty_list(self):
        with self.assertRaises(ValueError):
            self.run_build([entry('2026-11-10', 'Unrelated')])
        self.assertFalse((self.skill / 'changelog.md').exists())

    def test_skips_plugin_without_snapshot(self):
        (self.skill / 'references/SOURCE.json').unlink()
        with patch.object(c, 'get', self.fake_get([])):
            c.build(self.root, CONFIG, 'demo', datetime(2026, 11, 23, tzinfo=timezone.utc))
        self.assertEqual(self.urls, [])


if __name__ == '__main__':
    unittest.main()
