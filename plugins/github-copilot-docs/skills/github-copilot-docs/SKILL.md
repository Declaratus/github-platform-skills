---
name: github-copilot-docs
description: Look up GitHub's official Copilot documentation (content/copilot from github/docs), bundled locally. Covers Copilot plans and billing, AI credits and budgets, enterprise and org policies, model availability, content exclusion, MCP management, cloud agent, code review, Copilot CLI, custom instructions, custom agents, hooks, usage metrics, network allowlists, and rollout guidance. Use when the user asks how a Copilot feature works, how to configure or administer Copilot, what a Copilot setting, policy, metric, or model does, or needs the documented answer instead of a guess.
---

# GitHub Copilot docs

Local copy of https://docs.github.com/en/copilot, built from `content/copilot` in https://github.com/github/docs. Answers "how does Copilot do X" and "how do I configure X". For "what should our org do and why" (rollout strategy, governance design), pair with the `github-well-architected` skill.

Copilot changes fast. Prefer these docs over memory for feature names, policy names, model lists, and billing rules, and cite the page you used.

Read `references/SOURCE.json` for the immutable upstream revision, source commit date, build inputs and dependencies. These pages are a snapshot, not a claim about today's availability or prices. Preserve plan, preview, client and deployment qualifications. If current behavior matters, explicitly identify what needs checking against the live page; do not silently substitute memory for the snapshot.

## How to find the right page

1. Pick the section from the table below by question type.
2. Read that section's `index.md`. Its `children:` frontmatter lists the pages in order; read each relevant child's `intro:` and body.
3. If the section is unclear, `Grep` the whole `references/` tree for the feature or setting name. File names match URL slugs.

| Question type | Start in |
|---|---|
| What is X, how does it work, tradeoffs | `references/concepts/` |
| Step-by-step: enable, configure, use | `references/how-tos/` |
| Lookup tables: models, billing, metrics fields, CLI flags, config schemas | `references/reference/` |
| Worked examples, rollout playbooks, prompt/customization samples | `references/tutorials/` |
| First-time setup, plans | `references/get-started/` |
| GitHub Enterprise Server specifics | `references/copilot-on-ghes/` |
| Feature limitations and responsible AI notes | `references/responsible-use/` |

## Common entry points

**Administration and governance**
- Enterprise policies: `concepts/enterprise/policies.md`, `reference/supported-surfaces-for-policies.md`
- Admin how-tos: `how-tos/administer-copilot/manage-for-enterprise/`, `.../manage-for-organization/`
- MCP governance: `concepts/enterprise/mcp-management.md`, `how-tos/administer-copilot/manage-mcp-usage/`
- Content exclusion: `concepts/security-governance-and-network-settings/content-exclusion.md`, `how-tos/configure-content-exclusion/`
- Network allowlist: `reference/copilot-allowlist-reference.md`, `concepts/security-governance-and-network-settings/network-settings.md`
- Sandboxes and agent isolation: `concepts/security-governance-and-network-settings/`, `how-tos/cloud-and-local-sandboxes/`

**Billing, spend, and metrics**
- `concepts/billing-and-usage/`, `reference/copilot-billing/`
- Budgets: `how-tos/manage-and-track-spending/`, `tutorials/budgets/`
- Pricing: `reference/copilot-billing/models-and-pricing.md`. Distinguish token/AI-credit pricing from legacy annual Pro/Pro+ request multipliers in `reference/copilot-billing/request-based-billing-legacy/model-multipliers-for-annual-plans.md`; those multipliers do not apply to usage-based billing.
- Usage metrics: `reference/copilot-usage-metrics/`, `reference/metrics-data.md`, `how-tos/administer-copilot/view-usage-and-adoption.md`

**Models**: `concepts/models/`, `reference/ai-models/`

**Agents and automation**
- Cloud agent: `how-tos/use-copilot-agents/cloud-agent/`, `tutorials/cloud-agent/`
- Code review: `how-tos/use-copilot-agents/use-code-review.md`
- Agentic workflows (Actions): `how-tos/github-agentic-workflows/`
- Copilot CLI: `how-tos/copilot-cli/`, `reference/copilot-cli-reference/`
- SDK: `how-tos/copilot-sdk/`

**Customization**
- Overview: `concepts/customizations/`, `reference/customization-cheat-sheet.md`
- Custom instructions: `reference/custom-instructions-support.md`
- Custom agents: `reference/custom-agents-configuration.md`
- Hooks: `reference/hooks-reference.md`
- Plugins and marketplaces: `reference/plugin-and-marketplace-reference.md`
- Example library: `tutorials/customization-library/`

For customization semantics, also read `concepts/prompting-and-context/custom-instructions.md` and `concepts/customizations/`. Most clients, including CLI and VS Code, combine applicable instructions without a general override order. The personal/repository/organization precedence documented for GitHub.com Chat must not be applied to every client or cloud-agent feature. Read the exact surface row in `reference/custom-instructions-support.md`.

For hook configuration, distinguish `reference/hooks-reference.md` (CLI/cloud schemas and execution environments) from VS Code preview behavior in `reference/customization-cheat-sheet.md` and the linked IDE documentation. Agent-scoped YAML `hooks:` are Copilot CLI only, for local/repository agents; remote or organization-hosted agent definitions do not run them. Do not promise identical discovery, event names, payloads, commands or permission decisions across surfaces. Cloud runs non-interactively on Linux; CLI user/policy/settings sources do not automatically propagate. Check custom-agent field compatibility separately in `reference/custom-agents-configuration.md`.

**Feature availability by plan and surface**: `reference/copilot-feature-matrix.md`

**GHES**: Read `copilot-on-ghes/about-copilot-on-ghes.md` alongside `concepts/models/bring-your-own-key.md`; preserve the local BYOK license exception and client-specific support limits. Distinguish Copilot cloud sign-in from MCP-server authentication; do not infer MCP-to-GHES credentials from Copilot sign-in.

**Rollout**: `tutorials/roll-out-at-scale/`

## Reading the pages

Product-name variables and reusable snippets are already resolved at build time. A few github/docs conventions remain:

- `[AUTOTITLE](/copilot/a/b)` is a link to another page. Map it to `references/a/b.md` or `references/a/b/index.md`. Links outside `/copilot/` are not bundled; cite them as `https://docs.github.com/en<path>`.
- If that local path does not exist, search frontmatter `redirect_from:` for the original `/copilot/...` path, ignoring query/fragment while locating the file. Read the matching page and cite its current local path and mapped live URL. A redirect alias is not a missing page.
- `{% ifversion fpt %}...{% else %}...{% endif %}` splits GitHub.com (`fpt`, `ghec`) from GitHub Enterprise Server (`ghes`) text. Use the branch matching the user's deployment.
- `{% codetab %}` blocks are per-platform alternatives (Windows/macOS/Linux, or per-IDE).
- `(icon: name)` marks a UI icon next to a button label.
- Images were stripped. `![...]` references point at assets that are not bundled; the alt text still describes the screenshot.

When citing, give the live URL: `references/how-tos/foo/bar.md` is `https://docs.github.com/en/copilot/how-tos/foo/bar`.

## Source attribution

GitHub Docs content, © GitHub, licensed CC BY 4.0 (`references/LICENSE`). Modified from upstream: Liquid data tags resolved to plain text, octicons flattened, images removed. Rebuild with `./build/build.sh github-copilot-docs`.
