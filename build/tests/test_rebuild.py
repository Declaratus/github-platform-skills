import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'lib'))
import rebuild_copilot_docs as b


def inventory(root):
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob('*') if p.is_file()}


class RebuildTests(unittest.TestCase):
    def setUp(self):
        temp_root = Path(__file__).resolve().parents[2] / '.build-cache/test-temp'
        temp_root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=temp_root)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.upstream = self.root / 'upstream'; self.upstream.mkdir()
        self.target = self.root / 'target'
        self.dest = self.target / b.PLUGIN / 'references'
        self.dest.mkdir(parents=True)
        (self.dest / 'good.md').write_text('previous validated snapshot')
        self.original = inventory(self.dest)
        self.git('init')
        self.write('content/copilot/index.md', "---\ntitle: Fixture\nproduct: '{% data variables.product.name %}'\n---\n{{ defaultRestApiVersion }}\n")
        self.write('data/variables/product.yml', 'name: "organization\'s Copilot"\n')
        self.write('data/tables/example.yml', '- name: Alpha\n')
        self.write('data/reusables/example.md', 'snippet')
        self.write('LICENSE', 'fixture license — attribution café\n\n')
        self.write('src/rest/lib/config.json', json.dumps({'api-versions': {'fpt': ['2099-01-01', '2001-02-03']}}))
        self.write('src/frame/middleware/context/context.ts', 'defaultRestApiVersion = apiVersions[apiVersions.length - 1]')
        self.write('src/versions/lib/all-versions.ts', "apiVersions[key].sort().reverse(); plan: 'free-pro-team'; nonEnterpriseDefault: true")
        self.revision = self.commit()

    def write(self, path, text):
        p = self.upstream / path; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text, encoding='utf-8')

    def git(self, *args):
        return subprocess.check_output(['git', '-c', 'core.longpaths=true', '-c', 'user.name=Local tests',
                                       '-c', 'user.email=local-tests@example.invalid', '-C', str(self.upstream), *args],
                                      text=True, stderr=subprocess.DEVNULL).strip()

    def commit(self):
        self.git('add', '.'); self.git('commit', '-m', 'fixture'); return self.git('rev-parse', 'HEAD')

    def build(self, revision=None):
        with contextlib.redirect_stdout(io.StringIO()):
            b.rebuild(self.target, revision or self.revision, str(self.upstream))

    def assert_clean(self):
        self.assertFalse((self.dest.parent / '.references-build-lock').exists())
        self.assertFalse(list(self.dest.parent.glob('.references-stage-*')))

    def test_cold_build_and_authoritative_default(self):
        self.build()
        self.assertFalse((self.dest / 'good.md').exists())
        self.assertIn('2001-02-03', (self.dest / 'index.md').read_text())
        source = json.loads((self.dest / 'SOURCE.json').read_text())
        self.assertEqual(source['revision'], self.revision)
        self.assertEqual(source['markdown_pages'], 1)
        self.assertEqual(source['site_context']['defaultRestApiVersion'], '2001-02-03')
        license_blob = subprocess.check_output(['git', '-C', str(self.upstream), 'show', 'HEAD:LICENSE'])
        self.assertEqual((self.dest / 'LICENSE').read_bytes(), license_blob)
        self.assert_clean()

    def test_refresh_and_exact_repeat(self):
        self.build(); first = inventory(self.dest); self.build()
        self.assertEqual(inventory(self.dest), first)
        self.write('content/copilot/second.md', '---\ntitle: Second\n---\nnew page')
        newer = self.commit(); self.build(newer)
        self.assertTrue((self.dest / 'second.md').is_file())
        self.assertEqual(json.loads((self.dest / 'SOURCE.json').read_text())['revision'], newer)
        self.assert_clean()

    def test_cold_render_failure_preserves_snapshot(self):
        self.write('content/copilot/bad.md', '---\ntitle: Bad\n---\n{% data variables.absent %}')
        with self.assertRaisesRegex(ValueError, 'Unresolved data'):
            self.build(self.commit())
        self.assertEqual(inventory(self.dest), self.original)
        self.assert_clean()

    def test_refresh_validation_failure_preserves_snapshot(self):
        self.build(); previous = inventory(self.dest)
        self.write('content/copilot/bad.md', '---\nproduct: "unterminated\n---\n')
        with self.assertRaises(ValueError):
            self.build(self.commit())
        self.assertEqual(inventory(self.dest), previous)
        self.assert_clean()

    def test_refresh_missing_table_preserves_snapshot(self):
        self.build(); previous = inventory(self.dest)
        self.write('content/copilot/bad.md', '---\ntitle: Bad\n---\n{% for row in tables.missing %}empty{% endfor %}')
        with self.assertRaisesRegex(ValueError, 'undefined'):
            self.build(self.commit())
        self.assertEqual(inventory(self.dest), previous)
        self.assert_clean()

    def test_fetch_failure_preserves_snapshot_and_cleans_lock(self):
        with self.assertRaises(subprocess.CalledProcessError):
            self.build('0' * 40)
        self.assertEqual(inventory(self.dest), self.original)
        self.assert_clean()

    def test_dependency_failure_exits_before_any_mutation(self):
        script = Path(b.__file__)
        p = subprocess.run([sys.executable, '-S', str(script), '--repo-root', str(self.target)], capture_output=True)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn(b'ModuleNotFoundError', p.stderr)
        self.assertEqual(inventory(self.dest), self.original)
        self.assertFalse((self.target / '.build-cache').exists())
        self.assert_clean()

    def test_render_failure_cli_nonzero(self):
        self.write('content/copilot/bad.md', '---\ntitle: Bad\n---\n{% data variables.absent %}')
        revision = self.commit()
        config = self.target / 'build/copilot-docs-source.json'; config.parent.mkdir()
        config.write_text(json.dumps({'repository': str(self.upstream), 'revision': revision}))
        p = subprocess.run([sys.executable, str(Path(b.__file__)), '--repo-root', str(self.target)], capture_output=True)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn(b'Unresolved data', p.stderr)
        self.assertEqual(inventory(self.dest), self.original)
        self.assert_clean()

    def test_missing_dependencies_on_refresh_preserves_previous(self):
        self.build(); previous = inventory(self.dest)
        p = subprocess.run([sys.executable, '-S', str(Path(b.__file__)), '--repo-root', str(self.target)], capture_output=True)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn(b'ModuleNotFoundError', p.stderr)
        self.assertEqual(inventory(self.dest), previous)
        self.assert_clean()

    def test_unterminated_frontmatter_preserves_previous(self):
        self.write('content/copilot/bad.md', '---\ntitle: Bad\nmissing delimiter')
        with self.assertRaisesRegex(ValueError, 'unterminated YAML'):
            self.build(self.commit())
        self.assertEqual(inventory(self.dest), self.original)
        self.assert_clean()

    def test_mutable_revision_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'immutable'):
            self.build('main')
        self.assertEqual(inventory(self.dest), self.original)
        self.assertFalse((self.target / '.build-cache').exists())

    def test_unknown_site_algorithm_fails_before_publish(self):
        self.write('src/frame/middleware/context/context.ts', 'changed algorithm')
        with self.assertRaisesRegex(ValueError, 'algorithm changed'):
            self.build(self.commit())
        self.assertEqual(inventory(self.dest), self.original)
        self.assert_clean()

    def test_publish_failure_rolls_back_previous_directory(self):
        stage = self.root / 'staged'; stage.mkdir(); (stage / 'new.md').write_text('new')
        backup = self.root / 'previous'
        original_rename = Path.rename
        def rename(path, target):
            if path == stage:
                raise OSError('simulated destination rename failure')
            return original_rename(path, target)
        with patch.object(Path, 'rename', rename), self.assertRaisesRegex(OSError, 'simulated'):
            b.publish(stage, self.dest, backup)
        self.assertEqual(inventory(self.dest), self.original)
        self.assertFalse(backup.exists())

    def test_existing_lock_preserves_previous_and_lock(self):
        lock = self.dest.parent / '.references-build-lock'; lock.mkdir()
        with self.assertRaises(FileExistsError):
            self.build()
        self.assertTrue(lock.is_dir())
        self.assertEqual(inventory(self.dest), self.original)


if __name__ == '__main__':
    unittest.main()
