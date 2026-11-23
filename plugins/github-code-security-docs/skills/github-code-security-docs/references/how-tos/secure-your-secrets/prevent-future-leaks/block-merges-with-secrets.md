---
title: Blocking pull request merges that contain secrets
shortTitle: Block merges with secrets
intro: Prevent exposed secrets from reaching protected branches by requiring contributors to resolve secret scanning alerts before merging.
permissions: 'Organization owners, security managers, and organization members with the **admin** role{% ifversion enterprise-code-rulesets %}, and enterprise owners{% endif %}'
product: "GitHub Secret Protection is a set of features within GitHub Advanced Security that is available to the following users:\n\n* GitHub Team plan users\n* Enterprise organizations on GitHub Enterprise Cloud and GitHub Enterprise Server"
versions:
  feature: secret-scanning-merge-protection
contentType: how-tos
category:
  - Protect your secrets
redirect_from:
  - /code-security/how-tos/secure-your-secrets/prevent-future-leaks/block-pull-request-merges
---

> [!NOTE]
> The rule to require secret scanning alerts to be resolved before merging is in public preview and subject to change.

The **Require secret scanning alerts are resolved** rule is available for rulesets that target branches in repositories. You can use the rule to block a pull request from merging when either of these conditions applies:

* A secret scanning scan has not completed for the head commit of the pull request.
* A commit in the pull request introduced an open secret scanning alert that matches a secret type selected in the ruleset.

The rule supports provider, custom, and generic patterns. It does not support AI-detected secrets.

## Prerequisites

The repositories that you want to protect must have:

* Either GitHub Secret Protection or GitHub Advanced Security enabled
* Secret scanning enabled. See [AUTOTITLE](/code-security/how-tos/secure-your-secrets/detect-secret-leaks/enable-secret-scanning).

## Creating a merge protection ruleset for a repository

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the left sidebar, under{% ifversion fpt or ghec %} "Code, planning, and automation"{% elsif ghes %} "Code and automation"{% endif %}, click **Rulesets**, then click **Rulesets**.
1. Click **New ruleset**.
1. Click **New branch ruleset**.
1. Under "Ruleset name," type a name for the ruleset.
1. Optionally, to change the default enforcement status, click **(icon: skip) Disabled** (icon: triangle-down) and select an enforcement status.
To target branches or tags, in the "Target branches" or "Target tags" section, select **Add a target**, then select how you want to include or exclude branches or tags. You can use `fnmatch` syntax to include or exclude branches or tags based on a pattern. For more information, see [Using `fnmatch` syntax](/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository#using-fnmatch-syntax).

You can add multiple targeting criteria to the same ruleset. For example, you could include the default branch, include any branches matching the pattern `*feature*`, and then specifically exclude a branch matching the pattern `not-a-feature`.
1. Under "Branch protections", select **Require secret scanning alerts are resolved**.
1. Under "Secret types", select one or more types of secrets that should block merging:
    * **Provider patterns**
    * **Custom patterns**
    * **Generic patterns**
To finish creating your ruleset, click **Create**. If the enforcement status of the ruleset is set to "Active", the ruleset takes effect immediately.

{% ifversion repo-rules-enterprise %}
You can view insights for the ruleset to see how the rules are affecting your contributors. If the enforcement status is set to "Evaluate", you can see which actions would have passed or failed if the ruleset was active. For more information on insights for rulesets, see [AUTOTITLE](/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/managing-rulesets-for-a-repository#viewing-insights-for-rulesets).
{% endif %}

For information about configuring bypass permissions and other ruleset settings, see [AUTOTITLE](/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository).

## Creating a merge protection ruleset for repositories in an organization{% ifversion enterprise-code-rulesets %} or enterprise{% endif %}

{% ifversion enterprise-code-rulesets %}You can create this ruleset for repositories in your organization, or create it for an enterprise to apply merge protection consistently across repositories in multiple organizations.

### Accessing organization ruleset settings{% endif %}

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the sidebar, under "Code, planning, and automation", click **(icon: repo) Repository**, then click **Rulesets**.

{% ifversion enterprise-code-rulesets %}

### Accessing enterprise ruleset settings

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under "Policies", click **Code**.

### Configuring the ruleset{% endif %}

1. Click **New ruleset**.
1. Click **New branch ruleset**.
1. Under "Ruleset name," type a name for the ruleset.
1. Optionally, to change the default enforcement status, click **(icon: skip) Disabled** (icon: triangle-down) and select an enforcement status.
{% ifversion enterprise-code-rulesets %}
1. If you are creating an enterprise-level ruleset, under "Target organizations", choose the organizations that the ruleset will apply to.
{% endif %}
1. Under "Target repositories", choose the repositories that the ruleset will apply to.
To target branches or tags, in the "Target branches" or "Target tags" section, select **Add a target**, then select how you want to include or exclude branches or tags. You can use `fnmatch` syntax to include or exclude branches or tags based on a pattern. For more information, see [Using `fnmatch` syntax](/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository#using-fnmatch-syntax).

You can add multiple targeting criteria to the same ruleset. For example, you could include the default branch, include any branches matching the pattern `*feature*`, and then specifically exclude a branch matching the pattern `not-a-feature`.
1. Under "Branch protections", select **Require secret scanning alerts are resolved**.
1. Under "Secret types", select one or more types of secrets that should block merging:
    * **Provider patterns**
    * **Custom patterns**
    * **Generic patterns**
To finish creating your ruleset, click **Create**. If the enforcement status of the ruleset is set to "Active", the ruleset takes effect immediately.

{% ifversion repo-rules-enterprise %}
You can view insights for the ruleset to see how the rules are affecting your contributors. If the enforcement status is set to "Evaluate", you can see which actions would have passed or failed if the ruleset was active. For more information on insights for rulesets, see [AUTOTITLE](/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/managing-rulesets-for-a-repository#viewing-insights-for-rulesets).
{% endif %}

For information about configuring bypass permissions and other ruleset settings, see [AUTOTITLE](/organizations/managing-organization-settings/creating-rulesets-for-repositories-in-your-organization){% ifversion enterprise-code-rulesets %} and [AUTOTITLE](/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-governance){% endif %}.

## Unblocking a pull request

When this rule blocks a pull request because of open alerts, you must resolve each alert that matches the secret types selected in the ruleset. See [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-secret-scanning-alerts/resolving-alerts).
