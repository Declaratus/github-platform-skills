---
title: Inviting people to manage your enterprise
intro: You can {% ifversion ghec %}invite{% else %}add{% endif %} and remove enterprise owners{% ifversion ghec %} and billing managers{% endif %} for your enterprise account.
permissions: Enterprise owners can {% ifversion ghec %}invite other people to become{% elsif ghes %}add{% endif %} additional enterprise administrators.
redirect_from:
  - /github/setting-up-and-managing-your-enterprise/managing-users-in-your-enterprise/inviting-people-to-manage-your-enterprise
  - /github/setting-up-and-managing-your-enterprise-account/inviting-people-to-manage-your-enterprise-account
  - /articles/inviting-people-to-collaborate-in-your-business-account
  - /articles/inviting-people-to-manage-your-enterprise-account
  - /github/setting-up-and-managing-your-enterprise/inviting-people-to-manage-your-enterprise
  - /admin/user-management/managing-users-in-your-enterprise/inviting-people-to-manage-your-enterprise
versions:
  ghec: '*'
  ghes: '*'
shortTitle: Invite people to manage
contentType: how-tos
category:
  - Manage accounts and repositories
---

## About administrator management

{% ifversion ghec %}If you do not use Enterprise Managed Users, you{% else %}You{% endif %} can add or remove enterprise owners{% ifversion ghec %} and billing managers{% endif %} in your enterprise. For more information about the privileges that come with each enterprise role, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-roles-in-your-enterprise/abilities-of-roles).

{% ifversion ghes %}

If you want to manage enterprise owners and billing managers for an enterprise account on GitHub.com, see [the GitHub Enterprise Cloud documentation](/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/inviting-people-to-manage-your-enterprise).
{% endif %}

{% ifversion ghec %}

If you do use Enterprise Managed Users, enterprise owners and billing managers can only be added or removed through your identity provider. For more information, see [AUTOTITLE](/admin/concepts/identity-and-access-management/enterprise-managed-users).

{% endif %}

## {% ifversion ghec %}Inviting{% elsif ghes %}Adding{% endif %} an enterprise administrator to your enterprise account

{% ifversion ghec %}After you invite someone to join the enterprise account, they must accept the emailed invitation before they can access the enterprise account. Pending invitations will expire after 7 days.{% endif %}

You can see all pending invitations to become an administrator of your enterprise account. For more information, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/viewing-people-in-your-enterprise#viewing-pending-invitations).

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: person) People**.
1. Under "(icon: person) People", click **Administrators**.
1. Above the list of administrators, click {% ifversion ghec %}**Invite admin**{% elsif ghes %}**Add owner**{% endif %}.
1. Type the username, full name, or email address of the person you want to invite to become an enterprise administrator, then select the appropriate person from the results.
{%- ifversion ghec %}
1. Select **Owner** or **Billing Manager**.
1. Click **Send Invitation**.
{%- endif %}
{%- ifversion ghes %}
1. Click **Add**.
{%- endif %}

## Removing an enterprise administrator from your enterprise account

Only enterprise owners can remove other enterprise administrators from the enterprise account.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: person) People**.
1. Under "(icon: person) People", click **Administrators**.{% ifversion ghes %}
1. Next to the username of the person you'd like to remove, select the (icon: kebab-horizontal) dropdown menu, then click **Convert to member**.{% endif %}{% ifversion ghec %}
1. Next to the username of the person you'd like to remove, select the (icon: kebab-horizontal) dropdown menu.

   ![Screenshot of a user in the enterprise administrators list. A dropdown menu, labeled with a kebab icon, is highlighted with an orange outline.](/assets/images/help/business-accounts/administrator-settings.png)

1. Choose one of the following:

   * **Remove from enterprise**: Removes both the administrative role and all organization memberships.
   * **Convert to member**: Removes the administrative role but keeps the user’s organization memberships.
   * **Change role**, and then **Unaffiliated member**: If the user has no organization memberships, removes the administrative role but keeps the user in the enterprise as an unaffiliated member.{% endif %}

1. Read the confirmation message, then confirm.

## Further reading

* [AUTOTITLE](/organizations/managing-membership-in-your-organization)
* [AUTOTITLE](/organizations/managing-peoples-access-to-your-organization-with-roles)
