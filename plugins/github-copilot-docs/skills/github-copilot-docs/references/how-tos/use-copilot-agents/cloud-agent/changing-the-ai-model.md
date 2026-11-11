---
title: Changing the AI model for GitHub Copilot cloud agent
shortTitle: Changing the AI model
allowTitleToDifferFromFilename: true
intro: 'In supported entrypoints, when starting a task with Copilot cloud agent, you can select the model used, and, for supported models, the reasoning level.'
product: 'Copilot cloud agent is available for all paid Copilot plans.
          
          The agent is available in all repositories stored on GitHub, except repositories owned by managed user accounts and where it has been explicitly disabled.<br><a href="https://github.com/features/copilot/plans?ref_product=copilot&ref_type=purchase&ref_style=button" target="_blank" class="btn btn-primary mt-3 mr-3 no-underline"><span>Sign up for Copilot</span> (icon: link-external)</a>'
versions:
  feature: copilot
contentType: how-tos
category: 
  - Author and optimize with Copilot
redirect_from:
  - /copilot/how-tos/use-copilot-agents/coding-agent/changing-the-ai-model
---

> [!NOTE]
> For an overview of Copilot cloud agent, see [AUTOTITLE](/copilot/concepts/copilot-surfaces/copilot-on-github).

## Introduction

In supported entrypoints, you can select the model used by Copilot cloud agent.

You may find that different models perform better, or provide more useful responses, depending on the type of tasks you give Copilot.

> [!NOTE]
> Model selection for Copilot cloud agent is only supported when assigning an issue to Copilot on GitHub.com, when mentioning `@copilot` in a pull request comment on GitHub.com, when starting a task from the agents tab, agents panel, GitHub Mobile or the Raycast launcher, or from the Slack or Microsoft Teams integrations. Where a model picker is not available, Auto will be used automatically. See [AUTOTITLE](/copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions).

## Supported models

The following options are currently available:

* Auto 
* Claude Opus 5
* Claude Opus 5.5
* Claude Sonnet 5.5
* Claude Haiku 4.5
* Claude Haiku 5.5
* Gemini 3.8 Flash
* Gemini 4 Argon
* Gemini 4 Carbon
* GPT-5.6 Luna
* GPT-5.6 Sol
* GPT-5.6 Terra
* GPT-6 Astra
* GPT-6 Luna
* GPT-6 Sol
* GPT-6.1 Sol
* GPT-6.1 Terra
* Grok 4.5
* Grok 4.6
* Grok 4.7
* MAI Code 1.1 Flash

> [!NOTE] 
> If you select **Auto**, auto model selection will select the best model based on the task. See [AUTOTITLE](/copilot/concepts/models/auto-model-selection).

## Reasoning level

Some models support configurable reasoning levels, which control how much time and effort the model spends reasoning before it responds. Higher reasoning levels can improve the quality of responses to complex tasks, but may take longer and use more AI credits.

If you select a model that supports configurable reasoning, a second dropdown menu appears so you can choose the reasoning level you want Copilot cloud agent to use for that task. For more information about which models support configurable reasoning, see [AUTOTITLE](/copilot/reference/ai-models/supported-models#models-with-extended-capabilities).

