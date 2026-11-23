---
title: Finding repositories with security alerts using security overview
shortTitle: Find insecure repositories
intro: Monitor and prioritize security alerts with security overview.
permissions: 'Organization owners, security managers, and organization members with the **admin** role'
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
contentType: how-tos
redirect_from:
  - /code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings-on-a-repository
  - /code-security/securing-your-organization/managing-the-security-of-your-organization/interpreting-security-findings
  - /code-security/securing-your-organization/managing-the-security-of-your-organization
  - /code-security/how-tos/view-and-interpret-data/analyze-organization-data/interpreting-security-findings
category:
  - Secure at scale
---

> [!NOTE]
> The information shown by security overview varies according to your access to repositories and organizations, and according to whether Advanced Security features are used by those repositories and organizations. For more information, see [AUTOTITLE](/code-security/concepts/security-at-scale/security-overview).

1. On GitHub, navigate to the main page of the organization.
1. Under your organization name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. By default, security overview shows alerts for all native GitHub tools. To display alerts for a specific tool, replace `tool:github` in the filter text box:
    * `tool:dependabot` shows only alerts for dependencies identified by Dependabot
    * `tool:secret-scanning` shows only alerts for secrets identified by secret scanning
    * `tool:codeql` shows only alerts for potential security vulnerabilities identified by CodeQL code scanning
1. You can add further filters to show only the repositories you want to assess. The list of repositories and metrics displayed on the page automatically update to match your current selection. For more information on filtering, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/filtering-alerts-in-security-overview).
1. Optionally, use the sidebar on the left to explore alerts for a specific security feature in greater detail. On each page, you can use filters that are specific to that feature to refine your search.
