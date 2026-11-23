---
title: Exporting data from security overview
shortTitle: Export data
intro: From security overview, you can export CSV files of the data used for your organization or enterprise's overview, risk, coverage, and code scanning pull request insights pages.
permissions: "Access requires:\n* Organization views: **write** access to repositories in the organization\n* Enterprise views: organization owners and security managers"
product: "{% ifversion fpt %}\nOrganizations owned by a GitHub Team account with GitHub Secret Protection or GitHub Code Security, or owned by a GitHub Enterprise account\n{% endif %}"
versions:
  feature: security-overview-export-data
contentType: how-tos
redirect_from:
  - /code-security/security-overview/exporting-data-from-the-risk-and-coverage-pages
  - /code-security/security-overview/exporting-data-from-security-overview
  - /code-security/how-tos/view-and-interpret-data/analyze-organization-data/exporting-data-from-security-overview
category:
  - Secure at scale
---

From security overview, you can download comma-separated values (CSV) files containing data from several pages of your organization{% ifversion security-overview-export-data %} or enterprise{% endif %}'s security overview. These files can be used for efforts like security research and in-depth data analysis, and can integrate easily with external datasets.

The CSV file you download will contain data corresponding to the filters you have applied to security overview. For example, if you add the filter `dependabot-alerts:enabled`, your file will only contain data for repositories that have enabled Dependabot alerts.

{% ifversion ai-powered-security-detections %}
CSV files exported from the "Coverage" view include a `Code Scanning AI Scan for pull requests` column. The value for each repository is `enabled` or `not-enabled`.

In the "Code scanning on pull requests" report, CSV export is available on the **CodeQL** tab. CSV export is not yet available on the **AI Scan** tab.
{% endif %}

> [!NOTE]
> In the "Teams" column of the CSV file, each repository will list a maximum of 20 teams with write access to that repository. If more than 20 teams have write access to a repository, the data will be truncated.

## Exporting overview, coverage, and risk data from your organization's security overview

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. In the "Organizations" section, select the organization for which you would like to download security overview data.
1. Under your organization name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. In the sidebar, click **(icon: graph) Overview**, **(icon: meter) Coverage**, **(icon: shield) Risk**, or **(icon: graph) {% ifversion ai-powered-security-detections %}Code scanning on pull requests{% else %}CodeQL pull requests{% endif %}**.
1. Next to the search bar, click **(icon: download) Export CSV**.

    It may take a moment for GitHub to generate the CSV file of your data. Once the CSV file generates, the file will automatically start downloading, and a banner will appear confirming your report is ready. If you are downloading the CSV from the overview page, you will also receive an email when your report is ready, containing a link to download the CSV.

> [!NOTE]
> The summary views ("Overview", "Coverage" and "Risk") show data only for default alerts. Code scanning alerts from third-party tools, and secret scanning alerts for generic patterns or for ignored directories are all omitted from these views. Consequently, files exported from the summary views do not contain data for these types of alert.

## Exporting overview, coverage, and risk data from your enterprise's security overview

{% ifversion ghes %}1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.{% else %}1. Navigate to GitHub Enterprise Cloud.
                                                                                             1. In the top-right corner of GitHub, click your profile picture.
                                                                                             1. Depending on your environment, click **Enterprise**, or click **Enterprises** then click the enterprise you want to view.{% endif %}
1. At the top of the page, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. Choose the page that you want to export data from by clicking on **Overview**, **Risk**, or **Coverage**.
1. Next to the search bar, click (icon: download) **Export CSV**.

    It may take a moment for GitHub to generate the CSV file of your data. Once the CSV file generates, the file will automatically start downloading, and a banner will appear confirming your report is ready. If you are downloading the CSV from the overview page, you will also receive an email when your report is ready, containing a link to download the CSV.
