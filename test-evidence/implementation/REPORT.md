# PR #1 local implementation candidate

Parent: `875c75bc9c8bbf9f010e16633ef0c25475a3e1b3`. Branch: `fix/copilot-docs-pr1-validation-20261111`. Original comparison base: `9840fe3668b2b3e3aac33817295d18b4056331e1`. Upstream: `github/docs@7c3387d3b513ed43ea26c9b2e4c0e1b12234c010`.

All work was performed in the assigned `.fix/impl` worktree. No original reports or other evaluators' files were read or overwritten. Original commits remain ancestors; no amend, push, PR comment, deployment, account change, global installation or Security scan was performed. The initially reported modified working-tree page had no content diff after Git refreshed its status; no pre-existing content change was discarded.

## Implementation and design choices

The chosen repair retains a small Python resolver and Bash dispatcher. Alternatives considered were patching quotes with regex alone (cannot preserve YAML scalar semantics) or running the full upstream site renderer (substantially more dependencies and deployment-specific behavior). The implementation instead expands decoded YAML string scalars, preserves their original spelling when semantically safe, and otherwise encodes strings with YAML-compatible JSON quoting. Ordinary metadata types, Unicode, quotes and multiline values survive. Full metadata semantics are compared against decoded pinned source values for all 568 pages, including every one of the 15 previously invalid outputs.

The table interpreter protects deployment delimiters with nesting-aware markers, evaluates table-dependent outputs and scoped loop variables, and preserves unrelated templates and fenced/raw examples. Empty wrapper rows are removed at their source control-tag lines rather than deleting arbitrary output rows. Missing data, malformed inclusions, undefined table output/iteration, cycles, more than 64 nested expansions, and output over the configured 8 MB expansion limit fail with a page-specific diagnostic. The matrix's explicitly optional `notApplicable` list alone defaults to empty; optional truthiness tests are permitted. Literal comment examples in fences/raw blocks remain literal; author-only comments are removed with their whitespace controls respected.

The three `indented_data_reference` inclusions are generated from the pinned Java reusable. Four `defaultRestApiVersion` expressions are generated from pinned `src/rest/lib/config.json`, following the pinned site context's oldest-configured-FPT rule in `src/frame/middleware/context/context.ts` and `src/versions/lib/all-versions.ts`. This is not a guessed date or an assumption that the newest API version is the default. Changes to the recognized site algorithm fail for review.

The rebuild imports dependencies first, fetches only an immutable full SHA, stages the complete snapshot, resolves/validates every page, writes deterministic provenance, and publishes via sibling renames with rollback. Prior references remain intact on dependency, fetch, rendering or validation errors. Staging directories and locks are cleaned on handled failures; a concurrent build's lock is not removed. The upstream cache intentionally survives failures for retry. Both direct Python and the original Bash dispatcher are supported; the dispatcher now forwards pinned-revision arguments. Git long-path/EOL settings are command-scoped, not global.

`build/copilot-docs-source.json` supplies the default pin; `--revision <full SHA>` is the supported override. `build/requirements.txt` pins the tested Python packages. `references/SOURCE.json` records immutable revision, upstream commit date, inputs, authoritative API sources, dependency versions and LF-normalized generator hashes. No wall-clock field is included, so a repeat build produces the same bytes. LICENSE is read as the exact upstream Git blob.

SKILL now routes customization semantics through the actual concepts and surface-support pages, distinguishes CLI/VS Code instruction combination from GitHub.com Chat precedence, separates hook schemas/environments, describes redirect aliases, and tells readers how to use snapshot provenance/freshness. No ephemeral price guidance or unsupported live behavior was added.

## Regenerated corpus and scope checks

- **568 Markdown pages remain; no pages added or removed.**
- **531 Markdown pages are byte-identical to the original PR Git blobs; 37 changed.**
- **35 pages have metadata-only changes.** These repair invalid quoting or preserve actual multiline reusable values instead of relying on YAML's accidental folding.
- Only two bodies change: `how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions.md` (three authoritative code inclusions) and `how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-via-the-api.md` (four authoritative API header substitutions). The latter also has repaired multiline metadata.
- All existing table bodies, including pricing, model support and feature matrices, remain byte-identical. LICENSE remains byte-identical. SOURCE.json is the only added reference file.
- All 568 generated frontmatters parse. All decoded metadata matches the independently expanded source scalar values. All pages are idempotent through the resolver. No active data inclusions, table loops or default-API placeholders remain outside literal raw blocks.
- Changes outside the Copilot plugin are limited to the rebuild machinery, dependencies, tests, README, Python-bytecode ignore rule and this new evidence directory. The well-architected plugin and marketplace contents are unchanged.

