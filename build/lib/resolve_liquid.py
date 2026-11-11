#!/usr/bin/env python3
"""Resolve supported github/docs data, retaining literal and deployment templates."""
import json
import re
import sys
from pathlib import Path

import liquid
import yaml

DATA_TAG = re.compile(r"{%-?\s*data\s+([\w.\-]+)\s*-?%}")
INDENTED_TAG = re.compile(r"{%-?\s*indented_data_reference\s+([\w.\-]+)\s+spaces=(\d+)\s*-?%}")
OCTICON_TAG = re.compile(r'{%-?\s*octicon\s+"([\w\-]+)"[^%]*-?%}')
TOKEN = re.compile(r"{%-?\s*(\w+)\b(.*?)-?%}|{{-?\s*(.*?)\s*-?}}", re.S)
RAW = re.compile(r"{%-?\s*raw\s*-?%}.*?{%-?\s*endraw\s*-?%}", re.S)
FENCE = re.compile(r'(?m)^([ \t]*)(`{3,}|~{3,})(?![`~])[^\n]*\n.*?^\1\2[ \t]*(?:\n|$)', re.S)
FRONT = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", re.S)
MAX_DEPTH = 64
MAX_SIZE = 8_000_000


class ResolutionError(ValueError):
    """An incomplete source must not replace good references."""


def load_tables(data_dir):
    def load(path):
        if path.is_dir():
            return {p.stem: load(p) for p in sorted(path.iterdir()) if p.is_dir() or p.suffix == '.yml'}
        return yaml.safe_load(path.read_text(encoding='utf-8'))
    tables = load(data_dir / 'tables')
    # The upstream matrix intentionally omits this optional list when empty.
    # Default this one known field, not arbitrary undefined table paths.
    for ide in tables.get('copilot', {}).get('matrix', {}).values():
        if isinstance(ide, dict):
            ide.setdefault('notApplicable', [])
    return tables


def load_variables(data_dir):
    return {p.stem: yaml.safe_load(p.read_text(encoding='utf-8')) or {}
            for p in sorted((data_dir / 'variables').glob('*.yml'))}


def walk(node, parts):
    if not parts:
        return node
    if isinstance(node, dict):
        for i in range(1, len(parts) + 1):
            key = '.'.join(parts[:i])
            if key in node:
                found = walk(node[key], parts[i:])
                if found is not None:
                    return found
    return None


def lookup(key, variables, reusables_dir):
    kind, _, rest = key.partition('.')
    if kind == 'variables':
        value = walk(variables, rest.split('.'))
        return str(value).strip() if value is not None else None
    if kind == 'reusables':
        path = reusables_dir.joinpath(*rest.split('.')).with_suffix('.md')
        if path.is_file():
            return path.read_text(encoding='utf-8').strip()
    return None


def site_context(upstream):
    """Mirror the upstream default (oldest configured FPT version), not latest.

    Fail for algorithm changes rather than silently guessing an API date.
    """
    context = (upstream / 'src/frame/middleware/context/context.ts').read_text(encoding='utf-8')
    versions = (upstream / 'src/versions/lib/all-versions.ts').read_text(encoding='utf-8')
    if ('defaultRestApiVersion = apiVersions[apiVersions.length - 1]' not in context
            or 'apiVersions[key].sort().reverse()' not in versions
            or 'nonEnterpriseDefault: true' not in versions
            or "plan: 'free-pro-team'" not in versions):
        raise ResolutionError('Upstream REST default algorithm changed; review site_context')
    config = json.loads((upstream / 'src/rest/lib/config.json').read_text(encoding='utf-8'))
    dates = config['api-versions']['fpt']
    if not dates or not all(re.fullmatch(r'\d{4}-\d{2}-\d{2}', d) for d in dates):
        raise ResolutionError('Invalid upstream REST version data')
    return {'defaultRestApiVersion': sorted(dates)[0]}


