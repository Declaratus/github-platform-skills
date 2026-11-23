---
title: Enabling push protection for your repository
shortTitle: Enable push protection
intro: With push protection, secret scanning blocks contributors from pushing secrets to a repository and generates an alert whenever a contributor bypasses the block.
permissions: 'Repository owners, organization owners, security managers, and users with the **admin** role'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
contentType: how-tos
redirect_from:
  - /code-security/secret-scanning/enabling-secret-scanning-features/enabling-push-protection-for-your-repository
  - /code-security/how-tos/secure-your-secrets/prevent-future-leaks/enabling-push-protection-for-your-repository
category:
  - Protect your secrets
---

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. If you have not already enabled Secret Protection, to the right of "Secret Protection", click **Enable**.
1. In the "Secret Protection" section, to the right of "Push protection", click **Enable**.

{% ifversion secret-scanning-ai-push-protection %}

## Next steps

* [AUTOTITLE](/code-security/how-tos/secure-your-secrets/prevent-future-leaks/enable-ai-push-protection)

{% endif %}