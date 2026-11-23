---
title: Unlocking a locked account
intro: Your account's paid features are locked if your payment is past due because of billing problems.
redirect_from:
  - /github/setting-up-and-managing-billing-and-payments-on-github/unlocking-a-locked-account
  - /articles/what-happens-if-my-account-is-locked
  - /articles/if-my-account-is-locked-and-i-upgrade-it-do-i-owe-anything-for-previous-time
  - /articles/if-my-account-is-locked-and-i-upgrade-it-do-i-pay-backcharges
  - /articles/what-happens-if-my-repository-is-locked
  - /articles/unlocking-a-locked-personal-account
  - /articles/unlocking-a-locked-organization-account
  - /articles/unlocking-a-locked-account
  - /github/setting-up-and-managing-billing-and-payments-on-github/managing-your-github-billing-settings/unlocking-a-locked-account
  - /billing/managing-your-github-billing-settings/unlocking-a-locked-account
  - /billing/using-the-billing-platform/unlocking-a-locked-account
  - /billing/using-the-new-billing-platform/unlocking-a-locked-account
  - /billing/managing-your-billing/unlocking-a-locked-account
versions:
  fpt: '*'
  ghec: '*'
shortTitle: Locked account
contentType: how-tos
category:
  - Set up payment
---

You can unlock and access your account by updating your account's payment method and resuming paid status. We do not ask you to pay for the time elapsed in locked mode.

A failed authorization hold when you try to sign up for Copilot or increase a budget can also lock your personal account billing and block GitHub Actions or other free-tier access. This can happen even if you plan to stay on GitHub Free, have removed the payment method, or see no active Copilot plan or balance in the "Billing and licensing" section under your account's settings page.

You can downgrade your user account or organization to GitHub Free to continue with the same advanced features in public repositories. For more information, see [AUTOTITLE](/billing/how-tos/manage-plan-and-licenses/downgrade-plan).

## Unlocking an account's features due to a declined payment

If your account's advanced features are locked due to a declined payment, you'll need to update your billing information to trigger a newly authorized charge.

1. In the upper-right corner of any page on GitHub, click your profile picture.

1. Select the account you want to view and then access the "Billing & Licensing" pages:

   * **Personal accounts**: Click **Settings**, then in the **Access** section of the sidebar, click **(icon: credit-card) Billing & Licensing**.
   * **Organizations**: Click **Your organizations**, then next to the organization, click **Settings**. In the organization sidebar, click **(icon: credit-card) Billing & Licensing**.
   * For **enterprises**, click **Your enterprises**, then click the enterprise name. Click the **(icon: credit-card) Billing & Licensing** tab at the top of the page.

1. From the list of "Billing & licensing" pages, click **Payment information** to display full details of your payment method.

1. To edit or remove your payment method:

   * **Bank card or PayPal**: In "Payment method", click **Edit** to update your payment information or click **Remove** to remove your payment information.
   * **Azure subscription**: Under "Azure subscription", click (icon: pencil) to edit your subscription or (icon: trash) to remove your subscription. See [AUTOTITLE](/billing/how-tos/set-up-payment/connect-azure-sub).

>[!NOTE]
> * You may see an authorization hold on your provided payment method once it's updated or after accruing significant usage of metered services. GitHub initiates the release immediately, but your bank or card issuer may take a few days to make the funds available again. See [AUTOTITLE](/billing/how-tos/troubleshooting/authorization-holds).
> * If you have a paid subscription and remove your payment method, your subscription will automatically cancel on your next renewal date.
> * If you are currently on an active paid trial, you will not be able to remove your payment method.
> * To remove a payment method, you must have a balance of zero, and no billable metered usage in the current month, or the previous month if has yet to be paid.

If the new billing information is approved, we will immediately charge you for the paid product you chose. The account will automatically unlock when a payment has been successfully processed. Payments may take up to 24 hours to process.

## Unlocking an account's features due to a failed authorization hold

When initiating a subscription or trial, we verify the entered payment method using an authorization hold. If the hold is unsuccessful, the chosen subscription or trial will not activate.

If you want to continue with the chosen subscription, update your billing information to trigger a new authorization.

1. In the upper-right corner of any page on GitHub, click your profile picture.

1. Select the account you want to view and then access the "Billing & Licensing" pages:

   * **Personal accounts**: Click **Settings**, then in the **Access** section of the sidebar, click **(icon: credit-card) Billing & Licensing**.
   * **Organizations**: Click **Your organizations**, then next to the organization, click **Settings**. In the organization sidebar, click **(icon: credit-card) Billing & Licensing**.
   * For **enterprises**, click **Your enterprises**, then click the enterprise name. Click the **(icon: credit-card) Billing & Licensing** tab at the top of the page.

1. From the list of "Billing & licensing" pages, click **Payment information** to display full details of your payment method.

1. To edit or remove your payment method:

   * **Bank card or PayPal**: In "Payment method", click **Edit** to update your payment information or click **Remove** to remove your payment information.
   * **Azure subscription**: Under "Azure subscription", click (icon: pencil) to edit your subscription or (icon: trash) to remove your subscription. See [AUTOTITLE](/billing/how-tos/set-up-payment/connect-azure-sub).

>[!NOTE]
> * You may see an authorization hold on your provided payment method once it's updated or after accruing significant usage of metered services. GitHub initiates the release immediately, but your bank or card issuer may take a few days to make the funds available again. See [AUTOTITLE](/billing/how-tos/troubleshooting/authorization-holds).
> * If you have a paid subscription and remove your payment method, your subscription will automatically cancel on your next renewal date.
> * If you are currently on an active paid trial, you will not be able to remove your payment method.
> * To remove a payment method, you must have a balance of zero, and no billable metered usage in the current month, or the previous month if has yet to be paid.

If the new authorization is successful, the account will automatically unlock and you will be able to proceed with the chosen subscription.

If the "Billing and licensing" section under your account's settings page shows no active subscription, balance, or payment issue to resolve, contact {% ifversion fpt or ghec %}us through the [GitHub Support portal](https://support.github.com){% elsif ghes %}your site administrator{% endif %} to request a review of the billing lock.
