---
title: Exempting trusted actors from push protection
intro: Reduce friction for trusted automation by granting exemptions from push protection.
permissions: 'Repository owners, organization owners, security managers, and users with the **admin** role'
versions:
  feature: push-protection-org-enterprise-exemptions
contentType: how-tos
shortTitle: Grant exemptions
category:
  - Protect your secrets
---

{% ifversion push-protection-org-enterprise-exemptions %}
> [!WARNING]
> Push protection exemptions are designed for trusted automation that needs to push many commits with minimal friction. Exemptions may lead to leaked secrets, and should be granted with caution.
{% endif %}

{% ifversion push-protection-repo-exemptions %}

## Granting exemptions for your repository

> [!NOTE]
> If an organization or enterprise owner configures delegated bypass at the organization or enterprise level, the repository-level settings are disabled.

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. Under "Secret Protection," ensure that push protection is enabled for the repository.
1. Under "Push protection," to the right of "Who can bypass push protection for secret scanning," select the dropdown menu, then click **Specific roles or teams**.
1. Under "Bypass list," click **Add role or team**.
1. In the dialog box, select the roles and teams that you want to add to the bypass list, then click **Add selected**.

   > [!NOTE]
   > You can't add secret teams to the bypass list.
{% ifversion push-protection-org-enterprise-exemptions %}
1. To fully exempt the actors from push protection, to the right of the actors' details, select (icon: kebab-horizontal), then click **Exempt**.
{% endif %}

{% endif %}

## Granting exemptions for your organization

1. On GitHub, navigate to the main page of the organization.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the "Security" section of the sidebar, select the **(icon: codescan) Advanced Security** dropdown menu, then click **Configurations**.
1. Create a new custom security configuration, or edit an existing one. See [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/create-custom-configuration).
1. When defining the custom security configuration, under "Secret scanning," ensure that "Push protection" is set to **Enabled**.
1. Under "Push protection," to the right of "Bypass privileges," select the dropdown menu, then click **Specific actors**.
1. Select the (icon: plus) **Select actors** (icon: triangle-down) dropdown menu, then choose the actors you want to add to the bypass list.

   > [!NOTE]
   > * You can't add secret teams to the bypass list.

{% ifversion push-protection-org-enterprise-exemptions %}
1. To fully exempt the actors from push protection, to the right of the actors' details, select (icon: kebab-horizontal), then click **Exempt**.
{% endif %}
1. Click **Save configuration**.
1. Apply the security configuration to repositories in your organization. See [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/apply-custom-configuration).

## Granting exemptions for your enterprise

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. In the left sidebar, click **(icon: codescan) Advanced Security**.
1. In the "Security" section of the sidebar, select the **(icon: codescan) Advanced Security** dropdown menu, then click **Configurations**.
1. Create a new custom security configuration, or edit an existing one. See [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/establish-complete-coverage/create-custom-configuration).
1. Under **Secret scanning**, ensure **Push protection** is enabled.
1. Under "Push protection," to the right of "Bypass privileges," select the dropdown menu, then click **Specific actors**.

   > [!NOTE]
   > You can't add secret teams to the bypass list.

1. Select the (icon: plus) **Select actors** (icon: triangle-down) dropdown menu, then choose the actors you want to add to the bypass list.
{% ifversion push-protection-org-enterprise-exemptions %}
1. To fully exempt the actors from push protection, to the right of the actors' details, select (icon: kebab-horizontal), then click **Exempt**.
{% endif %}
1. Click **Save configuration**.
1. Apply the security configuration to organizations and repositories in your enterprise. See [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/establish-complete-coverage/apply-custom-configuration).
