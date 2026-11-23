---
title: Enabling GitHub Connect for GitHub.com
shortTitle: Enable for GitHub.com
intro: Enable GitHub Connect to access additional features and workflows from GitHub.com on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.
redirect_from:
  - /enterprise/admin/guides/developer-workflow/connecting-github-enterprise-to-github-com
  - /enterprise/admin/guides/developer-workflow/connecting-github-enterprise-server-to-github-com
  - /enterprise/admin/developer-workflow/connecting-github-enterprise-server-to-githubcom
  - /enterprise/admin/installation/connecting-github-enterprise-server-to-github-enterprise-cloud
  - /enterprise/admin/configuration/connecting-github-enterprise-server-to-github-enterprise-cloud
  - /admin/configuration/connecting-github-enterprise-server-to-github-enterprise-cloud
  - /admin/configuration/managing-connections-between-github-enterprise-server-and-github-enterprise-cloud/connecting-github-enterprise-server-to-github-enterprise-cloud
  - /admin/configuration/managing-connections-between-your-enterprise-accounts/connecting-your-enterprise-account-to-github-enterprise-cloud
  - /admin/configuration/configuring-github-connect/managing-github-connect
  - /admin/configuring-settings/configuring-github-connect/managing-github-connect
versions:
  ghes: '*'
contentType: how-tos
category:
  - Install and configure your instance
---

You can access additional features and workflows on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} by enabling GitHub Connect. See [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/about-github-connect).

## What happens when GitHub Connect is enabled?

When you enable GitHub Connect, you configure a connection between {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} and an enterprise account on GitHub Enterprise Cloud. The connection uses HTTPS over ports 443 or 80 and is secured by TLS.

Enabling GitHub Connect creates a GitHub App owned by the enterprise account on GitHub Enterprise Cloud. GitHub Enterprise Server uses the GitHub App's credentials to make requests to GitHub Enterprise Cloud.

GitHub Enterprise Server stores credentials from the GitHub App. The following credentials will be replicated to all nodes in a high availability or cluster environment, and stored in any backups, including snapshots created by GitHub Enterprise Server Backup Utilities.

* An authentication token, which is valid for one hour
* A private key, which is used to generate a new authentication token

## Prerequisites

* You must have an enterprise account on GitHub.com that uses GitHub Enterprise Cloud.
* Your enterprise account on GitHub.com must be invoiced. Enterprise accounts on the free trial of GitHub Enterprise Cloud or that pay by credit card cannot be connected to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.
* If your enterprise account on GitHub.com uses IP allow lists, you must add the IP address or network for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to your IP allow list. See [AUTOTITLE](/enterprise-cloud@latest/admin/configuring-settings/hardening-security-for-your-enterprise/restricting-network-traffic-to-your-enterprise-with-an-ip-allow-list#adding-an-allowed-ip-address) in the GitHub Enterprise Cloud documentation.
* To configure a connection, your proxy configuration must allow connectivity to `github.com`, `api.github.com`, and `uploads.github.com`. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-network-settings/configuring-an-outbound-web-proxy-server).
* If you have previously enabled GitHub Connect for an enterprise on GHE.com, you must change your configuration to allow connections to GitHub.com. See [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-github-connect-for-ghecom#reenabling-connections-to-githubcom).

## Enabling GitHub Connect

To enable GitHub Connect, you must be an enterprise owner on both GitHub Enterprise Server and GitHub Enterprise Cloud.

1. Sign in to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} and GitHub.com.
{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: plug) GitHub Connect**.
1. Under "GitHub Connect is not enabled yet", click **Enable GitHub Connect**. By clicking **Enable GitHub Connect**, you agree to the [AUTOTITLE](/free-pro-team@latest/site-policy/github-terms/github-terms-for-additional-products-and-features#connect).
1. To the right of the enterprise account you'd like to connect, click **Connect**.
