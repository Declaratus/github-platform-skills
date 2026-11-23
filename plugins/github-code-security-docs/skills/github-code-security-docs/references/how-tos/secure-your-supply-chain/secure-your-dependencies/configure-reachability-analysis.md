---
title: Configuring reachability analysis for Dependabot alerts
intro: Enable reachability analysis to prioritize alerts based on whether your application can call vulnerable functions in its dependencies.
allowTitleToDifferFromFilename: true
shortTitle: Configure reachability analysis
permissions: 'Repository administrators, organization owners, security managers, and enterprise owners can enable or disable reachability analysis for Dependabot alerts'
product: 'Reachability analysis is available for public, private, and internal repositories on GitHub Enterprise Cloud, including enterprises with data residency. A GitHub Code Security license is not required.'
versions:
  feature: dependabot-reachability
contentType: how-tos
category:
  - Secure your dependencies
---

> [!NOTE]
> Reachability analysis for Dependabot alerts is in public preview and subject to change.

Reachability analysis helps prioritize Dependabot alerts by identifying whether your application can reach vulnerable dependency code. See [AUTOTITLE](/code-security/concepts/supply-chain-security/about-reachability-analysis-for-dependabot-alerts).

## Enabling or disabling reachability analysis for your repository

Dependabot alerts must be enabled for reachability analysis to work.

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. To enable reachability analysis, you first need to enable Dependabot alerts. Under "Advanced Security", to the right of Dependabot alerts, toggle the setting to **On**.
1. In the "Dependabot" section, to the right of "Reachability analysis", toggle the setting **On** or **Off**.

## Enabling reachability analysis for your organization or enterprise

You can enable reachability analysis for repositories in your organization or enterprise with a custom security configuration. Security configurations are collections of security settings that you can customize and apply at scale. See:

* [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/create-custom-configuration)
* [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/establish-complete-coverage/create-custom-configuration)

## Next steps

To review alerts and prioritize fixes, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-dependabot-alerts/view-dependabot-alerts).
