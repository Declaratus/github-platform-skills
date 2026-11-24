---
title: Enabling scanning for AI-detected secrets
shortTitle: Enable AI-detected secrets
intro: You can enable scanning for AI-detected secrets for your repository or organization. Alerts for generic secrets found using AI, such as passwords, are displayed in a separate list on the secret scanning alerts page.
allowTitleToDifferFromFilename: true
permissions: 'Repository owners, organization owners, security managers, and users with the **admin** role'
versions:
  feature: secret-scanning-ai-generic-secret-detection
contentType: how-tos
docsTeamMetrics:
  - secret-protection
redirect_from:
  - /code-security/secret-scanning/enabling-ai-powered-generic-secret-detection
  - /code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/generic-secret-detection/enabling-ai-powered-generic-secret-detection
  - /code-security/secret-scanning/copilot-secret-scanning/enabling-ai-powered-generic-secret-detection
  - /code-security/how-tos/secure-your-secrets/detect-secret-leaks/enabling-ai-powered-generic-secret-detection
category:
  - Protect your secrets
---

## Enabling scanning for AI-detected secrets

{% ifversion ghec %}

To use scanning for AI-detected secrets, an enterprise owner must first set a policy at the enterprise level that controls whether the feature can be enabled and disabled for repositories in an organization. This policy is set to "allowed" by default.

{% endif %}

{% ifversion ghes %}
For GitHub Enterprise Server, a site administrator must first enable AI-detected secrets for the instance so that repository and security-configuration controls are available. If you don't have site administrator access, ask your GitHub Enterprise Server administrator to enable this setting first. See [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configure-secret-scanning#enabling-ai-detected-secrets).

{% endif %}
Enabling scanning for AI-detected secrets queues a historical scan of existing code. Findings appear in the **Generic** alerts list. Disabling AI-detected secrets doesn't disable standard secret scanning.

{% ifversion secret-scanning-ai-generic-secret-detection %}

> [!NOTE]
> You do not need a subscription to GitHub Copilot to use scanning for AI-detected secrets. The feature is available to repositories owned by organizations and enterprises with GitHub Secret Protection enabled.

{% endif %}

### Enabling scanning for AI-detected secrets for your repository

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. Under "Secret Protection", to the right of "Scan for AI-detected secrets", click **Enable**.

### Enabling scanning for AI-detected secrets for your organization

You must configure scanning for AI-detected secrets for your organization using a custom security configuration. You can then apply the security configuration to all (or selected) repositories in your organization.

1. Create a new custom security configuration, or edit an existing one. See [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/create-custom-configuration).
1. When creating the custom security configuration, ensure that "Secret Protection" is set to **Enabled**, and that the dropdown menu for "Scan for AI-detected secrets" is also set to **Enabled**.
1. Apply the custom security configuration to one or more repositories. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/apply-custom-configuration).

For information on how to view alerts for generic secrets that have been detected with AI, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-secret-scanning-alerts/viewing-alerts).

{% ifversion fpt or ghec %}

## Further reading

* [AUTOTITLE](/code-security/responsible-use/security-and-quality-ai-features)

{% endif %}
