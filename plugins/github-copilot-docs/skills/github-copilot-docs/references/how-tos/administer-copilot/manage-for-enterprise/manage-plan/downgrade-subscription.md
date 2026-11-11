---
title: Downgrading GitHub Copilot for your enterprise
shortTitle: Downgrade subscription
intro: 'You can downgrade organizations in your enterprise from Copilot Enterprise to Copilot Business.'
permissions: Enterprise owners
product: 'Enterprises with a Copilot Enterprise plan'
versions:
  feature: copilot
redirect_from:
  - /copilot/managing-copilot/managing-copilot-for-your-enterprise/downgrading-copilot-for-your-enterprise
  - /copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-the-copilot-subscription-for-your-enterprise/downgrading-copilot-for-your-enterprise
  - /copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-the-copilot-plan-for-your-enterprise/downgrading-copilot-for-your-enterprise
  - /copilot/how-tos/administer/enterprises/managing-the-copilot-plan-for-your-enterprise/downgrading-copilot-for-your-enterprise
  - /copilot/how-tos/administer/enterprises/managing-the-copilot-plan-for-your-enterprise/downgrade-subscription
  - /copilot/how-tos/administer/enterprises/manage-plan/downgrade-subscription
  - /copilot/how-tos/administer/manage-for-enterprise/manage-plan/downgrade-subscription
contentType: how-tos
category: 
  - Manage Copilot for a team
---

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: credit-card) Billing and licensing**.
1. In the "Billing and licensing" sidebar, click **(icon: law) Licensing**.
1. In the "Copilot" section, click **Manage**.
1. Click the **(icon: organization) Organizations** tab.
1. Locate the organization for which you want to downgrade Copilot.
1. To the right of the organization name, select the **Copilot** dropdown menu, and click **Business**.

   ![Screenshot of the Copilot "access management" page. A dropdown menu is selected, and a button labeled "Business" is outlined in orange.](/assets/images/help/copilot/copilot-downgrade-to-business.png)

1. In the pop-up window that appears, review the effects of downgrading the organization, then click **Confirm and downgrade**.
