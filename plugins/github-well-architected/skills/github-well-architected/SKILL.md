---
name: github-well-architected
description: Apply GitHub's Well-Architected Framework — prescriptive design thinking and recommendations for deploying GitHub Enterprise at scale across five pillars (Productivity, Collaboration, Application Security, Governance, Architecture). Use for organization-level decisions about repository structure, rulesets, GHAS rollout, Copilot adoption, polyrepo vs monorepo, migrations (ADO, etc.), governance policies, custom properties, and other "how should we use GitHub" questions where GitHub Docs answers "how do I configure it" but you need "what should we do and why".
---

# GitHub Well-Architected Framework

Community-driven, opinionated guidance for adopting and deploying GitHub effectively. Sourced from https://github.com/github/github-well-architected (the static-site source for https://wellarchitected.github.com).

This skill captures **design thinking**, not configuration instructions. For "how do I turn on Dependabot," consult GitHub Docs. For "should we enforce GHAS at scale, and how do we sequence the rollout," consult this framework.

## When to use this skill

Load this skill when the user is making **organization-level decisions** about GitHub deployment, not single-feature configuration. Concrete triggers:

- Designing or auditing **repository rulesets**, branch protections, custom properties, or repository taxonomies
- Planning a **GHAS / code scanning / Dependabot rollout** across many repos
- Deciding **polyrepo vs monorepo**, when to use Git LFS, how to scale large repositories
- **Copilot at scale**: champion programs, adoption metrics, governing AI agents, managing AI credits
- **Migrations**: Azure DevOps → GitHub, repository checklists, source-environment assessment
- **Governance**: policy best practices, administration essentials, governing agents, NIST-SSDF implementation
- **Engineering metrics**: measuring GenAI impact, engineering system metrics, DevOps methodology
- Comparing GitHub Well-Architected to Azure/AWS Well-Architected frameworks
- Any question that starts with "what's the right way to..." at the platform/org level

Do **not** use this skill for:
- Single-repo configuration ("how do I add a CODEOWNERS file") — that's GitHub Docs
- Code review of a specific PR — that's the code-review skill
- Anything outside the GitHub platform

## Framework structure

Three layers (`references/framework-overview.md` for full detail):

1. **Pillars** — strategic focus areas (the *what*)
2. **Design Principles** — concepts that guide decisions within each pillar (the *how*)
3. **Recommendations** — opinionated, prescriptive actions (the *do this*)

### The five pillars

| Pillar | Focus | Reference root |
|---|---|---|
| Productivity | Speed and efficiency: CI/CD, Actions, Packages, Copilot adoption | `references/library/productivity/` |
| Collaboration | Teamwork: PRs, code review, project boards, DevOps practices | `references/library/collaboration/` |
| Application Security | Securing apps: Dependabot, advisories, code scanning, GHAS | `references/library/application-security/` |
| Governance | Compliance and controls: permissions, audit logs, policies | `references/library/governance/` |
| Architecture | Designing the GitHub environment: scalability, reliability, repo structure | `references/library/architecture/` |

Each pillar directory contains:
- `_index.md` — pillar landing page
- `design-principles.md` — the *how* for that pillar
- `checklist.md` — assessment checklist
- `quick-links.md` — curated entry points
- `recommendations/` — the *do this* prescriptive guides

## How to navigate the references

When the user asks a question, **identify the pillar first**, then look at:

1. `references/library/<pillar>/design-principles.md` for the underlying principles
2. `references/library/<pillar>/recommendations/` for specific guides

Cross-cutting content lives outside the pillar tree:

- `references/charter.md` — framework charter, mission, scope
- `references/framework-overview.md` — pillars, layers, comparison vs Azure/AWS WAF
- `references/taxonomies.md` — how content is categorized (use when authoring or organizing)
- `references/library/_index.md` — content library landing
- `references/library/overview/` — getting-started checklist, layers, assessment
- `references/library/scenarios/` — cross-pillar scenarios:
  - `anti-patterns.md` — what *not* to do
  - `monorepos.md` — monorepo guidance
  - `nist-ssdf-implementation.md` — NIST Secure Software Development Framework mapping
  - `measuring-genai-impact.md` — engineering metrics for AI tooling
  - `migrations/azure-devops-migration-guide/` — multi-part ADO→GitHub migration guide

## Notable recommendations by pillar

These are the recommendations most likely to come up:

**Governance** (`references/library/governance/recommendations/`):
- `governance-administration-essentials/` — admin baseline
- `governance-policies-best-practices/` — policy design
- `governing-agents.md` — governing AI/Copilot agents
- `managing-ai-credits.md` — AI credit allocation
- `managing-repositories-at-scale/` — including `rulesets-best-practices.md` and `custom-properties-best-practices.md`

**Architecture** (`references/library/architecture/recommendations/`):
- `implementing-polyrepo-engineering.md` — polyrepo strategy
- `scaling-git-repositories/` — large repos, when to use LFS, repo architecture
- `deploying-actions-runner-controller.md` — self-hosted ARC
- `hosted-runner-private-networking/` — VNet-injected runners
- `expanding-enterprise-custom-agents-context.md`

**Application Security** (`references/library/application-security/recommendations/`):
- `enforce-ghas-at-scale/` — rolling out GitHub Advanced Security
- `actions-security/` — securing Actions workflows
- `prioritizing-alerts/`
- `managing-dependency-threats.md`
- `securing-developer-workspace.md`
- `threat-model/` — threat modeling

**Collaboration** (`references/library/collaboration/recommendations/`):
- `applying-devops-methodology.md`
- `champion-program/` — internal champions
- `scaling-actions-reusability/` — reusable workflows

**Productivity** (`references/library/productivity/recommendations/`):
- `adopting-copilot-at-scale/`
- `engineering-system-metrics.md`

## Source attribution

Source repo: https://github.com/github/github-well-architected (MIT). Skill bundles a curated subset of markdown from `/content/library`, `/docs/framework-overview.md`, `/docs/taxonomies.md`, and `/charter.md`. Binary assets (PDFs, images, diagrams) removed; refer to the live site at https://wellarchitected.github.com for visuals.
