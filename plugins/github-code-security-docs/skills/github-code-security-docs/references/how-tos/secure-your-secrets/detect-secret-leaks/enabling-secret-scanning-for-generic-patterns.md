---
title: Enabling secret scanning for generic patterns
allowTitleToDifferFromFilename: true
intro: You can enable secret scanning to detect additional potential secrets at the repository and organization levels.
permissions: 'Repository owners, organization owners, security managers, and users with the **admin** role'
product: "Scanning for generic patterns is available for the following repository types:\n\n{% ifversion fpt %}\n* Organization-owned repositories on GitHub Team with [GitHub Secret Protection](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{% ifversion ghec %}\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Secret Protection](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{% ifversion ghes %}\n* Organization-owned repositories with [GitHub Secret Protection](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}"
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
contentType: how-tos
shortTitle: Enable for generic patterns
redirect_from:
  - /code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/non-provider-patterns/enabling-secret-scanning-for-non-provider-patterns
  - /code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/non-provider-patterns
  - /code-security/how-tos/secure-your-secrets/detect-secret-leaks/enabling-secret-scanning-for-non-provider-patterns
category:
  - Protect your secrets
---

## Enabling scanning for generic patterns

You can enable scanning for generic patterns. Generic patterns correspond to secrets such as private keys.

For more information about generic patterns, see "{% ifversion fpt or ghec %}[AUTOTITLE](/code-security/reference/secret-security/supported-secret-scanning-patterns#supported-generic-patterns){% else %}[AUTOTITLE](/code-security/reference/secret-security/supported-secret-scanning-patterns#supported-generic-patterns){% endif %}."

### Enabling detection of generic patterns for a repository

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. Under "Secret Protection", to the right of "Generic patterns", click **Enable**.

### Enabling detection of generic patterns for an organization

You can enable scanning for generic patterns at the organization level by applying a custom security configuration. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/create-custom-configuration).
