---
title: Enabling delegated bypass for push protection
intro: Control who can push code containing secrets by requiring bypass approval from designated reviewers.
permissions: 'Repository owners, organization owners, security managers, and users with the **admin** role'
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
contentType: how-tos
shortTitle: Enable delegated bypass
redirect_from:
  - /code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/enabling-delegated-bypass-for-push-protection
  - /code-security/how-tos/secure-your-secrets/manage-bypass-requests/enabling-delegated-bypass-for-push-protection
category:
  - Protect your secrets
---

Delegated bypass for push protection lets you define who can push commits containing secrets and adds an approval process for other contributors. See [AUTOTITLE](/code-security/concepts/secret-security/delegated-bypass).

To enable delegated bypass, create the teams or roles that will manage bypass requests. Alternatively, use fine-grained permissions for more granular control. See [Using fine-grained permissions to control who can review and manage bypass requests](#using-fine-grained-permissions-to-control-who-can-review-and-manage-bypass-requests).

## Enabling delegated bypass for a repository

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
   > You can't add secret teams to the bypass list.{% ifversion push-protection-repo-exemptions %}
{% ifversion push-protection-org-enterprise-exemptions %}
1. Optionally, to fully exempt the actors from push protection, to the right of the actors' details, select (icon: kebab-horizontal), then click **Exempt**.
{% endif %}
    {% ifversion push-protection-org-enterprise-exemptions %}
    > [!WARNING]
    > Push protection exemptions are designed for trusted automation that needs to push many commits with minimal friction. Exemptions may lead to leaked secrets, and should be granted with caution.
    {% endif %}

{% endif %}

## Enabling delegated bypass for an organization

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
   > * In addition to assigning bypass privileges to roles and teams, you can also grant _individual_ organization members the ability to review and manage bypass requests using fine-grained permissions. See [Using fine-grained permissions to control who can review and manage bypass requests](#using-fine-grained-permissions-to-control-who-can-review-and-manage-bypass-requests).

{% ifversion push-protection-org-enterprise-exemptions %}
1. Optionally, to fully exempt the actors from push protection, to the right of the actors' details, select (icon: kebab-horizontal), then click **Exempt**.
{% endif %}
    {% ifversion push-protection-org-enterprise-exemptions %}
    > [!WARNING]
    > Push protection exemptions are designed for trusted automation that needs to push many commits with minimal friction. Exemptions may lead to leaked secrets, and should be granted with caution.
    {% endif %}
1. Click **Save configuration**.
1. Apply the security configuration to repositories in your organization. See [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/apply-custom-configuration).

{% ifversion push-protection-delegated-bypass-configurations-enterprise %}

## Enabling delegated bypass for an enterprise

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
1. Optionally, to fully exempt the actors from push protection, to the right of the actors' details, select (icon: kebab-horizontal), then click **Exempt**.
{% endif %}
    {% ifversion push-protection-org-enterprise-exemptions %}
    > [!WARNING]
    > Push protection exemptions are designed for trusted automation that needs to push many commits with minimal friction. Exemptions may lead to leaked secrets, and should be granted with caution.
    {% endif %}
1. Click **Save configuration**.
1. Apply the security configuration to organizations and repositories in your enterprise. See [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/establish-complete-coverage/apply-custom-configuration).
{% endif %}

## Using fine-grained permissions to control who can review and manage bypass requests

You can grant specific individuals or teams in your organization the ability to review and manage bypass requests using fine-grained permissions.

1. Ensure that delegated bypass is enabled for the organization. For more information, follow steps 1-3 in [Enabling delegated bypass for your organization](/code-security/how-tos/secure-your-secrets/manage-bypass-requests/enable-delegated-bypass#enabling-delegated-bypass-for-an-organization) and ensure you have saved and applied the security configuration to your selected repositories.
1. Create (or edit) a custom organization role. For information on creating and editing custom roles, see [AUTOTITLE](/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-organization-roles#creating-a-custom-role).
1. When choosing which permissions to add to the custom role, select the "Review and manage secret scanning bypass requests" permission.
1. Assign the custom role to individual members or teams in your organization. For more information on assigning custom roles, see [AUTOTITLE](/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles#assigning-an-organization-role).
