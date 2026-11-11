---
title: Canceling GitHub Copilot for your organization
shortTitle: Cancel
intro: 'Removing all assigned GitHub Copilot seats in your organization will cancel your organization''s Copilot plan.'
permissions: Organization owners
product: 'Copilot Business'
versions:
  feature: copilot
redirect_from:
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/canceling-copilot-for-your-organization
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-the-copilot-subscription-for-your-organization/canceling-copilot-for-your-organization
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-the-copilot-plan-for-your-organization/canceling-copilot-for-your-organization
  - /copilot/how-tos/administer/organizations/managing-the-copilot-plan-for-your-organization/canceling-copilot-for-your-organization
  - /copilot/how-tos/administer/organizations/managing-the-copilot-plan-for-your-organization/cancel
  - /copilot/how-tos/administer/organizations/manage-plan/cancel
  - /copilot/how-tos/administer/manage-for-organization/manage-plan/cancel
contentType: how-tos
category: 
  - Manage Copilot for a team
---

{% ifversion ghec %}
>[!NOTE]
> If your organization was granted access to Copilot through an enterprise, your enterprise admin will need to cancel the plan instead. See [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-plan/cancel-plan).
{% endif %}

To cancel your Copilot Business plan for your organization account, you need to remove all assigned GitHub Copilot seats.

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the "Access" section of the sidebar, click **(icon: credit-card) Billing & licensing** and then **Licensing** (new platform). Alternatively, in the "Code planning, and automation" section of the sidebar, click **(icon: copilot) Copilot**, and then click **Access** (original platform).

   >[!IMPORTANT] If you have not configured all policies for Copilot, you will not be able to complete the following steps. If that is the case, click **Go to policies** and ensure all policies are configured before proceeding.

1. Under {% ifversion ghec %}"Copilot Enterprise is active in your organization" or {% endif %}"Copilot Business is active in your organization," to revoke GitHub Copilot access for all users in your organization, select **Disabled**.
1. In the "Remove Copilot access" dialog, click **Confirm and remove seats**.
