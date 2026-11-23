---
title: Enabling validity checks for your repository
shortTitle: Enable validity checks
intro: Enabling validity checks on your repository helps you prioritize the remediation of alerts as it tells you if a secret is active or inactive.
product: "Validity checks for partner patterns are available for the following repository types:\n\n{% ifversion fpt %}\n* Organization-owned repositories on GitHub Team with [GitHub Secret Protection](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{% ifversion ghec %}\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Secret Protection](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{% ifversion ghes > 3.19 %}\n* Organization-owned repositories on GitHub Enterprise Server with [GitHub Secret Protection](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}"
versions:
  feature: secret-scanning-validity-check-partner-patterns
contentType: how-tos
redirect_from:
  - /code-security/secret-scanning/enabling-secret-scanning-features/enabling-validity-checks-for-your-repository
  - /code-security/how-tos/secure-your-secrets/customize-leak-detection/enabling-validity-checks-for-your-repository
category:
  - Protect your secrets
---

You can enable validity checks for individual repositories through repository settings. Validity checks verify whether detected secrets are still active, helping you prioritize remediation efforts. For information about what validity checks are and how they work, see [AUTOTITLE](/code-security/concepts/secret-security/validity-checks).

For a list of which secret patterns support validity checks, see [AUTOTITLE](/code-security/reference/secret-security/supported-secret-scanning-patterns).

{% ifversion ghes %}

Before you can enable validity checks for your repository, your site administrator must enable the feature for the whole instance. See [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configure-secret-scanning).

{% endif %}

## Enabling validity checks

To enable validity checks from the UI:

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. Under "Secret Protection", to the right of "Validity checks", click **Enable**.
1. Scroll to the bottom of the page and click **Save changes**.

> [!NOTE]
> You can also use the REST API to enable validity checks for partner patterns for your repository. For more information, see [AUTOTITLE](/rest/repos/repos#update-a-repository).

Alternatively, organization owners and enterprise administrators can enable the feature for all repositories in the organization or enterprise. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/create-custom-configuration) and [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/establish-complete-coverage/create-custom-configuration).

## Further reading

* [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-secret-scanning-alerts)
