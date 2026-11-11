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

### Keep generated validation output out of Git

Commit source, reusable tests and the bundled references/provenance. Raw logs,
per-run JSON results and temporary build files belong in ignored `.build-cache/`.
The concise [validation summary](test-evidence/README.md) records the completed
checks and their limitations.

After staging changes, run the same dependency-free guard used in CI:

```bash
python build/check_repository_hygiene.py
python -m unittest discover -s build/tests -p test_repository_hygiene.py -v
```

The guard checks the Git index, including force-added files. It rejects run logs,
Python caches/compiled output, and raw evidence under `test-evidence/`; only the
curated summary is retained there. Intentionally reviewed **input** log fixtures
may live under `build/tests/fixtures/` (explicitly add them with `git add -f`).
Bundled documentation and `SOURCE.json` remain normal tracked product content.
The `Repository hygiene` workflow runs on pull requests and pushes to `main`.
It reports failures; it does not change repository branch-protection settings.

For the full pinned rebuild validation, after installing the build dependencies
and making the Claude CLI available:

```bash
python build/validation/run_validation.py unique-run-label
# Optional historical regression reproduction, after the pinned rebuild:
python build/validation/verify_scalar_followup.py unique-scalar-label
```

Both scripts write to `.build-cache/validation-results/<label>/` and refuse to
overwrite an existing run. Use a new label for each run. The scalar script is
specific to the original PR regression and requires its historical Git commits;
it is not a general current-version acceptance test. Review output for credentials
and machine-specific paths before sharing it as a CI artifact or review attachment.
Ignoring files does not remove previously committed copies from Git history.


## License

MIT. Bundled upstream content remains under its own license, with attribution in each skill's `SKILL.md`. `github-well-architected` is MIT. `github-copilot-docs` is CC BY 4.0 (GitHub Docs content) and ships the upstream `LICENSE` in its `references/`.

The `github-copilot-docs` recipe needs `python3` with PyYAML and python-liquid to resolve Liquid tags and expand table data (`build/lib/resolve_liquid.py`).

### Reproducible Copilot references

Use Python 3.11 or newer and install the tested build dependencies in an isolated environment:

```bash
python3 -m venv .build-cache/venv
.build-cache/venv/bin/python -m pip install -r build/requirements.txt
PYTHON=.build-cache/venv/bin/python ./build/build.sh github-copilot-docs
```

`build/requirements.txt` is the canonical dependency list. The root
`requirements.txt` includes it so the org-required `org/security-baseline`
workflow detects Python and runs `pip-audit` against the build dependencies
and their resolved transitive dependencies. Keep pins in the build manifest
only. CI checks that the root entry point still includes it. A successful
workflow means its configured audit policy passed, not that no vulnerabilities
exist; inspect the audit step and its summary for findings and warnings.

On Windows, use `.build-cache/venv/Scripts/python.exe`, or run the Python entry point directly:

```powershell
python build/lib/rebuild_copilot_docs.py
python build/lib/rebuild_copilot_docs.py --revision 7c3387d3b513ed43ea26c9b2e4c0e1b12234c010
python -m unittest discover -s build/tests -v
```

The default revision is pinned in `build/copilot-docs-source.json`; overrides must be full immutable commit SHAs. This recipe never substitutes mutable `main`. It sparsely fetches the content, data and REST context sources, resolves into a disposable workspace under `.build-cache/github-copilot-docs-staging/`, validates every page, then publishes with rollback if replacement fails. Both the staged corpus and the previous-corpus backup stay outside the packaged plugin. The workspace and destination must share a filesystem; a cross-filesystem layout is rejected before fetching or publication. Missing dependencies, fetch, rendering or validation errors exit nonzero and leave the previous references untouched. An empty `plugins/github-copilot-docs/skills/github-copilot-docs/.references-build-lock` directory prevents concurrent replacements. Builds never adopt or remove another run's abandoned workspace or lock; use the interrupted-build recovery procedure below. Publication uses two directory renames, so readers may briefly observe a missing destination; it is not a transaction against power loss or filesystem failure during rollback.

`references/SOURCE.json` records the upstream commit and commit date, generator hashes, dependency versions, authoritative REST context sources and page count. It intentionally omits wall-clock timestamps so identical inputs give identical output. Review that provenance when assessing freshness. Updating the pin and reviewing the regenerated diff is an explicit maintenance action.

The resolver preserves deployment alternatives and literal raw blocks, rejects missing data, undefined table output/iteration, reusable cycles and expansion beyond 64 nested inclusions or 8 MB. Optional matrix `notApplicable` lists alone default to empty, matching upstream semantics. Other optional fields may be tested for truthiness; they cannot be printed or iterated when undefined. Unsupported source changes should fail for review, not produce an apparently successful partial snapshot.


### Recovering an interrupted Copilot reference build

Run these steps from the repository root. A hard termination bypasses normal cleanup and may leave an empty lock plus `.build-cache/github-copilot-docs-staging/.references-stage-<unique-id>/`. This ignored workspace can contain `references/` (the new staged corpus), `previous/` (the old published corpus during replacement), and `BUILD.json` (PID, resolved destination and upstream revision). It is not bundled plugin content. Successful builds and handled failures clean up only their own workspace. Retrying a build does not remove earlier leftovers.

1. Establish that the interrupted process has exited and no other build for this checkout is running. Inspect each workspace's `BUILD.json` and the original process/command when available; a PID alone is insufficient because it can be reused. Do not remove a lock or workspace belonging to an active or uncertain run.
2. Inspect `plugins/github-copilot-docs/skills/github-copilot-docs/references/` and each relevant workspace before deleting anything. Check `SOURCE.json`, the pinned revision, page count and validation results. If the published destination is absent or suspect, preserve all corpora. An intact `previous/` may be the only good snapshot: after confirming ownership and that the destination is absent, restore that exact directory by a same-filesystem rename to the destination, without overwriting an existing directory. If there are multiple possible backups or ownership is unclear, stop and retain them for investigation.
3. Once the previous good destination is confirmed and the stopped run's lock is known to be stale, remove only that **empty** lock. For example, the following refuses to remove a nonempty directory:

   ```powershell
   python -c "from pathlib import Path; Path('plugins/github-copilot-docs/skills/github-copilot-docs/.references-build-lock').rmdir()"
   ```

4. Retry `python build/lib/rebuild_copilot_docs.py` at the pin and validate the resulting references. The builder uses a fresh workspace and leaves abandoned ones untouched. Only after confirming the published snapshot is good and that no backup is needed, remove the individually inspected abandoned workspace by its exact absolute path. Do not delete the entire staging/cache directory or use wildcard deletion; it can contain other runs' data. You may retain the workspace for diagnosis instead.

Older builder versions placed `.references-stage-<unique-id>/` beside `SKILL.md`, inside the packaged skill. Those legacy leftovers are not migrated or deleted automatically. Apply the same ownership, corpus/backup inspection and exact-path cleanup procedure to each legacy workspace so it cannot be mistaken for bundled references.

A hard termination **during the two-rename publish gap has not been tested**. The pre-publication termination regression verifies preservation of the old references and isolation of the abandoned complete staged corpus; it does not establish power-loss recovery. Preserve backups if publication was interrupted, and do not assume the existence of a lock identifies which rename completed.
