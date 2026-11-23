---
title: Viewing metrics for Dependabot alerts
shortTitle: View Dependabot metrics
allowTitleToDifferFromFilename: true
intro: You can use security overview to see how many Dependabot alerts are in repositories across your organization, to prioritize the most critical alerts to fix, and to identify repositories where you may need to take action.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
permissions: "Access requires:\n* The `admin` role for the repository.\n* A custom repository role with the \"View Dependabot alerts\" fine-grained permissions for the repository. For more information, see [AUTOTITLE](/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/about-custom-repository-roles#security).\n* Access to alerts for the repository. For more information, see [AUTOTITLE](/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository#granting-access-to-security-alerts)."
product: 'Organizations owned by a GitHub Team account with GitHub Code Security, or owned by a GitHub Enterprise account with GitHub Code Security'
contentType: how-tos
redirect_from:
  - /code-security/security-overview/viewing-metrics-for-dependabot-alerts
category:
  - Secure at scale
---

You can view metrics for Dependabot alerts to track and prioritize vulnerabilities across your organization. For more information about the available metrics and how to use them, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-alert-metrics).

This article explains how to access and view these metrics for your organization.

## Viewing metrics for Dependabot for an organization

1. On GitHub, navigate to the main page of the organization.
1. Under your organization name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. In the sidebar, under "Insights", click **(icon: dependabot) Dependabot dashboard**.
1. Optionally, use the filters at your disposal, or build your own filters. See [Dependabot dashboard view filters](/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/filtering-alerts-in-security-overview).
1. Optionally, click on a number on the x-axis of the chart to filter the alert list by the relevant criteria (for example `has:patch severity:critical,high epss-percentage:>=0.01`).
1. Optionally, click on an individual repository to see the associated Dependabot alerts.

## Configuring funnel categories

The default funnel order is `has:patch, severity:critical,high, epss-percentage:>=0.01`. By tailoring the funnel’s order, you and your teams can focus on the vulnerabilities that matter most to your organization, environments, or regulatory obligations, making remediation efforts more effective and aligned with your specific needs.

1. On GitHub, navigate to the main page of the organization.
1. Under your organization name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. In the sidebar, under "Insights", click **(icon: dependabot) Dependabot dashboard**.
1. On the top right of the "Alert prioritization" graph, click (icon: gear).
1. In the "Configure funnel order" dialog, move the criteria as desired.
1. Once you're done, click **Move** to save your changes.

>[!TIP] You can reset the funnel order back to the default settings by clicking **Reset to default** to the right of the graph.

## Using metrics effectively

Use Dependabot metrics to:

* **Prioritize remediation**: Focus on critical and high-severity alerts that are easily exploitable. Developers can use severity and patch availability filters to identify vulnerabilities they can fix immediately, reducing noise and focusing attention on actionable issues.
* **Monitor progress**: Track how quickly your organization resolves security vulnerabilities and measure the effectiveness of vulnerability management efforts.
* **Make data-driven decisions**: Allocate resources based on actual risk and usage patterns. The repository-level breakdown helps you understand which projects are most at risk and where to focus remediation efforts.
* **Identify trends**: Understand whether your security posture is improving over time and ensure compliance with organizational or regulatory timelines.
* **Understand risk profiles**: Developers can use these metrics to understand the risk profile of their dependencies, enabling informed prioritization of work.
