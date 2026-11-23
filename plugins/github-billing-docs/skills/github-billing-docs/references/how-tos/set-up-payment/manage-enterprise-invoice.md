---
title: Managing invoices for your enterprise
shortTitle: Manage enterprise invoice
intro: 'You can view, pay, or download a current invoice for your enterprise, and you can view your payment history.'
redirect_from:
  - /billing/managing-billing-for-your-github-account/managing-invoices-for-your-enterprise
  - /billing/managing-the-plan-for-your-github-account/managing-invoices-for-your-enterprise
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
product: "Enterprise owners and billing managers of invoiced customers of GitHub Enterprise.\n\n* Customers who pay directly via credit card, PayPal, or Azure subscription, should instead see {% ifversion fpt or ghec %}[AUTOTITLE](/billing/how-tos/set-up-payment/manage-payment-info){% elsif ghes %}[AUTOTITLE](/enterprise-cloud@latest/billing/how-tos/set-up-payment/manage-payment-info) in the GitHub Enterprise Cloud docs{% endif %}\n* GitHub Enterprise Server customers with no enterprise account on GitHub.com should go to the [GitHub Enterprise website](https://enterprise.github.com/login)"
contentType: how-tos
category:
  - Set up payment
---

GitHub bills invoiced GitHub Enterprise customers through an enterprise account on GitHub.com. Each invoice includes a single bill charge for all of your paid GitHub.com services and any GitHub Enterprise Server instances. For more information, see [AUTOTITLE](/billing/concepts/enterprise-billing/billing-for-enterprises).

## Viewing your current invoice

1. Navigate to GitHub Enterprise Cloud.
1. In the top-right corner of GitHub, click your profile picture.
1. Depending on your environment, click **Enterprise**, or click **Enterprises** then click the enterprise you want to view.
1. At the top of the page, click **(icon: credit-card) Billing and licensing**.
1. On the "Overview" page, in the "Latest invoice" section, click **View invoice** to open a PDF of your latest invoice.

   ![Screenshot of the Billing and licensing "Overview" page for an invoiced enterprise account. A link, labeled "View invoice", is outlined in orange.](/assets/images/help/business-accounts/view-invoice-link.png)

   > [!TIP]
   > If all your invoices are paid, the "Latest invoice" section is labeled "Estimated next payment". To view paid invoices, in the sidebar, click **Past invoices**.

To understand the components of your invoice, see [AUTOTITLE](/billing/how-tos/manage-plan-and-licenses/view-enterprise-usage) and [AUTOTITLE](/billing/how-tos/products/view-productlicense-use).

## Paying your current invoice

1. On the "Overview" page, in the "Latest invoice" section, click **Pay now** to display a secure payment dialog.

   ![Screenshot of the Billing and licensing "Overview" page for an invoiced enterprise account. A button, labeled "Pay now", is outlined in orange.](/assets/images/help/business-accounts/pay-invoice-button.png)

1. Type your credit card information in the secure form, then click **Pay invoice** to pay the amount due.

## Viewing your payment history and downloading any invoice

1. In the sidebar of the Billing and licensing tab, click (icon: file) **Past invoices** to show details of your past invoices.
1. In the "REFERENCE" column, click the reference number of an invoice that you want to download.

   ![Screenshot of the Billing and licensing "Past invoices" page for an invoiced enterprise account. Two invoice references are outlined in orange.](/assets/images/help/business-accounts/download-invoice.png)
