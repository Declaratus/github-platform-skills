---
title: Preventing changes to your releases
shortTitle: Prevent release changes
intro: You can enforce immutable releases for a repository or organization to prevent potential vulnerabilities.
versions:
  feature: immutable-releases
redirect_from:
  - /code-security/supply-chain-security/understanding-your-software-supply-chain/preventing-changes-to-your-releases
  - /code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/preventing-changes-to-your-releases
contentType: how-tos
category:
  - Secure your dependencies
---

## Enforcing immutable releases for your repository

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. Scroll down to the "Releases" section, then select **Enable release immutability**. Be aware that immutability will only apply to future releases.

## Enforcing immutable releases for your organization

1. On GitHub, navigate to the main page of the organization.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the sidebar, under "Code, planning, and automation", select the (icon: repo) **Repository** dropdown menu, then click **General**.
1. In the "Releases" section of the page, select the **No policy** (icon: triangle-down) dropdown menu, then click either **All repositories** or **Selected repositories**. Be aware that immutability will only apply to future releases.
1. If you chose **Selected repositories**, to the right of the dropdown menu, click (icon: gear). Select the repositories you want to include, then click **Select repositories**.
