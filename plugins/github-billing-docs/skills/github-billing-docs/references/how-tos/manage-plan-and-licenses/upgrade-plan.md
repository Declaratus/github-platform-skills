---
title: Upgrading your account's plan
intro: 'You can upgrade the plan for a personal account or organization on GitHub at any time.'
redirect_from:
  - /github/setting-up-and-managing-billing-and-payments-on-github/upgrading-your-github-subscription
  - /articles/upgrading-your-personal-account-s-billing-plan
  - /articles/upgrading-your-personal-account
  - /articles/upgrading-your-personal-account-from-free-to-a-paid-account
  - /articles/upgrading-your-personal-account-from-free-to-paid-with-a-credit-card
  - /articles/upgrading-your-personal-account-from-free-to-paid-with-paypal
  - /articles/500-error-while-upgrading
  - /articles/upgrading-your-organization-s-billing-plan
  - /articles/changing-your-organization-billing-plan
  - /articles/upgrading-your-organization-account-from-free-to-paid-with-a-credit-card
  - /articles/upgrading-your-organization-account-from-free-to-paid-with-paypal
  - /articles/upgrading-your-organization-account
  - /articles/switching-from-per-repository-to-per-user-pricing
  - /articles/adding-seats-to-your-organization
  - /articles/upgrading-your-github-billing-plan
  - /articles/upgrading-your-github-subscription
  - /github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-your-github-account/upgrading-your-github-subscription
  - /billing/managing-billing-for-your-github-account/upgrading-your-github-subscription
  - /billing/managing-the-plan-for-your-github-account/upgrading-your-accounts-plan
versions:
  fpt: '*'
  ghec: '*'
shortTitle: Upgrade plan
contentType: how-tos
category:
  - Manage your plan and licenses
---

## Upgrading your personal account's plan

You can upgrade your personal account from GitHub Free to GitHub Pro to get advanced code review tools on private repositories owned by your personal account.

Upgrading your personal account does not affect any organizations you may manage or repositories owned by those organizations. See [AUTOTITLE](/get-started/learning-about-github/githubs-plans).

1. In the upper-right corner of any page on GitHub, click your profile picture, then click **(icon: gear) Settings**.
1. In the left sidebar, click **(icon: credit-card) Billing & Licensing**, then click **Licensing**.
1. Next to "Current plan", click **Upgrade**.
1. Under "Pro" on the "Compare plans" page, click **Upgrade to Pro**.
1. Under "Upgrade summary", choose whether you want to pay monthly or yearly.
1. Optionally, to see your plan's details, click **Show details**.
1. Under "Billing information", complete the form, then click **Save**.
1. Under "Payment method", choose to pay with a credit card or PayPal.
1. Complete the payment information form, then click **Submit**.
1. Review the information about the charge and your billing date, then click **Upgrade my account** or **Upgrade my organization's account**.

## Upgrading your organization's plan

You can upgrade your organization from GitHub Free for an organization to GitHub Team to access advanced collaboration and management tools for teams, or upgrade your organization to GitHub Enterprise Cloud for additional security, compliance, and deployment controls.

Upgrading an organization does not affect your personal account or repositories owned by your personal account. {% ifversion fpt or ghec %}For more information, see [AUTOTITLE](/get-started/learning-about-github/githubs-plans).{% endif %}

Organization owners and billing managers can access or change billing settings for an organization.

1. In the upper-right corner of any page on GitHub, click your profile picture, then click **(icon: gear) Settings**.
1. In the "Access" section of the sidebar, click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. If you are an organization owner or billing manager, in the "Access" section of the sidebar, click **(icon: credit-card) Billing and licensing**.
1. Click **Upgrade to Team** next to "Current plan".
1. Review the features of each plan, then, click either **Upgrade to Team** or **Upgrade to Enterprise**.
1. Under "Upgrade summary", choose whether you want to pay monthly or yearly.
1. Optionally, to see your plan's details, click **Show details**.
1. Under "Payment method", choose to pay with a credit card or PayPal.
1. Complete the payment information form, then click **Submit**.
1. Optionally, if your organization is owned by a business or institution, select **This organization is owned by a business**.
1. If your organization is owned by a business or institution, under "Name of business or institution this organization belongs to", type the name of the business or institution.
1. Review the information about the charge and your billing date, then click **Upgrade my account** or **Upgrade my organization's account**.

