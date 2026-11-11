# R2 interrupted-build workspace repair

This is a narrow supplement to the preserved scalar follow-up and original reports. Starting/frozen parent: `b8e4636e546167f8aba832a5972cc4b3645cf7b2`. `f4db74d994b2efaa51d70fb92b6458402e8f59c2` and the author commits remain in history. A new local commit is created for this change; no amend, push, merge, account change, global plugin installation or security scan is performed. Work stays in the assigned implementation worktree.

## Finding and design

R2 (Low) is valid: the older builder's temporary staging directory was under the packaged skill. A process exit bypassing cleanup after staging left a complete corpus there. Removing only the empty lock allowed a later build but did not remove the abandoned corpus, which could be mistaken for bundled references. The specifically authorized `kill-leftover-repro.txt` was inspected for this repair. No unrelated review findings were pursued.

`build/lib/rebuild_copilot_docs.py` now puts every disposable staged corpus and old-corpus backup under `.build-cache/github-copilot-docs-staging/.references-stage-<unique-id>/`, outside the plugin and covered by the existing `.build-cache/` ignore. Before fetching or publication it checks that the workspace and destination parent share the same filesystem (`st_dev`); a different filesystem raises an error without touching existing references. Publication still uses directory renames and rollback, with no copy fallback.

Each workspace has a `BUILD.json` containing its PID, resolved destination and immutable revision for recovery inspection. This transient file is not in the published references or deterministic provenance. The existing empty per-checkout lock remains in place to serialize builds. No build adopts or deletes a previous run's lock or workspace. Normal success and handled failures clean only that run's temporary directory.

README now documents exact current and legacy leftover locations, ownership/process checks, backup preservation and same-filesystem restoration when the destination is absent. It gives an empty-directory-only lock removal command and requires inspecting a specific workspace before any cleanup. It explicitly warns against wildcard/cache-wide deletion or treating a PID alone as proof of ownership. Legacy packaged leftovers are not migrated or deleted automatically.

## Regression evidence

Three permanent regression methods were added to `build/tests/test_rebuild.py`:

| Test | Result |
| --- | --- |
| `test_interrupted_568_page_stage_outside_package_and_safe_recovery` | PASS: real child process exits 9 via `os._exit` after resolving a 568-page fixture and writing provenance, immediately before publish. Old references and the plugin's Git untracked-file listing are unchanged; no staged corpus is under the packaged skill. The complete abandoned corpus and BUILD.json are outside the plugin. Retry refuses the existing lock and preserves its data. After the test confirms the child has exited and removes only its empty fixture lock, refresh succeeds without changing the abandoned workspace. |
| `test_stage_and_backup_are_outside_package_on_same_filesystem` | PASS: stage and backup share an external workspace on the destination filesystem; the prior references wait there until successful cleanup. |
| `test_cross_filesystem_workspace_fails_before_fetch_or_publish` | PASS: an injected device mismatch fails before any Git call; published bytes remain unchanged and no stage/lock is left. This is a simulated device mismatch, not a physical second-volume test. |

Existing cleanup assertions now inspect both the packaged skill and the external staging area. Failure-safety, rename rollback, concurrency-lock, cold/refresh failure and missing-dependency tests remain enabled.

## Full validation and regenerated scope

Commands from the assigned worktree:

```powershell
python -m unittest discover -s build/tests -p test_rebuild.py -v
python test-evidence/implementation/run_validation.py followup-r2
```

The focused rebuild suite passed **17/17**. Full validation passed **55 permanent tests**, with **0 failures, errors or skips**, and **22 pipeline assertions**, exit **0**. The full runner regenerated twice at immutable `github/docs@7c3387d3b513ed43ea26c9b2e4c0e1b12234c010`, performed a real fresh cold fetch/build and refresh, checked full-byte equality/idempotence, exercised an actual missing-dependency failure, ran Bash syntax and the pinned dispatcher, validated marketplace/plugin manifests, and checked corpus scope, license and lock/workspace cleanup. The permanent snapshot test retains the independent metadata oracle added by the scalar repair; all 568 frontmatters match upstream values.

The cold fixture is `.build-cache/validation-cold-root-followup-r2`. Installed Python 3.14.3, PyYAML 6.0.3 and python-liquid 2.3.6 were used. Existing plugin version/icon warnings are nonblocking and unchanged. Expected negative-fixture fetch diagnostics appear in validation.stderr.log. Native output was captured as UTF-8; new evidence files were normalized to LF and trailing line whitespace removed before staging. Staged whitespace validation is checked before committing.

Relative to `b8e4636`, **all 568 Markdown files and LICENSE are byte-identical**. Only `references/SOURCE.json` changes in the bundled corpus, updating the builder generator hash. No policy, routing, model, pricing or table guidance changes are included. Original PR comparison remains **531 unchanged / 37 changed Markdown files**, with the two previously authorized body fixes and all 15 original invalid YAML pages repaired.

The other changed files are README, the rebuild manager, its permanent tests and the validation runner's expanded cleanup assertion, plus this isolated evidence directory. All earlier reports/results remain unchanged.

Machine-readable evidence:

- [summary.json](summary.json), [unittest-results.json](unittest-results.json), [unittest.log](unittest.log): full suite counts and named tests.
- [validation-results.json](validation-results.json): exact commands, expected/actual values and 22 PASS outcomes, with per-command logs alongside it.
- [r2-results.json](r2-results.json): the three focused regression outcomes.
- [scope-results.json](scope-results.json): exact Git blob hash comparison against frozen b8e4636, without newline normalization.
- [corpus-comparison.json](corpus-comparison.json): original PR corpus comparison and preserved-path inventory.

## Limits

No tests are blocked and no unexpected failures remain. The termination regression uses a real child process with `os._exit(9)` to bypass Python cleanup after complete staging; it is not an external OS kill or power-loss test. **A kill during the two-rename publication gap remains untested.** The existing brief missing-destination window and filesystem/rollback failure limitations remain. README recovery guidance therefore requires preserving possible last-good backups and inspecting state before cleanup. No automatic stale-data cleanup or lock stealing was added.

Cross-filesystem rejection is tested with an injected stat result on the installed Windows environment. No physical multi-volume or cross-platform matrix is claimed. Remaining independent-review optional warnings are outside this repair's scope. The next local candidate SHA is reported after committing; the candidate will then stay frozen for handoff.
