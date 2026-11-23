---
title: Enforcing policies for code security and analysis for your enterprise
intro: You can enforce policies to manage the use of code security and analysis features within your enterprise's organizations.
permissions: Enterprise owners
product: "GitHub Code Security and GitHub Secret Protection are available for {% ifversion fpt or ghec %}accounts on GitHub Team and GitHub Enterprise Cloud{% elsif ghes %}accounts on GitHub Enterprise Server{% endif %}.\n\n{% ifversion fpt or ghec %} Some features are also available for free for public repositories on GitHub.com.{% endif %} For more information, see [AUTOTITLE](/get-started/learning-about-github/githubs-plans).\n\nFor information about GitHub Advanced Security for Azure DevOps, see [Configure GitHub Advanced Security for Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features) in Microsoft Learn."
versions:
  ghec: '*'
  ghes: '*'
redirect_from:
  - /admin/policies/enforcing-policies-for-advanced-security-in-your-enterprise
  - /github/setting-up-and-managing-your-enterprise/enforcing-policies-for-advanced-security-in-your-enterprise-account
  - /github/setting-up-and-managing-your-enterprise/setting-policies-for-organizations-in-your-enterprise-account/enforcing-policies-for-advanced-security-in-your-enterprise-account
  - /admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-advanced-security-in-your-enterprise
  - /admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-dependency-insights-in-your-enterprise
  - /articles/enforcing-a-policy-on-dependency-insights
  - /articles/enforcing-a-policy-on-dependency-insights-in-your-enterprise-account
  - /github/setting-up-and-managing-your-enterprise-account/enforcing-a-policy-on-dependency-insights-in-your-enterprise-account
  - /github/setting-up-and-managing-your-enterprise/enforcing-a-policy-on-dependency-insights-in-your-enterprise-account
  - /github/setting-up-and-managing-your-enterprise/setting-policies-for-organizations-in-your-enterprise-account/enforcing-a-policy-on-dependency-insights-in-your-enterprise-account
  - /admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise
shortTitle: Security & analysis
contentType: how-tos
category:
  - Secure and govern your enterprise
---

## About policies for using security features in your enterprise

You can enforce policies to manage the use of security features within organizations owned by your enterprise. You can allow or disallow people with admin access to a repository to enable or disable the security and analysis features.

Additionally, you can enforce policies for the use of GitHub Secret Protection, GitHub Code Security, or GitHub Advanced Security in your enterprise's organizations and repositories.

{% ifversion code-quality %}
Policies for Advanced Security do not control access to GitHub Code Quality. To manage access, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/allow-github-code-quality-in-enterprise).
{% endif %}

## Enforcing a policy for the availability of Advanced Security in your enterprise's organizations

