---
title: Viewing metrics for secret scanning push protection
shortTitle: View secret scanning metrics
allowTitleToDifferFromFilename: true
intro: Monitor push protection's performance across your organization{% ifversion security-overview-enterprise-secret-scanning-metrics %} or enterprise{% endif %} to identify repositories where you may need to take action.
permissions: "Access requires:\n* Organization views: **write** access to repositories in the organization\n* Enterprise views: organization owners and security managers"
product: "{% ifversion fpt %}\nOrganizations owned by a GitHub Team account with GitHub Secret Protection, or owned by a GitHub Enterprise account\n{% endif %}"
contentType: how-tos
redirect_from:
  - /code-security/security-overview/viewing-metrics-for-secret-scanning-push-protection-in-your-organization
  - /code-security/security-overview/viewing-metrics-for-secret-scanning-push-protection
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
category:
  - Secure at scale
---

> [!NOTE]
> Secret scanning metrics for push protection is currently in public preview and subject to change.

## Viewing metrics for secret scanning push protection for an organization

1. On GitHub, navigate to the main page of the organization.
1. Under your organization name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. In the sidebar, under "Insights", click **(icon: graph) Secret scanning**.
1. Click on an individual secret type or repository to see the associated secret scanning alerts for your organization.
1. You can use the options at the top of the page to filter the group of repositories that you want to see secret scanning metrics for.
    * Use the date picker to set the time range that you want to view metrics for. Note that the date used by the date picker corresponds to the date a secret was bypassed on.
    * Click in the search box to add further filters on the secret scanning metrics displayed. For more information, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/filtering-alerts-in-security-overview).

## Viewing metrics for secret scanning push protection for an enterprise

You can view metrics for secret scanning push protection across organizations in an enterprise. The information shown by security overview varies according to your access to repositories and organizations, and according to whether Advanced Security features are used by those repositories and organizations. For more information, see [AUTOTITLE](/code-security/concepts/security-at-scale/security-overview).

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. In the sidebar, click **Secret scanning**.
1. Click on an individual secret type or repository to see the associated secret scanning alerts for your enterprise.
1. You can use the options at the top of the page to filter the group of repositories that you want to see secret scanning metrics for.
    * Use the date picker to set the time range that you want to view metrics for. Note that the date used by the date picker corresponds to the date a secret was bypassed on.
    * Click in the search box to add further filters on the secret scanning metrics displayed. For more information, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/filtering-alerts-in-security-overview).

> [!TIP]
> You can use the `owner` filter in the search field to filter the data by organization. {% ifversion ghec %}If you're an owner of an enterprise with managed users, you can use the `owner-type` filter to filter the data by the type of repository owner, so that you can view data from either organization-owned repositories or user-owned repositories. {% endif %}For more information, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/filtering-alerts-in-security-overview).
