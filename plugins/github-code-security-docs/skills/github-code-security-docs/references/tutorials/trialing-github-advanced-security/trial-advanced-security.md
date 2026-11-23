---
title: Setting up a trial of GitHub Advanced Security
intro: Evaluate GitHub Code Security and GitHub Secret Protection on your existing repositories before you buy.
permissions: '{% ifversion fpt %}Owners of eligible organizations on GitHub Team{% else %}Enterprise owners <br> Otherwise, you need a trial of GitHub Enterprise Cloud with GitHub Advanced Security. See [AUTOTITLE](/enterprise-cloud@latest/admin/overview/setting-up-a-trial-of-github-enterprise-cloud) in the GitHub Enterprise Cloud documentation{% endif %}'
product: '{% ifversion fpt %}Eligible organizations on GitHub Team can start a self-serve trial of GitHub Advanced Security.{% else %}GitHub Advanced Security is available for accounts on GitHub Enterprise Cloud and GitHub Enterprise Server.{% endif %}'
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /billing/managing-billing-for-github-advanced-security/setting-up-a-trial-of-github-advanced-security
  - /billing/managing-billing-for-your-products/managing-billing-for-github-advanced-security/setting-up-a-trial-of-github-advanced-security
  - /billing/how-tos/products/trial-advanced-security
  - /code-security/trialing-github-advanced-security/trial-advanced-security
shortTitle: Trial Advanced Security
contentType: tutorials
category:
  - Plan your security strategy
---

## Prerequisites

{% ifversion fpt %}

To start a self-serve trial for an organization on GitHub Team, all of the following must be true:

* You are an owner of the organization.
* The organization does not currently have, and has not previously had, a paid license for GitHub Advanced Security.
* The organization is not already using metered billing for GitHub Advanced Security.
* If the organization has previously had a GitHub Advanced Security trial, it has had no more than one previous trial. That trial ended at least 180 days ago.

Your payment method does not affect whether you can start a trial. However, you can purchase GitHub Advanced Security through the trial checkout flow only if your organization pays by credit card, PayPal, or Azure.

{% else %}

To set up a trial of GitHub Advanced Security using this method, you must meet the following criteria:

* You are an owner of an enterprise account. See [AUTOTITLE](/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/enterprise-accounts).
* You are not already using metered billing for GitHub Advanced Security.
* If you have had a previous GitHub Advanced Security trial, you have had no more than one previous trial. That trial ended at least 180 days ago.

> [!TIP]
> **No enterprise account?** Start a trial of GitHub Enterprise Cloud with GitHub Advanced Security. See [AUTOTITLE](/enterprise-cloud@latest/admin/overview/setting-up-a-trial-of-github-enterprise-cloud).

{% endif %}

## What the trial includes

The trial gives you access to GitHub Code Security and GitHub Secret Protection for private repositories. You can evaluate capabilities such as:

* Code scanning, Copilot Autofix, dependency review, and security campaigns
* Secret scanning, push protection, custom patterns, validity checks, and delegated bypass

Use the trial on a sample of repositories so you can assess the results, developer experience, and controls before you purchase.

## Start your trial

{% ifversion fpt %}

An organization owner can start a trial from the organization's "Licensing" page.

1. In the upper-right corner of GitHub, click your profile picture, then click **Your organizations**.
1. Next to the organization, click **Settings**.
1. In the "Access" section of the sidebar, click **(icon: credit-card) Billing & Licensing**, then click **Licensing**.
1. To the right of "GitHub Advanced Security", click **Try free for 30 days**, then follow the prompts to start your trial.

{% else %}

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: credit-card) Billing and licensing**.
1. Click **Licensing** to show detailed information on license use.
1. To the right of "GitHub Advanced Security", click **Start free trial**.
1. Click **Start trial**.

   During a trial of GitHub Advanced Security, you can add any number of committers and enable GitHub Secret Protection and GitHub Code Security for any number of organizations.

{% endif %}

## Evaluate features during your trial

After you start the trial, enable the features you want to evaluate on a sample of repositories. See [AUTOTITLE](/code-security/tutorials/trialing-github-advanced-security/enable-security-features-trial).

As you evaluate the features, compare the results with the goals and success criteria you defined when planning the trial.

## Billing during your trial

During the trial, you do not pay license fees for GitHub Secret Protection or GitHub Code Security.

{% ifversion fpt %}

Usage-based billing applies for features that consume GitHub Actions minutes or AI credits. For private repositories, GitHub Actions minutes used by GitHub Advanced Security workflows count toward your organization's included usage. This includes code scanning workflows. Usage beyond the included amount is billed at the standard rate. For more information, see [AUTOTITLE](/billing/reference/product-usage-included).

{% elsif ghec %}

Usage-based billing applies for features that consume GitHub Actions minutes or AI credits.

For private repositories, minutes used by GitHub Advanced Security workflows on standard GitHub-hosted runners count toward the 50,000 minutes included each month with your GitHub Enterprise Cloud plan. This includes code scanning workflows. Workflows in public repositories or on self-hosted runners do not consume included minutes. larger runners are billed separately. Usage beyond the included amount is billed at the standard rate. For more information, see [AUTOTITLE](/billing/reference/product-usage-included).

{% endif %}

## Managing and finishing your trial

Your trial lasts 30 days. You can review the expiration date and current usage on the "Licensing" page for your organization or enterprise.

{% ifversion fpt %}

To purchase during the trial:

1. Access the "Licensing" page for the organization.
1. In the GitHub Advanced Security trial banner, click **Buy Advanced Security**.
1. Review the estimated monthly usage, billing information, and payment method.
1. Click **Purchase Advanced Security**.

If you do not purchase by the end of the trial, it expires automatically, and GitHub Secret Protection and GitHub Code Security features are disabled for private repositories.

{% else %}

You can finish your trial at any time by purchasing licenses for GitHub Secret Protection or GitHub Code Security. If you haven't made a purchase by the end of the 30 days, your trial will expire.

If you pay for GitHub Enterprise Cloud with metered billing, but did not set up a free trial of GitHub Advanced Security, you can still use metered-based billing to pay for Advanced Security products after the GitHub Enterprise Cloud trial ends. For more information, contact [GitHub's Sales team](https://enterprise.github.com/contact).

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. At the top of the page, click **(icon: credit-card) Billing and licensing**.
1. Click **Licensing** to show detailed information on license use.
1. To the right of "GitHub Advanced Security trial", select the **Manage** dropdown menu and click **Purchase**.
1. Confirm your billing information and payment method.
1. Click **Purchase Advanced Security**.

{% ifversion billing-auth-and-capture %}

Note that GitHub may apply a temporary authorization hold for the value of the usage-based costs in advance, which will appear as a pending charge in your account's payment method.

{% endif %}

> [!TIP]
> If you pay for GitHub using volume/subscription billing, you will also need define how many licenses to purchase.
> * Under "How many committers do you want to include?", enter the number of committers you want to purchase licenses for. See [Active committers and unique committers](/billing/concepts/product-billing/github-advanced-security#active-and-unique-committers).

{% endif %}
