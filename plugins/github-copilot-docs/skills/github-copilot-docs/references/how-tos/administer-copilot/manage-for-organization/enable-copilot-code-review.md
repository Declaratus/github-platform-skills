---
title: Enabling GitHub Copilot code review in your organization
intro: 'Turn on Copilot code review for your organization''s pull requests without assigning a Copilot license to any member.'
allowTitleToDifferFromFilename: true
permissions: Organization owners
product: 'Copilot Business, Copilot Enterprise, or the Copilot access plan for eligible enterprises'
versions:
  feature: copilot
shortTitle: Enable Copilot code review
contentType: how-tos
category:
  - Manage Copilot for a team
---

After you enable the policy for Copilot code review, members with a Copilot license from your organization can request reviews. You can also allow reviews without a license. The AI credits those reviews use are billed to your organization or enterprise.

## Subscribing to Copilot Business without assigning licenses

Your organization needs a Copilot plan and a payment method and billing information on file, but it doesn't need to assign any licenses. If your organization already has a plan, skip to [Enabling Copilot code review](#enabling-copilot-code-review). If your organization is owned by an enterprise, an enterprise owner sets up the plan. See [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-plan/subscribe).

1. Navigate to the [GitHub Copilot sign up page](https://github.com/github-copilot/purchase?ref_product=copilot&ref_type=purchase&ref_style=text).
1. Make sure you're signed in to the right organization account. If you aren't, click **(icon: arrow-switch) Switch** and select the organization.
1. Click **Enable GitHub Copilot**.

After you enable Copilot, you don't need to assign any licenses. You're billed for Copilot Business licenses only when you assign them.

## Enabling Copilot code review

We recommend having your organization pay for every review, so that no pull request goes without a review. Otherwise, reviews for members who use their own Copilot license, such as Copilot Pro, stop when those members run out of AI credits, and pull requests from authors without a license don't get reviews. To limit what your organization spends, see [Controlling spending](#controlling-spending).

If your organization is owned by an enterprise, you can't change settings that an enterprise owner has set. An enterprise owner can turn on reviews without a license or let organizations decide. See [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/enable-copilot-code-review#allowing-reviews-without-a-copilot-license).

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the sidebar, under "Code, planning, and automation", click **(icon: copilot) Copilot**, then **Policies**.
1. Under "Billing," next to "AI credit paid usage," select **Enabled**, or select **Enabled for selected products** and turn on **Opt in to Copilot AI Credits paid usage**.
1. Next to "Copilot code review," select **Enabled**.
1. Next to "Choose how members with a Copilot license are billed," select **Organization**.
1. Turn on **Allow reviews without a Copilot license**. Reviews without a license include pull requests from outside contributors, members on Copilot Free, and bots such as Dependabot.

Pull requests in your organization can now get reviews from Copilot, whether or not their authors have a license. Members without a license can't request reviews in IDEs.

## Configuring automatic code review

To have Copilot review pull requests without anyone requesting a review, create a ruleset for the repositories where you want automatic reviews. After members without a license can use Copilot code review, automatic reviews run on their pull requests too. See [AUTOTITLE](/copilot/how-tos/copilot-on-github/set-up-copilot/configure-code-review#configuring-automatic-code-review-for-repositories-in-an-organization).

## Controlling spending

If your organization isn't owned by an enterprise and has no assigned licenses, or is owned by an enterprise on the Copilot access plan, it has no included AI credits. Every review billed to it is paid usage.

To cap spending, create an organization budget for AI credits and select **Stop usage when budget limit is reached**. At the limit, reviews that need paid usage stop until the next billing cycle or until you raise the budget. See [AUTOTITLE](/billing/how-tos/set-up-budgets).

If your organization is owned by an enterprise, create the budget in your enterprise account's billing settings, with your organization as its scope. An enterprise owner can also set a budget for a cost center or the whole enterprise. See [AUTOTITLE](/copilot/concepts/billing-and-usage/organizations-and-enterprises/budgets#how-billing-flows-through-budgets).

Reviews also use GitHub Actions minutes. See [AUTOTITLE](/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/code-review#code-review-usage-and-billing).
