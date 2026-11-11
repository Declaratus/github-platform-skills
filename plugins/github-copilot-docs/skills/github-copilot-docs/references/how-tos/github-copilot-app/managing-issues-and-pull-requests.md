---
title: Managing issues and pull requests with the GitHub Copilot app
shortTitle: Managing issues and pull requests
allowTitleToDifferFromFilename: true
intro: 'Pick up an issue, direct an agent to implement changes, and land a pull request—all without leaving the GitHub Copilot app.'
product: 'The GitHub Copilot app is available for all Copilot plans.<br><a href="https://github.com/features/ai/github-app?utm_source=app-download-docs&utm_medium=docs&utm_campaign=universe-2026" target="_blank" class="btn btn-primary mt-3 mr-3 no-underline js-os-download" data-os-download-mac="https://gh.io/copilot-app-mac" data-os-download-mac-intel="https://gh.io/copilot-app-mac-intel" data-os-download-windows="https://gh.io/copilot-app-win64" data-os-download-windows-arm="https://gh.io/copilot-app-win-arm" data-os-download-linux="https://gh.io/copilot-app-linux" data-os-download-linux-arm="https://github.com/github/app/releases/latest/download/GitHub-Copilot-linux-arm64.AppImage">(icon: desktop-download) <span class="js-os-download-label">Download the GitHub Copilot app</span></a>'
versions:
  feature: copilot
contentType: how-tos
redirect_from:
  - /copilot/how-tos/github-app/managing-issues-and-pull-requests
category:
  - Author and optimize with Copilot
---

## Browsing your issues and pull requests

Click **Issues** or **Pull requests** in the sidebar to browse the corresponding items from your repositories.

## Creating an issue or pull request from a session

When you ask an agent in the app to create an issue, the agent chooses a repository issue template based on the type of issue. To use a particular template, specify it in your prompt.

When you ask an agent to create a pull request, it also follows the repository's pull request template.

## Starting a session from an issue

1. Click **Issues** in the sidebar.
1. Browse or filter to find an issue, then click it to view its details.
1. Click **New session**. The app creates a new session with the issue context already loaded.
1. Select a session mode from the dropdown below the prompt field—for example, **Plan** to have the agent propose a plan first, or **Interactive** to work collaboratively with the agent.
1. Prompt the agent with what you want it to do. If you chose **Plan** mode, the agent proposes a plan for you to review first; otherwise, the agent will start working on the issue and propose changes that you can iterate on. Follow along in the conversation view and provide feedback to steer the agent.

## Reviewing a pull request

1. Click **Pull requests** in the sidebar, then click a pull request to see its overview—including the summary, CI check results, and review activity.
1. Switch to the **Files changed** tab to review the diff.
1. Click **New session** to start a session for the pull request. Within the session, you can leave review comments on the diff, or ask the agent to make changes.
1. Once done reviewing in the session, you can go back to the pull request detail view and click **Review** at the top to submit a review.

You can also open the pull request in your browser or in another IDE directly from the app.

## Responding to a review

You can respond to review comments and resolve failing CI checks in the GitHub Copilot app.

1. Open a pull request.
1. Scroll down the page to see review comments on your PR. To ask an agent to resolve a comment, click **(icon: copilot) Fix**.
1. At the bottom of the page, view the status of CI checks. To ask an agent to fix failing checks, click **(icon: copilot) Fix failing checks**.

## Merging a pull request

Agent Merge is available in the GitHub Copilot app and as part of Copilot in the cloud. Both surfaces can fix failed GitHub Actions workflows and resolve merge conflicts. In the app, Agent Merge can also address review comments, which is not supported in the cloud.

When you want to merge a pull request, enable **Agent Merge** at the top of the app. Agent Merge will prompt the workspace's Copilot session to read your pull request, fix what is blocking it, and merge it as soon as GitHub allows. It runs in the background, survives app restarts, and turns itself off once your pull request is merged.

You can also use Agent Merge as part of Copilot in the cloud, directly from a pull request on GitHub. In the pull request's merge box, click **Watch and fix**, then choose **Fix failed Actions workflows**, **Resolve merge conflicts**, or both. Copilot fixes the selected blockers in an GitHub Actions-based development environment and posts timeline updates explaining why it started work.

The cloud option keeps your pull request ready to merge and can be combined with auto-merge to complete the merge when all requirements are met. You can also enable it automatically for pull requests you create. For setup, customization, and billing details, see [AUTOTITLE](/copilot/how-tos/copilot-on-github/use-copilot-agents/get-pull-requests-ready-to-merge).
