"""Independent data-only oracle for decoded upstream metadata.

Intentionally does not import the renderer: no body layout or YAML rewriting
is involved. Unknown macros fail so unsupported source cannot silently pass.
"""
import re
from pathlib import Path

DATA = re.compile(r"{%-?\s*data\s+([\w.\-]+)\s*-?%}")
OCTICON = re.compile(r'{%-?\s*octicon\s+"([\w\-]+)"[^%]*-?%}')


def metadata_oracle(node, variables, reusables):
    def variable(parts, value):
        if not parts:
            return value
        if isinstance(value, dict):
            for length in range(len(parts), 0, -1):
                key = '.'.join(parts[:length])
                if key in value:
                    return variable(parts[length:], value[key])
        raise KeyError('.'.join(parts))

    def expand(text, chain=()):
        def substitute(match):
            key = match[1]
            if key in chain or len(chain) >= 64:
                raise ValueError('Unbounded metadata inclusion: ' + key)
            kind, rest = key.split('.', 1)
            if kind == 'variables':
                value = str(variable(rest.split('.'), variables)).strip()
            elif kind == 'reusables':
                value = Path(reusables).joinpath(*rest.split('.')).with_suffix('.md').read_text(encoding='utf-8').strip()
            else:
                raise ValueError('Unknown metadata inclusion: ' + key)
            return expand(value, (*chain, key))
        text = DATA.sub(substitute, text)
        text = OCTICON.sub(r'(icon: \1)', text)
        retained = re.sub(r'{%-?\s*(?:ifversion\b[^%]*|else|endif)\s*-?%}', '', text)
        if '{%' in retained or '{{' in retained:
            raise ValueError('Unsupported metadata template: ' + text)
        return text

    if isinstance(node, str):
        return expand(node)
    if isinstance(node, list):
        return [metadata_oracle(x, variables, reusables) for x in node]
    if isinstance(node, dict):
        return {metadata_oracle(k, variables, reusables): metadata_oracle(v, variables, reusables)
                for k, v in node.items()}
    return node
