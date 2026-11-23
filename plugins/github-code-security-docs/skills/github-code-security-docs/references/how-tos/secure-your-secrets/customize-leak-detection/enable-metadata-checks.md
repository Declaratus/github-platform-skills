---
title: Enabling extended metadata checks for your repository
shortTitle: Enable metadata checks
intro: Learn how to enable extended metadata checks for detected secrets so alerts detected by secret scanning include additional information that help you assess and remediate leaks faster.
product: "Extended metadata checks are available for the following repository types:\n\n{% ifversion fpt %}\n* Organization-owned repositories on GitHub Team with [GitHub Secret Protection](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{% ifversion ghec %}\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Secret Protection](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{% ifversion ghes %}\n\n* Organization-owned repositories on GitHub Enterprise Server with [GitHub Secret Protection](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}"
permissions: 'Repository owners, organization owners, security managers, and users with the **admin** role'
versions:
  feature: secret-scanning-extended-metadata-checks
contentType: how-tos
redirect_from:
  - /code-security/secret-scanning/enabling-secret-scanning-features/enabling-extended-metadata-checks-for-your-repository
  - /code-security/how-tos/secure-your-secrets/customize-leak-detection/enabling-extended-metadata-checks-for-your-repository
category:
  - Protect your secrets
---

> [!NOTE] Extended metadata checks for tokens is in public preview and subject to change.

This article shows how you can enable extended metadata checks for individual repositories through repository settings. Alternatively, you can enable them at scale using **security configurations** at the organization or enterprise level. See [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/create-custom-configuration) or [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/establish-complete-coverage/create-custom-configuration).

{% ifversion secret-scanning-validity-check-partner-patterns %}

## Prerequisites

Before enabling metadata checks, you need to ensure that validity checks are enabled for the repository. See [AUTOTITLE](/code-security/how-tos/secure-your-secrets/customize-leak-detection/enable-validity-checks#enabling-validity-checks).

{% endif %}

## Enabling extended metadata checks

{% ifversion fpt or ghec %}

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. Under "Secret Protection" and "Validity checks", to the right of "Extended metadata", click **Enable**.

{% elsif ghes %}

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. Under "Secret Protection", to the right of "Validity checks", click **Enable**.
1. Under "Secret Protection", to the right of "Extended metadata", click **Enable**.

{% endif %}

## Further reading

* [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-secret-scanning-alerts)
