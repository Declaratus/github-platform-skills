---
title: Canceling a GitHub Marketplace app
intro: 'You can cancel and remove a GitHub Marketplace app from your account at any time.'
redirect_from:
  - /github/setting-up-and-managing-billing-and-payments-on-github/canceling-a-github-marketplace-app
  - /articles/canceling-an-app-for-your-personal-account
  - /articles/canceling-an-app-for-your-organization
  - /articles/canceling-a-github-marketplace-app
  - /github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-marketplace-apps/canceling-a-github-marketplace-app
  - /billing/managing-billing-for-github-marketplace-apps/canceling-a-github-marketplace-app
  - /billing/managing-billing-for-your-products/managing-billing-for-github-marketplace-apps/canceling-a-github-marketplace-app
versions:
  fpt: '*'
  ghec: '*'
shortTitle: Cancel Marketplace app
contentType: how-tos
category:
  - Pay third parties and manage client accounts
---

{% ifversion fpt %}>[!IMPORTANT] If you created a personal account (either on a GitHub Free or GitHub Pro plan) after February 13, 2025, these settings are available on the "Marketplace apps" page, which is located under "(icon: credit-card) Billing & Licensing" in the "Access" section of the sidebar.{% endif %}

**When you cancel a paid app, your access and subscription will end on your next billing date. If you cancel during a free trial, you will lose access immediately**. For more information, see [AUTOTITLE](/billing/concepts/third-party-payments/github-marketplace-apps).

Canceling an app or downgrading an app to free does not affect your [other paid subscriptions](/billing/get-started/how-billing-works) on GitHub. If you want to cease all of your paid subscriptions on GitHub, you must downgrade each paid subscription separately.

## Canceling an app for your personal account

1. In the upper-right corner of any page on GitHub, click your profile picture, then click **(icon: gear) Settings**.
1. In the "Access" section of the sidebar, click **(icon: credit-card) Billing and licensing**, then click **Additional billing details**.
1. Under "GitHub Marketplace," next to the app you want to cancel, select the **Edit** (icon: triangle-down) dropdown menu, then click **Cancel plan**.
1. In the dialog box, click **OK**.

## Canceling a free trial for an app for your personal account

1. In the upper-right corner of any page on GitHub, click your profile picture, then click **(icon: gear) Settings**.
1. In the "Access" section of the sidebar, click **(icon: credit-card) Billing and licensing**, then click **Additional billing details**.
1. Under "GitHub Marketplace," next to the free trial you'd like to cancel, use the **Edit** drop-down and click **Cancel plan**.
1. In the dialog box, click **OK**.

## Canceling an app for your organization

> [!TIP]
> If an app requires organization-level access, then only an organization owner can purchase, install, or cancel the app, and manage app billing for the organization. If the app doesn't require organization-level access, then a repository administrator can install and uninstall the app.

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the "Access" section of the sidebar, click **(icon: credit-card) Billing and licensing**.
1. Under "GitHub Marketplace," next to the app you want to cancel, select the **Edit** (icon: triangle-down) dropdown menu, then click **Cancel plan**.
1. In the dialog box, click **OK**.

## Canceling a free trial for an app for your organization

> [!TIP]
> If an app requires organization-level access, then only an organization owner can purchase, install, or cancel the app, and manage app billing for the organization. If the app doesn't require organization-level access, then a repository administrator can install and uninstall the app.

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the "Access" section of the sidebar, click **(icon: credit-card) Billing and licensing**.
1. Under "GitHub Marketplace," next to the free trial you'd like to cancel, use the **Edit** drop-down and click **Cancel plan**.
1. In the dialog box, click **OK**.

## Canceling an app in your enterprise

> [!NOTE]
> To use a GitHub Marketplace app, you must install the app on an organization account within your enterprise. For more information, see [AUTOTITLE](/apps/using-github-apps/installing-a-github-app-from-github-marketplace-for-your-organizations).
>
> You cannot purchase or manage paid GitHub Marketplace apps if your enterprise account is invoiced. Organizations belonging to an enterprise can view and use GitHub Marketplace apps from their billing settings, but you can only purchase or manage apps through your enterprise account. Only enterprise owners who are also organization owners can purchase GitHub Marketplace apps.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: credit-card) Billing and licensing**.
1. In the "Marketplace apps" tab, find the app you want to cancel.
1. Next to the organization where you want to cancel the app, select **(icon: kebab-horizontal)** and then click **Cancel plan**.
1. Click **Confirm**.
