---
title: Enabling Server Statistics for your enterprise
intro: 'You can analyze your own aggregate data from GitHub Enterprise Server and help us improve GitHub products by enabling Server Statistics.'
versions:
  ghes: '*'
redirect_from:
  - /early-access/github/analyze-how-your-team-works-with-server-statistics/about-server-statistics/enabling-server-statistics
  - /admin/configuration/configuring-github-connect/enabling-server-statistics-for-your-enterprise
shortTitle: Server Statistics
category:
  - Install and configure your instance
---

## About Server Statistics

Server Statistics collects aggregate usage data from {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, which you can use to better anticipate the needs of your organization, understand how your team works, and show the value you get from GitHub Enterprise Server.

Server Statistics only collects certain aggregate metrics on repositories, issues, pull requests, and other features. GitHub content, such as code, issues, comments, or pull request content, is not collected. For more information, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/analyzing-how-your-team-works-with-server-statistics/about-server-statistics).

By enabling Server Statistics, you are also helping to improve GitHub. The aggregated data you will provide helps us understand how our customers are using GitHub, and make better and more informed product decisions, ultimately benefiting you.

## Enabling Server Statistics

Before you can enable Server Statistics, you must first connect your GitHub Enterprise Server instance to GitHub.com using GitHub Connect. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-github-connect-for-githubcom).

You can disable Server Statistics from GitHub Enterprise Server at any time.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: plug) GitHub Connect**.
1. Under "Share server statistics with GitHub.com", select the dropdown menu and click **Enabled** or **Disabled**.