def render_tables(text, tables):
    """Evaluate table-dependent code; protect other outputs and version markers.

    Track conditional nesting so else/endif belonging to ifversion never reach
    Liquid, while ordinary row conditions still execute normally.
    """
    roots = {'tables', 'forloop'}
    loop_names = set()
    tokens = list(TOKEN.finditer(text))
    def depends(expr, allowed=None):
        expr = re.sub(r"'[^']*'|\"[^\"]*\"", '', expr)
        return any(re.search(r'(?<![\w.])' + re.escape(r) + r'(?![\w-])', expr) for r in (roots if allowed is None else allowed))
    # Alias closure handles table-derived assignments used later in the page.
    for _ in range(len(tokens) + 1):
        before = len(roots)
        for m in tokens:
            name, args, output = m.groups()
            if name == 'assign' and '=' in args:
                roots.add(args.split('=', 1)[0].strip())
            elif name == 'for' and ' in ' in args and depends(args.split(' in ', 1)[1]):
                var = args.split(' in ', 1)[0].strip()
                roots.add(var)
                loop_names.add(var)
        if len(roots) == before:
            break
    protected = []
    stack = []
    active = False
    def protect(s):
        protected.append(s)
        return f'\x00DOCS{len(protected)-1}\x00'
    def sub(m):
        nonlocal active
        name, args, output = m.groups()
        scoped = (roots - loop_names - {'forloop'}) | {entry[3] for entry in stack if entry[1] and entry[3]}
        if any(entry[0] == 'for' and entry[1] for entry in stack):
            scoped.add('forloop')
        if output is not None:
            return m.group() if depends(output, scoped) else protect(m.group())
        if name in ('if', 'unless', 'case', 'for', 'ifversion', 'comment', 'capture'):
            execute = name != 'ifversion' and (depends(args, scoped) or active or name == 'comment')
            var = args.split(' in ', 1)[0].strip() if name == 'for' else None
            stack.append((name, execute, active, var))
            active = active if name == 'ifversion' else execute
            return m.group() if execute else protect(m.group())
        if name in ('else', 'elsif', 'when'):
            return m.group() if stack and stack[-1][1] else protect(m.group())
        if name in ('endif', 'endunless', 'endcase', 'endfor', 'endcomment', 'endcapture'):
            if not stack:
                raise ResolutionError(f'Unmatched {name}')
            opening, execute, previous, var = stack.pop()
            expected = 'endif' if opening == 'ifversion' else 'end' + opening
            if name != expected:
                raise ResolutionError(f'Mismatched {opening}/{name}')
            active = previous
            return m.group() if execute else protect(m.group())
        if name == 'assign':
            return m.group() if depends(args) or active else protect(m.group())
        if name in ('break', 'continue') and active:
            return m.group()
        return protect(m.group())
    source = TOKEN.sub(sub, text)
    if stack:
        raise ResolutionError(f'Unclosed block: {stack[-1][0]}')
    # Optional field truthiness tests are valid. Undefined output/iteration is
    # an error, so a misspelled model table never silently disappears.
    env = liquid.Environment(undefined=liquid.FalsyStrictUndefined)
    env.loop_iteration_limit = 100_000
    env.output_stream_limit = MAX_SIZE
    rendered = env.from_string(source).render(tables=tables)
    return re.sub(r'\x00DOCS(\d+)\x00', lambda m: protected[int(m[1])], rendered)


