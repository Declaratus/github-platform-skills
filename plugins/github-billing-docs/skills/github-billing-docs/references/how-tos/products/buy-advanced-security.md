---
title: Buying Advanced Security for your organization or enterprise
intro: How to buy licenses for GitHub Advanced Security whether you have usage-based or volume/subscription billing.
permissions: Organization or enterprise owners can sign up for GitHub Secret Protection or GitHub Code Security
product: "{% ifversion fpt or ghec %}\nRequires GitHub Team or GitHub Enterprise\n{% endif %}"
versions:
  fpt: '*'
  ghec: '*'
redirect_from:
  - /billing/managing-billing-for-github-advanced-security/signing-up-for-github-advanced-security
  - /billing/managing-billing-for-your-products/managing-billing-for-github-advanced-security/signing-up-for-github-advanced-security
  - /billing/how-tos/products/add-advanced-security
shortTitle: Buy Advanced Security
contentType: how-tos
category:
  - Manage your plan and licenses
---

## Checking your current plan

You must use a GitHub Team or GitHub Enterprise plan before you can enable GitHub Secret Protection or GitHub Code Security on private repositories.

1. Navigate to your organization or enterprise. For example, from the [Organizations](https://github.com/settings/organizations?ref_product=github&ref_type=engagement&ref_style=text) or [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) pages on GitHub.com.
1. From the list of "Billing & licensing" pages, click **Licensing**.

Your current plan is shown with any options to upgrade to a different plan.

## Metered billing users

If your organization or enterprise uses metered billing, then you are ready to start enabling GitHub Secret Protection and GitHub Code Security. Whenever you enable a feature or apply a configuration, a modal dialog shows detailed information with estimated billing changes. You can confirm your change or return to the page without making changes.

The most effective way to control and enable these features is using security configurations, see [AUTOTITLE](/code-security/concepts/security-at-scale/organization-security).

## Volume/subscription users

If you use volume/subscription billing, then you will need to purchase licenses before you can start using GitHub Secret Protection or GitHub Code Security on private or internal repositories.

1. Navigate to your organization or enterprise. For example, from the [Organizations](https://github.com/settings/organizations?ref_product=github&ref_type=engagement&ref_style=text) or [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) pages on GitHub.com.
1. From the list of "Billing & licensing" pages, click **Licensing**.

1. To the right of "GitHub Advanced Security", click **Buy Advanced Security**.

   ![Screenshot of the Advanced Security section of the licensing screen. The "Buy Advanced Security" button is outlined in orange.](/assets/images/help/enterprises/ghas-buy-advanced-security-button.png)

1. Confirm your billing information and payment method.
1. Under "How many committers do you want to include?", enter the number of committers you want to purchase licenses for.
1. Click **Purchase Advanced Security**.

> [!TIP]
> To see how license use by committers is measured, see [AUTOTITLE](/billing/concepts/product-billing/github-advanced-security).

## Further reading

* [AUTOTITLE](/code-security/tutorials/trialing-github-advanced-security/planning-a-trial-of-ghas)
* [AUTOTITLE](/code-security/concepts/security-at-scale/organization-security){% ifversion ghec %}
* [AUTOTITLE](/code-security/tutorials/adopting-github-advanced-security-at-scale/introduction-to-adopting-github-advanced-security-at-scale){% endif %}
