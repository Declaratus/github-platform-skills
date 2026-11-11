---
title: Viewing the Copilot usage metrics dashboard
shortTitle: View usage and adoption
intro: 'Monitor adoption trends and use of Copilot to support long-term enablement.'
permissions: 'Enterprise owners, enterprise billing managers, organization owners, and people with a custom organization or enterprise role with the "View Organization Copilot Metrics" or "View Enterprise Copilot Metrics" permission.'
versions:
  feature: copilot
contentType: how-tos
allowTitleToDifferFromFilename: true
redirect_from:
  - /copilot/how-tos/administer-copilot/manage-for-enterprise/view-usage-and-adoption
category:
  - Copilot usage metrics
  - View metrics
  - Track Copilot usage
---

After your initial rollout, the Copilot usage metrics dashboard helps you monitor how usage evolves over time. By exploring adoption, feature, model, and language trends, you can see how developers are engaging with Copilot and identify areas where additional enablement or communication may drive deeper value.

> [!TIP]
> To connect these insights with broader governance and rollout decisions, see [AUTOTITLE](/copilot/get-started/enterprise-ai-governance).

## Prerequisite

To access Copilot usage metrics, the **"Copilot usage metrics"** policy must be enabled:

* [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies#defining-policies-for-your-enterprise)
* [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-organization/manage-policies#enabling-copilot-features-and-models-in-your-organization)

To grant visibility into metrics for a single organization without enterprise-level access, create a custom organization role with the "View organization Copilot metrics" permission and assign it to the people who need access. See [AUTOTITLE](/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/permissions-of-custom-organization-roles).

## Accessing the dashboard

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. Click the **Insights** tab.
1. In the left sidebar, click **Copilot usage**.

Data in the dashboard is primarily based on IDE telemetry and is supplemented by server-side telemetry to capture additional active users. Data for a given day is available within two full UTC days after that day closes. See [AUTOTITLE](/copilot/reference/copilot-usage-metrics/reconciling-usage-metrics).

## Using Copilot Chat to analyze exported data

For deeper analysis, you can export NDJSON reports from the dashboard and use Copilot Chat to explore the data in more detail. For example, you can ask:

```copilot copy prompt
* Which users have `user_initiated_interaction_count` > 0 but low `code_acceptance_activity_count`?
* Are there specific teams with lower adoption rates?
```
