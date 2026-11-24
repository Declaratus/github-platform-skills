---
title: Managing access to agentic autofix for code scanning
shortTitle: Manage agentic autofix
intro: Control the rollout of agentic autofix across your enterprise, organizations, and repositories.
product: "Agentic Autofix is available for public repositories on GitHub.com and for organization-owned repositories with GitHub Code Security or GitHub Advanced Security. Users don't need a GitHub Copilot license. Agentic Autofix is not available for user-owned repositories in an enterprise that uses Enterprise Managed Users."
versions:
  fpt: '*'
  ghec: '*'
contentType: how-tos
category:
  - Find and fix code vulnerabilities
---

## About access and rollout

Access controls for agentic autofix cascade from the enterprise to the organization and repository:

* For an enterprise-owned organization, an enterprise owner or security manager must allow organizations to configure agentic autofix. Allowing the feature doesn't enable it for organizations or repositories.
* An organization owner or security manager can enable agentic autofix for the organization. The organization setting enables it for eligible repositories by default.
* Repository administrators can opt individual repositories out or re-enable them, subject to the enterprise and organization settings.
* For an eligible public repository owned by a personal account, a repository administrator can enable or disable agentic autofix directly.

Agentic Autofix is not available for user-owned repositories in an enterprise that uses Enterprise Managed Users.

Enabling agentic autofix does not change the authentication requirements for assigning alerts through the REST API. GitHub App installation access tokens cannot be used to assign an alert to Copilot or start an agentic autofix session. For information about assigning an alert to Copilot, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/resolve-alerts#fixing-alerts-with-copilot).

If your organization used agentic autofix during the public preview, you must enable it again.

Before you enable the feature, review how the use of AI credits and GitHub Actions minutes affects your costs.

For a standalone organization, skip the enterprise procedure. For an eligible public repository owned by a personal account, skip the enterprise and organization procedures.

## Allowing agentic autofix for an enterprise

Enterprise owners and security managers can allow organizations in an enterprise to configure agentic autofix. This policy doesn't enable the feature for any organization or repository.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under (icon: law) "Policies", click **Advanced Security**.
1. For the **Agentic Autofix** policy, select **All organizations: Allowed**.

## Enabling agentic autofix for an organization

Organization owners and security managers can enable agentic autofix for all eligible repositories in their organization. For an enterprise-owned organization, the enterprise policy must also allow it.

Before you enable the organization setting, coordinate with repository administrators about any repositories that should opt out.

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the "(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security** then **Global settings**.
1. Under "Code scanning," to enable the feature, set **Agentic Autofix** to **On**.

## Managing agentic autofix for a repository

For an organization-owned repository, agentic autofix is enabled by default when the organization enables it. Repository administrators can disable or re-enable it for an individual repository. For an eligible public repository owned by a personal account, a repository administrator can enable or disable it directly.

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. In the "Code Security" section, enable or disable **Agentic Autofix** by setting the toggle to **On** or **Off**.

After you enable agentic autofix, users with write access to the repository can assign code scanning alerts to Copilot. See [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/resolve-alerts#fixing-alerts-with-copilot).

## Disabling agentic autofix

You can disable agentic autofix at the enterprise, organization, or repository level. If you disable it at the enterprise or organization level, repository administrators cannot re-enable it.

### Disallowing agentic autofix for an enterprise

Enterprise owners and security managers can prevent all organizations and repositories in their enterprise from using agentic autofix.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under (icon: law) "Policies", click **Advanced Security**.
1. For the **Agentic Autofix** policy, select **All organizations: Not allowed**.

### Disabling agentic autofix for an organization

Organization owners and security managers can disable agentic autofix for all repositories in their organization.

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the "(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security** then **Global settings**.
1. Under "Code scanning," set **Agentic Autofix** to **Off**.

### Disabling agentic autofix for a repository

Repository administrators can opt an individual repository out of agentic autofix. For an eligible public repository owned by a personal account, this disables the feature directly.

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. In the "Code Security" section, set **Agentic Autofix** to **Off**.
