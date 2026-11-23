---
title: Enabling secret scanning for your repository
shortTitle: Enable secret scanning
intro: You can configure how GitHub scans your repositories for leaked secrets and generates alerts.
product: "Secret scanning is available for the following repository types:\n\n* **Public repositories**: Secret scanning runs automatically for free.\n* **Organization-owned private and internal repositories**: Available with [GitHub Secret Protection](/get-started/learning-about-github/about-github-advanced-security) enabled on GitHub Team or GitHub Enterprise Cloud.\n* **User-owned repositories**: Available on GitHub Enterprise Cloud with Enterprise Managed Users. Available on GitHub Enterprise Server when the enterprise has [GitHub Secret Protection](/get-started/learning-about-github/about-github-advanced-security) enabled."
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
contentType: how-tos
redirect_from:
  - /code-security/secret-scanning/enabling-secret-scanning-features/enabling-secret-scanning-for-your-repository
  - /code-security/how-tos/secure-your-secrets/detect-secret-leaks/enabling-secret-scanning-for-your-repository
category:
  - Protect your secrets
---

## About enabling {% ifversion fpt or ghec %}secret scanning alerts for users{% else %}secret scanning{% endif %}

{% ifversion fpt %}

{% ifversion fpt or ghec %}Secret scanning alerts for users{% else %}Secret scanning{% endif %} can be enabled on any free public repository that you own.

{% endif %}

{% ifversion fpt or ghec %}Secret scanning alerts for users{% else %}Secret scanning{% endif %} can be enabled for any repository that is owned by an organization{% ifversion secret-scanning-user-owned-repos %}, and for repositories owned by user accounts when using GitHub Enterprise Cloud with Enterprise Managed Users{% endif %}.

If you're an organization owner, you can enable secret scanning for multiple repositories at a time using security configurations. For more information, see [AUTOTITLE](/code-security/concepts/security-at-scale/organization-security).

{% ifversion security-configuration-enterprise-level %}

If your organization is owned by an enterprise account, an enterprise owner can also enable secret scanning at the enterprise level. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/establish-complete-coverage/create-custom-configuration).

{% endif %}

## Enabling {% ifversion fpt or ghec %}secret scanning alerts for users{% else %}secret scanning{% endif %}

{% ifversion fpt or ghec %}Secret scanning alerts for users{% else %}Secret scanning{% endif %} are enabled when you enable Secret Protection for your repository.

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. To the right of "Secret Protection", click **Enable**.
1. Review the impact of enabling Secret Protection, then click **Enable Secret Protection**.

A repository administrator can choose to disable secret scanning for a repository at any time. For more information, see [AUTOTITLE](/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository).

{% ifversion secret-scanning-public-monitoring %}

## Extending detection with public monitoring

The enablement steps above configure secret scanning for repositories your organization or enterprise owns. To detect secrets leaked by your enterprise members in public repositories across GitHub, you can enable public monitoring at the enterprise level. See [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/manage-your-coverage/enabling-public-monitoring-for-your-enterprise).

{% endif %}

## Next steps

* [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-secret-scanning-alerts/viewing-alerts)
* [AUTOTITLE](/code-security/concepts/secret-security/about-alerts)
