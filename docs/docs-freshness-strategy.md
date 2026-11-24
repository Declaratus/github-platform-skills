# Docs freshness strategy

## Decision

Status: accepted, 2026-11-23. Shipped in #2.

Each docs plugin bundles a pinned snapshot of its upstream docs under `references/`, with the upstream commit recorded in `SOURCE.json`. A daily workflow moves the pins and opens one refresh PR for review (see README, "Scheduled refresh"). Skills fetch the live page only for facts that change between refreshes, and each SKILL.md lists its own triggers. For copilot-docs they are prices, model lists, preview or GA status, policy names and plan availability.

## Why

- **The bundle** works offline and needs no grants. It is pinned, so every answer can cite an exact upstream commit. It also keeps the GitHub.com vs GHES split that `{% ifversion %}` encodes, which matters for enterprise questions.
- **The live check** covers what a daily refresh can still miss. Prices, model lists and preview status can change within a day, and a user asking about "current" behaviour should get the page as it is now.

## Live-check rule

copilot-docs and migrations-docs find the page in the snapshot first, then fetch its live version with `curl -sL <url>.md`. admin-docs and code-security send the agent to the live page for the few things they don't bundle (GHES release notes, the per-provider secret pattern table), without naming a tool. billing-docs quotes prices with the snapshot date and points to the live page. projects-issues and well-architected are snapshot only. Five plugins also carry a generated `changelog.md` for changes newer than the snapshot ([changelog-strategy.md](changelog-strategy.md)).

The fetch is conditional. Each SKILL.md lists its own triggers: for copilot-docs, prices, model lists, preview or GA status, policy names and plan availability; for migrations-docs, size limits, preview or GA status, supported source versions, CLI flags and supported paths. Both also fetch when the question says "current", "latest" or "now", and skip it for stable concepts and procedures. Most answers need no fetch and no grant.

migrations-docs reads its `changelog.md` before the live page, because the live docs lag the changelog: ELM from Azure DevOps went GA on 2026-11-19 while the docs still said preview. It is the one place where the live page isn't the last word.

- **Keep the wording imperative.** In testing, a headless run skipped the fetch on "which models are currently available" until the rule said "You must fetch the live page before answering when...". Softening it brings the skip back.
- **Fallback.** If the fetch fails or is denied, the skill answers from the snapshot and says the page was not checked live. It never substitutes memory.
- **Return contract.** Each answer gives the live URL of every page used, and marks each key fact as snapshot (with the `SOURCE.json` commit date) or checked live.
- **Cost to users.** The fetch runs through Bash, so Claude Code prompts for it unless `Bash(curl:*)` is allowed.

## Alternatives considered

| Approach | How docs reach the agent | Outcome |
| --- | --- | --- |
| [Context7](https://github.com/upstash/context7) | Hosted index, queried through the `ctx7` CLI or an MCP server | Rejected: third-party service, API key, outbound traffic from enterprise networks. Its chunks may also lose the GitHub.com vs GHES split (unverified). |
| [openai-docs](https://github.com/openai/codex/tree/main/codex-rs/skills/src/assets/samples/openai-docs) (Codex sample) | Short SKILL.md routes to small curated files; scripts fetch the manual at runtime with a cache and sha256 check | Borrowed the routing layer and the live check for current behaviour |
| [microsoft-docs](https://github.com/microsoft/skills/tree/main/.github/skills/microsoft-docs) | Calls the first-party Learn MCP server, with a CLI fallback | Borrowed `context: fork`. Fully live isn't an option: GitHub has no first-party docs MCP server. |
| Compare-based freshness check | `gh api repos/github/docs/compare/<pin>...main`, then fetch only pages that changed | Rejected: bundled pages have `data/` snippets and tables resolved at build time, so a changed `data/` file can't be mapped to the pages that use it without a build-time index. With a daily refresh there is little left for it to catch. |

## Cross-host consequences

The marketplace is meant to serve Codex, Copilot, Gemini CLI, pi and Hermes as well as Claude Code. Checked against each host's docs on 2026-11-23, the decision holds, with four consequences.

- **The bundle is the only path that works everywhere.** Every host can read `references/` without extra grants.
- **The fork is Claude Code only.** Other hosts ignore `context: fork` and `agent:`, so copilot-docs and migrations-docs run inline there and page reads land in the main context. Their bodies are written for a fork (`Question: $ARGUMENTS`, "You cannot see the conversation", `${CLAUDE_SKILL_DIR}` paths) and need rewording to read right both ways. Not done yet.
- **A denied curl degrades, it doesn't break.** Several hosts deny shell in headless runs or until a trust step. The skill then answers from the snapshot and says so.
- **Packaging limits.** Agent Skills and Copilot cap descriptions at 1,024 characters; code-security, admin-docs and migrations are over it today. Hermes warns past 60 reference files. That warning is accepted, because the `references/` tree mirrors github/docs paths so citations map straight to live URLs.

## When to revisit

Revisit a plugin's mix of bundle and live when a no-skill run with web access matches the plugin on qualification cases and beats it on fast-moving ones. The eval strategy (not yet written) owns the measurement and these tags:

- **qualification**: judgment calls where the bundle should win, because search plus fetch tends to miss them. Examples: custom-instruction precedence by client, agent-scoped hooks being CLI only, the GHES BYOK license exception, AI-credit vs legacy request-multiplier billing.
- **fast-moving**: prices, model lists, preview vs GA. Live should win here.

## Appendix: docs.github.com endpoints

Appending `.md` to a docs URL returns the page as markdown, rendered for that deployment with versioning and variables resolved. copilot-docs uses the first four rows. migrations-docs uses the first three. Tested 2026-11-12.

| Endpoint | Returns | Used for |
| --- | --- | --- |
| `https://docs.github.com/en/<section>/<path>.md` | GitHub.com page | Live check |
| `https://docs.github.com/en/enterprise-cloud@latest/<section>/<path>.md` | GHE.com page | Live check |
| `https://docs.github.com/en/enterprise-server@<version>/<section>/<path>.md` | GHES page (`@latest` works too) | Live check |
| `https://docs.github.com/api/pagelist/en/free-pro-team@latest` | Every live path, plain text | Finding pages added since the snapshot (copilot-docs) |
| `https://docs.github.com/api/article/meta?pathname=...` | Title, intro and breadcrumbs as JSON | Not used |
| `https://docs.github.com/api/search/v1` | Needs `client_name`; returned 0 hits in testing | Don't rely on it |

Two live sources sit outside docs.github.com: [Microsoft Learn's ELM overview](https://learn.microsoft.com/azure/devops/repos/enterprise-live-migrations/overview) (migrations-docs, ELM from Azure DevOps) and the Copilot Trust Center FAQ (copilot-docs, which bundles a dated capture in `trust-center/` and checks the live FAQ when it can).
