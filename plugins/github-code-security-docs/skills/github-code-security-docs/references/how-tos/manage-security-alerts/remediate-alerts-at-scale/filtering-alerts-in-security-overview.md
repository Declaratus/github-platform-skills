---
title: Filtering alerts in security overview
intro: Find the security alerts that matter most by filtering your security overview data.
permissions: "Access requires:\n* Organization views: **write** access to repositories in the organization\n* Enterprise views: organization owners and security managers"
product: "{% ifversion fpt %}\nOrganizations owned by a GitHub Team account with GitHub Secret Protection or GitHub Code Security, or owned by a GitHub Enterprise account\n{% endif %}"
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
contentType: how-tos
shortTitle: Filter security alerts
redirect_from:
  - /code-security/security-overview/filtering-alerts-in-the-security-overview
  - /code-security/security-overview/filtering-alerts-in-security-overview
category:
  - Secure at scale
---

Security overview can show alerts across many repositories in your organization or enterprise. Filtering helps you focus on specific alerts based on severity, alert type, repository characteristics, and other factors.

You can combine multiple filters to narrow your results. For example, you can show only critical Dependabot alerts in public repositories owned by a specific team.

For a complete list of available filters, see [AUTOTITLE](/code-security/reference/security-at-scale/overview-dashboard-filters).

> [!NOTE]
> The information shown by security overview varies according to your access to repositories and organizations, and according to whether Advanced Security features are used by those repositories and organizations. For more information, see [AUTOTITLE](/code-security/concepts/security-at-scale/security-overview).

## Filter methods

All security views have features to help you define filters. These provide an easy way to set up filters and understand the options available.

* **Interactive search text box.** When you click in the search box and press the keyboard "Space" key, a pop-up text box shows the filter options available in that view. You can use the mouse or keyboard arrow keys to select the options you want in the text box before pressing the keyboard "Return" key to add the filter. Supported for all views.
* **Dropdown selectors and toggles.** Shown at the end of the "Search text box" or in the header of the data table. As you choose the data to view, the filters shown in the search text box are updated accordingly. Supported on the alert views.
* **Advanced filters dialog.** When you click the **(icon: filter) Filter** button, you can use dropdown lists to select the "Qualifier," "Operator," and "Values" for each filter. Supported on the "Overview" and "Insights" views.

## Accessing security overview for your organization

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. In the "Organizations" section, select the organization you want to look at.
1. Under your organization name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.

## Accessing security overview for your enterprise

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. Click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab. The "Overview" dashboard of security overview is displayed.

## Applying simple filters

1. In security overview, select the view of your choice on the left navigation panel. For instructions about how to access security overview, see [Accessing security overview for your organization](#accessing-security-overview-for-your-organization) or [Accessing security overview for your enterprise](#accessing-security-overview-for-your-enterprise).
1. Click in the box adjacent to the **(icon: filter) Filter** control. If there is text in the box, delete it. A popup shows available filters for the current view.
1. Select a filter and a value for the filter.
1. Press <kbd>Enter</kbd>.

## Using the advanced filters dialog

The advanced filters dialog is available in "Overview" and "Insights" views and helps you build filters.

1. In the desired view of security overview, click **(icon: filter) Filter**.
1. In the "Advanced filters" dialog, use the dropdown lists to build your filter:
   * **Qualifier**: Select the filter type (for example, "Severity" or "Tool")
   * **Operator**: Select how to match values (for example, "is one of" and "is not one of")
   * **Value**: Select what to filter for (for example, "Critical" or "CodeQL")
1. Optionally, click **(icon: plus) Add a filter** to add a custom filter.
1. Click **Apply**.

## Combining filters

* **AND logic (default):** Multiple filters show results matching all filters.

  `severity:critical visibility:public`

* **OR logic:** Use commas between values for a single filter.

  `severity:critical,high`

* **NOT logic:** Use a minus sign to exclude results.

  `-repo:my-org/archived-repo`

## Common filter examples

* Show critical alerts in public repositories:

  `severity:critical visibility:public`

* Show repositories with more than N code scanning alerts:

  `code-scanning-alerts:>100`

* Show alerts for a specific team's repositories:

  `team:security-team`

* Show Dependabot alerts with available fixes:

  `has:patch`

* Show active secrets from a specific provider:

  `provider:amazon_aws validity:active`
