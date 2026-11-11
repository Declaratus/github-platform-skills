---
title: Viewing the code generation dashboard
shortTitle: View code generation
intro: The code generation dashboard shows how Copilot generates code across your enterprise, including activity from both users and agents.
permissions: 'Enterprise owners, enterprise billing managers, organization owners, and people with a custom organization or enterprise role with the "View Organization Copilot Metrics" or "View Enterprise Copilot Metrics" permission.'
versions:
  feature: copilot
contentType: how-tos
allowTitleToDifferFromFilename: true
redirect_from:
  - /copilot/how-tos/administer-copilot/manage-for-enterprise/view-code-generation
category:
  - Copilot usage metrics
  - View metrics
  - Track Copilot usage
---

By comparing user-initiated and agent-initiated activity across models, languages, and modes, you can see how teams are adopting AI-assisted and agent-driven development.

The dashboard shows aggregated code generation activity, including:

* **Lines of code changed with AI**. The total lines of code added and deleted across all modes.
* **User-initiated code changes**. Lines suggested or manually added through completions and chat actions.
* **Agent-initiated code changes**. Lines automatically added or deleted by agents across edit, agent, and custom modes.
* **Activity by model and language**. User-initiated and agent-initiated activity grouped by model and language.

For a detailed list of available metrics and definitions, see [AUTOTITLE](/copilot/reference/copilot-usage-metrics/copilot-usage-metrics#code-generation-dashboard-metrics).

## Prerequisite

To access Copilot usage metrics, the **"Copilot usage metrics"** policy must be enabled:

* [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies#defining-policies-for-your-enterprise)
* [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-organization/manage-policies#enabling-copilot-features-and-models-in-your-organization)

## Accessing the dashboard

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. Click the **Insights** tab.
1. In the left sidebar, click **Code generation**.
