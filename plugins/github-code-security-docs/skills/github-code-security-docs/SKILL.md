---
name: github-code-security-docs
description: Look up GitHub's official code security documentation (content/code-security from github/docs), bundled locally, plus pointers to the application-security and supply-chain-security changelogs for newer changes. Covers GitHub Advanced Security (GHAS) and its Secret Protection and Code Security products, licensing and active committers, security configurations and global settings, enforcement, code scanning (default and advanced setup, CodeQL, CodeQL CLI and packs, SARIF upload, third-party tools, merge protection, troubleshooting), Copilot Autofix, AI Scan, secret scanning (push protection, bypass and delegated bypass, custom patterns, validity checks, generic and AI-detected secrets, public monitoring), Dependabot (alerts, security and version updates, dependabot.yml, auto-triage rules, private registries, runners), dependency graph, dependency review, SBOM, artifact attestations and linked artifacts, package firewall, repository security advisories and private vulnerability reporting, security overview, security campaigns, risk assessments, alert dismissal, GitHub Code Quality, and the phased GHAS rollout guide. Use when configuring or rolling out GHAS, writing a CodeQL workflow or dependabot.yml, debugging a failed code scanning or Dependabot run, triaging or dismissing alerts, planning secret leak remediation, or when the user needs the documented behaviour instead of a guess.
---

# GitHub code security docs

Local copy of https://docs.github.com/en/code-security, built from `content/code-security` in https://github.com/github/docs. Answers "how does GHAS, code scanning, secret scanning or Dependabot do X" and "how do I configure X". For "what should our org standardise on and why", pair with the `github-well-architected` skill (its Application Security pillar).

GHAS packaging, setup types and AI features changed a lot in 2025 and 2026 (the Secret Protection and Code Security split, security configurations replacing per-feature enablement, Copilot Autofix, AI Scan, delegated dismissal, Code Quality). Prefer these docs over memory for licensing, which plan or repository visibility gets which feature, configuration and enforcement behaviour, alert states, permission rules and `dependabot.yml` or workflow keys, and cite the page you used.

## Check for newer changes first

The docs snapshot lags the product. Read `changelog.md` (next to this file) and check the label feeds it points at for anything newer than the `upstream_committed_at` date in `references/SOURCE.json`. New secret detectors, CodeQL releases, Dependabot ecosystems and preview features often appear only in the changelog at snapshot time. Preserve preview vs GA status and plan or account-type qualifications as stated.

## How to find the right page

1. Pick the area from the table below. The tree is split by Diátaxis type: `concepts/` (what and why), `how-tos/` (steps), `reference/` (options, limits, troubleshooting), `tutorials/` (end-to-end guides).
2. Read that folder's `index.md`. Its `children:` frontmatter lists pages in order.
3. Otherwise `Grep` the whole `references/` tree for the feature, setting, error message or YAML key. File names match URL slugs.

| Topic | Start in |
|---|---|
| Which features exist, which product (Secret Protection, Code Security) and plan includes them | `getting-started/github-security-features.md`, `concepts/security-at-scale/organization-security.md` |
| Security configurations, global settings, enforcement, enterprise-level enablement | `how-tos/secure-at-scale/configure-organization-security/`, `.../configure-enterprise-security/`, `reference/security-at-scale/` |
| GHAS licensing, active committers, pricing estimates | `how-tos/secure-at-scale/configure-organization-security/manage-usage-and-access/`, `.../configure-specific-tools/estimate-price.md` |
| Rollout planning, pilots, trials | `tutorials/adopting-github-advanced-security-at-scale/`, `tutorials/trialing-github-advanced-security/`, `concepts/security-at-scale/select-pilot-repositories.md` |
| Code scanning concepts, setup types, CodeQL, autofix, AI Scan | `concepts/code-scanning/` |
| Configuring code scanning, advanced setup, larger runners, merge protection | `how-tos/find-and-fix-code-vulnerabilities/` |
| CodeQL workflow keys, build modes, hardware, SARIF limits | `reference/code-scanning/` |
| Code scanning failures | `reference/code-scanning/troubleshoot-analysis-errors/`, `.../sarif-files/troubleshoot-sarif-uploads/` |
| CodeQL CLI and custom queries | `how-tos/find-and-fix-code-vulnerabilities/scan-from-the-command-line/`, `reference/code-scanning/codeql/codeql-cli-manual/`, `tutorials/customize-code-scanning/` |
| Secret scanning, push protection, bypass, custom patterns | `concepts/secret-security/`, `how-tos/secure-your-secrets/`, `reference/secret-security/` |
| Leaked secret response | `tutorials/remediate-leaked-secrets/`, `tutorials/secure-your-organization/organize-leak-remediation.md` |
| Dependabot, dependency graph, dependency review, SBOM, attestations, package firewall | `concepts/supply-chain-security/`, `how-tos/secure-your-supply-chain/`, `reference/supply-chain-security/` |
| Alert triage, dismissal, delegated dismissal, campaigns | `how-tos/manage-security-alerts/` |
| Security overview, metrics, risk assessments, exports | `concepts/security-at-scale/security-overview.md`, `how-tos/view-and-interpret-data/`, `reference/security-at-scale/` |
| Repository security advisories, private vulnerability reporting, Advisory Database | `concepts/vulnerability-reporting-and-management/`, `how-tos/report-and-fix-vulnerabilities/` |
| Incident preparation and response | `tutorials/secure-your-organization/prepare-for-a-security-incident.md`, `.../respond-to-a-security-incident.md`, `reference/security-incident-response/` |
| GitHub Code Quality | `concepts/code-quality/`, `how-tos/maintain-quality-code/`, `reference/code-quality/` |
| Permissions for security features | `reference/permissions/` |

