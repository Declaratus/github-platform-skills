---
title: Network ports
redirect_from:
  - /enterprise/admin/articles/configuring-firewalls
  - /enterprise/admin/articles/firewall
  - /enterprise/admin/guides/installation/network-configuration
  - /enterprise/admin/guides/installation/network-ports-to-open
  - /enterprise/admin/installation/network-ports
  - /enterprise/admin/configuration/network-ports
  - /admin/configuration/network-ports
  - /admin/configuration/configuring-network-settings/network-ports
intro: Open network ports selectively based on the network services you need to expose for administrators, end users, and email support.
versions:
  ghes: '*'
contentType: reference
category:
  - Install and configure your instance
---
## Administrative ports

Some administrative ports are required to configure {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} and run certain features. Administrative ports are not required for basic application use by end users.

| Port | Service | Description |
|---|---|---|
| 8443 | HTTPS | Secure web-based Management Console. Required for basic installation and configuration. |
| 8080 | HTTP | Plain-text web-based Management Console. Not required unless TLS is disabled manually. |
| 122 | SSH | Shell access for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. Required to be open to incoming connections between all nodes in a high availability configuration. The default SSH port (22) is dedicated to Git and SSH application network traffic. |
| 1194/UDP | VPN | Secure replication network tunnel in high availability configuration. Required to be open for communication between all nodes in the configuration.|
| 123/UDP| NTP | Required for time protocol operation. |
| 161/UDP | SNMP | Required for network monitoring protocol operation. |
| 9103/TCP | HTTP | Required for future support of Prometheus scraping. |

## Application ports for end users

Application ports provide web application and Git access for end users.

| Port | Service | Description |
|---|---|---|
| 443 | HTTPS | Access to the web application and Git over HTTPS. |
| 80 | HTTP | Access to the web application. All requests are redirected to the HTTPS port if TLS is configured. |
| 22 | SSH | Access to Git over SSH. Supports clone, fetch, and push operations to public and private repositories. |
| 9418 | Git | Git protocol port supports clone and fetch operations to public repositories with unencrypted network communication. If you have enabled private mode on your instance, then opening this port is only required if you also enabled anonymous Git read access. For more information, see [AUTOTITLE](/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise#configuring-anonymous-git-read-access). |

> [!WARNING]
> When terminating HTTPS connections on a load balancer, the requests from the load balancer to GitHub Enterprise Server also need to use HTTPS. Downgrading the connection to HTTP is not supported.

## Email ports

Email ports must be accessible directly or via relay for inbound email support for end users.

| Port | Service | Description |
|---|---|---|
| 25 | SMTP | Support for SMTP with encryption (STARTTLS). |

## GitHub Actions ports

GitHub Actions ports must be accessible for self-hosted runners to connect to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. For more information, see [AUTOTITLE](/actions/reference/runners/self-hosted-runners).

| Port | Service | Description |
|---|---|---|
| 443 | HTTPS | Self-hosted runners connect to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to receive job assignments and to download new versions of the runner application. Required if TLS is configured.
| 80 | HTTP | Self-hosted runners connect to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to receive job assignments and to download new versions of the runner application. Required if TLS is not configured.

If you enable automatic access to GitHub.com actions, GitHub Actions will always search for an action on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} first, via these ports, before checking GitHub.com. For more information, see [AUTOTITLE](/admin/managing-github-actions-for-your-enterprise/managing-access-to-actions-from-githubcom/enabling-automatic-access-to-githubcom-actions-using-github-connect#about-resolution-for-actions-using-github-connect).

## GitHub Connect ports

If you enable GitHub Connect, the connection between GitHub Enterprise Server and GitHub.com uses HTTPS over ports 443 or 80, and TLS is required. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/about-github-connect).

## Further reading

* [AUTOTITLE](/admin/configuring-settings/hardening-security-for-your-enterprise/configuring-tls)
