---
title: Pricing and enabling GitHub Secret Protection
shortTitle: Protect your secrets
intro: Secure your organization's secrets within your budget by enabling GitHub Secret Protection.
product: Organizations on GitHub Team or GitHub Enterprise
allowTitleToDifferFromFilename: true
contentType: how-tos
docsTeamMetrics:
  - secret-protection
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/choosing-github-secret-protection
  - /code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/protect-your-secrets
category:
  - Secure at scale
---

## Prerequisites

Before you configure GitHub Secret Protection:

* Run the free secret risk assessment to inform your enablement strategy. See [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/configure-specific-tools/assess-your-secret-risk).
* Review best practices for choosing pilot repositories. See [AUTOTITLE](/code-security/concepts/security-at-scale/select-pilot-repositories).

## Configuring GitHub Secret Protection

1. On GitHub, navigate to the main page of the organization.
1. Under your organization name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. In the sidebar, under "Security", click **(icon: key) Assessments**.
1. In the banner display, select the **Get started** (icon: triangle-down) dropdown menu, then click one of following enablement options:
   * **For public repositories for free**: Click to enable for _only_ public repositories in your organization.
   * **For all repositories**: Click to see an estimated cost for GitHub Secret Protection for all repositories in your organization.
     * If you are satisfied with the pricing estimate, to enable secret scanning alerts and push protection across your organization, click **Enable Secret Protection**.
     * Alternatively, click **Configure in settings** to customize which repositories you want to enable Secret Protection for. See [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/create-custom-configuration).

{% ifversion secret-scanning-public-monitoring %}

> [!TIP]
> To extend secret detection beyond repositories your enterprise owns, enterprise owners can enable public monitoring. Public monitoring detects secrets leaked by enterprise members in public repositories across GitHub. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/manage-your-coverage/enabling-public-monitoring-for-your-enterprise).

{% endif %}
