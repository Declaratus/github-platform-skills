# GitHub Changelog entries newer than the docs snapshots

Status: accepted, 2026-11-23. Shipped in #8 and #10.

## Decision

Generate each docs plugin's `changelog.md` from the GitHub Changelog REST API with one shared script, `build/lib/build_changelog.py`, driven by `build/changelog.json`. The daily refresh workflow runs it after the docs rebuild, so changelog updates land in the same refresh PR as the docs. No standalone changelog skill, and no hand-maintained seed lists.

## What exists upstream (checked 2026-11-23)

There is no git-backed source. `github/changelog` and `github/blog` do not exist (404 via `gh api`). `github/roadmap` exists but was last pushed 2024-10-15. `github/docs` has a `CHANGELOG.md`, but it records docs-team edits, not product changes.

The changelog runs on WordPress, and two machine-readable sources work:

| Source | Result |
|---|---|
| `https://github.blog/wp-json/wp/v2/changelogs` | 200, JSON. Filters: `label`, `type`, `after`, `before`, `modified_after`, `search`. `X-WP-Total` reported 3942 entries. 100 per page. |
| `https://github.blog/wp-json/wp/v2/label` | 200, the 12 current labels plus legacy ones, with ids and counts |
| `https://github.blog/wp-json/wp/v2/type` | 200: `new-releases`, `improvements`, `deprecations` |
| `https://github.blog/changelog/feed/` | 200, RSS, 10 items per page |
| `https://github.blog/changelog/label/<slug>/feed/` | 200, RSS, 10 items per page, `?paged=N` for older |

The RSS feeds are fine for an agent checking live, but 10 items per page makes them poor for a build. The REST API gives a full date window in one or two requests, so the build uses that.

Nothing here is pinnable the way a github/docs commit is. Entries can be edited after publication and there is no revision id. The generated file records the window it covers instead (`This list covers <start> to <build date>`), and the refresh PR diff shows what changed.

## Labels

Current labels with useful counts: `copilot` (861), `application-security` (715), `platform-governance` (517), `collaboration-tools` (483), `enterprise-management-tools` (429), `actions` (397), `ecosystem-and-accessibility` (299), `supply-chain-security` (292), `community-engagement` (219), `client-apps` (215), `account-management` (184), `projects-and-issues` (136).

There is no billing label. `/changelog/label/billing/` and `/changelog/label/enterprise-management/` return 404. The working slugs are `account-management` and `enterprise-management-tools` (both the HTML page and `/feed/` return 200). `enterprise-management-tools` is broad and carries a lot of Copilot admin news, so the billing config adds a `match` regex over title and excerpt. It still lets a few non-billing entries through (for example "EMU deletions fix"), which is cheap compared to missing a budget or SKU change.

Plugin mapping in `build/changelog.json`:

| Plugin | Labels | Extra |
|---|---|---|
| github-projects-issues-docs | `projects-and-issues` | |
| github-billing-docs | `account-management`, `enterprise-management-tools` | `match` regex |
| github-code-security-docs | `application-security`, `supply-chain-security` | 180 day lookback |

The script skips a plugin that has no `references/SOURCE.json` yet, so billing and code security can sit in the config before their branches merge.

## Window

Each list starts `lookback_days` before the plugin's docs snapshot date (`upstream_committed_at`) and ends at the build date. The lookback exists because docs lag the changelog by more than the gap between snapshot and today: the Nov 2026 `content/issues` snapshot does not mention hierarchy view at all, and it went GA on 2026-03-19. Default lookback is 365 days. Code security uses 180 because its labels are busy (151 entries in 180 days, about 28 KB).

Sizes from the prototype run: projects-issues 35 entries (7 KB), billing 31 (6 KB), code security 151 (28 KB).

## Why per-plugin generated files

A standalone changelog skill would compete with the docs skills for triggering. The question that needs it ("how do I set a budget on a cost center") already triggers the billing docs skill, and a second skill with a generic "what changed recently" description will either not load or load for everything. Keeping the list next to SKILL.md means the skill that triggers already has it.

A single shared file across plugins does not work either. Plugins install independently, so a file in one plugin cannot be relied on from another, and copying a shared file into each plugin is what the generator already does, just without the per-plugin filtering.

Per-plugin files generated from one script and one config give the same SKILL.md wording everywhere, no hand-curated seed lists to drift, and one place to add a plugin.

## SKILL.md wording

Each docs SKILL.md keeps a short "Check for newer changes first" section pointing at `changelog.md`: the list covers up to its build date, and the label feed it names covers anything after. The projects-issues SKILL.md on this branch shows the wording.

## Open questions

- github-copilot-docs has no changelog file and instead tells the agent to fetch live pages. Adding `copilot` to the config would give it a list, but that label averages over 2 entries a day, so it needs a short lookback (60 to 90 days) or a `match` filter. Left out of the prototype.
- The REST API is stock WordPress, not a documented GitHub API. If it goes away, the script fails loudly and the last good `changelog.md` stays in place; the fallback is paging the RSS feeds.
- Changelog entries change daily, so the refresh PR will open most days even when the docs pins do not move. That is the point, but it is more PR traffic than today.
- billing and code-security branches each carry a hand-written `changelog.md`. When they merge, delete those and run `python3 build/lib/build_changelog.py`.
