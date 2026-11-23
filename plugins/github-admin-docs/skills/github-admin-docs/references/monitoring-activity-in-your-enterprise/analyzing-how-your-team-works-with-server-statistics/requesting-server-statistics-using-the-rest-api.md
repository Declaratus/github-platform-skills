---
title: Requesting Server Statistics using the REST API
shortTitle: Server Statistics and REST API
intro: 'You can use your own tools to analyze your GitHub Enterprise Server usage over time by requesting the Server Statistics metrics collected using the REST API.'
versions:
  ghes: '*'
redirect_from:
  - /early-access/github/analyze-how-your-team-works-with-server-statistics/requesting-server-statistics-using-the-rest-api
category:
  - Monitor and audit your enterprise
---

You can request up to 365 days of metrics in a single Server Statistics REST API request. This data, which includes aggregate metrics on repositories, issues, and pull requests, can help you anticipate the needs of your organization, understand how your team works, and show the value you get from GitHub Enterprise Server. For a list of the metrics collected, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/analyzing-how-your-team-works-with-server-statistics/about-server-statistics#server-statistics-data-collected).

Before you can use the Server Statistics REST API, you must enable Server Statistics. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-server-statistics-for-your-enterprise).

For more information about using the REST API to request server statistics, see [AUTOTITLE](/enterprise-cloud@latest/rest/enterprise-admin/admin-stats#get-github-enterprise-server-statistics) in the GitHub Enterprise Cloud documentation.
