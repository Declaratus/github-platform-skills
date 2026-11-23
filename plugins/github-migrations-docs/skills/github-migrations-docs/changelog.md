# Migration changes newer than the docs snapshot

github/docs does not carry the GitHub Changelog. The bundled `references/` tree is a snapshot (see `references/SOURCE.json` for the upstream commit date), and migration tooling often changes status, limits or supported paths before the docs catch up. The live docs can lag too.

Before answering anything about preview vs GA status, size limits or which paths a tool supports, check the label feed for entries newer than the snapshot:

https://github.blog/changelog/label/enterprise-management-tools/feed/

Migration entries share that label with other enterprise admin changes, so filter titles for "migration", "Importer", "GEI" or "ELM". Older entries are on `?paged=2`, `?paged=3` and so on. Where the feed and the docs disagree, the newer dated source wins, and say which one you used.

## Seed list

| Date | Change | Link |
|---|---|---|
| 2026-11-19 | Enterprise Live Migrations from Azure DevOps GA (docs snapshot of 2026-11-23 still says public preview) | https://github.blog/changelog/2026-11-19-enterprise-live-migrations-from-azure-devops-generally-available |

This list is a starting point, not a complete record. Read the linked entry for the actual scope and limits before relying on it.
