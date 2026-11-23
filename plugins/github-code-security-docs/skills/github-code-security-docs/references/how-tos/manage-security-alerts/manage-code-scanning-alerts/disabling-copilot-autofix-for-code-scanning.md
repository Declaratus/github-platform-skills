---
title: Disabling Copilot Autofix for code scanning
shortTitle: Disable Copilot Autofix
intro: 'You can disable Copilot Autofix for an enterprise, organization, or repository.'
product: "Agentic Autofix has narrower eligibility requirements than Copilot Autofix, and isn't available for user-owned repositories in an enterprise that uses Enterprise Managed Users. For details, see [AUTOTITLE](/code-security/concepts/code-scanning/autofix-for-code-scanning#where-is-autofix-available).\n\nCopilot Autofix for code scanning is available for the following repository types:\n\n{% ifversion fpt %}\n* Public repositories on GitHub.com\n* Organization-owned repositories on GitHub Team with GitHub Code Security enabled{% endif %}\n\n{% ifversion ghec %}\n* Public repositories on GitHub.com\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with GitHub Code Security enabled{% endif %}\n\nFor more information about eligible products, see [AUTOTITLE](/get-started/learning-about-github/about-github-advanced-security)."
versions:
  feature: code-scanning-autofix
contentType: how-tos
redirect_from:
  - /code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/disabling-autofix-for-code-scanning
  - /code-security/code-scanning/managing-code-scanning-alerts/disabling-autofix-for-code-scanning
category:
  - Find and fix code vulnerabilities
---


This article covers disabling Copilot Autofix. Agentic Autofix has separate access controls. To disable agentic autofix, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/managing-access-to-agentic-autofix-for-code-scanning#disabling-agentic-autofix).

For enterprise-owned organizations, controls for Copilot Autofix follow this hierarchy:

* Enterprise owners control whether the feature is **allowed** in the enterprise. When allowed, it **can** be enabled at lower levels (but is not automatically enabled).
* When it's enabled by the enterprise, organization owners can still disable it for their organization. This prevents any repository in the organization from enabling it.
* If both the enterprise and organization have the feature enabled, repository administrators can disable it for the individual repository.

For standalone organizations, the organization and repository controls apply without an enterprise policy.

Disabling Copilot Autofix at any level closes all open suggestions that it added as comments on code scanning alerts in affected pull requests. If you later re-enable it, suggestions are generated only for new pull requests. To generate suggestions for existing pull requests, re-run code scanning security analysis.

> [!NOTE]
> Copilot Autofix is an integral part of GitHub Code Quality and will continue to run on code quality results even when it is disabled for code security results.

## Blocking use of Copilot Autofix for an enterprise

Enterprise owners can disallow Copilot Autofix for security results across all organizations and repositories in their enterprise.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under (icon: law) "Policies", click **Advanced Security**.
1. Under "Copilot Autofix", use the dropdown and select **All organizations: Not allowed**.

## Disabling Copilot Autofix for an organization

Organization owners can disable Copilot Autofix for all repositories in their organization. For enterprise-owned organizations, this setting is only available if the enterprise allows Copilot Autofix.

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the "(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security** then **Global settings**.
1. Under the "Code scanning" section, set **Copilot Autofix** to **Off**.

## Disabling Copilot Autofix for a repository

Repository administrators can disable Copilot Autofix if their organization enables it. For enterprise-owned organizations, this setting is only available if the enterprise also allows Copilot Autofix.

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. In the "Code Security" section, set **Copilot Autofix** to **Off**.
