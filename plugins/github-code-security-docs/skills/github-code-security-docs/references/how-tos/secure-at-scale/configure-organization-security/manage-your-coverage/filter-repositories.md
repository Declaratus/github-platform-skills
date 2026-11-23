---
title: Filtering repositories in your organization using the repository table
shortTitle: Filter repositories
intro: You can filter the repository table for your organization to better manage the security settings of specific repositories.
permissions: 'Organization owners, security managers, and organization members with the **admin** role'
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /code-security/securing-your-organization/managing-the-security-of-your-organization/filtering-repositories-in-your-organization-using-the-repository-table
  - /code-security/how-tos/secure-at-scale/configure-organization-security/manage-your-coverage/filtering-repositories-in-your-organization-using-the-repository-table
contentType: how-tos
category:
  - Secure at scale
---

You can filter the repository table in your organization to quickly find and manage specific repositories when applying security configurations or managing Advanced Security license usage in the organization. This article explains how to use filters in the repository table.

## Filtering the repository table with the search bar

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the "Security" section of the sidebar, select the **(icon: codescan) Advanced Security** dropdown menu, then click **Configurations**.
1. Click the **Repositories** tab.
1. In the "Apply configurations" section, use the **Search repositories** search bar to filter repositories in your organization in one of two ways:
    * Find repositories by name with free-text search
    * Select filters from the dropdown menu that appears once you click the search bar

## Filtering the repository table with the advanced filter builder

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the "Security" section of the sidebar, select the **(icon: codescan) Advanced Security** dropdown menu, then click **Configurations**.
1. Click the **Repositories** tab.
1. To open the advanced filter dialog, in the "Apply configurations" section, click **(icon: filter) Filter**.
1. In the "Advanced filters" window, select the **(icon: plus) Add a filter** dropdown menu, then click a filter.
1. To search for repositories matching the selected filter, fill out the available fields for that filter, then click **Apply**. You can repeat this process to add as many filters as you would like to your search.
1. Optionally, to remove a filter from your search, click **(icon: filter) Filter**. In the row of the filter you want to remove, click (icon: x), then click **Apply**.
