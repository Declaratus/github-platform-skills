# github-platform-skills

Claude Code marketplace of skills for working with GitHub at the **platform / organization level** — well-architected guidance, rulesets, governance, scaling, migrations. Not for everyday repo work; for "how should this org use GitHub" decisions.

## Install

```bash
/plugin marketplace add Declaratus/github-platform-skills
/plugin install github-well-architected@github-platform-skills
/reload-plugins
```

Then ask Claude anything that fits the skill's scope (organization-level decisions about GitHub) and it will load the relevant content automatically.

## Available plugins

| Plugin | What it gives Claude |
|---|---|
| [`github-well-architected`](plugins/github-well-architected/) | The five pillars + recommendations from [github/github-well-architected](https://github.com/github/github-well-architected). Use for ruleset design, GHAS rollout, polyrepo vs monorepo, ADO migrations, governance policies. |
| [`github-copilot-docs`](plugins/github-copilot-docs/) | The full Copilot section of [GitHub Docs](https://docs.github.com/en/copilot) (`content/copilot` from [github/docs](https://github.com/github/docs)). Use for Copilot policies, billing and budgets, models, content exclusion, MCP, cloud agent, CLI, customization, metrics. |

## Repo layout

```
.
├── .claude-plugin/marketplace.json       # lists every plugin in this marketplace
├── plugins/<plugin-name>/
│   ├── .claude-plugin/plugin.json        # plugin manifest
│   └── skills/<skill-name>/
│       ├── SKILL.md                      # hand-edited source-of-truth
│       └── references/                   # curated from upstream by build/recipes/
├── build/
│   ├── build.sh                          # dispatch: ./build/build.sh <plugin> [--all]
│   └── recipes/<plugin-name>.sh          # per-plugin: upstream URL + curation
└── .build-cache/                         # gitignored: shallow clones of upstream
```

## Adding a new skill

1. Pick a plugin name (kebab-case, e.g. `github-actions-security`).
2. Create the plugin scaffold:
   ```bash
   mkdir -p plugins/<name>/.claude-plugin
   mkdir -p plugins/<name>/skills/<name>
   ```
3. Write `plugins/<name>/.claude-plugin/plugin.json` (use `github-well-architected`'s as a template).
4. Write `plugins/<name>/skills/<name>/SKILL.md` — the hand-edited source-of-truth. The YAML `description` field is what Claude uses to decide when to load the skill; be specific about triggers.
5. If the skill bundles content from an upstream repo, add `build/recipes/<name>.sh` (copy the well-architected recipe and adapt the upstream URL + curation rules).
6. Add the plugin entry to `.claude-plugin/marketplace.json`.
7. Run `claude plugin validate .` to sanity-check.
8. Commit and push.

## Rebuilding references from upstream

```bash
./build/build.sh github-well-architected     # rebuild one
./build/build.sh --all                       # rebuild every plugin with a recipe
```

The build script:
- shallow-clones (or refreshes) the upstream into `.build-cache/<name>/`
- restages the curated subset under `plugins/<name>/skills/<name>/references/`
- never touches `SKILL.md`

`git diff` after a rebuild shows exactly what upstream changed in the references — review before committing.

## Validate before pushing

```bash
claude plugin validate .
```

Checks `marketplace.json` syntax, plugin names, source paths, and version coherence.

## License

MIT. Bundled upstream content remains under its own license, with attribution in each skill's `SKILL.md`. `github-well-architected` is MIT. `github-copilot-docs` is CC BY 4.0 (GitHub Docs content) and ships the upstream `LICENSE` in its `references/`.

The `github-copilot-docs` recipe needs `python3` with PyYAML and python-liquid to resolve Liquid tags and expand table data (`build/lib/resolve_liquid.py`).