## Common entry points

- Default vs advanced setup: `concepts/code-scanning/setup-types.md`. Advanced setup workflow: `how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configuring-advanced-setup-for-code-scanning.md`. Every workflow key: `reference/code-scanning/workflow-configuration-options.md`.
- Compiled languages and build modes (`none`, `autobuild`, `manual`): `concepts/code-scanning/codeql/codeql-for-compiled-languages.md`, `reference/code-scanning/codeql/build-options-for-compiled-languages.md`.
- Third-party scanners and SARIF: `how-tos/find-and-fix-code-vulnerabilities/integrate-with-existing-tools/upload-sarif-file.md`, `reference/code-scanning/sarif-files/sarif-support.md`.
- Blocking merges on findings: `concepts/code-scanning/merge-protection.md`, `how-tos/find-and-fix-code-vulnerabilities/manage-your-configuration/set-merge-protection.md`. Rulesets themselves live under `/repositories/` upstream and are not bundled.
- Security configurations at org level: `how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/create-custom-configuration.md`, `.../apply-custom-configuration.md`, `.../configure-global-settings.md`. Enforcement and statuses: `reference/security-at-scale/configuration-enforcement.md`, `.../configuration-statuses.md`. When a feature turns on or off unexpectedly: `reference/security-at-scale/troubleshoot-security-configurations/`.
- Push protection and bypass: `concepts/secret-security/push-protection.md`, `concepts/secret-security/delegated-bypass.md`, `how-tos/secure-your-secrets/manage-bypass-requests/`. Supported patterns: `reference/secret-security/supported-secret-scanning-patterns.md` has the generic and AI-detected patterns, but its per-provider table (which tokens are detected, push protected or validity checked) is generated upstream from `src/secret-scanning/data/pattern-docs/` and is not bundled. For a specific provider's token, use the live page https://docs.github.com/en/code-security/reference/secret-security/supported-secret-scanning-patterns and check the application-security changelog for detectors added since the snapshot. Say so if neither is reachable instead of guessing.
- `dependabot.yml`: `concepts/supply-chain-security/about-the-dependabot-yml-file.md`, every option in `reference/supply-chain-security/dependabot-options-reference.md`. Private registries: `how-tos/secure-your-supply-chain/manage-your-dependency-security/configure-private-registries.md`. Auto-triage rules: `concepts/supply-chain-security/dependabot-auto-triage-rules.md`.
- Dependency review action: `how-tos/secure-your-supply-chain/manage-your-dependency-security/configure-dependency-review-action.md`, `tutorials/secure-your-dependencies/customize-dependency-review-action.md`.
- Dependabot failures: `reference/supply-chain-security/troubleshoot-dependabot/`, logs in `how-tos/view-and-interpret-data/view-dependabot-logs.md`.

The REST API, webhook and audit log **reference** pages (code scanning, secret scanning, Dependabot, security configurations, advisories) live under `content/rest`, `content/webhooks` and `content/admin` upstream and are not bundled. Nor is Actions hardening (`/actions/`), billing (`/billing/`), or the GHAS product overview at `/get-started/learning-about-github/about-github-advanced-security`. Cite them live, for example https://docs.github.com/en/rest/code-scanning, https://docs.github.com/en/rest/secret-scanning, https://docs.github.com/en/rest/dependabot and https://docs.github.com/en/rest/code-security/configurations.

## Reading the pages

Product-name variables and reusable snippets are resolved at build time. Remaining github/docs conventions:

- `[AUTOTITLE](/code-security/a/b)` links another page. Map it to `references/a/b.md` or `references/a/b/index.md`. Links outside `/code-security/` are not bundled; cite them as `https://docs.github.com/en<path>`.
- If that local path does not exist, search frontmatter `redirect_from:` for the original `/code-security/...` path. This tree was restructured heavily, so old paths often survive only as redirect aliases.
- `versions:` frontmatter and `{% ifversion ... %}` blocks gate text by deployment or feature flag. `fpt` is GitHub.com Free/Pro/Team, `ghec` is GitHub Enterprise Cloud, `ghes` is GitHub Enterprise Server (often with a version comparison like `ghes > 3.19`). Security features differ a lot between these, and between public and private repositories. Use the branch matching the user's deployment and repository visibility, and don't assume a GitHub.com feature exists on GHES.
- `{% raw %}...{% endraw %}` wraps literal Actions expressions in examples. Drop the wrapper when copying YAML.
- `(icon: name)` marks a UI icon next to a button label. Images were stripped; alt text remains.

When citing, give the live URL: `references/a/b.md` is `https://docs.github.com/en/code-security/a/b`.

## Source attribution

GitHub Docs content, © GitHub, licensed CC BY 4.0 (`references/LICENSE`). Modified from upstream: Liquid data tags resolved to plain text, octicons flattened, images removed. Rebuild with `./build/build.sh github-code-security-docs`.
