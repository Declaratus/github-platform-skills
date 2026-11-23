---
title: Managing your paid use of Advanced Security
shortTitle: Manage paid GHAS use
intro: Control the costs of GitHub Secret Protection and GitHub Code Security in your organization.
allowTitleToDifferFromFilename: true
permissions: 'Organization owners, security managers, and organization members with the **admin** role'
product: "{% ifversion fpt or ghec %}\nRequires GitHub Team or GitHub Enterprise\n{% endif %}"
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /code-security/securing-your-organization/managing-the-security-of-your-organization/managing-your-github-advanced-security-license-usage
contentType: how-tos
category:
  - Secure at scale
---

## Prerequisites

Before you can effectively manage your paid use of Advanced Security, you should understand how Advanced Security is billed. See [AUTOTITLE](/billing/concepts/product-billing/github-advanced-security).

## Understanding your license usage

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the "Security" section of the sidebar, select the **(icon: codescan) Advanced Security** dropdown menu, then click **Configurations**.
1. Click the **Repositories** tab.
1. In the "Apply configurations" section, your current license usage will be displayed. This screenshot shows metered usage. If you have bought a volume/subscription license, then the number of licenses available is also reported.

    ![Screenshot of the "Apply configurations" section. The current license use for the enterprise is outlined in dark orange.](/assets/images/help/security-configurations/current-sp-cs-license-usage.png)

1. Optionally, to find specific repositories in your organization, filter the repository table. To learn more, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/manage-your-coverage/filter-repositories).
<!--This functionality is shown in modal dialogs when you enable a security configuration following the release of separate SKUs for GHAS.-->

{% ifversion ghec %}
> [!TIP]
> For information about buying more volume/subscription licenses, see [AUTOTITLE](/billing/how-tos/products/manage-ghas-licenses).
{% endif %}

## Turning off Secret Protection or Code Security

The simplest way to turn off all Secret Protection or Code Security features for one or more repositories is to create a security configuration where the product is disabled at the top level. You can apply this custom configuration to repositories where you want to turn off paid features.

To keep Code Security disabled, set "Default setup" and "Prevent direct alert dismissals" in the "Code scanning" section to **Disabled**. You can leave "Dependency graph" and "Dependabot alerts" enabled because they are included in all plans.

> [!WARNING]
> Changing "Prevent direct alert dismissals" in the "Code scanning" section to **Not set** automatically switches Code Security to **Enabled**. To avoid unintentionally enabling paid features, organization administrators must keep "Default setup" and "Prevent direct alert dismissals" in this section **Disabled** and recheck the top-level Code Security setting before saving and applying the configuration.

Ensure that you give your custom configuration a very clear name, for example: "No Code Security" or "Secret Protection and Supply chain only" to avoid confusion.

For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/create-custom-configuration) and [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/apply-custom-configuration).

{% ifversion ghec or ghes %}
To prevent future enablement of security features, we recommend you ask your enterprise administrator to set the enterprise account's Advanced Security policies so that:
* Advanced Security is **not available**.
* Repository administrators are **not allowed** to enable or disable Advanced Security features for their repositories.
See [AUTOTITLE](/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise).
{% endif %}
