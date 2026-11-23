---
name: github-billing-docs
description: Look up GitHub's official billing documentation (content/billing from github/docs), bundled locally, plus a pointer to the changelog for newer changes. Covers metered vs volume/subscription billing, billing cycles, budgets and alerts (hard vs soft, scopes, SKU-level), cost centers and allocation, product billing for Actions, Packages, Codespaces, Git LFS, Advanced Security (active committers), Code Quality, Copilot licenses and sandboxes, product and SKU identifiers, billing usage and license reports, the billing usage REST API, billing roles and billing managers, Azure subscription and Visual Studio billing, GHES license files and license sync, plan upgrades and downgrades, payment methods, invoices, sales tax, and billing troubleshooting. Use when estimating or controlling GitHub spend, designing a cost center or budget scheme, scripting usage reporting, explaining a charge or license count, or when the user needs the documented billing behaviour instead of a guess.
---

# GitHub billing docs

Local copy of https://docs.github.com/en/billing, built from `content/billing` in https://github.com/github/docs. Answers "how is X billed", "how do I control or report on spend" and "who can see or change billing". For "what should our org standardise on and why", pair with the `github-well-architected` skill.

Billing changed a lot in 2025 and 2026 (enhanced billing platform, metered enterprise licenses, cost centers, hard budgets, AI credits). Prefer these docs over memory for what is billed, how it is counted, which budgets actually stop usage, and who has permission, and cite the page you used.

## Check for newer changes first

The docs snapshot lags the product. Read `changelog.md` (next to this file) for anything newer than the `upstream_committed_at` date in `references/SOURCE.json`. Budget limits, SKU lists and REST endpoints move fastest.

## Copilot billing lives in another skill

`references/concepts/product-billing/github-copilot-billing.md` here is a short router. The detail on AI credits, included allowances, pooling, Copilot budgets and per-model pricing is under `content/copilot` upstream. Use the `github-copilot-docs` skill for those (its `references/concepts/billing-and-usage/` and `references/reference/copilot-billing/`). This skill still covers the shared mechanics Copilot sits on: budgets, cost centers, SKU names, usage reports, seat licensing and billing roles.

## How to find the right page

1. Pick the section from the table below.
2. Read that section's `index.md`. Its `children:` frontmatter lists pages in order.
3. Otherwise `Grep` the whole `references/` tree for the product, SKU or setting name. File names match URL slugs.

| Topic | Start in |
|---|---|
| What is charged, when, authorization holds | `references/get-started/how-billing-works.md`, `.../introduction-to-billing.md` |
| Billing cycles, plan changes, discounts | `references/concepts/` (top-level pages) |
| Budgets and alerts, stopping usage | `references/concepts/budgets-and-alerts.md`, `references/how-tos/set-up-budgets.md` |
| Cost centers | `references/concepts/cost-centers.md`, `references/reference/cost-center-allocation.md`, `references/how-tos/products/use-cost-centers.md` |
| Per-product billing (Actions, Packages, Codespaces, LFS, GHAS, Code Quality, sandboxes) | `references/concepts/product-billing/` |
| Actions runner prices, included usage per plan | `references/reference/actions-runner-pricing.md`, `.../product-usage-included.md` |
| Enterprise licensing, metered licenses, GHES, Visual Studio, ADO | `references/concepts/enterprise-billing/` |
| Product and SKU identifiers for budgets and the API | `references/reference/product-and-sku-names.md` |
| Usage and license reports, report fields | `references/reference/billing-reports.md`, `.../license-reports.md`, `references/how-tos/products/` |
| Who can do what (owners, billing managers) | `references/reference/billing-roles.md` |
| Payment methods, invoices, Azure subscriptions, tax | `references/how-tos/set-up-payment/`, `references/reference/supported-payment-methods.md` |
| GHES license files and license sync | `references/how-tos/manage-server-licenses/` |
| Partners and client accounts | `references/how-tos/manage-for-client/` |
| Marketplace apps and Sponsors | `references/concepts/third-party-payments/`, `references/how-tos/pay-third-parties/` |
| Declined cards, locked accounts, license count surprises | `references/how-tos/troubleshooting/` |

## Common entry points

- Cost control end to end (cost center strategy, budgets in the UI and REST API, automation): `tutorials/control-costs-at-scale.md`. Starting smaller: `tutorials/soft-budgets.md`.
- Hard vs soft budgets: `concepts/budgets-and-alerts.md`, section "Stopping usage". A budget on a license-based product (Copilot seats, Team, Enterprise) alerts but does not stop usage. Metered products and GHAS SKUs can be capped, with different effects. Don't promise a cap the docs don't describe.
- GHAS licensing (unique active committers, 90-day window, what a hard budget blocks): `concepts/product-billing/github-advanced-security.md`, `how-tos/products/view-ghas-committers.md`.
- Usage reporting from the REST API (token types, filters, response fields): `tutorials/automate-usage-reporting.md`. Check the token requirements there before writing a script; billing usage endpoints do not accept every token type.
- Metered enterprise licenses (who counts, how seats are measured): `concepts/enterprise-billing/usage-based-licenses.md`, `reference/github-license-users.md`.
- Estimating spend: `how-tos/products/estimate-spending.md`.

Paths in this list are under `references/`.

The REST **reference** pages for billing (usage, budgets, cost centers) live under `content/rest` upstream and are not bundled. Cite them live, for example https://docs.github.com/en/rest/billing/usage.

## Reading the pages

Product-name variables and reusable snippets are resolved at build time. Remaining github/docs conventions:

- `[AUTOTITLE](/billing/a/b)` links another page. Map it to `references/a/b.md` or `references/a/b/index.md`. Links outside `/billing/` are not bundled; cite them as `https://docs.github.com/en<path>`.
- If that local path does not exist, search frontmatter `redirect_from:` for the original `/billing/...` path. Billing pages were renamed several times, so old paths usually resolve this way.
- `versions:` frontmatter and `{% ifversion ... %}` blocks gate text by deployment or feature flag. `fpt` is GitHub.com Free/Pro/Team, `ghec` is Enterprise Cloud, `ghes` is Enterprise Server. Use the branch matching the user's account type, and say so when the answer differs between them. Feature flag definitions are not bundled. At the snapshot, the billing ones map to:

  | Flag | Applies to |
  |---|---|
  | `enhanced-billing-platform`, `code-quality`, `code-security-risk-assessment`, `copilot` | fpt, ghec |
  | `enterprise-billing-github-app` (GitHub App auth for enterprise billing APIs) | ghec, ghes 3.23+ |
  | `enterprise-licensing-language` | ghec, ghes 3.17+ |
  | `disable-ghas-button` | fpt, ghec, ghes 3.22+ |
  | `repository-collaborators` | ghec |

  An unlisted flag means the snapshot gained one. Check `data/features/<flag>.yml` upstream rather than guessing.
- `(icon: name)` marks a UI icon next to a button label. Images were stripped; alt text remains.

Prices, included minutes and storage allowances in these pages are a snapshot. Quote them with the snapshot date and point to the live page for anything that will drive a purchase.

When citing, give the live URL: `references/a/b.md` is `https://docs.github.com/en/billing/a/b`.

## Source attribution

GitHub Docs content, © GitHub, licensed CC BY 4.0 (`references/LICENSE`). Modified from upstream: Liquid data tags resolved to plain text, octicons flattened, images removed. Rebuild with `./build/build.sh github-billing-docs`.
