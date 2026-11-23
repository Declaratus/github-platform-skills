# Billing changes newer than the docs snapshot

github/docs does not carry the GitHub Changelog. The bundled `references/` tree is a snapshot (see `references/SOURCE.json` for the upstream commit date), and budget limits, SKUs and API endpoints often change before the docs catch up.

The changelog has no billing label. Billing entries are tagged "Account management" or "Enterprise management tools". Check for entries newer than the snapshot:

https://github.blog/changelog/label/account-management/

For "Enterprise management tools", filter the changelog index by that label: https://github.blog/changelog/. Where the changelog and the docs disagree, the newer dated source wins, and say which one you used.

## Seed list (2026)

| Date | Change |
|---|---|
| 2026-10-13 | Search and filter for budgets |
| 2026-10-15 | Download GitHub Code Quality license usage as CSV |
| 2026-11-03 | Look up a resource's cost center with the REST API |
| 2026-11-16 | Budget limit raised to 40,000 budgets per account |

This list is a starting point, not a complete record. Read the entry on the changelog for the actual scope and limits before relying on it.
