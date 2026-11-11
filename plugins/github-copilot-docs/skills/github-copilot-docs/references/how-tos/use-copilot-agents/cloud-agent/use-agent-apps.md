---
title: Using agent apps
shortTitle: Use agent apps
intro: 'Start a partner-built agent from an issue, a pull request comment, or the Agents UI on GitHub.'
product: 'Available for all paid [Copilot plans](/copilot/get-started/plans).<br><a href="https://github.com/features/copilot/plans?ref_product=copilot&ref_type=purchase&ref_style=button&utm_source=docs-use-agent-apps&utm_medium=docs&utm_campaign=msbuild-2026" target="_blank" class="btn btn-primary mt-3 mr-3 no-underline"><span>Sign up for Copilot</span> (icon: link-external)</a>'
versions:
  feature: copilot
contentType: how-tos
category:
  - Author and optimize with Copilot
---

> [!NOTE] Agent apps are currently in public preview and subject to change.

## Introduction

Agent apps let you delegate work to partner-built agents from within GitHub. For an overview, see [AUTOTITLE](/copilot/concepts/agent-capabilities/about-agents/agent-apps).

Before you can use an agent app, the GitHub App must be installed on the account or organization that owns the repository, and agent features must be enabled for the app. If the repository is owned by an organization that belongs to an enterprise, the "Agent apps" Copilot policy must also be enabled in your enterprise settings.

## Installing an agent app

1. View available apps on [GitHub Marketplace](https://github.com/marketplace?type=apps&category=agent-apps).
1. On the app page, click **Add**, then install the app on your personal account or organization.

## Authorizing an agent app

The first time you use an agent app, GitHub prompts you to authorize the app through an OAuth flow. Follow the prompts to authorize the app before the agent runs. For more information, see [AUTOTITLE](/apps/using-github-apps/authorizing-github-apps).

## Starting an agent from the Agents UI

1. Open the agents panel or tab:

   * Open the **(icon: agent) Agents** tab in a repository.
   * **Navigate to the GitHub Copilot all sessions page**: Go to [github.com/copilot](https://github.com/copilot?ref_product=copilot&ref_type=engagement&ref_style=text&utm_source=open-agent-panel-reusable-home&utm_medium=docs&utm_campaign=universe-2026). You can also get here by opening the GitHub Copilot menu in top navigation bar, then clicking **View all sessions**.
   * **Open the agents panel**: From the code tab in a repository, click (icon: agent) to the right of the "Go to file" search bar.
1. Under the prompt box, select the agent app you want to use.
1. Type a prompt describing your request, then start the task.

## Starting an agent from an issue

You can assign an agent app to an issue in the same way you assign Copilot cloud agent.

1. Navigate to the issue you want the agent to work on.
1. In the sidebar, under "Assignees," assign the agent app to the issue.

The agent starts work on the issue and reports back on its progress.

## Starting an agent from a pull request comment

You can ask an agent app to make changes or perform other tasks by mentioning it in a pull request comment.

1. Navigate to the pull request you want the agent to work on.
1. Add a comment that mentions the agent and describes what you want it to do, for example `@AGENT-NAME add a feature flag for the new checkout flow`. Pick the agent from the autocomplete picker.

The agent responds to your comment and works on the requested changes.

## Using agent apps on GitHub Mobile

You can start agent apps from the same entry points on GitHub Mobile. For more information about using agents on mobile, see [AUTOTITLE](/copilot/how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-on-mobile).

## Billing

Agent apps are powered by Copilot. When you use an agent app, the AI usage is billed to your Copilot subscription, and sessions consume AI credits in the same way as Copilot. See [AUTOTITLE](/billing/concepts/product-billing/github-copilot-billing).
