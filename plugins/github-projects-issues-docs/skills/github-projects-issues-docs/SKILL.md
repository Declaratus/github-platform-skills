---
name: github-projects-issues-docs
description: Look up GitHub's official Projects and Issues documentation (content/issues from github/docs), bundled locally, plus a pointer to the Projects and Issues changelog for newer changes. Covers GitHub Projects boards, tables and roadmaps, custom fields (single select, iteration, date, number, text), views, filters, hierarchy view, auto-add and built-in workflows, archiving, Actions and API automation, insights and charts, project templates, project access and visibility, sub-issues, issue dependencies, issue types, issue fields, issue relationships, labels and milestones, and the Projects API (GraphQL and REST). Use when planning or configuring a Projects board, designing an issue hierarchy or type/field scheme, scripting project automation, or when the user needs the documented behaviour instead of a guess.
---

# GitHub Projects and Issues docs

Local copy of https://docs.github.com/en/issues, built from `content/issues` in https://github.com/github/docs. Answers "how does Projects or Issues do X" and "how do I configure X". For "what should our org standardise on and why", pair with the `github-well-architected` skill.

Projects and Issues changed a lot in 2025 and 2026 (sub-issues, issue types, issue fields, hierarchy view, multi-select, "Relates to"). Prefer these docs over memory for field types, limits, automation behaviour and permission rules, and cite the page you used.

## Check for newer changes first

The docs snapshot lags the product. Read `changelog.md` (next to this file) and check the label feed it points at for anything newer than the `upstream_committed_at` date in `references/SOURCE.json`. Some recent features (for example hierarchy view, multi-select fields and the "Relates to" relationship) may be described only in the changelog at snapshot time. Preserve preview vs GA status and plan or account-type qualifications as stated.

## How to find the right page

1. Pick the section from the table below.
2. Read that section's `index.md`. Its `children:` frontmatter lists pages in order.
3. Otherwise `Grep` the whole `references/` tree for the feature or field name. File names match URL slugs.

| Topic | Start in |
|---|---|
| What Projects are, best practices, quickstart | `references/planning-and-tracking-with-projects/learning-about-projects/` |
| Creating or copying projects, templates | `.../creating-projects/`, `.../managing-your-project/managing-project-templates-in-your-organization.md` |
| Fields (iteration, single select, date, issue type, issue fields, sub-issue progress) | `.../understanding-fields/` |
| Views, layouts (table, board, roadmap), filters, grouping | `.../customizing-views-in-your-project/` |
| Built-in workflows, auto-add, auto-archive, Actions, API | `.../automating-your-project/` |
| Access, visibility, linking to repos and teams, export | `.../managing-your-project/` |
| Insights and charts | `.../viewing-insights-from-your-project/` |
| Sub-issues, dependencies, issue types, issue fields | `references/tracking-your-work-with-issues/using-issues/` |
| Issue admin (transfer, close, delete, duplicates, AI triage) | `references/tracking-your-work-with-issues/administering-issues/` |
| Labels and milestones | `references/using-labels-and-milestones-to-track-work/` |

`...` is `references/planning-and-tracking-with-projects`.

## Common entry points

- Projects API from GraphQL and the `gh` CLI: `planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects.md`. Actions examples: `.../automating-your-project/automating-projects-using-actions.md`.
- Built-in workflows and auto-add limits: `.../automating-your-project/using-the-built-in-automations.md`, `.../adding-items-automatically.md`.
- Hierarchy and sub-issues: `tracking-your-work-with-issues/using-issues/adding-sub-issues.md`, `.../browsing-sub-issues.md`, `planning-and-tracking-with-projects/understanding-fields/about-parent-issue-and-sub-issue-progress-fields.md`.
- Issue types: `tracking-your-work-with-issues/using-issues/managing-issue-types.md`, `planning-and-tracking-with-projects/understanding-fields/about-the-issue-type-field.md`.
- Issue fields: `tracking-your-work-with-issues/using-issues/managing-issue-fields.md`, `.../adding-and-managing-issue-fields.md`, `planning-and-tracking-with-projects/understanding-fields/about-issue-fields.md`. Distinguish org-level issue fields from per-project custom fields.
- Dependencies (blocked by / blocking): `tracking-your-work-with-issues/using-issues/creating-issue-dependencies.md`.
- Access and visibility: `.../managing-your-project/managing-access-to-your-projects.md`, `.../managing-visibility-of-your-projects.md`.

The REST and GraphQL **reference** pages for Projects and Issues (endpoints, object schemas, fields, views, drafts) live under `content/rest` and `content/graphql` upstream and are not bundled. Cite them live: https://docs.github.com/en/rest/projects, https://docs.github.com/en/graphql/reference/projects and https://docs.github.com/en/graphql/reference/issues.

## Reading the pages

Product-name variables and reusable snippets are resolved at build time. Remaining github/docs conventions:

- `[AUTOTITLE](/issues/a/b)` links another page. Map it to `references/a/b.md` or `references/a/b/index.md`. Links outside `/issues/` are not bundled; cite them as `https://docs.github.com/en<path>`.
- If that local path does not exist, search frontmatter `redirect_from:` for the original `/issues/...` path. A redirect alias is not a missing page.
- `versions: feature: <name>` frontmatter and `{% ifversion ... %}` blocks gate text by deployment or feature flag. `fpt`/`ghec` is GitHub.com, `ghes` is GitHub Enterprise Server. Use the branch matching the user's deployment, and don't assume a GitHub.com feature exists on GHES.
- `{% raw %}...{% endraw %}` wraps literal Actions expressions in examples. Drop the wrapper when copying YAML.
- `(icon: name)` marks a UI icon next to a button label. Images were stripped; alt text remains.

When citing, give the live URL: `references/a/b.md` is `https://docs.github.com/en/issues/a/b`.

## Source attribution

GitHub Docs content, © GitHub, licensed CC BY 4.0 (`references/LICENSE`). Modified from upstream: Liquid data tags resolved to plain text, octicons flattened, images removed. Rebuild with `./build/build.sh github-projects-issues-docs`.
