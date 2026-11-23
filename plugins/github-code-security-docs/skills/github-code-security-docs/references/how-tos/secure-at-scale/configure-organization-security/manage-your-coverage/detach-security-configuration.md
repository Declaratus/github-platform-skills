---
title: Detaching repositories from their security configurations
shortTitle: Detach security configuration
intro: Go back to managing a repository's security settings on an individual basis.
permissions: 'Organization owners, security managers, and organization members with the **admin** role'
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /code-security/securing-your-organization/managing-the-security-of-your-organization/detaching-repositories-from-their-security-configurations
  - /code-security/how-tos/secure-at-scale/configure-organization-security/manage-your-coverage/detaching-repositories-from-their-security-configurations
contentType: how-tos
category:
  - Secure at scale
---

If you decide that the security needs of a repository are too specific for a security configuration to be useful, you can detach that repository from the linked configuration and instead manage security enablement settings at the repository level.

Detaching a repository from a security configuration will not change the existing security enablement settings for that repository.

Alternatively, if you want to apply a security configuration to a repository that's already attached to a different configuration, you can apply the configuration as normal, and you do not need to detach the current configuration. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/apply-custom-configuration).

## Detaching repositories from linked security configurations

Detached repositories show a status of "No configuration" in the repository table on the security configurations settings page. For more information about all configuration statuses, see [AUTOTITLE](/code-security/reference/security-at-scale/configuration-statuses).

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the "Security" section of the sidebar, select the **(icon: codescan) Advanced Security** dropdown menu, then click **Configurations**.
1. Click the **Repositories** tab.
1. Optionally, in the "Apply configurations" section, filter for specific repositories you would like to detach from their configurations. To learn more, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/manage-your-coverage/filter-repositories).
1. In the repository table, select repositories with one of three methods:
     * Select each repository you would like to apply the security configuration to.
     * To select all repositories displayed on the current page of the repository table, select the checkbox associated with "NUMBER repositories".
     * After selecting the current page of repositories, "25 of NUMBER selected", to select _all_ repositories in your organization that match any filters you have applied, click **Select all**.
1. Select the **Apply configuration** (icon: triangle-down) dropdown menu, then click **No configuration**.
1. To finish detaching your repositories from their linked security configurations, in the "No configuration?" window, click **No configuration**.

## Next steps

You can now manage security enablement settings at the repository level. For an introduction, see [AUTOTITLE](/code-security/getting-started/quickstart-for-securing-your-repository).
