---
title: Linking code scanning alerts to GitHub issues
shortTitle: Track alerts in issues
intro: Create or connect GitHub issues to code scanning alerts to track security fixes in your team's workflow.
permissions: People with write access for the repository can link code scanning alerts to issues.
versions:
  feature: code-scanning-link-alert-to-issue
contentType: how-tos
category:
  - Find and fix code vulnerabilities
redirect_from:
  - /code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/linking-code-scanning-alerts-to-github-issues
---

> [!NOTE]
> Code scanning alert tracking using GitHub issues is currently in public preview and subject to change.

{% ifversion ghes %}

> [!NOTE]
> Your site administrator must enable code scanning before you can use this feature. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance).
>
> You may not be able to enable or disable code scanning if an enterprise owner has set a GitHub Code Security policy at the enterprise level. For more information, see [AUTOTITLE](/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise).

{% endif %}

When code scanning identifies a vulnerability, you can link it to a new or existing GitHub issue. This makes security fixes visible in your planning and project boards alongside your team's regular development work. For more information about how alert tracking works, see [AUTOTITLE](/code-security/concepts/code-scanning/alert-tracking-with-issues).

## Creating an issue from an alert

Create a new issue directly from a code scanning alert, pre-populated with vulnerability details.

1. On GitHub, navigate to the main page of the repository.
1. Under the repository name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab. If you cannot see the "(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" tab, select the **(icon: kebab-horizontal)** dropdown menu, and then click **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}**.
1. In the left sidebar, click **(icon: codescan) Code scanning**.
1. Under "Code scanning," click the alert you'd like to explore to display the detailed alert page.
1. On the right of the alert page, click **Tracking**.
1. From the dropdown list, select **Create issue**.
   * Select the repository to create the issue in.
   * If applicable, select the template to use for your new issue.
1. Fill in the issue, providing as much detail as possible.
1. Optionally, assign the issue to a team member, add labels, or add it to a project.
1. Click **Create**.

The newly created issue automatically links to the alert. View it by clicking the issue icon below the alert name.

## Linking an alert to an existing issue

Connect an existing issue to a code scanning alert.

1. On GitHub, navigate to the main page of the repository.
1. Under the repository name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab. If you cannot see the "(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" tab, select the **(icon: kebab-horizontal)** dropdown menu, and then click **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}**.
1. In the left sidebar, click **(icon: codescan) Code scanning**.
1. Under "Code scanning," click the alert you'd like to explore to display the detailed alert page.
1. On the right of the alert page, click **Tracking**.
1. From the dropdown list, select **Add existing GitHub issue**.
1. Search by issue number or title, or select a different repository by clicking the Back icon.
1. Click the issue you want to link.

You can link to issues in different repositories, as long as you have access and GitHub Issues is enabled.

## Viewing linked issues

Once you link an issue to an alert, you can view the linked issue in two places:

* **On the alert detail page**: Click the issue icon below the alert name to navigate to the full issue details.
* **In the list of code scanning alerts**: Linked issues appear alongside their corresponding alerts in the main alerts list view.

## Changing or unlinking a linked issue

1. On GitHub, navigate to the main page of the repository.
1. Under the repository name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab. If you cannot see the "(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" tab, select the **(icon: kebab-horizontal)** dropdown menu, and then click **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}**.
1. In the left sidebar, click **(icon: codescan) Code scanning**.
1. Under "Code scanning," click the alert you'd like to explore to display the detailed alert page.
1. On the right of the alert page, click **Tracking**.
1. Click **Change or remove issue**.

When you unlink an issue from an alert, the link is removed from the alert page and alert list. The issue itself remains unchanged.
