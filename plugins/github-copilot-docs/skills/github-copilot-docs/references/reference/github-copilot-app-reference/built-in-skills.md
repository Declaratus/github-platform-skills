---
title: Built-in skills for the GitHub Copilot app
shortTitle: Built-in skills
allowTitleToDifferFromFilename: true
intro: 'Use this reference to find built-in agent skills available in the GitHub Copilot app.'
product: 'The GitHub Copilot app is available for all Copilot plans.<br><a href="https://github.com/features/ai/github-app?utm_source=app-download-docs&utm_medium=docs&utm_campaign=universe-2026" target="_blank" class="btn btn-primary mt-3 mr-3 no-underline js-os-download" data-os-download-mac="https://gh.io/copilot-app-mac" data-os-download-mac-intel="https://gh.io/copilot-app-mac-intel" data-os-download-windows="https://gh.io/copilot-app-win64" data-os-download-windows-arm="https://gh.io/copilot-app-win-arm" data-os-download-linux="https://gh.io/copilot-app-linux" data-os-download-linux-arm="https://github.com/github/app/releases/latest/download/GitHub-Copilot-linux-arm64.AppImage">(icon: desktop-download) <span class="js-os-download-label">Download the GitHub Copilot app</span></a>'
versions:
  feature: copilot
contentType: reference
category:
  - Author and optimize with Copilot
---

This page lists GitHub-provided built-in agent skills for the GitHub Copilot app. It does not list agent skills from plugins, repositories, organizations, or personal customizations.

## Built-in skills in the GitHub Copilot app

Some built-in skills are available as slash commands. When available in your current context, you can run them by typing `/<skill-id>` in the prompt box, for example `/orchestrate`. Other built-in skills may run automatically as part of specific app workflows or when you mention a relevant task in your prompt.

| Skill ID | When to use |
| --- | --- |
| `af` | Find installable MCP servers, tools, skills, and agents by searching ARD Agent Finder. Invoke this skill with `/af`. See [AUTOTITLE](/copilot/concepts/customizations/mcp#agent-finder). |
| `agent-merge` | Follow up on review comments, failing checks, and merge conflicts after Agent Merge is enabled for a pull request. The Agent Merge workflow invokes this skill automatically. See [AUTOTITLE](/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests#merging-a-pull-request). |
| `create-canvas` | Create and troubleshoot canvas extensions in the app side panel, including actions, inputs, rendered content, and setup. Invoke this skill with `/create-canvas`. See [AUTOTITLE](/copilot/how-tos/github-copilot-app/working-with-canvas-extensions). |
| `orchestrate` | Coordinate work across sessions and repositories by creating and guiding child sessions. Invoke this skill with `/orchestrate`. |
| `pr-stack` | Create and manage a stack of dependent pull requests, with one child session for each layer. Invoke this skill with `/pr-stack`. See [AUTOTITLE](/pull-requests/get-started/about-stacked-prs). |
| `customize-cloud-agent` | Set up the cloud agent environment, including `copilot-setup-steps.yml`, preinstalled tools and dependencies, runners, and settings. The app invokes this skill when your prompt asks to set up or customize the cloud agent environment. |

## Further reading

* [AUTOTITLE](/copilot/reference/github-copilot-app-reference/slash-commands)
* [AUTOTITLE](/copilot/how-tos/github-copilot-app/customize-github-copilot-app)
* [AUTOTITLE](/copilot/concepts/agents/about-agent-skills)
