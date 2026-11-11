#!/usr/bin/env python3
"""Resolve github/docs Liquid data tags in a tree of markdown files, in place.

Expands loops over data/tables/** (model lists, pricing, feature matrix),
substitutes {% data variables.* %} from data/variables/*.yml, inlines
{% data reusables.* %} from data/reusables/**/*.md, and flattens
{% octicon "name" %} to "(icon: name)". Everything else (ifversion,
codetabs, AUTOTITLE links) is left alone.

Usage: resolve_liquid.py <data-dir> <markdown-root>
"""
import re
import sys
from pathlib import Path

import liquid
import yaml

DATA_TAG = re.compile(r"{%-?\s*data\s+([\w.\-]+)\s*-?%}")
OCTICON_TAG = re.compile(r"{%-?\s*octicon\s+\"([\w\-]+)\"[^%]*-?%}")
ANY_TAG = re.compile(r"{%-?\s*(\w+).*?-?%}", re.DOTALL)
STANDARD_TAGS = {
    "for", "endfor", "if", "elsif", "else", "endif", "unless", "endunless",
    "case", "when", "endcase", "assign", "capture", "endcapture",
    "comment", "endcomment", "raw", "endraw", "break", "continue",
}
EMPTY_ROW = re.compile(r"^\|[\s|]*$")
MAX_PASSES = 10


def load_tables(data_dir):
    def load(path):
        if path.is_dir():
            out = {p.stem: load(p) for p in path.iterdir() if p.is_dir() or p.suffix == ".yml"}
            return out
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    return load(data_dir / "tables")


def render_tables(text, tables):
    """Run pages that loop over data/tables through a real Liquid engine.

    github/docs-only tags (rowheaders, ifversion, data, per-IDE blocks) are
    swapped for placeholders first so the engine doesn't reject them.
    """
    protected = []

    def protect(m):
        if m.group(1) in STANDARD_TAGS:
            return m.group(0)
        protected.append(m.group(0))
        return f"\x00{len(protected) - 1}\x00"

    rendered = liquid.Template(ANY_TAG.sub(protect, text)).render(tables=tables)
    rendered = re.sub(r"\x00(\d+)\x00", lambda m: protected[int(m.group(1))], rendered)
    # Loop wrappers like "| {% for %} |" leave rows of bare pipes behind.
    return "\n".join(l for l in rendered.split("\n") if not EMPTY_ROW.match(l))


def load_variables(data_dir):
    out = {}
    for f in (data_dir / "variables").glob("*.yml"):
        out[f.stem] = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
    return out


def walk(node, parts):
    # Some keys contain dots (e.g. "qwen3.8-flash-next"), so try longer joins too.
    if not parts:
        return node
    if not isinstance(node, dict):
        return None
    for i in range(1, len(parts) + 1):
        key = ".".join(parts[:i])
        if key in node:
            found = walk(node[key], parts[i:])
            if found is not None:
                return found
    return None


def lookup(key, variables, reusables_dir):
    kind, _, rest = key.partition(".")
    if kind == "variables":
        node = walk(variables, rest.split("."))
        return str(node).strip() if node is not None else None
    if kind == "reusables":
        f = reusables_dir.joinpath(*rest.split(".")).with_suffix(".md")
        return f.read_text(encoding="utf-8").strip() if f.is_file() else None
    return None


def resolve_data(text, variables, reusables_dir, missing):
    def sub(m):
        value = lookup(m.group(1), variables, reusables_dir)
        if value is None:
            missing.add(m.group(1))
            return m.group(0)
        if "\n" in value:
            # Keep multi-line reusables inside list items and indented blocks.
            line_start = text.rfind("\n", 0, m.start()) + 1
            prefix = text[line_start:m.start()]
            indent = prefix if prefix.strip() == "" else " " * len(prefix)
            value = value.replace("\n", "\n" + indent)
        return value

    for _ in range(MAX_PASSES):
        new = DATA_TAG.sub(sub, text)
        if new == text:
            break
        text = new
    return text


def resolve(text, variables, reusables_dir, tables, missing):
    # Data first so table loops inside reusables get inlined, then again for
    # data tags carried in by table values.
    text = resolve_data(text, variables, reusables_dir, missing)
    if re.search(r"\btables\.", text):
        text = render_tables(text, tables)
        text = resolve_data(text, variables, reusables_dir, missing)
    return OCTICON_TAG.sub(r"(icon: \1)", text)


def main():
    data_dir, root = Path(sys.argv[1]), Path(sys.argv[2])
    variables = load_variables(data_dir)
    reusables_dir = data_dir / "reusables"
    tables = load_tables(data_dir)
    missing = set()
    files = list(root.rglob("*.md"))
    for f in files:
        original = f.read_text(encoding="utf-8")
        resolved = resolve(original, variables, reusables_dir, tables, missing)
        if resolved != original:
            f.write_text(resolved, encoding="utf-8", newline="\n")
    remaining = sum(len(DATA_TAG.findall(f.read_text(encoding="utf-8"))) for f in files)
    print(f"  -> liquid: {len(files)} files, {remaining} unresolved data tags")
    for key in sorted(missing):
        print(f"    unresolved: {key}")


if __name__ == "__main__":
    main()
