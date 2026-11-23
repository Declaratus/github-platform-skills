---
title: Deleting a custom security configuration
shortTitle: Delete custom configuration
intro: You can delete unnecessary custom security configurations in your organization.
permissions: 'Organization owners, security managers, and organization members with the **admin** role'
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /code-security/securing-your-organization/managing-the-security-of-your-organization/deleting-a-custom-security-configuration
  - /code-security/how-tos/secure-at-scale/configure-organization-security/manage-your-coverage/deleting-a-custom-security-configuration
contentType: how-tos
category:
  - Secure at scale
---

## About deleting a custom security configuration

If you no longer need a custom security configuration, you can delete that configuration to ensure it will not be applied to any repositories in the future. If you are deleting a custom security configuration because you want to change the security enablement settings in that configuration, you can instead edit the configuration. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/manage-your-coverage/edit-custom-configuration).

> [!WARNING]
> Deleting a custom security configuration will detach all repositories that are linked to that configuration. The existing security settings for those repositories will be unchanged, but you must apply a different security configuration or manage their security settings at the repository level to keep their settings up to date.

## Deleting a custom security configuration from your organization

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the "Security" section of the sidebar, select the **(icon: codescan) Advanced Security** dropdown menu, then click **Configurations**.
1. In the configurations table, click the name of the custom security configuration you want to delete.
1. Scroll to the bottom of the page, then click **Delete configuration**.
1. In the "Delete this configuration?" window, read the warning to confirm you are comfortable deleting the custom security configuration, then click **Delete configuration**.
