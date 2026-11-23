---
title: Security overview
shortTitle: Security overview
intro: You can gain insights into the overall security landscape of your organization or enterprise and identify repositories that require intervention using security overview.
product: "Security overview is available for all organizations owned by GitHub Team or GitHub Enterprise that have run Secret risk assessment.\n\nAdditional views are available for {% ifversion ghec %}enterprises and their organizations.{% elsif ghes %}organizations.\n\n{% elsif fpt %}\n* Organizations owned by a GitHub Team account with GitHub Secret Protection or GitHub Code Security\n* Organizations owned by a GitHub Enterprise account\n{% endif %}\n\n<a href=\"https://github.com/get_started?with=risk-assessment\" class=\"btn btn-primary mt-3 mr-3 no-underline\"><span>Run a security risk assessment</span></a>\n"
redirect_from:
  - /code-security/security-overview/exploring-security-alerts
  - /code-security/security-overview/about-the-security-overview
  - /code-security/security-overview/about-security-overview
  - /code-security/security-overview
  - /code-security/concepts/security-at-scale/about-security-overview
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
contentType: concepts
category:
  - Secure at scale
---

{% ifversion fpt %}

Security overview provides insights into the security of code stored in repositories in your organization.

* **All organizations** on GitHub Team can use the free **secret risk assessment** to evaluate the exposure of their organization to leaked secrets, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/configure-specific-tools/viewing-your-security-risk-assessment-reports).
* GitHub Team accounts that purchase **GitHub Secret Protection or GitHub Code Security** have access to views with additional insights.

The information below describes the views available to organizations with GitHub Secret Protection or GitHub Code Security that you can use to identify trends in detection, remediation, and prevention of security alerts and dig deep into the current state of your repositories.

{% elsif ghec or ghes %}

Security overview contains focused views where you can explore trends in detection, remediation, and prevention of security alerts and dig deep into the current state of your codebases.

{% ifversion ghec %}
All organizations on GitHub Enterprise can use:
* **Secret risk assessment** to evaluate the exposure of their organization to leaked secrets, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/configure-specific-tools/viewing-your-security-risk-assessment-reports).
* **Dependabot** data to evaluate the security of their supply chain in all repositories.
{% else %}
All organizations on GitHub Enterprise can use Dependabot data to evaluate the security of their supply chain in all repositories.
{% endif %}

In addition, data for **Advanced Security** features, such as code scanning and secret scanning, is shown for organizations and enterprises that use GitHub Secret Protection, GitHub Code Security, or GitHub Advanced Security{% ifversion ghec %}, and for public repositories{% endif %}, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-alerts) and [AUTOTITLE](/get-started/learning-about-github/about-github-advanced-security).

{% endif %}

## About the views

> [!NOTE]
> All views show information and metrics for the **default** branches of the repositories you have permission to view in an organization or enterprise.

The views are interactive with filters that allow you to look at the aggregated data in detail and identify sources of high risk, see security trends, and see the impact of pull request analysis on blocking security vulnerabilities entering your code. As you apply multiple filters to focus on narrower areas of interest, all data and metrics across the view change to reflect your current selection. For more information, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/filtering-alerts-in-security-overview).

{% ifversion security-overview-export-data %}
From security overview, you can download comma-separated values (CSV) files containing data from several pages of your organization{% ifversion security-overview-export-data %} or enterprise{% endif %}'s security overview. These files can be used for efforts like security research and in-depth data analysis, and can integrate easily with external datasets. For more information, see [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/analyze-organization-data/export-data).
{% endif %}

There are dedicated views for each type of security alert. You can limit your analysis to a specific type of alert, and then narrow the results further with a range of filters specific to each view. For example, in the secret scanning view, you can use the "Secret type" filter to view only secret scanning alerts for a specific secret, like a GitHub personal access token.

> [!NOTE]
> Security overview displays active alerts raised by security features. If there are no alerts shown in security overview for a repository, undetected security vulnerabilities or code errors may still exist or the feature may not be enabled for that repository.

## About security overview for organizations

The application security team at your company can use the different views for both broad and specific analyses of your organization's security status. For example, the team can use the "Overview" dashboard view to track your organization's security landscape and progression.

You can find security overview on the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab for any organization. Each view shows a summary of the data that you have access to. As you add filters, all data and metrics across the view change to reflect the repositories or alerts that you've selected.

Security overview has multiple views that provide different ways to explore enablement and alert data.

