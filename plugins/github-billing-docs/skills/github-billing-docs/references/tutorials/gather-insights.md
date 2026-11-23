---
title: Gathering insights on your spending
intro: 'Get insights into the usage of your {% ifversion fpt %}organization{% elsif ghec or ghes %}enterprise{% endif %} members.'
versions:
  feature: enhanced-billing-platform
permissions: '{% ifversion fpt %}Organization owners, billing managers, and personal account users {% elsif ghec %}Enterprise owners, organization owners, and billing managers {% endif %}'
redirect_from:
  - /billing/using-the-enhanced-billing-platform-for-enterprises/gathering-insights-on-your-spending
  - /billing/using-the-new-billing-platform/gathering-insights-on-your-spending
  - /billing/managing-your-billing/gathering-insights-on-your-spending
shortTitle: Gather insights
contentType: tutorials
category:
  - Track spending and control costs
---

The billing platform provides you with the tools to:

* **Get insights** into usage trends to understand how your resources are being used.
* **Search and filter usage** by repository, product, or SKU, and group data accordingly.
* **Generate reports** on past usage for various time periods, including the current hour, today, this month, last month, this year, last year, or a custom date range.

{% ifversion fpt %}

## Viewing usage for your personal account

You can view the usage of your personal account and download the usage data for further analysis.

1. In the upper-right corner of any page on GitHub, click your profile picture, then click **(icon: gear) Settings**.
1. In the "Access" section of the sidebar, click **(icon: credit-card) Billing and licensing**.
1. Click **Usage**.
1. To search or filter the graph, click the search bar. Then click the filter you want to use.
1. To further filter the graph, use the dropdown menus.

   * To see the usage by group, select **Group**, then click a group.
   * To filter by time, select **Time Frame**, then click a time period.
   * Optionally, to view the monthly budget and actual usage per day, select **Group: None** and **Time Frame: Current Month**.

   Below the graph, you can see a more granular overview of the usage. Click the arrow next to a specific date to see a nested table with usage per SKU, units, price/unit, and actual usage.

   >[!NOTE] The usage graph is configured to represent the start of the month to the end of the month, not your specific billing period.

1. To request a CSV usage report, select **Get usage report** in the upper-right corner of the page.

   You can choose a pre-selected option or use the "Custom range" option to specify a date range of up to 31 days.

{% endif %}

## Viewing usage for your {% ifversion fpt %}organization{% elsif ghec or ghes %}enterprise{% endif %}

{% ifversion fpt %}Organization **owners**{% elsif ghec or ghes %}Enterprise **owners**{% endif %} and **billing managers** can view the usage of your {% ifversion fpt %}organization{% elsif ghec or ghes %}enterprise{% endif %} members and download the usage data for further analysis.

{% ifversion fpt %}

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. On the left side of the page, in the organization sidebar, click **(icon: credit-card) Billing & Licensing**.

{% elsif ghec %}

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: credit-card) Billing and licensing**.

{% endif %}

1. Click **Usage**, then click **Metered usage** or **AI usage**.
1. To search or filter the graph, click the search bar. Then click the filter you want to use.
1. To further filter the graph, use the dropdown menus.

   * To see the usage by group, select **Group**, then click a group.
   * To filter by time, select **Time Frame**, then click a time period.
   * Optionally, to view the monthly budget and actual usage per day, select **Group: None** and **Time Frame: Current Month**.

   Below the graph, you can see a more granular overview of the usage. Click the arrow next to a specific date to see a nested table with usage per SKU, units, price/unit, and actual usage.

   >[!NOTE] The usage graph is configured to represent the start of the month to the end of the month, not your specific billing period.

1. To request a CSV usage report, select **(icon: download) Get usage report** in the upper-right corner of the page.

> [!NOTE] Data for the detailed usage report is available only through the GitHub web interface and cannot be obtained via the REST API `/usage` endpoint. The REST API only provides access to summarized billing information.

## Viewing license usage

You can view the license usage of your {% ifversion fpt %}organization{% elsif ghec or ghes %}enterprise{% endif %} members and download the usage data for further analysis.

{% ifversion fpt %}

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. On the left side of the page, in the organization sidebar, click **(icon: credit-card) Billing & Licensing**.

{% elsif ghec %}

The following license types are available:

* User
* GitHub Secret Protection and GitHub Code Security
* GitHub Enterprise

You can also view your active GitHub Enterprise instances and users.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: credit-card) Billing and licensing**.

{% endif %}

1. From the list of "Billing & licensing" pages, click **Licensing**.
1. To download a CSV report of the license usage, click (icon: kebab-horizontal) to the right of the usage you want to download, then click **(icon: download) CSV report**.

## Further reading

{% ifversion ghec %}
* [AUTOTITLE](/rest/billing/billing){% endif %}
* [AUTOTITLE](/billing/how-tos/manage-plan-and-licenses/manage-user-licenses)
