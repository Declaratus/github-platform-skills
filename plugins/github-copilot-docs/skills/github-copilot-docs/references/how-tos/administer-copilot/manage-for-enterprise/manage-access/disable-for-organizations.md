---
title: Disabling Copilot for organizations in your enterprise
shortTitle: Disable for organizations
intro: 'Disable GitHub Copilot for some or all of the organizations in your enterprise.'
permissions: Enterprise owners
product: 'Enterprises with a Copilot Enterprise or Copilot Business plan'
versions:
  feature: copilot
redirect_from:
  - /copilot/managing-copilot/managing-copilot-for-your-enterprise/disabling-copilot-for-organizations-in-your-enterprise
  - /copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-access-to-copilot-in-your-enterprise/disabling-copilot-for-organizations-in-your-enterprise
  - /copilot/how-tos/administer/enterprises/managing-access-to-copilot-in-your-enterprise/disabling-copilot-for-organizations-in-your-enterprise
  - /copilot/how-tos/administer/enterprises/managing-access-to-copilot-in-your-enterprise/disable-for-organizations
  - /copilot/how-tos/administer/enterprises/manage-access/disable-for-organizations
  - /copilot/how-tos/administer/manage-for-enterprise/manage-access/disable-for-organizations
contentType: how-tos
category:
  - Manage Copilot for a team
---

This procedure applies to Copilot Business and Copilot Enterprise. When you disable access for organizations, organization owners cannot assign licenses to their members. Enterprise owners can still assign Copilot Business seats directly to users and teams in the enterprise settings.

For how seat assignment works with Copilot access, see [AUTOTITLE](/copilot/concepts/billing-and-usage/organizations-and-enterprises/seats-and-billing-cycles#seat-assignment).

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: credit-card) Billing and licensing**.
1. In the "Billing and licensing" sidebar, click **(icon: law) Licensing**.
1. In the "Copilot" section, click **Manage**.
1. Next to "Organization access", choose whether to disable Copilot for all organizations or allow for specific organizations.

   ![Screenshot of the "Organization access" section, with the dropdown menu highlighted.](/assets/images/help/copilot/organization-access-menu.png)

1. If you selected **Allow for specific organizations**:

   1. Click the **Organizations** tab.
   1. Locate the organization for which you want to disable Copilot.
   1. To the right of the organization name, select the **Copilot** dropdown menu.
       * If your enterprise has a Copilot Business plan, click **Disabled**.
       * If your enterprise has a Copilot Enterprise plan, click **Remove access**.

Once Copilot is disabled, licenses that are currently granted through the organization will be revoked at the end of the billing period. You will **not** be double-billed if a user also receives a license from your enterprise during this period.

## Further reading

* [AUTOTITLE](/billing/concepts/product-billing/github-copilot-licenses)
* [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies)