* **Overview:** visualize trends in **Detection**, **Remediation**, and **Prevention** of security alerts. For information about accessing and using the dashboard, see [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/analyze-organization-data/viewing-security-insights). For detailed explanations of metrics and calculations, see [AUTOTITLE](/code-security/reference/security-at-scale/overview-dashboard-metrics).
* **Risk:** explore the risk from security alerts of all types or focus on a single alert type and identify your risk from specific vulnerable dependencies, code weaknesses, or leaked secrets, see [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/analyze-organization-data/assessing-code-security-risk).
* **Coverage:** assess the adoption of security features across repositories in the organization, see [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/analyze-organization-data/assessing-adoption-code-security).
* **Assessments:** regardless of the enablement status of Advanced Security features, organizations on GitHub Team and GitHub Enterprise can run a free report to scan the code in the organization for leaked secrets, see [AUTOTITLE](/code-security/concepts/secret-security/secret-security-with-github).{% ifversion security-campaigns %}
* **Campaigns:** coordinate and measure targeted remediation efforts, grouping related security tasks across repositories, assigning owners, and tracking progress toward defined risk‑reduction goals.{% endif %}
* **Enablement:** see how quickly different teams are adopting security features.
* **{% ifversion ai-powered-security-detections %}Code scanning on pull requests{% else %}CodeQL pull requests{% endif %}:** assess the impact of running CodeQL{% ifversion ai-powered-security-detections %} and AI Scan{% endif %} on pull requests, and how development teams resolve {% ifversion ai-powered-security-detections %}alerts and findings{% else %}code scanning alerts{% endif %}, see [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/analyze-organization-data/viewing-metrics-for-pull-request-alerts).
* **Dependabot**: prioritize and track critical vulnerabilities by identifying, remediating, and measuring security improvements across repositories.
* **Secret scanning:** find out which types of secret are blocked by push protection and which teams are bypassing push protection, see [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/analyze-organization-data/viewing-metrics-for-secret-scanning-push-protection) and [AUTOTITLE](/code-security/how-tos/secure-your-secrets/manage-bypass-requests/review-bypass-requests).

{% ifversion security-campaigns %}
You also create and manage security campaigns to remediate alerts from security overview, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/creating-managing-security-campaigns) and [AUTOTITLE](/code-security/tutorials/secure-your-organization/best-practice-fix-alerts-at-scale).
{% endif %}

## About security overview for enterprises

You can find security overview on the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab for your enterprise. Each page displays aggregated and repository-specific security information for your enterprise.

Security overview for enterprises has multiple views that provide different ways to explore data, including an overview dashboard that visualizes alert trends. For information about the dashboard, see [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/analyze-organization-data/viewing-security-insights) and [AUTOTITLE](/code-security/reference/security-at-scale/overview-dashboard-metrics).

## Access to data in security overview

What you can see in security overview depends on your role and permissions in the organization or enterprise.

In general:

* **Organization owners and security managers** can view security data across all repositories in their organization.
* **Organization members** can view data only for repositories where they have access to security alerts.
* **Enterprise owners** can view aggregated security data in the enterprise-level security overview for organizations where they are an organization owner or security manager. To see repository-level details, they must have the appropriate role within the organization.

Security overview displays data only for repositories you have permission to view, and some views or actions may be limited based on your role.

For detailed, role-by-role permission information, including which views are available and how repository access affects visibility, see [AUTOTITLE](/code-security/reference/permissions/security-overview).

## Understanding dashboard data accuracy

The overview dashboard displays metrics based on the current state of your repositories and the historical state of security alerts. This data model has important implications for data consistency:

**Data changes over time:** Dashboard metrics can change for the same historical time period when viewed at different times. This occurs when repositories are deleted, security advisories are modified, or other changes affect the underlying data. If you need consistent data for compliance reports or auditing purposes, use the audit log instead. See [AUTOTITLE](/code-security/concepts/security-at-scale/audit-security-alerts).

**Alert data is historical; repository attributes are current:** The dashboard tracks security alerts based on their historical state during the selected time period. However, repository filters (such as archived/active status) reflect the _current state_ of repositories.

For example, if you archive a repository today, any open alerts in that repository are automatically closed. If you then view the overview dashboard for last week:

* The repository only appears when you filter to show archived repositories (its current state)
* The alerts from that repository appear as open (their state during last week)

This design ensures alert trends accurately reflect security activity during the time period you're analyzing, while repository filters help you focus on your current repository structure.

## Further reading

* [AUTOTITLE](/code-security/getting-started/quickstart-for-securing-your-repository){% ifversion fpt or ghec %}
* [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security){% elsif ghes %}
* [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/establish-complete-coverage){% endif %}
* [AUTOTITLE](/code-security/tutorials/adopting-github-advanced-security-at-scale/introduction-to-adopting-github-advanced-security-at-scale)
