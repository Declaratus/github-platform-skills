"""Keep the build dependency pins discoverable by the org dependency audit."""
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]


class DependencyManifestTests(unittest.TestCase):
    def test_root_requirements_includes_the_canonical_build_manifest(self):
        # The required security workflow detects and audits requirements.txt
        # at the repository root. An include avoids duplicating dependency pins.
        entries = [line.strip() for line in (ROOT / 'requirements.txt').read_text(
            encoding='utf-8').splitlines()
            if line.strip() and not line.lstrip().startswith('#')]
        self.assertEqual(entries, ['-r build/requirements.txt'])
        self.assertTrue((ROOT / 'build/requirements.txt').is_file())


if __name__ == '__main__':
    unittest.main()
