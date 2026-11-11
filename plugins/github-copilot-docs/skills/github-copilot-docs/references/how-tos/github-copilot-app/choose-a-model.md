---
title: Choosing a model in the Copilot app
shortTitle: Choose a model
intro: 'Choose which large language model you want to use for a task in the Copilot app.'
versions:
  feature: copilot
product: 'The GitHub Copilot app is available for all Copilot plans.<br><a href="https://github.com/features/ai/github-app?utm_source=app-download-docs&utm_medium=docs&utm_campaign=universe-2026" target="_blank" class="btn btn-primary mt-3 mr-3 no-underline js-os-download" data-os-download-mac="https://gh.io/copilot-app-mac" data-os-download-mac-intel="https://gh.io/copilot-app-mac-intel" data-os-download-windows="https://gh.io/copilot-app-win64" data-os-download-windows-arm="https://gh.io/copilot-app-win-arm" data-os-download-linux="https://gh.io/copilot-app-linux" data-os-download-linux-arm="https://github.com/github/app/releases/latest/download/GitHub-Copilot-linux-arm64.AppImage">(icon: desktop-download) <span class="js-os-download-label">Download the GitHub Copilot app</span></a>'
contentType: how-tos
category:
  - Author and optimize with Copilot # Copilot discovery page
---

## Introduction

Copilot supports a range of AI models. Different models have different strengths. For example, some prioritize low latency, while others are optimized for complex reasoning or large context windows. You can choose the model you think best fits your needs for a particular task.

For details of models and their capabilities, see [AUTOTITLE](/copilot/reference/ai-models/supported-models) and [AUTOTITLE](/copilot/reference/ai-models/model-comparison). The models available to you depend on your Copilot plan and your enterprise or organization settings.

## Identifying the currently selected model

Details of the currently selected model are displayed below the prompt box.

To see the model that was used for a completed response, hover over the response until the information icon (<span style="vertical-align: 2px">(icon: info)</span>) is displayed below the response. Hover over the information icon to view the model details. If multiple models were used during work on a task, the information box shows the model used by the main agent, not any subagents that were used.

## Choosing a model

You can choose which model you want to use at any point during a session. Your choice takes effect immediately if Copilot is currently idle, or when the current turn completes. The model will continue to be used for the remainder of the session, unless you change it again. Your choice becomes the default model for future sessions, but the model used in other existing sessions is not affected.

If you have installed local models, these are only available if you are currently in a local session. See [AUTOTITLE](/copilot/how-tos/github-copilot-app/add-llm-models).

1. Click the current model choice, shown below the prompt box.
1. To use Copilot Fusion:
   1. Toggle the **Copilot Fusion** switch to the on position.
   1. Choose an effort level:

      * **Fusion Standard** – Prioritizes versatile models for everyday coding.
      * **Fusion High** – Prioritizes capable models for challenging tasks and deeper reasoning.
      * **Fusion Max** – Prioritizes the most capable models for the most demanding tasks and complex reasoning.response times.

   1. Click outside the dialog to dismiss it.

   When you choose the **Copilot Fusion** option, Copilot analyzes each task and selects a model to complete it, orchestrating multiple models through execution patterns when needed. For more information, see [AUTOTITLE](/copilot/concepts/models/copilot-fusion).

1. To choose a specific model:
   1. Toggle the **Copilot Fusion** switch to the off position.
   1. Hover over the current model choice in the dialog and click to select a different model from the list that's displayed.
   1. Depending on the model you choose, additional options for effort level and context window size may be available.

      Select the appropriate options based on your needs.

   1. Click outside the dialog to dismiss it.

## Further reading

* [AUTOTITLE](/copilot/concepts/models/overview)
* [AUTOTITLE](/copilot/how-tos/github-copilot-app/add-llm-models)
