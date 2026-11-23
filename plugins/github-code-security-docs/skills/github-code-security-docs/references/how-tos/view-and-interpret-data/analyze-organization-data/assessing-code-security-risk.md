---
title: Assessing the security risk of your code
shortTitle: Assess security risk of code
allowTitleToDifferFromFilename: true
intro: You can use security overview to see which teams and repositories are affected by security alerts, and identify repositories for urgent remedial action.
permissions: "Access requires:\n* Organization views: **write** access to repositories in the organization\n* Enterprise views: organization owners and security managers"
product: "{% ifversion fpt %}\nOrganizations owned by a GitHub Team account with GitHub Secret Protection or GitHub Code Security, or owned by a GitHub Enterprise account\n{% endif %}"
contentType: how-tos
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/security-overview/viewing-the-security-overview
  - /code-security/security-overview/assessing-code-security-risk
category:
  - Secure at scale
---

## Exploring the security risks in your code

You can use the different views on your **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab to explore the security risks in your code.

* **Overview:** use to explore trends in **Detection**, **Remediation**, and **Prevention** of security alerts.
* **Risk:** use to explore the current state of repositories, across all alert types.
* **Assessments:** use to explore the current state of repositories, for secret leaks specifically
* **Findings:** use to explore code scanning, Dependabot, or secret scanning alerts in greater detail.

These views provide you with the data and filters to:

* Assess the landscape of security risk of code stored in all your repositories.
* Identify the highest impact vulnerabilities to address.
* Monitor your progress in remediating potential vulnerabilities.
* Understand how your organization is affected by secret leaks and exposures.{% ifversion security-overview-export-data %}
* Export your current selection of data for further analysis and reporting.  {% endif %}

For information about the **Overview**, see [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/analyze-organization-data/viewing-security-insights).

## Viewing organization-level security risks in code

1. On GitHub, navigate to the main page of the organization.
1. Under your organization name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. To display the "Security risk" view, in the sidebar, click **(icon: shield) Risk**.
1. Use options in the page summary to filter results to show the repositories you want to assess. The list of repositories and metrics displayed on the page automatically update to match your current selection. For more information on filtering, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/filtering-alerts-in-security-overview).
    * Use the **Teams** dropdown to show information only for the repositories owned by one or more teams.
    * Click **NUMBER affected** or **NUMBER unaffected** in the header for any feature to show only the repositories with open alerts or no open alerts of that type.
    * Click any of the descriptions of "Open alerts" in the header to show only repositories with alerts of that type and category. For example, **1 critical** to show the repository with a critical alert for Dependabot.
    * At the top of the list of repositories, click **NUMBER Archived** to show only repositories that are archived.
    * Click in the search box to add further filters to the repositories displayed.

   ![Screenshot of the "Security risk" view for an organization. The options for filtering are outlined in dark orange.](/assets/images/help/security-overview/security-risk-view-highlights.png)

    > [!NOTE] The set of unaffected repositories includes all repositories without open alerts and also any repositories where the security feature is not enabled.

1. Optionally, use the sidebar on the left to explore alerts for a specific security feature in greater detail. On each page, you can use filters that are specific to that feature to refine your search. {% ifversion security-overview-export-data %}
1. Optionally, use the **(icon: download) Export CSV** button to download a CSV file of the data currently displayed on the page for security research and in-depth data analysis. For more information, see [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/analyze-organization-data/export-data). {% endif %}

>[!NOTE] The summary views ("Overview", "Coverage" and "Risk") show data only for default alerts. Secret scanning alerts for ignored directories and generic alerts are all omitted from these views. Consequently, the individual alert views may include a larger number of open and closed alerts.

## Viewing enterprise-level security risks in code

You can view data for security alerts across organizations in an enterprise.

> [!TIP]
> You can use the `owner` filter in the search field to filter the data by organization. {% ifversion ghec %}If you're an owner of an enterprise with managed users, you can use the `owner-type` filter to filter the data by the type of repository owner, so that you can view data from either organization-owned repositories or user-owned repositories. {% endif %}For more information, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/filtering-alerts-in-security-overview).

{% ifversion ghes %}1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.{% else %}1. Navigate to GitHub Enterprise Cloud.
                                                                                             1. In the top-right corner of GitHub, click your profile picture.
                                                                                             1. Depending on your environment, click **Enterprise**, or click **Enterprises** then click the enterprise you want to view.{% endif %}
1. At the top of the page, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. To display the "Security risk" view, in the sidebar, click **(icon: shield) Risk**.
1. Use options in the page summary to filter results to show the repositories you want to assess. The list of repositories and metrics displayed on the page automatically update to match your current selection. For more information on filtering, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/filtering-alerts-in-security-overview).
    * Use the **Teams** dropdown to show information only for the repositories owned by one or more teams.
    * Click **NUMBER affected** or **NUMBER unaffected** in the header for any feature to show only the repositories with open alerts or no open alerts of that type.
    * Click any of the descriptions of "Open alerts" in the header to show only repositories with alerts of that type and category. For example, **1 critical** to show the repository with a critical alert for Dependabot.
    * At the top of the list of repositories, click **NUMBER Archived** to show only repositories that are archived.
    * Click in the search box to add further filters to the repositories displayed.

    ![Screenshot of the "Security risk" view for an enterprise. The options for filtering are outlined in dark orange.](/assets/images/help/security-overview/security-risk-view-highlights-enterprise.png)

    > [!NOTE] The set of unaffected repositories includes all repositories without open alerts and also any repositories where the security feature is not enabled.
1. Optionally, use the sidebar on the left to explore alerts for a specific security feature in greater detail. On each page, you can use filters that are specific to that feature to refine your search.{% ifversion security-overview-export-data %}
1. Optionally, use the (icon: download) **Export CSV** button to download a CSV file of the data currently displayed on the page for security research and in-depth data analysis. For more information, see [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/analyze-organization-data/export-data). {% endif %}

>[!NOTE] The summary views ("Overview", "Coverage" and "Risk") show data only for default alerts. Secret scanning alerts for ignored directories and generic alerts are all omitted from these views. Consequently, the individual alert views may include a larger number of open and closed alerts.

{% ifversion security-campaigns %}

## Next steps

When you have assessed your security risks, you are ready to create a security campaign to collaborate with developers to remediate alerts. For information about fixing security alerts at scale, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/creating-managing-security-campaigns) and [AUTOTITLE](/code-security/tutorials/secure-your-organization/best-practice-fix-alerts-at-scale).
{% endif %}
