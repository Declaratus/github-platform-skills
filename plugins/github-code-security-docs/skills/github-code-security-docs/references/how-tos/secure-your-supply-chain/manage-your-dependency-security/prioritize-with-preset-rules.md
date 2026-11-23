---
title: Using GitHub preset rules to prioritize Dependabot alerts
intro: Focus on alerts that matter by auto-dismissing low impact development alerts for npm dependencies.
permissions: "* Organization owners\n* Security managers\n* Users with **admin** access (can enable, disable, and view GitHub presets for the repository)"
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
shortTitle: Prioritize with preset rules
redirect_from:
  - /code-security/dependabot/dependabot-alert-rules/using-github-curated-alert-rules-to-prioritize-dependabot-alerts
  - /code-security/dependabot/dependabot-auto-triage-rules/using-github-curated-default-rules-to-prioritize-dependabot-alerts
  - /code-security/dependabot/dependabot-auto-triage-rules/using-github-preset-rules-to-prioritize-dependabot-alerts
  - /code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/using-github-preset-rules-to-prioritize-dependabot-alerts
contentType: how-tos
category:
  - Secure your dependencies
---

## Prerequisites

Before you enable GitHub presets for your repository, you should be familiar with their functionality and purpose. See [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-auto-triage-rules).

## Enabling GitHub preset rules

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. In the "Dependabot" section, to the right of "Dependabot rules", click (icon: gear).

   ![Screenshot of the "Advanced Security" page for a repository. The gear icon is highlighted with an orange outline.](/assets/images/help/repository/dependabot-rules-page.png)

1. In the "GitHub presets" section, to the right of the rule you want to enable, click (icon: pencil).
1. In the "State" section, select the dropdown menu, then click **Enabled**.
1. Click **Save rule**.
