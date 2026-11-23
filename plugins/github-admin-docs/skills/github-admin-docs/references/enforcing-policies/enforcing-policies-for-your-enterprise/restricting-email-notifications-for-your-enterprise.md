---
title: Restricting email notifications for your enterprise
intro: You can prevent your enterprise's information from leaking into personal email accounts by restricting the domains where members can receive email notifications about activity in organizations owned by your enterprise.
product: 'Restriction of email notifications to approved or verified domains is available with GitHub Enterprise Cloud and GitHub Enterprise Server. For more information, see [AUTOTITLE](/get-started/learning-about-github/githubs-plans).'
versions:
  ghec: '*'
  ghes: '*'
permissions: Enterprise owners can restrict email notifications for an enterprise.
redirect_from:
  - /admin/policies/restricting-email-notifications-for-your-enterprise
  - /github/setting-up-and-managing-your-enterprise/restricting-email-notifications-for-your-enterprise-account-to-approved-domains
  - /github/setting-up-and-managing-your-enterprise/restricting-email-notifications-for-your-enterprise-account
  - /github/setting-up-and-managing-your-enterprise/setting-policies-for-organizations-in-your-enterprise-account/restricting-email-notifications-for-your-enterprise-account
  - /admin/policies/enforcing-policies-for-your-enterprise/restricting-email-notifications-for-your-enterprise
shortTitle: Restrict email notifications
contentType: how-tos
category:
  - Secure and govern your enterprise
---

## About email restrictions for your enterprise

When you restrict email notifications, enterprise members can only use an email address in a verified or approved domain to receive email notifications about activity in organizations owned by your enterprise.

> [!NOTE]
> The ability to approve a domain not owned by your organization or enterprise is currently in public preview and subject to change.

The domains can be inherited from the enterprise or configured for the specific organization. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-user-applications-for-your-enterprise/verifying-or-approving-a-domain-for-your-enterprise) and [AUTOTITLE](/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/restricting-email-notifications-for-your-organization).

{% ifversion fpt or ghec %}To continue receiving email notifications after you enable restrictions, members must verify any email addresses within domains that you verify or approve. For more information, see [AUTOTITLE](/account-and-profile/how-tos/email-preferences/verifying-your-email-address).{% endif %}

If email restrictions are enabled for an enterprise, organization owners cannot disable email restrictions for any organization owned by the enterprise. If changes occur that result in an organization having no verified or approved domains, either inherited from an enterprise that owns the organization or for the specific organization, email restrictions will be disabled for the organization.

## Restricting email notifications for your enterprise

Before you can restrict email notifications for your enterprise, you must verify or approve at least one domain for the enterprise. {% ifversion ghec %} For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-user-applications-for-your-enterprise/verifying-or-approving-a-domain-for-your-enterprise).{% endif %}

Users will not be notified when you enable email restrictions. It is your responsibility to inform users that, in the future, they will only receive email notifications related to your enterprise if they've added an email address belonging to a verified or approved domain to their account settings.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. Under "Settings", click **Verified & approved domains**.
1. Under "Notification preferences", select **Restrict email notifications to only approved or verified domains**.
1. Click **Save**.
