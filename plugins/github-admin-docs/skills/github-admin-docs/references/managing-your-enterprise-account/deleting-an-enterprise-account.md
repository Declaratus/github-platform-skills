---
title: Deleting an enterprise account
intro: You can delete an enterprise account to stop paying for GitHub Enterprise.
versions:
  ghec: '*'
permissions: Enterprise owners can delete an enterprise account if the company pays by credit card or PayPal.
shortTitle: Delete enterprise account
redirect_from:
  - /admin/overview/deleting-an-enterprise-account
contentType: how-tos
category:
  - Get started with GitHub Enterprise
---

## Prerequisites

Before you can delete an enterprise account, you must remove, transfer, or delete all organizations in the enterprise. For more information, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-organizations-in-your-enterprise/adding-organizations-to-your-enterprise#transferring-an-existing-organization) and [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-organizations-in-your-enterprise/removing-organizations-from-your-enterprise).

After removing organizations, check the "People" tab in your enterprise settings and remove any unaffiliated members who remain in the enterprise. Unaffiliated members are users who are not part of any organization within the enterprise.

You cannot delete an enterprise account if any of the following apply:

* The enterprise account is paid via invoice.
* The enterprise account is currently in a trial period.

If either of these apply to your enterprise account, you can contact [GitHub's Sales team](https://github.com/enterprise/contact) to discuss deleting the account.

## What happens when I delete the account?

Deleting your enterprise account cancels the enterprise license and removes the enterprise account from GitHub.

If there are any outstanding balances on your account, you will be charged a one-time payment when you initiate the deletion process. If you delete your enterprise account partway through a billing cycle, contact {% ifversion fpt or ghec %}us through the [GitHub Support portal](https://support.github.com){% elsif ghes %}your site administrator{% endif %} to request a prorated refund for the remainder of the billing cycle.

When you delete your enterprise account, you lose the policies, billing settings, and user roles you've configured. You do not lose data like repositories or packages, unless you choose to delete the organizations that contain that data.

If you upgraded to an enterprise account from a single organization and then delete that enterprise account, the associated billing history will also be deleted. We recommend that you save any important billing information before deleting your enterprise account.

## Deleting an enterprise account on GitHub

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. If you are not trialing GitHub Enterprise Cloud, delete your enterprise account:
   1. Under **(icon: gear) Settings**, click **General**.
   1. In the "Danger Zone" section, click **Delete this enterprise**.
   1. In the text box, type the enterprise slug to confirm the deletion, then click **Delete this enterprise**.
1. If you are trialing GitHub Enterprise Cloud, cancel your trial, or delete the expired trial:
   1. At the top of the page, click **(icon: credit-card) Billing and licensing**.
   1. At the top of the page, click **Cancel trial** if your trial is active, or click **Delete trial** if your trial is expired.
   1. Follow the prompts.

If you want to restore an enterprise account that you have deleted, you must contact {% ifversion fpt or ghec %}us through the [GitHub Support portal](https://support.github.com){% elsif ghes %}your site administrator{% endif %}.
