---
title: Viewing code scanning metrics for pull requests
shortTitle: View pull request metrics
allowTitleToDifferFromFilename: true
intro: Monitor how CodeQL{% ifversion ai-powered-security-detections %} and AI Scan{% endif %} perform in pull requests across your organizations to identify repositories where you may need to take action.
permissions: "Access requires:\n* Organization views: **write** access to repositories in the organization\n* Enterprise views: organization owners and security managers"
product: 'Organizations owned by a GitHub Team account with GitHub Code Security, or owned by a GitHub Enterprise account with GitHub Code Security'
contentType: how-tos
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /code-security/security-overview/viewing-metrics-for-pull-request-alerts
category:
  - Secure at scale
---

## Viewing code scanning pull request metrics for an organization

1. On GitHub, navigate to the main page of the organization.
1. Under your organization name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. In the sidebar, under "Insights", click **(icon: graph) {% ifversion ai-powered-security-detections %}Code scanning on pull requests{% else %}CodeQL pull requests{% endif %}**.
{% ifversion ai-powered-security-detections %}
1. Select the **CodeQL** or **AI Scan** tab.
{% endif %}
1. Optionally, use the date picker to set the time range. The date picker filters data based on when the pull request alerts or findings were created.
1. Optionally, apply filters in the search box at the top of the page.
1. Alternatively, you can open the advanced filter dialog:
    * At the top of the page, next to the search box, click **(icon: filter) Filter**.
    * Click **(icon: plus) Add a filter**, then select a filter from the dropdown menu.
    * To search for repositories matching the selected filter, fill out the available fields for that filter, then click **Apply**. You can repeat this process to add as many filters as you would like to your search.
    * Optionally, to remove a filter from your search, click **(icon: filter) Filter**. In the row of the filter you want to remove, click (icon: x), then click **Apply**.{% ifversion security-overview-export-data %}
1. {% ifversion ai-powered-security-detections %}On the **CodeQL** tab, you can use the **(icon: download) Export CSV** button to download a CSV file of the displayed data. CSV export is not yet available for the **AI Scan** tab. {% else %}You can use the **(icon: download) Export CSV** button to download a CSV file of the data currently displayed on the page.{% endif %} For more information, see [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/analyze-organization-data/export-data). {% endif %}

## Viewing code scanning pull request metrics for your enterprise

You can also view code scanning metrics for pull requests across organizations in your enterprise.

1. Navigate to GitHub Enterprise Cloud.
1. In the top-right corner of GitHub, click your profile picture.
1. Depending on your environment, click **Enterprise**, or click **Enterprises** then click the enterprise you want to view.
1. At the top of the page, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. In the sidebar, under "Insights", click **(icon: graph) {% ifversion ai-powered-security-detections %}Code scanning on pull requests{% else %}CodeQL pull requests{% endif %}**.
{% ifversion ai-powered-security-detections %}
1. Select the **CodeQL** or **AI Scan** tab.
{% endif %}
1. Optionally, use the date picker or filters to limit the displayed data.

> [!TIP]
> You can use the `owner` filter in the search field to filter the data by organization. {% ifversion ghec %}If you're an owner of an enterprise with managed users, you can use the `owner-type` filter to filter the data by the type of repository owner, so that you can view data from either organization-owned repositories or user-owned repositories. {% endif %}For more information, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/filtering-alerts-in-security-overview).
