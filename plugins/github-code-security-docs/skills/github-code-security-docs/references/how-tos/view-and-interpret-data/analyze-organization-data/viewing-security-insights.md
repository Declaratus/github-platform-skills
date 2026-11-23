---
title: Viewing security insights
shortTitle: View security insights
intro: Monitor your organization{% ifversion security-overview-dashboard-enterprise %} or enterprise{% endif %} security posture, identify high-risk repositories, and track alert remediation progress using the overview dashboard in security overview.
permissions: "Access requires:\n* Organization views: **write** access to repositories in the organization\n* Enterprise views: organization owners and security managers"
product: "{% ifversion fpt %}\nOrganizations owned by a GitHub Team account with GitHub Secret Protection or GitHub Code Security, or owned by a GitHub Enterprise account\n{% endif %}"
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
contentType: how-tos
redirect_from:
  - /code-security/security-overview/viewing-security-insights-for-your-organization
  - /code-security/security-overview/viewing-security-insights
allowTitleToDifferFromFilename: true
category:
  - Secure at scale
---

The overview page in security overview provides a consolidated dashboard of your organization{% ifversion security-overview-dashboard-enterprise %} or enterprise{% endif %}'s security landscape. You can filter the dashboard by time period, tool, and other criteria to focus on specific areas of interest. For more information about the overview dashboard, available metrics, and access permissions, see [AUTOTITLE](/code-security/concepts/security-at-scale/security-overview).

{% ifversion ai-powered-security-detections %}
The **Prevention** tab includes AI Scan metrics for your organization or enterprise. You can track AI Scan findings, resolution rates, and accepted Copilot Autofix suggestions. For more detailed findings, use the "Code scanning on pull requests" report. See [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/analyze-organization-data/viewing-metrics-for-pull-request-alerts).
{% endif %}

{% ifversion security-overview-export-data %}
You can download a CSV file of the overview dashboard data for your organization or enterprise. For more information, see [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/analyze-organization-data/export-data).
{% endif %}


>[!NOTE] The summary views ("Overview", "Coverage" and "Risk") show data only for default alerts. Secret scanning alerts for ignored directories and generic alerts are all omitted from these views. Consequently, the individual alert views may include a larger number of open and closed alerts.

## Viewing the security overview dashboard{% ifversion security-overview-dashboard-enterprise %} for your organization{% endif %}

1. On GitHub, navigate to the main page of the organization.
1. Under your organization name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. The overview page is the primary view that you will see after clicking on the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab. To get to the dashboard from another security overview page, in the sidebar, click **(icon: graph) Overview**.
1. By default, the **Detection** tab is displayed. If you want to switch to another tab to see other metrics, click **Remediation** or **Prevention**.
1. Use the options at the top of the overview page to filter the group of alerts you want to see metrics for. All of the data and metrics on the page will change as you adjust the filters.
   * Use the date picker to set the time range that you want to view alert activity and metrics for.
   * Click in the search box to add further filters on the alerts and metrics displayed.

    ![Screenshot of the overview page in security overview. Filtering options are outlined in dark orange, including the date picker and search field.](/assets/images/help/security-overview/security-overview-dashboard-filters-3-tab.png)

{% ifversion security-overview-dashboard-enterprise %}

## Viewing the security overview dashboard for your enterprise

{% ifversion ghes %}1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.{% else %}1. Navigate to GitHub Enterprise Cloud.
                                                                                             1. In the top-right corner of GitHub, click your profile picture.
                                                                                             1. Depending on your environment, click **Enterprise**, or click **Enterprises** then click the enterprise you want to view.{% endif %}
1. At the top of the page, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. By default, the **Detection** tab is displayed. If you want to switch to another tab to see other metrics, click **Remediation** or **Prevention**.
1. Use the options at the top of the overview page to filter the group of alerts you want to see metrics for. All of the data and metrics on the page will change as you adjust the filters.
   * Use the date picker to set the time range that you want to view alert activity and metrics for.
   * Click in the search box to add further filters on the alerts and metrics displayed.

    ![Screenshot of the overview page in security overview. Filtering options are outlined in dark orange, including the date picker and search field.](/assets/images/help/security-overview/security-overview-dashboard-filters-3-tab.png)

> [!TIP]
> You can use the `owner` filter in the search field to filter the data by organization. {% ifversion ghec %}If you're an owner of an enterprise with managed users, you can use the `owner-type` filter to filter the data by the type of repository owner, so that you can view data from either organization-owned repositories or user-owned repositories. {% endif %}For more information, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/filtering-alerts-in-security-overview).

{% ifversion secret-scanning-public-monitoring %}
The enterprise security overview also includes a **Public monitoring** page, where you can view alerts for secrets leaked by enterprise members in public repositories outside your enterprise. See [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/analyze-organization-data/viewing-public-monitoring-alerts).
{% endif %}

{% endif %}

## Next steps

The dashboard displays metrics about alert status, remediation velocity, and high-risk repositories in your organization{% ifversion security-overview-dashboard-enterprise %} or enterprise{% endif %}. For detailed explanations of each metric and how it's calculated, see [AUTOTITLE](/code-security/reference/security-at-scale/overview-dashboard-metrics).

You can filter the dashboard by time period, tool, repository, and other criteria. For more information, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/filtering-alerts-in-security-overview).
