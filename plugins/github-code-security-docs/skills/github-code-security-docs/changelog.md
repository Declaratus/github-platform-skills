# Code security changes newer than the docs snapshot

github/docs does not carry the GitHub Changelog. The bundled `references/` tree is a snapshot (see `references/SOURCE.json` for the upstream commit date), and security features ship, change status or get renamed often, usually before the docs catch up.

Before answering anything about feature availability, preview vs GA status, new secret detectors, CodeQL versions or language support, or Dependabot ecosystem support, check both label feeds for entries newer than the snapshot:

- Code scanning, secret scanning, CodeQL, security overview, campaigns, AI Scan: https://github.blog/changelog/label/application-security/feed/
- Dependabot, dependency graph, dependency review, advisories, package firewall, SBOM, attestations: https://github.blog/changelog/label/supply-chain-security/feed/

Older entries are on `?paged=2`, `?paged=3` and so on. Where the feed and the docs disagree, the newer dated source wins, and say which one you used.

## Seed list (late 2026)

| Date | Change | Link |
|---|---|---|
| 2026-10-16 | Open source license compliance GA | https://github.blog/changelog/2026-10-16-open-source-license-compliance-generally-available |
| 2026-10-20 | GitHub package firewall, public preview | https://github.blog/changelog/2026-10-20-github-package-firewall-in-public-preview |
| 2026-10-28 | AI Scan for repositories, public preview | https://github.blog/changelog/2026-10-28-ai-scan-for-repositories-in-public-preview |
| 2026-10-28 | Code scanning for AI applications, public preview | https://github.blog/changelog/2026-10-28-code-scanning-for-ai-applications-in-public-preview |
| 2026-10-28 | Push protection beyond predefined secret patterns | https://github.blog/changelog/2026-10-28-push-protection-beyond-predefined-secret-patterns |
| 2026-10-28 | Public monitoring for enterprises GA | https://github.blog/changelog/2026-10-28-public-monitoring-for-enterprises-generally-available |
| 2026-10-28 | Dependabot reachability analysis for alert prioritization | https://github.blog/changelog/2026-10-28-prioritize-dependabot-alerts-with-reachability-analysis |
| 2026-11-02 | `pull_request_target` blocked by default from December 2 | https://github.blog/changelog/2026-11-02-pull_request_target-blocked-by-default-december-2 |
| 2026-11-09 | Secret scanning covers GitHub Actions workflow logs | https://github.blog/changelog/2026-11-09-secret-scanning-detects-secrets-in-github-actions-workflow-logs |
| 2026-11-10 | Dependabot alerts pause on inactive repositories | https://github.blog/changelog/2026-11-10-dependabot-alerts-will-pause-on-inactive-repositories |
| 2026-11-16 | Dependabot alert dismissal requests last one year | https://github.blog/changelog/2026-11-16-dependabot-alert-dismissal-requests-now-last-one-year |
| 2026-11-17 | Secret scanning on demand for developers and agents | https://github.blog/changelog/2026-11-17-secret-scanning-on-demand-for-developers-and-agents |
| 2026-11-18 | Security risk assessments run automatically on GitHub Team | https://github.blog/changelog/2026-11-18-security-risk-assessments-run-automatically-on-github-team |
| 2026-11-20 | Security advisory permissions GA | https://github.blog/changelog/2026-11-20-security-advisory-permissions-are-now-generally-available |

This list is a starting point, not a complete record. Read the linked entry for the actual scope and limits before relying on it.