### Next steps for organizations using GitHub Enterprise Cloud

As part of your upgrade to GitHub Enterprise Cloud, you set up an enterprise account. An enterprise account allows you to manage multiple organizations. Optionally, you can set up identity and access management for an individual organization or enterprise account. See [AUTOTITLE](/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/enterprise-accounts) and [AUTOTITLE](/enterprise-cloud@latest/admin/concepts/identity-and-access-management/identity-and-access-management-fundamentals#authentication-through-githubcom-with-additional-saml-access-restriction){% ifversion fpt %} in the GitHub Enterprise Cloud documentation.{% else %}.{% endif %}

<!-- expires 2027-01-30 -->

<!-- When this expires, check with the stakeholder for release #4079 on whether or not the content is still needed. See https://github.com/github/releases/issues/4079#issuecomment-3954280272 for context. -->

If you currently use GitHub Enterprise Cloud with a single organization, we encourage you to create an enterprise account. <!-- end expires 2027-01-30 --> See [AUTOTITLE](/enterprise-cloud@latest/admin/managing-your-enterprise-account/creating-an-enterprise-account){% ifversion fpt %} in the GitHub Enterprise Cloud documentation.{% else %}.{% endif %}

>[!NOTE] If the organization has write permissions for GitHub Actions, you must manually set write permissions for the enterprise. For more information, see [AUTOTITLE](/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#managing-github-actions-permissions-for-your-repository). For more information about managing organization-level permissions for GitHub Actions, see [AUTOTITLE](/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#managing-github-actions-permissions-for-your-organization).

## Troubleshooting a 500 error when upgrading

If you receive a 500 error when trying to upgrade your account:
* Try clearing your browser's cache, then resubmit your information.
* Check to make sure you have entered your payment data correctly.

If that doesn't resolve the error, please contact {% ifversion fpt or ghec %}us through the [GitHub Support portal](https://support.github.com){% elsif ghes %}your site administrator{% endif %}.

## Switching your organization from per-repository to per-user pricing

If your organization is using a legacy per-repository billing plan, you can switch to per-user pricing at any time. You will not be able to switch back to repository pricing once you've upgraded to per-user pricing. See [AUTOTITLE](/billing/reference/github-license-users).

1. In the upper-right corner of any page on GitHub, click your profile picture, then click **(icon: gear) Settings**.
1. In the "Access" section of the sidebar, click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. If you are an organization owner or billing manager, in the "Access" section of the sidebar, click **(icon: credit-card) Billing and licensing**.
1. To the right of your plan name, select the **Edit** dropdown menu, then click **Edit plan**.
1. To the right of "Advanced tools for teams", click **Upgrade now**.
1. Review the features of each plan, then, click either **Upgrade to Team** or **Upgrade to Enterprise**.
1. Under "Upgrade summary", choose whether you want to pay monthly or yearly.
1. Optionally, if your organization is owned by a business or institution, select **This organization is owned by a business**.
1. If your organization is owned by a business or institution, under "Name of business or institution this organization belongs to", type the name of the business or institution.
1. Review the information about the charge and your billing date, then click **Upgrade my account** or **Upgrade my organization's account**.

## Further reading

* [AUTOTITLE](/billing/how-tos/manage-plan-and-licenses/manage-user-licenses)
* [AUTOTITLE](/get-started/learning-about-github/githubs-plans)
* [AUTOTITLE](/billing/concepts/impact-of-plan-changes)
* [AUTOTITLE](/billing/get-started/how-billing-works)
