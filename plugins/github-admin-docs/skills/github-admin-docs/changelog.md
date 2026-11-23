# Enterprise admin changes newer than the docs snapshot

github/docs does not carry the GitHub Changelog or the GitHub Enterprise Server release notes. The bundled `references/` tree is a snapshot (see `references/SOURCE.json` for the upstream commit date). Enterprise Cloud features often ship, change status or get renamed before the docs catch up, and GHES behaviour changes with each feature and patch release.

## GitHub Enterprise Cloud (including GHE.com)

Check these label feeds for entries newer than the snapshot:

- https://github.blog/changelog/label/enterprise-management-tools/feed/ (enterprise settings, audit log, apps, billing, metrics)
- https://github.blog/changelog/label/platform-governance/feed/ (rulesets, custom properties, policy, audit)
- https://github.blog/changelog/label/account-management/feed/ (authentication, tokens, SSH, proof of presence)

Older entries are on `?paged=2`, `?paged=3` and so on. Where a feed and the docs disagree, the newer dated source wins, and say which one you used.

## GitHub Enterprise Server

The bundled `release-notes.md` and `all-releases.md` are layout stubs; their content is generated from other upstream data and is not included. Use the live pages:

- Release notes for one version: `https://docs.github.com/en/enterprise-server@<version>/admin/release-notes` (for example `@3.22`). These carry known issues, deprecations and the patch-level fixes that matter for upgrade planning.
- Support window, closing-down dates and minimum supporting versions: https://docs.github.com/en/enterprise-server@latest/admin/all-releases
- Upgrade requirements and supported paths between versions: `references/upgrading-your-instance/preparing-to-upgrade/upgrade-requirements.md`, then the target version's release notes.

`references/VERSIONS.md` lists the supported releases and any release candidate at the snapshot.

## Seed list (late 2026)

| Date | Change | Link |
|---|---|---|
| 2026-09-29 | External custom properties | https://github.blog/changelog/2026-09-29-bring-business-context-with-external-custom-properties |
| 2026-10-13 | GitHub App improvements for least privilege and management | https://github.blog/changelog/2026-10-13-github-app-improvements-for-least-privilege-and-management |
| 2026-10-20 | Bulk migrate branch protections to rulesets | https://github.blog/changelog/2026-10-20-bulk-migrate-branch-protections-to-rulesets-for-a-repository |
| 2026-11-10 | GitHub App support for enterprise Copilot seat management | https://github.blog/changelog/2026-11-10-github-app-support-for-enterprise-copilot-seat-management |
| 2026-11-19 | S3 audit log streaming with OIDC on GHE.com | https://github.blog/changelog/2026-11-19-s3-audit-log-streaming-with-openid-connect-expands-to-ghe-com |
| 2026-11-20 | Security advisory permissions GA | https://github.blog/changelog/2026-11-20-security-advisory-permissions-are-now-generally-available |

This list is a starting point, not a complete record. Read the linked entry for the actual scope and limits before relying on it.
