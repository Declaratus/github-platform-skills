---
title: Editing a custom security configuration
shortTitle: Edit custom configuration
intro: Meet the security needs of your repositories by editing your custom security configuration.
permissions: 'Organization owners, security managers, and organization members with the **admin** role'
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /code-security/securing-your-organization/managing-the-security-of-your-organization/editing-a-custom-security-configuration
  - /code-security/how-tos/secure-at-scale/configure-organization-security/manage-your-coverage/editing-a-custom-security-configuration
contentType: how-tos
category:
  - Secure at scale
---

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the "Security" section of the sidebar, select the **(icon: codescan) Advanced Security** dropdown menu, then click **Configurations**.
1. Under "Security configurations", click the name of the custom security configuration you want to edit.

    > [!NOTE]
    > The default security configuration for an organization is only automatically applied to new repositories created in your organization. If a repository is transferred into your organization, you will still need to apply an appropriate security configuration to the repository manually.

1. Edit the name and description of your custom security configuration as desired.
1. Edit the enablement settings of your custom security configuration as desired.
1. In the "Policy" section, you can modify the configuration's enforcement status. Enforcing a configuration will block repository owners from changing features that are enabled or disabled by the configuration, but features that are not set aren't enforced. Next to "Enforce configuration", select **Enforce** or **Don't enforce** from the dropdown menu.

    > [!NOTE] Some situations can break the enforcement of security configurations. See [AUTOTITLE](/code-security/reference/security-at-scale/configuration-enforcement).

1. To apply your changes, click **Update configuration**.
