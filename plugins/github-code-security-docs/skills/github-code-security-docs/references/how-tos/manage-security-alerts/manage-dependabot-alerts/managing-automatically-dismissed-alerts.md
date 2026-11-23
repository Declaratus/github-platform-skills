---
title: Managing alerts that have been automatically dismissed by a Dependabot auto-triage rule
intro: You can filter to see which alerts have been auto-dismissed by a rule, and you can reopen dismissed alerts.
allowTitleToDifferFromFilename: true
permissions: "* Organization owners\n* Security managers\n* Users with **admin** access (can enable, disable, and view auto-triage rules for the repository, as well as create custom auto-triage rules)"
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
contentType: how-tos
shortTitle: Manage auto-dismissed alerts
redirect_from:
  - /code-security/dependabot/dependabot-alert-rules/managing-automatically-dismissed-alerts
  - /code-security/dependabot/dependabot-auto-triage-rules/managing-automatically-dismissed-alerts
category:
  - Secure your dependencies
---

## Managing automatically dismissed alerts

> [!NOTE]
> The Dependabot alerts page defaults to showing open alerts. To filter and view auto-dismissed alerts, you must first clear the `is:open` default filter from the view.

1. On GitHub, navigate to the main page of the repository.
1. Under the repository name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab. If you cannot see the "(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" tab, select the **(icon: kebab-horizontal)** dropdown menu, and then click **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}**.
1. To filter to see all closed alerts, click **(icon: check) Closed**. Alternatively, use the `is:closed` filter query in the search bar.

   ![Screenshot of the "Dependabot Alerts" page. A button, labeled "Closed" is highlighted with an orange outline.](/assets/images/help/repository/dependabot-alerts-closed-tab.png)

1. To see all auto-dismissed alerts, select **Closed as**, then in the dropdown menu, click **Auto-dismissed**.

   ![Screenshot of the "Dependabot Alerts" page. A button, labeled "Closed as" is highlighted with an orange outline.](/assets/images/help/repository/dependabot-alerts-closed-as.png)

1. To reopen an auto-dismissed alert, to the left of the alert title, click the checkbox adjacent to the alert, then click **Reopen**.

   ![Screenshot of an alert title on the "Dependabot Alerts" page. To the left of the alert, a checkbox is highlighted in an orange outline.](/assets/images/help/repository/dependabot-reopen-closed-alert.png)
