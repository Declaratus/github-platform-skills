---
name: github-admin-docs
description: Look up GitHub's official enterprise administration documentation (content/admin from github/docs), bundled locally, with a generated table of supported GitHub Enterprise Server releases and feature-flag version ranges, plus changelog and release-notes pointers. Covers GitHub Enterprise Cloud enterprise accounts, Enterprise Managed Users (EMU), GHE.com data residency, and GitHub Enterprise Server (GHES) installation, configuration, upgrades and hotpatches, backups and the backup service, high availability, clustering, geo-replication, monitoring (collectd, OpenTelemetry, SNMP), the Management Console and administrative shell (ghe-* utilities), SAML, OIDC, LDAP, CAS, SCIM provisioning, IdP group team sync, recovery codes, enterprise roles and custom roles, enterprise teams, enterprise policies (repository, Actions, Copilot, code security, PATs), pre-receive hooks, audit log search and streaming, IP allow lists, GitHub Connect, Actions and Packages storage on GHES, and enterprise GitHub Apps. Use when an enterprise owner or site administrator asks how to configure, operate, upgrade or troubleshoot their enterprise or instance, whether something works on GHES or a given version, or needs the documented procedure instead of a guess.
---

# GitHub enterprise admin docs

Local copy of https://docs.github.com/en/admin, built from `content/admin` in https://github.com/github/docs. Answers "how does enterprise admin do X", "how do I configure X" and "does X exist on my deployment". For "what should our enterprise standardise on and why", pair with the `github-well-architected` skill. Copilot policies and billing are covered in more depth by `github-copilot-docs`.

## Pin down the deployment first

The same page often says different things for each deployment, and many pages exist for only one. Before answering, establish which one the user runs, from what they said or by asking:

- **GitHub Enterprise Cloud** on GitHub.com, with personal accounts or with **Enterprise Managed Users**. EMU changes a lot (who can create repos, what users can see, how authentication works), so find out which.
- **GHE.com** (Enterprise Cloud with data residency). Always EMU. See `references/data-residency/` for what differs.
- **GitHub Enterprise Server**, and which version. Version matters for most GHES answers.

If the user doesn't say and it changes the answer, give both and label them, rather than guessing.

## Read version gates, don't skip them

Pages keep their Liquid version blocks. Read them against the user's deployment:

- `fpt` is Free/Pro/Team, `ghec` is Enterprise Cloud, `ghes` is Enterprise Server. `{% ifversion ghes %}...{% else %}...{% endif %}` means the first branch is GHES only and the `else` branch is everything else.
- `{% ifversion ghes > 3.19 %}` and similar compare against GHES release numbers. `references/VERSIONS.md` lists the supported releases at the snapshot (and any release candidate, which is not GA yet).
- Any other name in an `ifversion`, or under `versions: feature:` in frontmatter, is a feature flag. Look it up in `references/VERSIONS.md` to see which deployments and GHES versions it covers. A flag with a range like `ghes '>=3.14'` that starts below the oldest supported release applies to every supported GHES version.
- `{{ enterpriseServerReleases.latest }}`, `.supported[1]`, `.oldestSupported` and similar are unrendered placeholders. Fill them from the supported list in `references/VERSIONS.md`: `latest` is the first entry (which may be the release candidate), `supported[n]` is the entry at index n counting from 0, `oldestSupported` is the last.
- Frontmatter `versions:` tells you whether the whole page applies. A page with only `ghes: '*'` does not apply to Enterprise Cloud.

Say which branch you used ("on GHES 3.20 and later..."), so the user can spot a wrong assumption.

## Check for newer changes

The docs snapshot lags the product and does not include GHES release notes. Read `changelog.md` (next to this file) when the question is about recent features, preview vs GA status, known issues, or upgrade planning for a specific GHES version. Compare against `upstream_committed_at` in `references/SOURCE.json`.

## How to find the right page

1. Pick the section from the table below.
2. Read that section's `index.md`. Its `children:` frontmatter lists pages in order.
3. Otherwise `Grep` the whole `references/` tree for the feature, setting or `ghe-` command name. File names match URL slugs.

| Topic | Start in |
|---|---|
| Choosing Cloud vs Server, EMU vs personal accounts, roles, teams, governance | `concepts/`, `overview/` |
| Enterprise account settings (create, rename URL, delete, display names) | `managing-your-enterprise-account/` |
| GHE.com data residency | `data-residency/` |
| Authentication and provisioning (SAML, OIDC, LDAP, CAS, SCIM, recovery codes, incidents) | `managing-iam/` |
| Users, orgs, repos, enterprise teams, roles and custom roles | `managing-accounts-and-repositories/` |
| Enterprise policies (repos, Actions, Copilot, code security, PATs, Codespaces), pre-receive hooks | `enforcing-policies/` |
| Audit log (search, export, streaming, API), server statistics, global webhooks, log forwarding | `monitoring-activity-in-your-enterprise/` |
| IP allow list, GitHub Connect, private networking for hosted runners, rate limits, email, TLS, firewall | `configuring-settings/` |
| Enterprise GitHub Apps | `managing-github-apps-for-your-enterprise/` |
| Actions for the enterprise; on GHES, storage backends and offline actions | `managing-github-actions-for-your-enterprise/` |
| Packages on GHES | `configuring-packages/` |
| GHES install on each platform, staging instances | `installing-your-enterprise-server/` |
| GHES Management Console, admin shell, `ghe-*` utilities, maintenance mode | `administering-your-instance/` |
| GHES upgrades, hotpatches, upgrade requirements, known issues | `upgrading-your-instance/` |
| GHES backups (backup service and Backup Utilities), restore | `backing-up-and-restoring-your-instance/` |
| GHES HA, clustering, geo-replication, repository caching, monitoring, resizing | `monitoring-and-managing-your-instance/` |
| GHES symptom-based troubleshooting | `troubleshooting-your-instance/` |

