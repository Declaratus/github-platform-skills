---
title: Changing the "used by" data for a repository
shortTitle: Change "used by" data
intro: Display your repository's dependents for a different package.
permissions: 'Repository administrators'
versions:
  fpt: '*'
  ghec: '*'
contentType: how-tos
category:
  - Secure your dependencies
---

Some repositories have a "Used by" section in the sidebar of the **Code** tab. This section shows the number of public references to a package that were found, and displays the avatars of some of the owners of the dependent projects. For more information, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependency-graph#dependents-and-used-by-data).

If you have admin permissions to a repository that contains multiple packages, you can choose which package the "Used by" section represents.

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. Under "Advanced Security", click the drop-down menu in the "Used by counter" section and choose a package.
