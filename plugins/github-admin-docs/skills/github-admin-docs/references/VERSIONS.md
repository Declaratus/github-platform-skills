# Versions at this snapshot

Generated from upstream `src/versions/lib/enterprise-server-releases.ts` and `data/features/` at the pinned commit (see `SOURCE.json`).

## GitHub Enterprise Server releases

Supported, newest first: 3.23, 3.22, 3.21, 3.20, 3.19.
Release candidate: 3.23 (not yet generally available).

## Feature flags used in these pages

`{% ifversion <flag> %}` and `versions: feature: <flag>` text applies only to the versions listed. `fpt` is GitHub Free/Pro/Team, `ghec` is GitHub Enterprise Cloud, `ghes` is GitHub Enterprise Server.

| Flag | Versions |
|---|---|
| `actions-hosted-runners` | fpt `*`, ghec `*` |
| `actions-workflow-lockfiles` | fpt `*`, ghec `*` |
| `actions-workflow-policy` | fpt `*`, ghec `*` |
| `ai-applications-scanning` | ghec `*`, fpt `*` |
| `ai-powered-security-detections` | ghec `*`, fpt `*` |
| `artifacts-v3-deprecation` | fpt `*`, ghec `*` |
| `audit-log-streaming-for-api` | fpt `*`, ghec `*` |
| `audit-log-streaming-health-check` | ghec `*`, ghes `>= 3.14` |
| `backup-service-cluster-ha` | ghes `>=3.20` |
| `cluster-ha-replication` | ghes `<3.22` |
| `code-quality` | fpt `*`, ghec `*` |
| `code-scanning-autofix` | ghec `*`, fpt `*` |
| `copilot` | fpt `*`, ghec `*` |
| `custom-org-roles` | ghec `*`, ghes `>=3.14` |
| `custom-properties-enterprise` | ghec `*`, ghes `>= 3.18` |
| `custom-properties-required-explicit-values` | fpt `*`, ghec `*`, ghes `> 3.20` |
| `dedicated-redis-cluster-node` | ghes `>=3.23` |
| `dependabot-delegated-alert-dismissal` | fpt `*`, ghec `*`, ghes `> 3.20` |
| `dependabot-malware-alerts` | fpt `*`, ghec `*`, ghes `> 3.21` |
| `deploy-keys-enterprise-org-policy` | ghec `*`, ghes `>= 3.16` |
| `emu-owned-repos` | ghec `*` |
| `emu-public-scim-schema` | ghec `*` |
| `ent-owner-custom-org-roles` | ghec `*`, ghes `>3.18` |
| `ent-security-manager` | ghec `*`, ghes `>=3.20` |
| `enterprise-app-manager` | ghec `*`, ghes `>=3.19` |
| `enterprise-apps-public-beta` | ghec `*`, ghes `>=3.17` |
| `enterprise-audit-log-ip-addresses` | ghec `*` |
| `enterprise-code-rulesets` | ghec `*` |
| `enterprise-custom-roles` | ghec `*`, ghes `>=3.20` |
| `enterprise-installed-apps` | ghec `*`, ghes `>=3.19` |
| `enterprise-licensing-language` | ghec `*`, ghes `>=3.17` |
| `enterprise-manage-organization-members` | ghec `*` |
| `enterprise-member-csv` | ghec `*` |
| `enterprise-orgs-sponsors-with-cc` | ghec `*` |
| `enterprise-readme` | ghec `*`, ghes `>=3.13` |
| `enterprise-teams` | ghec `*`, ghes `>=3.20` |
| `enterprise-teams-ga` | ghec `*`, ghes `>=3.22` |
| `enterprise-token-inventory` | ghec `*` |
| `external-custom-properties` | fpt `*`, ghec `*` |
| `ghas-in-license-sync` | ghec `*`, ghes `>=3.12` |
| `ghecom-github-connect` | ghes `>=3.12` |
| `ghes-collectd-available` | ghes `<3.23` |
| `ghes-manage-api-cli-extension` | ghes `>=3.11` |
| `ghes-node-eligibility-service-available` | ghes `<3.23` |
| `ghes-opentelemetry` | ghes `>=3.18` |
| `ghes-replication-controller` | ghes `>=3.21` |
| `ghes-replication-controller-expanded-services` | ghes `>=3.22` |
| `guest-collaborators` | ghec `*` |
| `idp-tenant-migration` | ghec `*` |
| `internal-actions` | ghec `*`, ghes `>=3.5` |
| `mandatory-2fa-dotcom-contributors` | fpt `*`, ghec `*` |
| `mandatory-2fa-required-overview` | fpt `*`, ghec `*` |
| `oidc-for-emu` | ghec `*` |
| `pause-audit-log-stream` | ghec `*` |
| `project-visibility-policy` | ghec `*` |
| `prometheus-metrics-exporter` | ghes `>=3.16 <3.23` |
| `proof-of-presence` | ghec `*`, ghes `>=3.23` |
| `push-rule-allowed-exceptions` | fpt `*`, ghec `*` |
| `push-rule-delegated-bypass` | ghec `*`, ghes `>3.15` |
| `remove-enterprise-members` | ghec `*` |
| `repo-admin-branch-rename` | fpt `*`, ghec `*`, ghes `>=3.22` |
| `repo-policy-rules` | ghec `*` |
| `repo-rules-enterprise` | ghec `*`, ghes `>3.10` |
| `repo-rules-history` | ghec `*`, ghes `>=3.19` |
| `repository-collaborators` | ghec `*` |
| `revoke-enterprise-tokens` | ghec `*` |
| `saml-nameid-case-sensitive-upgrade` | ghes `>=3.19 <3.23` |
| `scim-enterprise-scope` | ghec `*`, ghes `>=3.16` |
| `scim-for-ghes-ga` | ghes `>=3.17` |
| `scim-for-ghes-public-beta` | ghes `>=3.14` |
| `secret-scanning-actions-logs` | ghec `*` |
| `secret-scanning-ai-generic-secret-detection` | fpt `*`, ghec `*`, ghes `>=3.23` |
| `security-and-quality-tab` | fpt `*`, ghec `*` |
| `security-feature-enablement-policies-dependabot` | ghec `*`, ghes `>=3.9` |
| `single_user_cred_revocation` | fpt `*`, ghec `*` |
| `ssh-ca-expires` | ghec `*`, ghes `>=3.13` |
| `ssh-user-ca` | ghec `*`, ghes `>= 3.14` |
| `sso-redirect` | ghec `*` |
| `streaming-oidc-s3` | ghec `*` |
| `team-sync-manage-org-invites` | ghec `*` |
| `token-audit-log-more-metadata` | ghec `*` |
| `unaffiliated-users` | fpt `*`, ghec `*` |
| `virtual-registry` | fpt `*`, ghec `*` |