See [corpus-comparison.json](corpus-comparison.json) for every preserved/changed path and all 15 original YAML errors.

## Commands and results

Environment: Python 3.14.3, PyYAML 6.0.3, python-liquid 2.3.6, Git Bash, Claude Code 2.1.322. Installed dependencies were used; no packages were installed globally.

Final validation command:

```powershell
python test-evidence/implementation/run_validation.py final
```

The runner executes these checks, captures command output and raises nonzero on any failed assertion. A real cold-build fixture is retained under `.build-cache/validation-cold-root-final`; repeat the whole validation with a new label to preserve the existing fixture. Permanent tests use temporary directories under this worktree's ignored `.build-cache/test-temp` and clean them afterward.

| Command/check | Result |
| --- | --- |
| `python -m unittest discover -s build/tests -v` | **49 passed, 0 failures/errors/skips**; final runner uses the same discovery with JSON reporting |
| `python build/lib/rebuild_copilot_docs.py --revision 7c3387d3b513ed43ea26c9b2e4c0e1b12234c010` twice | Both succeed; exact byte idempotence including provenance |
| Same builder against a new fixture `--repo-root` | Real GitHub cold fetch/build succeeds; full byte equivalence with primary build |
| Refresh that fixture's cache/build | Succeeds; full byte equivalence |
| `python -S build/lib/rebuild_copilot_docs.py` | Expected import failure, exit 1; all previous 568 pages and metadata unchanged |
| Bash `-n` for dispatcher and recipe | Pass |
| `PYTHON=<installed Python> bash build/build.sh github-copilot-docs --revision <pin>` | Pass; byte-identical output to Python entry point |
| `claude plugin validate .` | Pass; existing missing-version warnings only |
| `claude plugin validate ./plugins/github-copilot-docs` | Pass; nonblocking version/listing-icon warnings |
| `git -c core.longpaths=true -c core.autocrlf=false diff --check` | Pass |
| Full original Git blob/body/path/license comparison | Pass; only intended body changes and one provenance file |
| Post-success/failure staging and lock inspection | Pass; no staging debris |

The permanent suite additionally exercises cold/refresh render failures, invalid YAML and missing delimiters, undefined table failures, import failures on both paths, failed fetches, publish-rename rollback, lock contention, mutable revision rejection, changed upstream API-default algorithms, bounded reusable recursion, raw/fenced literals, dotted keys, Unicode/multiline quoting, nested version/table combinations, and valid ordinary tables. Failure assertions verify previous reference bytes, not merely exception messages. CLI rendering failures have nonzero exits.

There are **22 passing validation assertions**, separate from the **49 passing permanent tests**. Machine-readable outcomes: [validation-results.json](validation-results.json), [unittest-results.json](unittest-results.json), and [summary.json](summary.json). Commands, return codes and expected/actual values are retained. Large directory comparisons are represented by deterministic SHA-256 inventory digests and file counts.

PowerShell's treatment of native stderr redirection initially reported a shell failure despite a completed successful Python validation. The final invocation explicitly propagated `$LASTEXITCODE` and returned **0**. Native Git fixture progress/warnings are retained in validation.stderr.log; they are not suite failures. An early full-source build exposed a Windows default-codepage decoding error before publication; Git output is now decoded explicitly as UTF-8 and a Unicode license regression covers it. An API test initially counted the three already-literal headers as new replacements; its expectation now compares original occurrences plus the four source placeholders. These were corrected before the candidate was committed.

## Limits and handoff

The pipeline intentionally supports the bundled github/docs dialect rather than the entire site renderer. Unknown upstream default-version logic or unresolved supported constructs fail for review. Literal templates in raw/fenced examples are preserved intentionally, not treated as unresolved build failures. Dependency testing covers the pinned package versions on the installed Windows Python; no cross-platform/version matrix or live GitHub product/account behavior is claimed.

Directory replacement is rollback-protected for handled filesystem errors, not a power-loss transaction. There is a brief rename gap for readers. A killed process can leave a lock/staging directory for inspection; README documents that limitation. No global settings were changed to avoid it.

This local candidate is ready for the independently assigned sessions to test at its exact commit. The final candidate SHA is reported separately after committing, to avoid a self-referential hash inside its own committed report. No push is authorized or performed.