All paths are under `references/`.

## Common entry points

- `ghe-*` command reference: `administering-your-instance/administering-your-instance-from-the-command-line/command-line-utilities.md` (large, grep it for the command).
- EMU: `managing-iam/understanding-iam-for-enterprises/getting-started-with-enterprise-managed-users.md`, `.../abilities-and-restrictions-of-managed-user-accounts.md`, `concepts/identity-and-access-management/enterprise-managed-users.md`.
- SCIM: `managing-iam/provisioning-user-accounts-with-scim/` (Entra ID, Okta, PingFederate, REST API, GHES-specific page `user-provisioning-with-scim-on-ghes.md`).
- Locked out by the IdP: `managing-iam/managing-recovery-codes-for-your-enterprise/accessing-your-enterprise-account-if-your-identity-provider-is-unavailable.md`.
- Audit log streaming: `monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise.md`. Event names: `.../audit-log-events-for-your-enterprise.md`.
- Upgrades: `upgrading-your-instance/preparing-to-upgrade/overview-of-the-upgrade-process.md`, `.../upgrade-requirements.md`, `upgrading-your-instance/troubleshooting-upgrades/known-issues-with-upgrades-to-your-instance.md`.
- HA vs clustering: `monitoring-and-managing-your-instance/configuring-clustering/differences-between-clustering-and-high-availability-ha.md`.
- Backups: `backing-up-and-restoring-your-instance/` covers both the built-in backup service and GitHub Enterprise Server Backup Utilities. Check which one the user runs, and which the version gates allow.
- Actions on GHES: `managing-github-actions-for-your-enterprise/getting-started-with-github-actions-for-your-enterprise/getting-started-with-github-actions-for-github-enterprise-server.md`, then the storage page under `enabling-github-actions-for-github-enterprise-server/`.

## Operations that are hard to undo

Many GHES procedures (failover with `ghe-repl-promote`, replica removal, cluster node replacement, restores, hostname changes, disabling SAML or SCIM, deleting an enterprise) cause downtime, lose data or lock users out if done out of order. When the user is about to run one, quote the documented steps and their warnings in order, point out prerequisites such as maintenance mode, a fresh backup or recovery codes, and say what can't be reversed. Don't invent flags or commands the page doesn't show.

## What is not bundled

These live in other `content/` sections upstream. Cite them live:

- Enterprise and site-admin REST API endpoints (`/rest/enterprise-admin`): https://docs.github.com/en/rest/enterprise-admin. On GHES, use `https://docs.github.com/en/enterprise-server@<version>/rest/enterprise-admin`.
- Billing, licences and cost centres: https://docs.github.com/en/billing
- Organization-level settings: https://docs.github.com/en/organizations
- Migrations to GitHub (GEI, ADO, Bitbucket, GHES to Cloud): https://docs.github.com/en/migrations
- GHES release notes and the support matrix: see `changelog.md`.

## Reading the pages

Product-name variables and reusable snippets are resolved at build time. Remaining github/docs conventions:

- `[AUTOTITLE](/admin/a/b)` links another page. Map it to `references/a/b.md` or `references/a/b/index.md`. Links with a version prefix such as `/enterprise-cloud@latest/admin/a/b` or `/enterprise-server@latest/admin/a/b` point at the same local page, read with that deployment's branch. Links outside `/admin/` are not bundled; cite them as `https://docs.github.com/en<path>`.
- If that local path does not exist, search frontmatter `redirect_from:` for the original `/admin/...` path. A redirect alias is not a missing page.
- `release-notes.md`, `all-releases.md` and `enterprise-onboarding.md` are rendered from layouts or data that are not bundled. Use their live URLs.
- `{% raw %}...{% endraw %}` wraps literal expressions in examples. Drop the wrapper when copying.
- `(icon: name)` marks a UI icon next to a button label. Images were stripped; alt text remains.

When citing, give the live URL: `references/a/b.md` is `https://docs.github.com/en/admin/a/b` for Enterprise Cloud, and `https://docs.github.com/en/enterprise-server@<version>/admin/a/b` for a GHES version.

## Source attribution

GitHub Docs content, © GitHub, licensed CC BY 4.0 (`references/LICENSE`). Modified from upstream: Liquid data tags resolved to plain text, octicons flattened, images removed, `VERSIONS.md` generated from upstream version data. Rebuild with `./build/build.sh github-admin-docs`.
