# Final scenario-guidance qualification follow-up

Parent candidate: `44606613c56ac34c793cc98afa43490c5bc87ba1`, containing the completed R2 repair. This new local commit adds only concise guidance in SKILL.md and this evidence directory. It preserves all prior commits, frozen answers, reports and results. No push, merge, global installation, account change or security scan was performed.

The authorized CROSS-VALIDATION.md was read for guidance scope. Its model-answer limitations were used to qualify routing, not to change the correct upstream corpus or reproduce scenario answers in the entrypoint. The skill-creator guidance was applied to keep the edit narrow.

## Source-checked guidance

- **Agent-scoped YAML hooks:** SKILL.md:65 now explicitly says Copilot CLI only, for local/repository agents; remote or organization-hosted definitions do not run them. Bundled `reference/hooks-reference.md:64-69` establishes the CLI-only agent-frontmatter hook map; `:84-90` gives the supported behavior and excludes remote/organization-hosted definitions. Existing warnings about schemas, execution environments and separate custom-agent compatibility remain.
- **GHES qualifications:** SKILL.md:69 routes to `copilot-on-ghes/about-copilot-on-ghes.md` and `concepts/models/bring-your-own-key.md`, reminding readers to retain the local BYOK license exception and client support limits. The GHES source at `:14-18` explicitly states the exception; the BYOK source at `:24-37` describes direct provider credentials, use without a subscription and supported clients. GHES `:29-31` separately describes cloud-account authentication for Copilot and a local MCP server connection to GHES. The new guidance prevents inferring MCP-to-GHES credentials from Copilot sign-in; it does not assert an undocumented authentication mechanism.
- **Pricing systems:** SKILL.md:43 routes separately to `reference/copilot-billing/models-and-pricing.md` and `reference/copilot-billing/request-based-billing-legacy/model-multipliers-for-annual-plans.md`. The former `:13-24` documents token-to-credit pricing and `:163-165` routes legacy annual Pro/Pro+ subscribers. The latter `:15-21` explicitly limits those request multipliers to legacy annual plans and says they do not apply to usage-based billing. No price values, model rows or claims about today's availability were added.

All source line bounds were verified directly against the pinned bundled files. [source-checks.json](source-checks.json) contains exact source excerpts, file paths and SKILL line numbers. These are manual semantic source checks, not automated evidence that another model will follow the guidance.

## Validation

Exact commands and exit codes are retained in [results.json](results.json), with per-command logs:

| Check | Result |
| --- | --- |
| skill-creator `quick_validate.py` against the plugin skill | PASS, exit 0 |
| `claude plugin validate .` | PASS, exit 0; existing missing-version warnings |
| `claude plugin validate ./plugins/github-copilot-docs` | PASS, exit 0; existing version/icon warnings |
| `python -m unittest discover -s build/tests -v` | **55 passed**, 0 failures/errors/skips |
| Git whitespace check | PASS, exit 0 |
| Git corpus diff against R2 parent 4460661 | Empty, exit 0 |

The source remains pinned to `github/docs@7c3387d3b513ed43ea26c9b2e4c0e1b12234c010`. All **568 Markdown pages, LICENSE and SOURCE.json are unchanged** by this final guidance edit. R2's full pinned cold/refresh/repeat/shell/build checks remain documented in [the R2 report](../followup-r2/REPORT.md) and [its 22 pipeline results](../followup-r2/validation-results.json). No pipeline code changed after that validation; the full permanent suite was rerun here.

No checks are blocked. No new live-product verification, model scenario execution or native activation probe was performed for this prose edit. There is no claim of nine perfect first-pass scenarios or guaranteed model adherence. R2's hard-termination-during-publication and physical multi-volume test limits remain unchanged. The final candidate SHA is reported after creating the new local commit, and the candidate will remain frozen for handoff.