def resolve(text, variables, reusables_dir, tables, missing=None, context=None, *, scalar=False):
    """Expand docs macros, with continuation indentation only for page bodies.

    Decoded YAML strings already carry their semantic whitespace. Reusable
    substitution in those strings must not add Markdown continuation padding,
    including inside nested reusables or the candidate YAML spelling.
    """
    protected = []
    def raw(m):
        protected.append(m.group())
        return f'\x00RAW{len(protected)-1}\x00'
    def expand(s, chain=()):
        if len(chain) > MAX_DEPTH:
            raise ResolutionError('Reusable nesting exceeds 64: ' + ' -> '.join(chain))
        s = RAW.sub(raw, s)
        def data(m):
            key = m[1]
            if key in chain:
                raise ResolutionError('Reusable cycle: ' + ' -> '.join((*chain, key)))
            value = lookup(key, variables, reusables_dir)
            if value is None:
                if missing is not None:
                    missing.add(key)
                raise ResolutionError('Unresolved data: ' + key)
            value = expand(value, (*chain, key))
            if m.re is INDENTED_TAG:
                indent = ' ' * int(m[2])
                return indent + value.replace('\n', '\n' + indent)
            if not scalar and '\n' in value:
                prefix = s[s.rfind('\n', 0, m.start()) + 1:m.start()]
                indent = prefix if not prefix.strip() else ' ' * len(prefix)
                value = value.replace('\n', '\n' + indent)
            return value
        s = INDENTED_TAG.sub(data, s)
        s = DATA_TAG.sub(data, s)
        if len(s) > MAX_SIZE:
            raise ResolutionError('Expanded page exceeds 8 MB')
        return s
    def body(s):
        s = expand(s)
        if re.search(r'{%-?\s*(?:data|indented_data_reference)\b', s):
            raise ResolutionError('Unsupported or malformed data inclusion')
        for key, value in (context or {}).items():
            s = re.sub(r'{{-?\s*' + re.escape(key) + r'\s*-?}}', lambda _: str(value), s)
        if re.search(r'{{\s*defaultRestApiVersion\s*}}', s):
            raise ResolutionError('defaultRestApiVersion requires upstream site context')
        s = OCTICON_TAG.sub(r'(icon: \1)', s)
        # Docs macros inside examples expand, but example Liquid is not a
        # program. Mask fences before interpreting table code elsewhere.
        s = FENCE.sub(raw, s)
        s = re.sub(r'(\s*){%(-)?\s*comment\s*-?%}.*?{%-?\s*endcomment\s*(-)?%}(\s*)',
                   lambda m: ('' if m[2] else m[1]) + ('' if m[3] else m[4]), s, flags=re.S)
        if re.search(r'(?:{%-?\s*(?:for|assign)\b[^%]*|{{[^}]*?)\btables[.\[]', s):
            # Remove only explicit loop-wrapper pipes, never unrelated rows.
            s = re.sub(r'^\|[ \t]*((?:{%-?\s*(?:for|endfor|if|endif|elsif|else|case|when|endcase)\b[^%]*%}[ \t]*)+)\|[ \t]*(?:\n|$)',
                       lambda m: ''.join(t.group() for t in TOKEN.finditer(m[1])), s, flags=re.M)
            s = render_tables(s, tables)
            s = expand(s)
        return OCTICON_TAG.sub(r'(icon: \1)', s)
    front = None if scalar else FRONT.match(text)
    if front:
        source = front[1]
        tree = yaml.compose(source)
        replacements = []
        def visit(node):
            if isinstance(node, yaml.ScalarNode) and node.tag == 'tag:yaml.org,2002:str':
                value = resolve(node.value, variables, reusables_dir, tables, missing, context, scalar=True)
                if value != node.value:
                    start, end = node.start_mark.index, node.end_mark.index
                    suffix = '\n' if source[start:end].endswith('\n') else ''
                    replacement = json.dumps(value, ensure_ascii=False) + suffix
                    # Retain author formatting when expansion of the original
                    # scalar spelling parses to the exact intended string.
                    # Otherwise JSON quoting is a YAML-safe string encoding.
                    candidate = resolve(source[start:end], variables, reusables_dir, tables, missing, context, scalar=True)
                    try:
                        if yaml.safe_load('value: ' + candidate) == {'value': value}:
                            replacement = candidate
                    except yaml.YAMLError:
                        pass
                    replacements.append((start, end, replacement))
            elif isinstance(node, yaml.MappingNode):
                for key, value in node.value:
                    visit(key); visit(value)
            elif isinstance(node, yaml.SequenceNode):
                for value in node.value:
                    visit(value)
        visit(tree)
        for start, end, value in sorted(replacements, reverse=True):
            source = source[:start] + value + source[end:]
        text = '---\n' + source + '\n---\n' + body(text[front.end():])
    else:
        text = body(text)
    for _ in range(len(protected) + 1):
        restored = re.sub(r'\x00RAW(\d+)\x00', lambda m: protected[int(m[1])], text)
        if restored == text:
            break
        text = restored
    if front:
        yaml.safe_load(FRONT.match(text)[1])
    return text


def resolve_tree(data_dir, root, context):
    variables = load_variables(data_dir)
    tables = load_tables(data_dir)
    outputs = {}
    for path in sorted(root.rglob('*.md')):
        try:
            original = path.read_text(encoding='utf-8')
            if not FRONT.match(original):
                raise ResolutionError('Missing or unterminated YAML frontmatter')
            outputs[path] = resolve(original, variables, data_dir / 'reusables', tables, context=context)
            metadata = yaml.safe_load(FRONT.match(outputs[path])[1])
            if not isinstance(metadata, dict) or not isinstance(metadata.get('title'), str):
                raise ResolutionError('Frontmatter must be a mapping with a string title')
        except Exception as exc:
            raise ResolutionError(f'{path}: {exc}') from exc
    # Validate all pages before changing any file, even in the disposable tree.
    for path, text in outputs.items():
        path.write_text(text, encoding='utf-8', newline='\n')
    print(f'  -> liquid: {len(outputs)} files, 0 unresolved data tags')


def main():
    data_dir, root = map(Path, sys.argv[1:3])
    resolve_tree(data_dir, root, site_context(data_dir.parent))


if __name__ == '__main__':
    main()
