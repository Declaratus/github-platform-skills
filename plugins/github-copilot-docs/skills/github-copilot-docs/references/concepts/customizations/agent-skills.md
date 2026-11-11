---
title: Agent skills
shortTitle: Agent skills
intro: 'Give Copilot repeatable workflows with task-specific instructions, scripts, and resources.'
product: "Copilot cloud agent is available for all paid Copilot plans.\n\nThe agent is available in all repositories stored on GitHub, except repositories owned by managed user accounts and where it has been explicitly disabled.<br><br>GitHub Copilot CLI is available with all Copilot plans. If you receive Copilot from an organization, the Copilot CLI policy must be enabled in the organization's settings.<br><a href=\"https://github.com/features/copilot/plans?ref_product=copilot&ref_type=purchase&ref_style=button\" target=\"_blank\" class=\"btn btn-primary mt-3 mr-3 no-underline\"><span>Sign up for Copilot</span> (icon: link-external)</a>"
versions:
  feature: copilot
category:
  - Learn about Copilot
  - Learn about Copilot CLI
contentType: concepts
redirect_from:
  - /copilot/concepts/agents/about-agent-skills
---

## About agent skills

Agent skills are folders of instructions, scripts, and resources that Copilot can load when relevant to improve its performance in specialized tasks. The Agent Skills specification is an [open standard](https://github.com/agentskills/agentskills), used by a range of different AI systems.

You can create your own skills to teach Copilot to perform tasks in a specific, repeatable way—or use skills shared online, for example in the [`anthropics/skills`](https://github.com/anthropics/skills) repository or GitHub's community-created [`github/awesome-copilot`](https://github.com/github/awesome-copilot) collection. 

For example, a skill for writing release notes can include your team's template, a script for gathering changes, and instructions for grouping them. The agent loads those resources when working on release notes, rather than including the whole workflow in every conversation.

## Where you can use agent skills

You can use agent skills with:

* The GitHub Copilot app.
* GitHub Copilot CLI.
* Copilot cloud agent and Copilot code review on GitHub.com.
* Agent mode in Visual Studio Code, Visual Studio, and JetBrains IDEs.

IDE support depends on the version you use. See [AUTOTITLE](/copilot/reference/copilot-feature-matrix).

## Finding and storing skills

You can also use `gh skill` in GitHub CLI to discover and install skills from GitHub repositories. For more information, see [AUTOTITLE](/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills#managing-skills-with-github-cli).

Copilot supports:

* Project skills, stored in your repository (`.github/skills`, `.claude/skills`, or `.agents/skills`)
* Personal skills, stored in your home directory and shared across projects (`~/.copilot/skills` or `~/.agents/skills`)
  * To make personal skills available in cloud sandbox sessions, include them in `.copilot/skills` in your dotfiles repository. This does not apply to GitHub Actions-based sessions. See [AUTOTITLE](/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/personalize-cloud-sessions).

Supported locations depend on the surface. Use its setup guide to choose a location rather than assuming that a personal skill is available to an agent running in the cloud.

## Next steps

To create or add agent skills, see:

* [AUTOTITLE](/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
* [AUTOTITLE](/copilot/how-tos/copilot-cli/customize-copilot/add-skills)
* [AUTOTITLE](/copilot/how-tos/github-copilot-app/customize-github-copilot-app)
* [AUTOTITLE](/copilot/reference/customization-cheat-sheet)
