---
name: github-migrations-docs
description: Look up GitHub's official migration documentation (content/migrations from github/docs), bundled locally. Covers choosing a migration path, GitHub Enterprise Importer (GEI) and the gh gei, gh ado2gh, gh bbs2gh and gh gl2gh CLI extensions, migrations from Azure DevOps, Bitbucket Server and Data Center, GitLab, GitHub Enterprise Server and between GitHub.com accounts or EMU enterprises, Enterprise Live Migrations (ELM) to GHE.com, ghe-migrator, GitHub Importer and command-line imports from SVN, Mercurial, TFVC and Perforce, what data is and is not migrated, size limits, mannequins and reclaiming them, migrator role and token scopes, blob storage, migration logs, ruleset bypasses, and troubleshooting. Use when planning, scoping or running a repository or organization migration to or between GitHub products, or when the user needs the documented answer instead of a guess. Runs in an isolated subagent that cannot see the conversation, so pass the complete question as the argument, including source platform and version, destination (GitHub.com, GHE.com with data residency, EMU or not, GHES and version), and scale when known.
argument-hint: "<question, with source, destination and scale>"
context: fork
agent: Explore
background: false
---

# GitHub migrations docs

Question: $ARGUMENTS

Answer the question above from GitHub's migration documentation. You cannot see the conversation that asked it. The source platform and the destination decide which tool and which page apply. If either matters and the question does not say, answer for each relevant case instead of guessing one.

Local copy of https://docs.github.com/en/migrations, built from `content/migrations` in https://github.com/github/docs. Answers "which tool migrates X to Y", "what comes across and what doesn't" and "how do I run it". For "how should our org approach the migration and why" (sequencing, org structure, governance after the move), say in your answer that the `github-well-architected` skill covers it.

All `references/` paths below are under `${CLAUDE_SKILL_DIR}/references/`.

Read `references/SOURCE.json` for the immutable upstream revision, source commit date, build inputs and dependencies. These pages are a snapshot. Size limits, preview status and supported paths change; when they affect the answer, check the changelog and the live page (see "Checking for newer changes").

## Pick the tool first

Most wrong answers come from mixing up tools. The path decides the tool, and each tool has its own CLI, auth, data coverage and limits.

| Tool | Paths | Notes |
|---|---|---|
| GitHub Enterprise Importer (GEI) | ADO Services, Bitbucket Server/DC, GitLab, GHES 3.4.1+, GitHub.com to GitHub Enterprise Cloud (incl. GHE.com, EMU) | Source, history and metadata. Repo is unavailable during its migration. CLI: `gh gei`, `gh ado2gh`, `gh bbs2gh`, `gh gl2gh`. |
| Enterprise Live Migrations (ELM) | GHES or ADO Services to GHE.com only | Minimal downtime, continuous sync, monorepos. Fewer concurrent migrations than GEI. GHES path CLI: `gh elm`. The ADO path runs through Azure DevOps and is documented on Microsoft Learn, one repo at a time. |
| ghe-migrator | GitHub.com or GHES into GHES | Runs on the GHES appliance. |
| GitHub Importer, command line | Any Git, SVN, Mercurial, TFVC, Perforce, Bitbucket Cloud | Source and history only, no metadata. |

`references/overview/migration-paths-to-github.md` is the authority on scope, tooling and caveats for every source/destination pair, including paths that need GitHub Expert Services. Read it before recommending a tool.

## How to find the right page

1. Use the table above and `overview/migration-paths-to-github.md` to fix the tool and path.
2. Read that section's `index.md`. Its `children:` frontmatter lists pages in order (the ADO, GitLab and ELM guides are multi-part, read in sequence).
3. Otherwise `Grep` the whole `references/` tree for the command, flag, limit or data type. File names match URL slugs.

| Topic | Start in |
|---|---|
| Choosing a path, tooling overview, planning, locked repos | `references/overview/` |
| Mannequins and attributing user activity | `overview/mannequins-and-user-activity.md`, `using-github-enterprise-importer/completing-your-migration-with-github-enterprise-importer/` |
| GEI concepts and supported paths | `using-github-enterprise-importer/understanding-github-enterprise-importer/` |
| Azure DevOps (six-part guide) | `using-github-enterprise-importer/ado/` |
| GitLab | `using-github-enterprise-importer/migrate-from-gitlab/` |
| Bitbucket Server / Data Center | `using-github-enterprise-importer/migrating-from-bitbucket-server-to-github-enterprise-cloud/` |
| GHES or GitHub.com to GitHub Enterprise Cloud, EMU, data residency | `using-github-enterprise-importer/migrating-between-github-products/` |
| ELM, GHES to GHE.com | `references/elm/` |
| ghe-migrator (into GHES) | `references/using-ghe-migrator/` |
| Source-only imports (Git, SVN, Hg, TFVC, GitHub Importer) | `references/importing-source-code/` |
| Errors, migration logs, ruleset bypasses | `references/troubleshooting/` |

## Common entry points

