---
title: Creating custom roles in an enterprise
intro: Create roles with fine-grained permissions for consistent access to settings and resources.
versions:
  feature: ent-owner-custom-org-roles
shortTitle: Create custom roles
redirect_from:
  - /admin/managing-accounts-and-repositories/managing-organizations-in-your-enterprise/custom-organization-roles
  - /enterprise-onboarding/setting-up-organizations-and-teams/creating-custom-roles
contentType: how-tos
category:
  - Manage accounts and repositories
docsTeamMetrics:
  - enterprise-onboarding
---

To tailor access management to your company's needs, you can create custom roles for your{% ifversion enterprise-custom-roles %} enterprise account and{% endif %} organizations.

Custom roles are sets of permissions for settings and resources that you can assign to users and teams.{% ifversion enterprise-custom-roles %} To learn best practices for using roles on GitHub, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-roles-in-your-enterprise/identify-role-requirements).{% endif %}

{% ifversion enterprise-custom-roles %}

## Creating enterprise custom roles

> [!NOTE] This feature is in public preview and subject to change.

Enterprise custom roles grant access to a subset of enterprise settings, such as viewing audit logs and creating organizations. GitHub plans to expand the list of available permissions over time.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: person) People**.
1. In the left sidebar, click **(icon: globe) Enterprise roles**, then click **Role management**.
1. Click **Create custom role**.
1. Enter the details, then click **Create role**.

{% endif %}

## Creating organization custom roles

Organization custom roles grant access to organization settings and repositories. Custom organization roles created at the enterprise level use the same permissions and base roles as roles created at the organization level. For more information, see [AUTOTITLE](/organizations/managing-peoples-access-to-your-organization-with-roles/permissions-of-custom-organization-roles).

Enterprise owners can create and edit custom organization roles, but cannot assign them. Organization owners can assign custom roles in an organization.

> [!NOTE] An enterprise can create up to 20 custom organization roles. This limit applies to the enterprise: each organization can also create up to 20 custom organization roles.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: person) People**.
1. In the left sidebar, select **Organization roles**.
1. Click **Create custom role**.
1. Enter the details, then click **Create role**.
