---
title: Creating an enterprise account
intro: Learn the steps and effects of creating an enterprise account.
versions:
  ghec: '*'
permissions: Organization owners
product: 'GitHub Enterprise Cloud'
shortTitle: Create enterprise account
redirect_from:
  - /admin/overview/creating-an-enterprise-account
contentType: how-tos
category:
  - Get started with GitHub Enterprise
---

<!-- expires 2027-01-30 -->

<!-- When this expires, check with the stakeholder for release #4079 on whether or not the content is still needed. See https://github.com/github/releases/issues/4079#issuecomment-3954280272 for context. If the content is no longer needed, delete this entire article and all links to it. -->

<!-- expires 2027-01-30 -->

<!-- When this expires, check with the stakeholder for release #4079 on whether or not the content is still needed. See https://github.com/github/releases/issues/4079#issuecomment-3954280272 for context. -->

> [!NOTE] Currently, GitHub Enterprise Cloud customers who use a single organization are being automatically upgraded to an enterprise account at no additional cost. For details, see [AUTOTITLE](/admin/managing-your-enterprise-account/creating-an-enterprise-account#what-will-happen-after-i-upgrade-my-organization).

<!-- end expires 2027-01-30 -->

<!-- end expires 2027-01-30 -->

## When should I create an enterprise account?

GitHub Enterprise Cloud allows you to create an enterprise account, which enables collaboration between **multiple organizations** and gives administrators a single point of visibility and management. See [AUTOTITLE](/admin/concepts/enterprise-fundamentals/enterprise-accounts).

In most cases, you can create an enterprise account **yourself**.

* When you start a free trial of GitHub Enterprise Cloud, you'll create an enterprise account as part of the process. See [AUTOTITLE](/admin/overview/setting-up-a-trial-of-github-enterprise-cloud).
* If you currently use GitHub Enterprise Cloud with a single organization, you can upgrade to an enterprise account by following the steps later in this article.

You'll **need help** creating an enterprise account if you require:

* GitHub Enterprise Server
* GitHub Enterprise Cloud with data residency
* Invoicing

In these cases, contact [GitHub's Sales team](https://github.com/enterprise/contact).

> [!NOTE]
> GitHub no longer provisions separate "dedicated" enterprise accounts for managing GitHub Copilot Business licenses without adopting GitHub Enterprise. In any enterprise account, you can assign GitHub Copilot Business licenses directly to members who don't belong to an organization, and those members don't consume a GitHub Enterprise license. See [AUTOTITLE](/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-a-dedicated-enterprise-for-copilot-business).

## What will happen after I upgrade my organization?

The following changes also apply to single organizations that are automatically upgraded to an enterprise account. For details, see [the GitHub Blog](https://github.blog/changelog/2024-06-19-upcoming-automatic-upgrade-to-the-enterprise-account-experience/).

* **Ownership transfer:** Your organization will automatically be owned by the enterprise account. For details, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-organizations-in-your-enterprise/adding-organizations-to-your-enterprise).
* **Ownership roles:** All organization owners will become enterprise owners.
* **Billing details:** The organization’s billing details will now apply to the enterprise account.
* **Billing managers:** All organization billing managers will become enterprise billing managers.
* **Billing process:** GitHub will bill the enterprise account for usage within **all** organizations owned by the enterprise.
* **Enterprise account name:** During the upgrade, the new enterprise account name will match your organization name or be as close as possible if taken. You can rename it after the upgrade.
* **SAML SSO:** Existing SAML SSO will stay at the organization level after being added to the new enterprise account. You can configure SSO at the enterprise level post-upgrade, which will override the organization level. Existing PATs and SAML-authorized tokens will remain unchanged.
* **Policies:** The new enterprise account starts with no policies, so existing organization policies won't be overridden.
* **Spending limits:** Existing organization spending limits transfer to the new enterprise account. Post-upgrade, billing is handled at the enterprise level. To adjust spending limits, at the top of the page, click (icon: credit-card) **Billing & Licensing**.
* **Coupons:** Existing coupons will carry over to the new enterprise account with no interruptions.
* **Workflow permissions:** The new enterprise account will inherit your organization's workflow permissions. If the organization has a permissive setting ("Read and write"), the enterprise account will also default to permissive. Otherwise, it defaults to restrictive ("Read repository contents and packages"). For workflows with the id-token permission, the default changes to read-only due to a February 2023 update. Add an explicit permissions block in these workflows to grant the required permissions.

## Upgrading an organization to an enterprise account

1. In the upper-right corner of any page on GitHub, click your profile picture, then click **(icon: gear) Settings**.
1. In the "Access" section of the sidebar, click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. If you are an organization owner or billing manager, in the "Access" section of the sidebar, click **(icon: credit-card) Billing and licensing**.
1. Click **Upgrade to enterprise account**.
1. Under "Enterprise name", type a name for your enterprise account.
1. Under "Enterprise URL slug", type a slug to be used in the URL for your enterprise.

   For example, if you choose `octo-enterprise`, the URL will be `https://github.com/enterprises/octo-enterprise`.
1. Click **Confirm and upgrade**.
1. Read the warnings, then click **Create enterprise account**.

## Next steps

Set up your new enterprise with our [AUTOTITLE](/enterprise-cloud@latest/admin/enterprise-onboarding) journey for GitHub Enterprise Cloud.

## Further reading

* [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-roles-in-your-enterprise/abilities-of-roles)
