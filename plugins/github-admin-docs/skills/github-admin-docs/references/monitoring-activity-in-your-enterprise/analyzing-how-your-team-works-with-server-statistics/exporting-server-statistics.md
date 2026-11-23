---
title: Exporting Server Statistics
shortTitle: Export Server Statistics
intro: 'You can use your own tools to analyze your GitHub Enterprise Server usage over time by downloading your Server Statistics metrics in a CSV or JSON file.'
versions:
  ghes: '*'
redirect_from:
  - /early-access/github/analyze-how-your-team-works-with-server-statistics/exploring-server-statistics
category:
  - Monitor and audit your enterprise
---

You can download up to the last 365 days of Server Statistics data in a CSV or JSON file. This data, which includes aggregate metrics on repositories, issues, and pull requests, can help you anticipate the needs of your organization, understand how your team works, and show the value you get from GitHub Enterprise Server.

Before you can download this data, you must enable Server Statistics. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-server-statistics-for-your-enterprise).

To preview the metrics available to download, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/analyzing-how-your-team-works-with-server-statistics/about-server-statistics).

To download these metrics, you must be an enterprise owner or organization owner on GitHub Enterprise Cloud.
* If {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} is connected to an enterprise account on GitHub Enterprise Cloud, see [Downloading metrics from your enterprise account](#downloading-metrics-from-your-enterprise-account).
* If {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} is connected to an organization on GitHub Enterprise Cloud, see [Downloading metrics from your organization](#downloading-metrics-from-your-organization).

To learn more about GitHub Connect, see [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/about-github-connect).

## Downloading metrics from your enterprise account

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}

1. At the top of the page, in the enterprise account sidebar, click (icon: plug) **GitHub Connect**.

1. To start your download, next to "Server Statistics", select the **Export** dropdown menu, then choose whether you want to download a JSON or CSV file.

## Downloading metrics from your organization

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.

1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)

1. In the left sidebar, click **GitHub Connect**.

1. To start your download, next to "Server Statistics", select the **Export** dropdown menu, then choose whether you want to download a JSON or CSV file.