You are billed for GitHub Secret Protection, GitHub Code Security, and GitHub Advanced Security products on a per-committer basis. See [AUTOTITLE](/billing/concepts/product-billing/github-advanced-security#managing-committers-and-costs).

You can enforce a policy that controls whether repository administrators are allowed to enable features for Advanced Security in an organization's repositories. You can configure a policy for all organizations owned by your enterprise account, or for individual organizations that you choose.

Disallowing GitHub Secret Protection, GitHub Code Security, or GitHub Advanced Security for an organization prevents repository administrators from enabling these features for additional repositories, but does not disable the features for repositories where the features are already enabled.

> [!NOTE]
> This policy only impacts repository administrators, specifically. Organization owners and security managers can always enable security features, regardless of how you set this policy. For more information, see [AUTOTITLE](/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization).

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under (icon: law) "Policies", click **Advanced Security**.
1. On the "Policies" tab of the "Advanced Security" page, select the dropdown menu, then click a policy for the organizations owned by your enterprise.
1. Optionally, if you chose **Allow for selected organizations**, to the right of an organization, select the dropdown menu to define which Advanced Security products are available to the organization.

   ![Screenshot of the dropdown menu to choose a Advanced Security policy for selected organizations in the enterprise. The dropdown is outlined.](/assets/images/help/enterprises/select-advanced-security-individual-organization-policy.png)

> [!NOTE]
> If GitHub Actions is not available for an organization, code scanning will be unable to run even if it is made available with this policy.{% ifversion code-quality %} Similarly, GitHub Code Quality will be unable to run even if it is made available with its own policy.{% endif %} See [AUTOTITLE](/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise#policies).

{% ifversion ghec %}

## Enforcing a policy for visibility of dependency insights

Dependency insights show all open source projects that repositories within your enterprise's organizations depend on. Dependency insights include aggregated information about security advisories and licenses. For more information, see [AUTOTITLE](/organizations/collaborating-with-groups-in-organizations/viewing-insights-for-dependencies-in-your-organization).

Across all organizations owned by your enterprise, you can control whether organization members can view dependency insights. You can also allow owners to administer the setting on the organization level. For more information, see [AUTOTITLE](/organizations/managing-organization-settings/changing-the-visibility-of-your-organizations-dependency-insights).

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under (icon: law) "Policies", click **Advanced Security**.
1. In the "Policies" section, under "Dependency insights", review the information about changing the setting.
1. Optionally, to view the current configuration for all organizations in the enterprise account before you change the setting, click **(icon: eye) View your organizations' current configurations**.
   
      ![Screenshot of a policy in the enterprise settings. A link, labeled "View your organizations' current configurations", is outlined.](/assets/images/help/business-accounts/view-current-policy-implementation-link.png)
1. Under "Dependency insights", select the dropdown menu and click a policy.

{% endif %}

{% ifversion security-feature-enablement-policies-dependabot %}

## Enforcing a policy to manage the use of Dependabot alerts in your enterprise

Across all organizations owned by your enterprise, you can allow members with admin permissions for repositories to enable or disable Dependabot alerts and change Dependabot alerts settings.

> [!NOTE]
> This policy only impacts repository administrators, specifically. Organization owners and security managers can always enable security features, regardless of how you set this policy. For more information, see [AUTOTITLE](/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization).

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under (icon: law) "Policies", click **Advanced Security**.
1. In the "Policies" section, under "Enable or disable Dependabot alerts by repository admins", use the dropdown menu to choose a policy.

{% endif %}

## Enforcing a policy to manage the use of Advanced Security features in your enterprise's repositories

Across all of your enterprise's organizations, you can allow or disallow people with admin access to repositories to manage the use of Advanced Security features in the repositories.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under (icon: law) "Policies", click **Advanced Security**.
1. In the "Policies" section, under "Repository administrators can enable or disable `PRODUCT`", use the dropdown menu to define whether repository administrators can change the enablement of GitHub Secret Protection, GitHub Code Security, or GitHub Advanced Security.

<!--This option is included automatically by the "Repository Admins can Enable or Disable Secret Protection" option, which is why this section is omitted for `ghas-products` versions.-->

{% ifversion secret-scanning-ai-generic-secret-detection %}

## Enforcing a policy to manage the use of AI detection for secret scanning in your enterprise's repositories

Across all of your enterprise's organizations, you can allow or disallow people with admin access to repositories to manage and configure AI detection in secret scanning for the repositories. This policy only takes effect if repository administrators are also allowed to change enablement of Secret Protection (controlled by the "Repository administrators can enable or disable Secret Protection" policy).

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under (icon: law) "Policies", click **Advanced Security**.
1. In the "Policies" section, under "AI detection in secret scanning", select the dropdown menu and click a policy.

{% endif %}

{% ifversion secret-scanning-actions-logs %}

## Enforcing a policy for secret scanning in GitHub Actions workflow logs

As an enterprise owner, you can choose whether GitHub scans GitHub Actions workflow logs for secrets. This policy is disabled by default.

When you enable the policy, GitHub scans the logs of new workflow runs in all repositories in your enterprise where secret scanning is enabled.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under (icon: law) "Policies", click **Advanced Security**.
1. Under "Secret scanning for Actions workflow logs", select the **All repositories** dropdown menu, then click **Enabled** or **Disabled**.

{% endif %}

{% ifversion code-scanning-autofix %}

## Enforcing a policy to manage the use of Copilot Autofix in your enterprise's repositories

Across all of your enterprise's organizations, you can allow or disallow people with admin access to repositories to manage where Copilot Autofix is enabled for Code Security results. GitHub Code Security must be enabled for the organization for this policy to take effect.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under (icon: law) "Policies", click **Advanced Security**.
1. In the "Policies" section, under "Copilot Autofix", select the dropdown menu and click a policy.

> [!NOTE]
> This policy controls the use of Copilot Autofix on results found by code scanning security queries only. Copilot Autofix is an integral part of GitHub Code Quality and cannot be disabled for that feature.

{% endif %}

{% ifversion ai-powered-security-detections %}

## Enforcing a policy to manage AI Scan in your enterprise's repositories

As an enterprise owner, you can control whether organizations in your enterprise can enable AI Scan. This policy is set to "Not allowed" by default.

{% ifversion ai-applications-scanning %}
This same policy also controls AI applications scanning; there's no separate enterprise-level policy for that detector.
{% endif %}

Allowing this policy does not enable AI Scan{% ifversion ai-applications-scanning %} or AI applications scanning{% endif %} for any organization. Organization administrators must separately enable {% ifversion ai-applications-scanning %}each detector{% else %}AI Scan{% endif %} for their organization. Eligible repositories where code scanning is enabled inherit the organization setting, and repository administrators can opt out for individual repositories{% ifversion ai-applications-scanning %}, for each detector{% endif %}.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under (icon: law) "Policies", click **Advanced Security**.
1. Under "AI Scan", select the dropdown menu and click a policy.

{% ifversion ai-applications-scanning %}
For information about enabling AI applications scanning at the organization level, see [AUTOTITLE](/code-security/concepts/code-scanning/ai-applications-scanning-for-pull-requests#how-to-enable-ai-applications-scanning).
{% endif %}

{% endif %}
