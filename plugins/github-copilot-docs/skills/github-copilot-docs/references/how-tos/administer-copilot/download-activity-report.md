---
title: Downloading a GitHub Copilot activity report for your organization or enterprise
intro: Monitor Copilot license usage with a detailed report.
permissions: Enterprise owners and organization owners
product: 'Copilot Enterprise or Copilot Business'
versions:
  feature: copilot
allowTitleToDifferFromFilename: true
shortTitle: Download activity report
redirect_from:
  - /copilot/how-tos/administer/download-activity-report
contentType: how-tos
category:
  - Manage Copilot for a team
---

You can download a CSV report for Copilot user activity in your organization. The data in the report allows you to:

* Accurately monitor Copilot license usage accurately.
* Understand patterns in user authentication.
* Manage licenses and measure key performance indicators.

## Downloading the report for an enterprise

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: credit-card) Billing and licensing**.
1. In the "Billing and licensing" sidebar, click **(icon: law) Licensing**.
1. Next to "Copilot", click **(icon: download) Get activity report**.

## Downloading the report for an organization

1. Navigate to your organization settings.
1. In the left sidebar, click **Copilot**, then click **Access**.
1. Next to "Access management", click **Get usage report**, then click **Get activity report**.

   ![Screenshot of the "Access" page. The "Get activity report" button is highlighted with an orange outline.](/assets/images/help/copilot/activity-report-org.png)

## Report fields

For field definitions and details of included features, see [AUTOTITLE](/copilot/reference/metrics-data#copilot-activity-report).
