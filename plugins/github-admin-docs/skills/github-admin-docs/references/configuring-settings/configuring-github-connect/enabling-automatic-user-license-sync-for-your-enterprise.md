---
title: Enabling automatic user license sync for your enterprise
intro: You can manage license usage across your GitHub Enterprise environments by automatically syncing user licenses from {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to GitHub Enterprise Cloud.
redirect_from:
  - /enterprise/admin/installation/enabling-automatic-user-license-sync-between-github-enterprise-server-and-github-enterprise-cloud
  - /enterprise/admin/configuration/enabling-automatic-user-license-sync-between-github-enterprise-server-and-github-enterprise-cloud
  - /admin/configuration/enabling-automatic-user-license-sync-between-github-enterprise-server-and-github-enterprise-cloud
  - /admin/configuration/managing-connections-between-github-enterprise-server-and-github-enterprise-cloud/enabling-automatic-user-license-sync-between-github-enterprise-server-and-github-enterprise-cloud
  - /admin/configuration/managing-connections-between-your-enterprise-accounts/enabling-automatic-user-license-sync-between-github-enterprise-server-and-github-enterprise-cloud
  - /admin/configuration/configuring-github-connect/enabling-automatic-user-license-sync-for-your-enterprise
permissions: Enterprise owners can enable automatic user license synchronization.
versions:
  ghes: '*'
shortTitle: Automatic user license sync
contentType: how-tos
category:
  - Install and configure your instance
---
## About automatic license synchronization

GitHub uses a unique-user licensing model. With the GitHub Enterprise plan, you're entitled to use both GitHub Enterprise Cloud and GitHub Enterprise Server. Your GitHub Enterprise Cloud allowance includes **one** deployment, on either GitHub.com or GHE.com.

GitHub determines how many {% ifversion enterprise-licensing-language %}licenses{% else %}licensed seats{% endif %} you're consuming based on the number of unique users across your deployments. Each user only consumes one license, no matter how many GitHub Enterprise Server instances the user uses, or how many organizations the user is a member of on your GitHub Enterprise Cloud deployment. This model allows each person to use multiple GitHub Enterprise deployments without incurring extra costs.

For a person using multiple GitHub Enterprise environments to only consume a single license, you must synchronize license usage between environments. Then, GitHub will deduplicate users based on the email addresses associated with their user accounts. GitHub deduplicates licenses for the GitHub Enterprise plan itself, and{% ifversion ghec %} if you use GitHub Enterprise Server version 3.12 or later,{% endif %} for GitHub Advanced Security products. See {% ifversion ghes %}[AUTOTITLE](/billing/how-tos/manage-server-licenses/sync-license-usage){% else %}[AUTOTITLE](/enterprise-cloud@latest/billing/how-tos/manage-server-licenses/sync-license-usage){% endif %}. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/about-github-connect#data-transmission).

If you enable automatic user license sync for your enterprise, every week, GitHub Connect will automatically synchronize license usage between GitHub Enterprise Server and your enterprise on GitHub.com or GHE.com. You can also synchronize your license data at any time outside of the automatic weekly sync, by manually triggering a license sync job. For more information, see [AUTOTITLE](/billing/how-tos/manage-server-licenses/sync-license-usage#triggering-a-license-sync-job).

If you use multiple GitHub Enterprise Server instances, you can enable automatic license sync between each of your instances and the same enterprise account on GitHub Enterprise Cloud.

After you synchronize license usage, you can see a report of consumed licenses across all your environments in the enterprise settings on GitHub Enterprise Cloud. For more information, see [AUTOTITLE](/enterprise-cloud@latest/billing/how-tos/manage-plan-and-licenses/view-enterprise-usage).

You can also manually upload GitHub Enterprise Server user license information to GitHub Enterprise Cloud. For more information, see [AUTOTITLE](/billing/how-tos/manage-server-licenses/sync-license-usage).

> [!NOTE] To make troubleshooting easier, if you synchronize license usage and do not use Enterprise Managed Users, we highly recommend enabling verified domains for your enterprise account on GitHub Enterprise Cloud. See [AUTOTITLE](/enterprise-cloud@latest/admin/configuring-settings/configuring-user-applications-for-your-enterprise/verifying-or-approving-a-domain-for-your-enterprise){% ifversion not ghec %} in the GitHub Enterprise Cloud documentation.{% else %}.{% endif %}

## Enabling license synchronization

Before enabling license synchronization on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, you must enable GitHub Connect. See [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-github-connect-for-ghecom) or [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-github-connect-for-githubcom).

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: plug) GitHub Connect**.
1. To the right of "License sync", click **Enable**.

   ![Screenshot of the "License sync" option on the GitHub Connect page. The "Enable" button is highlighted with an orange outline.](/assets/images/enterprise/site-admin-settings/enable-user-license-drop-down.png)

> [!NOTE]
> If SAML with SCIM is enabled, the `scim-admin` setup user will not consume a license. For more information, see [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/configuring-scim-provisioning-for-users#1-create-a-built-in-setup-user).