- What GEI migrates and does not, size limits, branch protections, commit signatures: the "about" page for the path, for example `migrating-between-github-products/about-migrations-between-github-products.md`, `ado/understand-migrations-from-azure-devops-to-github.md`, `migrate-from-gitlab/understand-migrations.md`, `migrating-from-bitbucket-server-to-github-enterprise-cloud/about-migrations-from-bitbucket-server-to-github-enterprise-cloud.md`. Limits differ by path; quote the one for the user's source.
- Tokens, scopes and the migrator role: the `manage-access` or `managing-access-...` page in each path's folder, plus `ado/granting-the-migrator-role.md` and `migrate-from-gitlab/grant-the-migrator-role.md`.
- Blob storage for archives (Azure Blob, AWS S3, GitHub-owned storage, GHES 3.16+ local storage): `migrate-from-gitlab/configure-storage.md`, and the "Set up blob storage" step in `migrating-between-github-products/migrating-repositories-from-github-enterprise-server-to-github-enterprise-cloud.md`.
- Scripting via GraphQL rather than the CLI: `ado/use-graphql-to-migrate-repositories-from-azure-devops-to-github-enterprise-cloud.md`, `migrate-from-gitlab/use-graphql.md`, `overview/programmatically-importing-repositories.md`.
- Post-migration follow-up: `ado/follow-up-tasks.md`, `migrate-from-gitlab/follow-up-tasks.md`, `completing-your-migration-with-github-enterprise-importer/`.
- ADO to GitHub concept mapping (projects, pipelines, boards, permissions): `ado/key-differences-between-azure-devops-and-github.md`.
- ELM CLI flags and what ELM migrates: `elm/ghes-to-ghecom/elm-cli-reference.md`, `elm/ghes-to-ghecom/migrated-data-reference.md`.
- Rulesets blocking a migration push: `troubleshooting/setting-ruleset-bypasses-for-repository-migrations.md`.

Pipelines are not migrated by GEI. GitHub Actions Importer (for Azure Pipelines, Jenkins, GitLab CI and others) lives under `content/actions` upstream and is not bundled; cite https://docs.github.com/en/actions/tutorials/migrate-to-github-actions live.

## Reading the pages

Product-name variables and reusable snippets are resolved at build time. Remaining github/docs conventions:

- `[AUTOTITLE](/migrations/a/b)` links another page. Map it to `references/a/b.md` or `references/a/b/index.md`. Links outside `/migrations/` are not bundled; cite them as `https://docs.github.com/en<path>`.
- If that local path does not exist, search frontmatter `redirect_from:` for the original `/migrations/...` path. A redirect alias is not a missing page.
- `{% ifversion fpt or ghec %}...{% else %}...{% endif %}` splits GitHub.com from GitHub Enterprise Server (`ghes`) text. Use the branch matching where the user is reading or running the tool; GitHub Importer, for example, is not on GHES.
- `(icon: name)` marks a UI icon next to a button label. Images were stripped; alt text remains.

When citing, give the live URL: `references/a/b.md` is `https://docs.github.com/en/migrations/a/b`.

## Checking for newer changes

Read `${CLAUDE_SKILL_DIR}/changelog.md` whenever preview or GA status, limits or supported paths matter. It is a generated list of migration changelog entries from before the snapshot date up to the date it was built; for anything after that, check the feed it points at. The live docs lag the changelog, so a live page that still says "public preview" does not settle it. For example, ELM from Azure DevOps went GA on 2026-11-19 while the docs still said preview.

ELM from Azure DevOps is documented by Microsoft, not GitHub. For its data coverage, limits and workflow, fetch https://learn.microsoft.com/azure/devops/repos/enterprise-live-migrations/overview and say the facts came from there.

Then fetch the live docs page before answering when the answer depends on size limits, preview or GA status, supported source versions, CLI flags, or which paths a tool supports, or when the question says "current", "latest" or "now". Find the page in the snapshot first, then fetch its live version. Skip this for stable concepts and procedures.

Append `.md` to the live URL to get the rendered page as markdown:

```bash
curl -sL https://docs.github.com/en/migrations/overview/migration-paths-to-github.md
```

For a GHES destination (ghe-migrator), use `https://docs.github.com/en/enterprise-server@<version>/migrations/...` (or `@latest`). For GHE.com, use `https://docs.github.com/en/enterprise-cloud@latest/migrations/...`.

If the live page differs from the snapshot on something that affects the answer, use the live text and say what changed. If the fetch fails, answer from the snapshot and say it was not checked live.

## What to return

Your answer is all the caller sees. Return:

- The direct answer, naming the tool and path it applies to, with preview, version and destination qualifications.
- What will not come across, when the question is about planning or scope.
- The live URL of each page relied on.
- Whether each key fact came from the snapshot (give the commit date from `SOURCE.json`) or was checked live, and anything left unverified.

Keep it short. Do not paste whole pages.

## Source attribution

GitHub Docs content, © GitHub, licensed CC BY 4.0 (`references/LICENSE`). Modified from upstream: Liquid data tags resolved to plain text, octicons flattened, images removed. Rebuild with `./build/build.sh github-migrations-docs`.
