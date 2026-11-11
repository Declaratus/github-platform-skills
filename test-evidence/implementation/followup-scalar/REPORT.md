# Scalar whitespace follow-up to frozen f4db74d

This supplements the preserved original implementation report and results. The starting commit was `f4db74d994b2efaa51d70fb92b6458402e8f59c2` on `fix/copilot-docs-pr1-validation-20261111`. The new local commit retains that candidate as its parent. No original commits were amended, no original reports were overwritten, and no push or merge was performed.

## Finding and correction

The independent reviewer correctly identified one metadata regression: `references/concepts/customizations/plugins.md`, `product`, acquired 55 spaces on each continuation/blank line of the cloud-agent reusable. A decoded YAML scalar entered the resolver's Markdown continuation-indentation logic. The source value's newlines should have been preserved without added padding.

The resolver now explicitly distinguishes scalar substitution from body layout. Both decoded scalar expansion and the original scalar-spelling candidate use scalar mode; nested reusable expansions inherit that mode. The existing Markdown body/list indentation and explicit `indented_data_reference` handling remain intact. Original scalar whitespace is not stripped. A scalar is also not interpreted as a complete frontmatter document merely because its contents start with a frontmatter delimiter.

Three new permanent regression methods assert literal expected values for prefix + multiline reusable (direct and nested), a YAML literal scalar retaining existing indentation, and the same multiline reusable in metadata versus a Markdown list body. These assertions fail against the frozen implementation: **4 failures across 3 test methods**, with no errors. They pass against the repaired implementation. [before-fix-regressions.log](before-fix-regressions.log) runs the frozen source from Git in memory, without checking it out or modifying the current source. The literal-block expectation preserves the value decoded by the existing frontmatter delimiter parser; this repair does not change delimiter parsing.

## Earlier oracle blind spot

The original report's claim that metadata was checked against independently expanded source values was too strong. Its semantic test called the production resolver on decoded source scalars to compute expected values. This avoided the document-level YAML rewrite but **shared the faulty indentation logic**, allowing the same added spaces on both sides of the comparison. The 49 original passing tests therefore did not establish independent source-semantic equivalence. The original candidate had **567/568** correct frontmatters by the independent oracle.

The permanent snapshot test now uses `build/tests/frontmatter_oracle.py`, a separate data-only substitution oracle that never imports or calls the production resolver. It loads pinned upstream YAML variables directly, recursively substitutes reusables without Markdown layout, expands octicons, and preserves deployment condition markers. It fails on unknown metadata macros. It does not claim to implement the full site renderer. The evidence checker also uses its own frontmatter split expression and verifies all 568 source/candidate mappings, independently of the production YAML rewrite.

Only the specifically authorized reviewer evidence and oracle were read. No other reviewer files or sibling evaluator reports were inspected. The review oracle itself was not executed, because its output path would write into the review worktree. The permanent independent oracle and evidence checker were implemented in this worktree.

## Pinned regeneration and results

Upstream is still exactly `github/docs@7c3387d3b513ed43ea26c9b2e4c0e1b12234c010`. No mutable branch was substituted. Installed Python 3.14.3, PyYAML 6.0.3 and python-liquid 2.3.6 were used.

Commands executed from the assigned implementation worktree:

```powershell
python build/lib/rebuild_copilot_docs.py --revision 7c3387d3b513ed43ea26c9b2e4c0e1b12234c010
python test-evidence/implementation/followup-scalar/verify_followup.py
python test-evidence/implementation/run_validation.py followup-scalar
```

The full runner was launched via Python `subprocess.run` with UTF-8 stdout/stderr files and explicit propagation of the child exit code, avoiding PowerShell's native redirection encoding. The runner accepts a label for a separate evidence output directory as well as the separate cold fixture. Original `f4db74d` artifacts remain unchanged.

| Validation | Expected | Actual |
| --- | --- | --- |
| Pinned upstream HEAD | Exact immutable SHA | Match |
| Independent oracle on frozen f4db74d | Reproduce the single plugins.md mismatch | 1 mismatch, same page/key |
| Independent oracle on repaired corpus | All frontmatters equal decoded upstream values | **568/568 match**, 0 errors |
| New literal regressions on frozen resolver | Fail and expose padding | 4 failures in 3 methods, 0 errors |
| Full permanent suite | No failure/error/skip | **52 passed**, 0 failures/errors/skips |
| Full validation runner | All assertions pass, exit 0 | **22 passed**, exit 0 |
| Pinned rebuild and repeat | Exact inventory equality | Pass |
| Fresh real cold fetch/build | Same full reference inventory | Pass |
| Cold-cache refresh | Same full reference inventory | Pass |
| Missing dependency execution | Exit 1 and preserve previous references | Pass |
| Bash syntax, dispatcher/recipe execution | Exit 0 and identical references | Pass |
| Marketplace and plugin validation | Exit 0 | Pass, existing version/icon warnings |
| Whitespace check | No whitespace errors | Pass |
| Failure/cleanup regression coverage | Preserve previous references, no stage/lock debris | Pass |

The permanent suite includes cold/refresh render/import failures, publish rollback, bounded expansion and cycles, table/version/literal combinations, undefined data/table failures and nonzero CLI exits. No global installation or account changes were needed. Fixture stderr includes expected failed-fetch diagnostics from negative tests; these are captured in [validation.stderr.log](validation.stderr.log), not unexpected failures.

Machine-readable results: [followup-results.json](followup-results.json) (6 assertions), [validation-results.json](validation-results.json) (22 assertions and commands), [unittest-results.json](unittest-results.json) (52 tests), and [summary.json](summary.json). Detailed commands/logs and original-PR corpus comparisons are retained alongside this report. [verify_followup.py](verify_followup.py) reproduces the independent comparison and the frozen negative regression. [frozen-oracle-mismatches.json](frozen-oracle-mismatches.json) records the original defect.

## Scope and remaining limits

Relative to frozen `f4db74d`, **567 Markdown pages remain byte-identical and only plugins.md metadata changes**. All **568 page bodies are unchanged**. `SOURCE.json` updates the resolver generator hash. There are no changes to manifests, routing guidance, LICENSE, table output or other plugin content. The code/test/evidence changes are limited to scalar expansion, its independent oracle/regressions and preserving per-run evidence. [scope-results.json](scope-results.json) compares exact frozen Git blob hashes with current bytes, without newline normalization.

Relative to original PR head `875c75bc9c8bbf9f010e16633ef0c25475a3e1b3`, the prior totals remain **531 unchanged / 37 changed Markdown pages**, 35 metadata-only changes and the two previously authorized body fixes. All 15 originally invalid YAML pages still parse. No Markdown pages were added or removed.

No checks are blocked and no unexpected test failures remain. This is local Windows validation using the pinned dependencies and immutable snapshot; it does not establish live product behavior or a cross-platform matrix. Existing rollback/power-loss limitations remain as documented in the original report. Independent review outside this reported metadata finding is still in progress. The next candidate SHA is supplied after the local commit; no further mutation is planned after handoff.

The final staged whitespace check initially identified CRLF in captured stdout and a trailing space in unittest progress output. Those new evidence files were normalized to UTF-8/LF with trailing line whitespace removed; diagnostic string contents and outcomes are unchanged. The staged whitespace check was then repeated before committing.
