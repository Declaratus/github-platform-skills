---
title: Set code scanning merge protection
shortTitle: Set merge protection
intro: Secure your codebase by blocking pull requests that fail code scanning checks.
permissions: 'Organization owners, security managers, and organization members with the **admin** role'
product: "Code scanning is available for the following repository types:\n\n* Public repositories on GitHub.com\n* Organization-owned repositories on GitHub Team, GitHub Enterprise Cloud, or GitHub Enterprise Server, with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled."
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /code-security/code-scanning/managing-your-code-scanning-configuration/set-code-scanning-merge-protection
  - /code-security/how-tos/scan-code-for-vulnerabilities/manage-your-configuration/set-code-scanning-merge-protection
  - /code-security/how-tos/find-and-fix-code-vulnerabilities/manage-your-configuration/set-code-scanning-merge-protection
contentType: how-tos
category:
  - Find and fix code vulnerabilities
---

## Creating a merge protection ruleset for a repository

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the left sidebar, under{% ifversion fpt or ghec %} "Code, planning, and automation"{% elsif ghes %} "Code and automation"{% endif %}, click **Rulesets**, then click **Rulesets**.
1. Click **New ruleset**.
1. To create a ruleset targeting branches, click **New branch ruleset**.
1. Under "Ruleset name," type a name for the ruleset.
1. Optionally, to change the default enforcement status, click **(icon: skip) Disabled** (icon: triangle-down) and select an enforcement status.
1. Under "Branch protections", select **Require code scanning results**.
1. Under "Required tools and alert thresholds", click **(icon: plus) Add tool** and select a code scanning tool with the dropdown. For example, "CodeQL".
1. Next to the name of a code scanning tool:
    * Click **Alerts** and select one of: **None**, **Errors**, **Errors and Warnings** or **All**.
    * Click **Security alerts** and select one of: **None**, **Critical**, **High or higher**, **Medium or higher**, or **All**.

    ![Screenshot of the "Required tools and alert thresholds" section of "Rulesets" settings.](/assets/images/help/repository/rulesets-require-code-scanning.png)

For more information about alert severity and security severity levels, see [AUTOTITLE](/code-security/concepts/code-scanning/code-scanning-alerts#about-alert-severity-and-security-severity-levels).

For more information about managing rulesets in a repository, see [AUTOTITLE](/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets).

{% ifversion ghec or ghes %}

## Creating a merge protection ruleset for all repositories in an organization

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the sidebar, under "Code, planning, and automation", click **(icon: repo) Repository**, then click **Rulesets**.
1. Click **New ruleset**.
1. To create a ruleset targeting branches, click **New branch ruleset**.
1. Under "Ruleset name," type a name for the ruleset.
1. Optionally, to change the default enforcement status, click **(icon: skip) Disabled** (icon: triangle-down) and select an enforcement status.
1. Under "Branch protections", select **Require code scanning results**.
1. Under "Required tools and alert thresholds", click **(icon: plus) Add tool** and select a code scanning tool with the dropdown. For example, "CodeQL".
1. Next to the name of a code scanning tool:
    * Click **Alerts** and select one of: **None**, **Errors**, **Errors and Warnings** or **All**.
    * Click **Security alerts** and select one of: **None**, **Critical**, **High or higher**, **Medium or higher**, or **All**.

    ![Screenshot of the "Required tools and alert thresholds" section of "Rulesets" settings.](/assets/images/help/repository/rulesets-require-code-scanning.png)

For more information about alert severity and security severity levels, see [AUTOTITLE](/code-security/concepts/code-scanning/code-scanning-alerts#about-alert-severity-and-security-severity-levels).

For more information about managing rulesets for repositories in an organization, see [AUTOTITLE](/organizations/managing-organization-settings/managing-rulesets-for-repositories-in-your-organization).

{% endif %}

## Creating a merge protection ruleset with the REST API

You can use the REST API to create a ruleset with the `code_scanning` rule, which allows you to define specific tools and set alert thresholds. For more information, see [AUTOTITLE](/rest/repos/rules?apiVersion=2022-11-28#create-a-repository-ruleset).
