---
title: Downgrading your account's plan
intro: 'You can downgrade the plan for any type of account on GitHub at any time.'
redirect_from:
  - /github/setting-up-and-managing-billing-and-payments-on-github/downgrading-your-github-subscription
  - /articles/downgrading-your-personal-account-s-billing-plan
  - /articles/how-do-i-cancel-my-account
  - /articles/downgrading-a-user-account-to-free
  - /articles/removing-paid-seats-from-your-organization
  - /articles/downgrading-your-organization-s-paid-seats
  - /articles/downgrading-your-organization-s-billing-plan
  - /articles/downgrading-an-organization-with-per-seat-pricing-to-free
  - /articles/downgrading-an-organization-with-per-repository-pricing-to-free
  - /articles/downgrading-your-organization-to-free
  - /articles/downgrading-your-organization-from-the-business-plan-to-the-team-plan
  - /articles/downgrading-your-organization-from-github-business-cloud-to-the-team-plan
  - /articles/downgrading-your-github-billing-plan
  - /articles/downgrading-your-github-subscription
  - /github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-your-github-account/downgrading-your-github-subscription
  - /billing/managing-billing-for-your-github-account/downgrading-your-github-subscription
  - /billing/managing-the-plan-for-your-github-account/downgrading-your-accounts-plan
versions:
  fpt: '*'
  ghec: '*'
shortTitle: Downgrade plan
contentType: how-tos
category:
  - Manage your plan and licenses
---

## Downgrading your personal account's plan

If you downgrade your personal account from GitHub Pro to GitHub Free, the account will lose access to advanced code review tools on private repositories. See [AUTOTITLE](/get-started/learning-about-github/githubs-plans).

1. In the upper-right corner of any page on GitHub, click your profile picture, then click **(icon: gear) Settings**.
1. In the "Access" section of the sidebar, click **(icon: credit-card) Billing and licensing**, then click **Additional billing details**.
1. Under "Current plan", use the **Edit** drop-down and click **Downgrade to Free**.
   ![Screenshot of the "Current plan" section of the billing settings page. The "Edit" dropdown menu is expanded and highlighted with an orange outline.](/assets/images/help/billing/downgrade-to-free.png)
1. Read the information about the features your personal account will no longer have access to on your next billing date, then click **I understand. Continue with downgrade**.

If you published a GitHub Pages site in a private repository and added a custom domain, remove or update your DNS records before downgrading from GitHub Pro to GitHub Free, to avoid the risk of a domain takeover. For more information, see [AUTOTITLE](/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

## Downgrading your organization's plan

Organization owners and billing managers can access or change billing settings for an organization.

After an organization's plan is downgraded, the organization will lose access to any functionality that is not included in the new plan. If an advanced feature, such as GitHub Pages, is not available for private repositories in your new plan, consider whether you'd like to retain access to the feature by making affected repositories public. For more information, see [AUTOTITLE](/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility).

Downgrading from GitHub Enterprise Cloud disables any SAML settings. If you later purchase GitHub Enterprise, you will need to reconfigure SAML.

> [!NOTE]
> If your organization is owned by an enterprise account, billing cannot be managed at the organization level. To downgrade, you must remove the organization from the enterprise account first. For more information, see [AUTOTITLE](/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-organizations-in-your-enterprise/removing-organizations-from-your-enterprise).

1. In the upper-right corner of any page on GitHub, click your profile picture, then click **(icon: gear) Settings**.
1. In the "Access" section of the sidebar, click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. If you are an organization owner or billing manager, in the "Access" section of the sidebar, click **(icon: credit-card) Billing and licensing**.
1. Under "Current plan", use the **Edit** drop-down and click the downgrade option you want.
   ![Screenshot of the "Current plan" section of the billing settings page. The "Edit" dropdown menu is expanded and highlighted with an orange outline.](/assets/images/help/billing/downgrade-to-free.png)
1. Read the information about the features your organization will no longer have access to on your next billing date, then click **I understand. Downgrade my organization**.

## Downgrading an organization's plan with legacy per-repository pricing

Organization owners and billing managers can access or change billing settings for an organization.

If your organization is using a legacy per-repository billing plan, you can switch to per-user pricing at any time. You will not be able to switch back to repository pricing once you've upgraded to per-user pricing. For more information, see [AUTOTITLE](/billing/how-tos/manage-plan-and-licenses/upgrade-plan#switching-your-organization-from-per-repository-to-per-user-pricing).

1. In the upper-right corner of any page on GitHub, click your profile picture, then click **(icon: gear) Settings**.
1. In the "Access" section of the sidebar, click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. If you are an organization owner or billing manager, in the "Access" section of the sidebar, click **(icon: credit-card) Billing and licensing**.
5. Under "Subscriptions", next to your current plan, select the **Edit** dropdown menu and click **Edit plan**.
1. Under "Billing/Plans", next to the plan you want to change, click **Downgrade**.
1. Enter the reason you're downgrading your account, then click **Downgrade plan**.

## Downgrading your enterprise account's plan

Enterprise accounts are only available with GitHub Enterprise, so it's not possible to downgrade an enterprise account to another plan.

If you want to stop paying for GitHub Enterprise altogether and your company pays via invoice, contact [GitHub's Sales team](https://github.com/enterprise/contact).

If you have a self-serve enterprise account, an enterprise account owner can:

1. Remove or delete all organizations from the enterprise. Removing an organization from an enterprise automatically downgrades the organization to GitHub Free. See [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-organizations-in-your-enterprise/removing-organizations-from-your-enterprise).
1. Review and remove any remaining unaffiliated members from the enterprise. Depending on your policy settings, members who don't belong to any organizations may remain in your enterprise as unaffiliated members. To fully close the account, remove these unaffiliated members.
1. Delete the enterprise account to cancel the GitHub Enterprise subscription. See [AUTOTITLE](/admin/managing-your-enterprise-account/deleting-an-enterprise-account).

## Further reading

* [AUTOTITLE](/billing/how-tos/manage-plan-and-licenses/manage-user-licenses)
* [AUTOTITLE](/get-started/learning-about-github/githubs-plans)
* [AUTOTITLE](/billing/concepts/impact-of-plan-changes)
* [AUTOTITLE](/billing/get-started/how-billing-works).
* [AUTOTITLE](/billing/reference/github-license-users)
