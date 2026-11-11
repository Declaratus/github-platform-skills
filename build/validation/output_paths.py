"""Keep generated validation output in a fresh, ignored run directory."""
from pathlib import Path
import re


def output_directory(root: Path, label: str) -> Path:
    if not re.fullmatch(r'[a-zA-Z0-9_-]+', label):
        raise ValueError('Validation label must contain only letters, digits, _ or -')
    root = root.resolve()
    output = root / '.build-cache' / 'validation-results' / label
    # Also reject a pre-existing symlink/junction that redirects outside cache.
    if not output.resolve().is_relative_to(root / '.build-cache'):
        raise ValueError('Validation output must stay in the repository build cache')
    output.mkdir(parents=True, exist_ok=False)
    return output
