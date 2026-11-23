---
title: Enabling subdomain isolation
intro: You can set up subdomain isolation to securely separate user-supplied content from other portions of your GitHub Enterprise Server appliance.
redirect_from:
  - /enterprise/admin/guides/installation/about-subdomain-isolation
  - /enterprise/admin/installation/enabling-subdomain-isolation
  - /enterprise/admin/configuration/enabling-subdomain-isolation
  - /admin/configuration/enabling-subdomain-isolation
  - /admin/configuration/configuring-network-settings/enabling-subdomain-isolation
  - /admin/configuration/hardening-security-for-your-enterprise/enabling-subdomain-isolation
versions:
  ghes: '*'
shortTitle: Enable subdomain isolation
contentType: how-tos
category:
  - Secure and govern your enterprise
---
## About subdomain isolation

Subdomain isolation mitigates cross-site scripting and other related vulnerabilities. For more information, see [Cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting) on Wikipedia. We highly recommend that you enable subdomain isolation on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.

When subdomain isolation is enabled, GitHub Enterprise Server replaces several paths with subdomains. After enabling subdomain isolation, attempts to access the previous paths for some user-supplied content, such as `http(s)://HOSTNAME/raw/`, may return `404` errors.

| Path without subdomain isolation  | Path with subdomain isolation   |
| --- | --- |
| `http(s)://HOSTNAME/` | `http(s)://docker.HOSTNAME/` |
| `http(s)://HOSTNAME/_registry/npm/` | `https://npm.HOSTNAME/` |
| `http(s)://HOSTNAME/_registry/rubygems/` | `https://rubygems.HOSTNAME/` |
| `http(s)://HOSTNAME/_registry/maven/` | `https://maven.HOSTNAME/` |
| `http(s)://HOSTNAME/_registry/nuget/` | `https://nuget.HOSTNAME/` |
| `http(s)://HOSTNAME/assets/` | `http(s)://assets.HOSTNAME/` |
| `http(s)://HOSTNAME/avatars/` | `http(s)://avatars.HOSTNAME/` |
| `http(s)://HOSTNAME/codeload/` | `http(s)://codeload.HOSTNAME/` |
| `http(s)://HOSTNAME/gist/` | `http(s)://gist.HOSTNAME/` |
| `http(s)://HOSTNAME/media/` | `http(s)://media.HOSTNAME/` |
| `http(s)://HOSTNAME/notebooks/` | `http(s)://notebooks.HOSTNAME/` |
| `http(s)://HOSTNAME/pages/` | `http(s)://pages.HOSTNAME/` |
| `http(s)://HOSTNAME/raw/` | `http(s)://raw.HOSTNAME/` |
| `http(s)://HOSTNAME/reply/` | `http(s)://reply.HOSTNAME/` |
| `http(s)://HOSTNAME/uploads/` | `http(s)://uploads.HOSTNAME/` |
| `http(s)://HOSTNAME/viewscreen/` | `http(s)://viewscreen.HOSTNAME/` |
| Not supported | `https://containers.HOSTNAME/` |

## Prerequisites

{% ifversion ghes %}

> [!WARNING]
> If subdomain isolation is disabled, we recommend also disabling GitHub Pages on your enterprise. There will be no way to isolate user-supplied GitHub Pages content from the rest of your enterprise's data. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-user-applications-for-your-enterprise/configuring-github-pages-for-your-enterprise).

{% endif %}

Before you enable subdomain isolation, you must configure your network settings for your new domain.

* Specify a valid domain name as your hostname, instead of an IP address. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-network-settings/configuring-the-hostname-for-your-instance).

> [!WARNING]
> Do not change the hostname for GitHub Enterprise Server after initial setup. Changing the hostname will cause unexpected behavior, up to and including instance outages and invalidation of users' security keys. If you have changed the hostname for your instance and are experiencing problems, contact GitHub Enterprise Support or GitHub Premium Support.

* Set up a wildcard Domain Name System (DNS) record or individual DNS records for the subdomains listed above. We recommend creating an A record for `*.HOSTNAME` that points to your server's IP address so you don't have to create multiple records for each subdomain.
* Get a wildcard Transport Layer Security (TLS) certificate for `*.HOSTNAME` with a Subject Alternative Name (SAN) for both `HOSTNAME` and the wildcard domain `*.HOSTNAME`. For example, if your hostname is `github.octoinc.com`, get a certificate with the Common Name value set to `*.github.octoinc.com` and a SAN value set to both `github.octoinc.com` and `*.github.octoinc.com`.
* Enable TLS on your appliance. For more information, see [AUTOTITLE](/admin/configuring-settings/hardening-security-for-your-enterprise/configuring-tls).

## Enabling subdomain isolation

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. In the "Settings" sidebar, click **Hostname**.
1. Select **Subdomain isolation (recommended)**.
1. Under the "Settings" sidebar, click **Save settings**.

   > [!NOTE]
   > Saving settings in the Management Console restarts system services, which could result in user-visible downtime.

1. Wait for the configuration run to complete.
