---
title: Validating your domain settings
intro: Ensure that your domain settings are properly configured before booting up {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} for the first time.
redirect_from:
  - /enterprise/admin/installation/validating-your-domain-settings
  - /enterprise/admin/configuration/validating-your-domain-settings
  - /admin/configuration/validating-your-domain-settings
  - /admin/configuration/configuring-network-settings/validating-your-domain-settings
versions:
  ghes: '*'
shortTitle: Validate domain settings
contentType: how-tos
category:
  - Install and configure your instance
---
1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. In the "Settings" sidebar, click **Hostname**.
1. To test your appliance's DNS and SSL settings, under "Hostname", click **Test domain settings**.
1. If you don't receive a green checkmark next to all entries, review your configuration for the setting that failed. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-network-settings/configuring-dns-nameservers).
1. Under the "Settings" sidebar, click **Save settings**.

   > [!NOTE]
   > Saving settings in the Management Console restarts system services, which could result in user-visible downtime.

1. Wait for the configuration run to complete.
