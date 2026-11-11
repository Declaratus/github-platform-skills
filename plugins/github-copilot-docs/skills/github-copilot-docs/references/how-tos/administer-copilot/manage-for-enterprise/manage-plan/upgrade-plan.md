---
title: Upgrading GitHub Copilot for your enterprise
shortTitle: Upgrade plan
intro: 'Change your organizations'' plans from Copilot Business to Copilot Enterprise.'
permissions: Enterprise owners
product: 'Enterprises with a Copilot Business plan'
versions:
  feature: copilot
redirect_from:
  - /copilot/managing-copilot/managing-copilot-for-your-enterprise/upgrading-copilot-for-your-enterprise
  - /copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-the-copilot-subscription-for-your-enterprise/upgrading-copilot-for-your-enterprise
  - /copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-the-copilot-plan-for-your-enterprise/upgrading-copilot-for-your-enterprise
  - /copilot/how-tos/administer/enterprises/managing-the-copilot-plan-for-your-enterprise/upgrading-copilot-for-your-enterprise
  - /copilot/how-tos/administer/enterprises/managing-the-copilot-plan-for-your-enterprise/upgrade-plan
  - /copilot/how-tos/administer/enterprises/manage-plan/upgrade-plan
  - /copilot/how-tos/administer/manage-for-enterprise/manage-plan/upgrade-plan
contentType: how-tos
category: 
  - Manage Copilot for a team
---

>[!NOTE]
> You must already have a paid Copilot Business plan to upgrade to Copilot Enterprise. Trial plans are not eligible for upgrade.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: credit-card) Billing and licensing**.
1. In the "Billing and licensing" sidebar, click **(icon: law) Licensing**.
1. In the "Copilot" section, click **Manage**.
1. Click the **(icon: organization) Organizations** tab.
1. Locate the organization for which you want to upgrade Copilot.
1. To the right of the organization name, select the **Copilot** dropdown menu, and click **Copilot Enterprise**.

## Next steps

After upgrading to Copilot Enterprise, you can assign Copilot Enterprise or Copilot Business to individual organizations in the enterprise. See [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-access/grant-access).

## Troubleshooting plan migrations

When transitioning between different Copilot plans, you may encounter situations that require support.

### Trial expiration notices

If you see a trial expiration notice but have an active paid subscription, this is a display issue and does not affect your access. If this persists, contact [GitHub Support](https://support.github.com).

### Migrations requiring support assistance

Some migrations cannot be completed through self-service options.

* **Changing between Copilot Business and Copilot Enterprise**: If you need to migrate between these plans within your enterprise and the option isn't available in your "Billing & Licensing" settings, contact [GitHub Support](https://support.github.com) or your account manager for assistance.
* **Non-enterprise to enterprise environment migrations**: When moving from standalone Copilot plans to a GitHub Enterprise environment, contact [GitHub Support](https://support.github.com) or your account manager to coordinate a migration. Attempting to complete this transition without explicit and careful coordination with your account team and support representatives may result in duplicate billing of Copilot seats for the remainder of the billing cycle. See [AUTOTITLE](/copilot/reference/copilot-billing/license-changes#removing-seats-1).

## Further reading

* [AUTOTITLE](/billing/concepts/product-billing/github-copilot-licenses)
