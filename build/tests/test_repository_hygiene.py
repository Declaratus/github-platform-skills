"""Fast, dependency-free tests for artifact hygiene and output placement."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

BUILD = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BUILD))
sys.path.insert(0, str(BUILD / 'validation'))
from check_repository_hygiene import artifact_reason, tracked_artifacts
from output_paths import output_directory


class RepositoryHygieneTests(unittest.TestCase):
    def test_generated_artifact_paths_are_rejected(self):
        for path in ['run.log', 'nested/BUILD.LOG', '.build-cache/result.json',
                     'nested/__pycache__/module.pyc', 'build/cache.pyo',
                     'test-evidence/run/results.json', 'test-evidence/run/REPORT.md']:
            with self.subTest(path=path):
                self.assertIsNotNone(artifact_reason(path))

    def test_source_provenance_summary_and_input_fixtures_are_allowed(self):
        for path in ['build/tests/test_snapshot.py', 'build/validation/run_validation.py',
                     'test-evidence/README.md', 'build/tests/fixtures/sample.log',
                     'plugins/example/references/SOURCE.json', 'docs/audit-logs.md']:
            with self.subTest(path=path):
                self.assertIsNone(artifact_reason(path))

    def test_index_guard_catches_force_added_files_but_not_ignored_output(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            def git(*args):
                return subprocess.run(['git', '-C', str(root), *args], check=True, capture_output=True)
            git('init')
            (root / '.gitignore').write_text('*.log\n.build-cache/\n', encoding='utf-8')
            (root / 'build output.log').write_text('generated', encoding='utf-8')
            git('add', '.gitignore')
            self.assertEqual(tracked_artifacts(root), [])
            git('add', '-f', 'build output.log')
            self.assertEqual([p for p, _ in tracked_artifacts(root)], ['build output.log'])
            cli = subprocess.run([sys.executable, str(BUILD / 'check_repository_hygiene.py'),
                                  '--repo-root', str(root)], capture_output=True)
            self.assertEqual(cli.returncode, 1)
            self.assertIn(b'build output.log', cli.stderr)

    def test_run_output_is_ignored_and_existing_run_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            subprocess.run(['git', '-C', str(root), 'init'], check=True, capture_output=True)
            (root / '.gitignore').write_text('.build-cache/\n', encoding='utf-8')
            output = output_directory(root, 'test-123')
            log = output / 'results.json'
            log.write_text('preserved', encoding='utf-8')
            ignored = subprocess.run(['git', '-C', str(root), 'check-ignore', '--',
                                      log.relative_to(root).as_posix()], capture_output=True)
            self.assertEqual(ignored.returncode, 0)
            with self.assertRaises(FileExistsError):
                output_directory(root, 'test-123')
            self.assertEqual(log.read_text(encoding='utf-8'), 'preserved')

    def test_invalid_output_labels_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            for label in ['', '../outside', 'nested/run', 'nested\\run', '.', 'run name']:
                with self.subTest(label=label), self.assertRaises(ValueError):
                    output_directory(Path(temp), label)
            self.assertFalse((Path(temp) / '.build-cache').exists())


if __name__ == '__main__':
    unittest.main()
