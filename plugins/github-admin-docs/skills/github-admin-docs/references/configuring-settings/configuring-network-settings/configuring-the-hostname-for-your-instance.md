---
title: Configuring the hostname for your instance
shortTitle: Configure hostname
intro: You can provide reliable access to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} by assigning a hostname that's accessible over your network.
redirect_from:
  - /enterprise/admin/guides/installation/configuring-hostnames
  - /enterprise/admin/installation/configuring-a-hostname
  - /enterprise/admin/configuration/configuring-a-hostname
  - /admin/configuration/configuring-a-hostname
  - /admin/configuration/configuring-network-settings/configuring-a-hostname
  - /admin/configuration/configuring-network-settings/configuring-the-hostname-for-your-instance
versions:
  ghes: '*'
contentType: how-tos
category:
  - Install and configure your instance
---

## About the hostname for GitHub Enterprise Server

To provide reliable access to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} via a known name on the network, you can configure a hostname. If you configure a hostname instead of using a hard-coded IP address, you will be able to change the physical hardware that {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} runs on without affecting users or client software.

The hostname setting in the Management Console should be set to an appropriate fully qualified domain name (FQDN) which is resolvable on the internet or within your internal network. For example, your hostname setting could be `github.companyname.com.` Web and API requests will automatically redirect to the hostname configured in the Management Console. Note that `localhost` is not a valid hostname setting.

Hostnames must be less than 63 characters in length per [Section 2.3.4 of the Domain Names Specification RFC](https://datatracker.ietf.org/doc/html/rfc1035#section-2.3.4).

After you configure a hostname, you can enable subdomain isolation to further increase the security of {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. For more information, see [AUTOTITLE](/admin/configuring-settings/hardening-security-for-your-enterprise/enabling-subdomain-isolation).

GitHub strongly recommends that you do not change the hostname for an existing GitHub Enterprise Server instance. Changing the hostname will cause unexpected behavior, up to and including instance outages. Instead, configure a new instance with the desired hostname, and then restore settings and data from the original instance to the new instance.

For more information on the supported hostname types, see [Section 2.1 of the HTTP RFC](https://tools.ietf.org/html/rfc1123#section-2).

## Configuring the hostname

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. In the "Settings" sidebar, click **Hostname**.
1. Under "Hostname", type the hostname you'd like to set for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.
1. To test the DNS and SSL settings for the new hostname, click **Test domain settings**.
1. If you don't receive a green checkmark next to all entries, review your configuration for the setting that failed. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-network-settings/configuring-dns-nameservers).
1. Under the "Settings" sidebar, click **Save settings**.

   > [!NOTE]
   > Saving settings in the Management Console restarts system services, which could result in user-visible downtime.

1. Wait for the configuration run to complete.

To help mitigate various cross-site scripting vulnerabilities, we recommend that you enable subdomain isolation for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} after you configure a hostname. For more information, see [AUTOTITLE](/admin/configuring-settings/hardening-security-for-your-enterprise/enabling-subdomain-isolation).

## Changing the hostname

If you need to change the hostname for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, you must restore a backup of your existing instance to a new instance with the desired hostname. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-network-settings/changing-the-hostname-for-your-instance).

> [!WARNING]
> Do not change the hostname for GitHub Enterprise Server after initial setup. Changing the hostname will cause unexpected behavior, up to and including instance outages and invalidation of users' security keys. If you have changed the hostname for your instance and are experiencing problems, contact GitHub Enterprise Support or GitHub Premium Support.
