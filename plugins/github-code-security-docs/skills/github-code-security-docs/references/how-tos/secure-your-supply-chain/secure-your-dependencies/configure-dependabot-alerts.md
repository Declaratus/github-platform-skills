---
title: Configuring Dependabot alerts
intro: Enable Dependabot alerts to be generated when a new vulnerable dependency is found in one of your repositories.
shortTitle: Configure Dependabot alerts
permissions: "* Repository administrators, organization owners, and people with **write** or **maintain** access\n* Users and teams with explicit access. See [Granting access to security alert](/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository#granting-access-to-security-alerts)."
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/dependabot/dependabot-alerts/configuring-dependabot-alerts
  - /code-security/dependabot/dependabot-alerts
  - /code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configuring-dependabot-alerts
contentType: how-tos
category:
  - Secure your dependencies
---

When Dependabot detects vulnerable dependencies in a repository, it generates alerts. For more information, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-alerts).

You can enable or disable Dependabot alerts for:
* Your personal account
* Your repository
* Your organization{% ifversion dependabot-alerts-enterprise-enablement or ghes %}
* Your enterprise{% endif %}

{% ifversion ghes %}
> [!NOTE]
> An enterprise owner must first set up Dependabot for your enterprise before you can configure Dependabot alerts. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-dependabot-for-your-enterprise).
{% endif %}

## Managing Dependabot alerts for your personal account

{% ifversion fpt or ghec %}

You can enable or disable Dependabot alerts for all repositories owned by your personal account.

<a href="https://github.com/settings/security_analysis?ref_product=github&ref_type=engagement&ref_style=button" target="_blank" class="btn btn-primary mt-3 mr-3 no-underline"><span>Go to your security settings</span> (icon: link-external)</a>

### Enabling or disabling Dependabot alerts for existing repositories

1. Under "Advanced Security", to the right of Dependabot alerts, click **Disable all** or **Enable all**.
1. Optionally, to enable Dependabot alerts by default for new repositories that you create, in the dialog box, select "Enable by default for new repositories".
1. Click **Disable Dependabot alerts** or **Enable Dependabot alerts** to disable or enable Dependabot alerts for all the repositories you own.

When you enable Dependabot alerts for existing repositories, you will see any results displayed on GitHub within minutes.

### Enabling or disabling Dependabot alerts for new repositories

1. Under "Advanced Security", to the right of Dependabot alerts, select **Automatically enable for new repositories**.

{% else %}
Dependabot alerts for your repositories can be enabled or disabled by your enterprise owner. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-dependabot-for-your-enterprise).

{% endif %}

## Managing Dependabot alerts for your repository

You can manage Dependabot alerts for your public, private or internal repository.

By default, we notify people with write, maintain, or admin permissions in the affected repositories about new Dependabot alerts. GitHub never publicly discloses insecure dependencies for any repository. You can also make Dependabot alerts visible to additional people or teams working on repositories that you own or have admin permissions for.

{% ifversion fpt or ghec %}
If you enable security and analysis features, GitHub performs read-only analysis on your repository.
{% endif %}

{% ifversion ghes %}
An enterprise owner must first set up Dependabot for your enterprise before you can manage Dependabot alerts for your repository. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-dependabot-for-your-enterprise).{% endif %}

### Enabling or disabling Dependabot alerts for a repository

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. Under "Advanced Security", to the right of Dependabot alerts, click **Enable** to enable alerts or **Disable** to disable alerts.

## Managing Dependabot alerts for your organization

You can enable Dependabot alerts for all eligible repositories in your organization. For more information, see [AUTOTITLE](/code-security/concepts/security-at-scale/organization-security).

{% ifversion ghec or ghes %}

## Managing Dependabot alerts for your enterprise

{% ifversion security-configuration-enterprise-level %}

Security configurations, which are collections of security settings, allow you to manage Dependabot alerts for your enterprise. You can configure your own custom security configuration to have the enablement settings to meet the specific security needs of your enterprise. See [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/establish-complete-coverage/create-custom-configuration).

{% else %}

You can enable or disable Dependabot alerts for all current and future repositories owned by organizations in your enterprise. Your changes affect all repositories.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. In the left sidebar, click **(icon: codescan) Advanced Security**.
1. In the "Dependabot" section, to the right of Dependabot alerts, click **Disable all** or **Enable all**.
1. Optionally, select **Automatically enable for new repositories** to enable Dependabot alerts by default for your organizations' new repositories.
{% endif %}

{% endif %}

## Managing Dependabot alerts at scale with rules

Additionally, you can use Dependabot auto-triage rules to manage your alerts at scale, so you can auto-dismiss or snooze alerts, and specify which alerts you want Dependabot to open pull requests for. For information about the different types of auto-triage rules, and whether your repositories are eligible, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-auto-triage-rules).
