---
title: Enabling GitHub Connect for GHE.com
shortTitle: Enable for GHE.com
intro: 'Enable GitHub Connect to share data between GHE.com and {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.'
versions:
  feature: ghecom-github-connect
redirect_from:
   - /early-access/admin/preview-of-data-residency-for-github-enterprise/configuring-github-connect-during-the-preview-of-data-residency
   - /early-access/admin/private-ga-of-data-residency-for-github-enterprise-cloud/configuring-github-connect-during-the-private-ga-of-data-residency
   - /early-access/admin/data-residency-for-github-enterprise-cloud/configuring-github-connect-for-data-residency
category:
  - Install and configure your instance
---

You can access additional features and workflows on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} by enabling GitHub Connect. See [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/about-github-connect).

* Server Statistics is not available.
* Automatic user license sync requires GitHub Enterprise Server version 3.15 or later.
* Actions from GitHub.com require GitHub Enterprise Server version 3.20.6 or later, or any feature release from 3.21.0.

## What happens when GitHub Connect is enabled?

When you enable GitHub Connect, you configure a connection between {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} and an enterprise account on GitHub Enterprise Cloud. The connection uses HTTPS over ports 443 or 80 and is secured by TLS.

Enabling GitHub Connect creates a GitHub App owned by the enterprise account on GitHub Enterprise Cloud. GitHub Enterprise Server uses the GitHub App's credentials to make requests to GitHub Enterprise Cloud.

GitHub Enterprise Server stores credentials from the GitHub App. The following credentials will be replicated to all nodes in a high availability or cluster environment, and stored in any backups, including snapshots created by GitHub Enterprise Server Backup Utilities.

* An authentication token, which is valid for one hour
* A private key, which is used to generate a new authentication token

## Prerequisites

* **Administrative access:** You need administrative access to both an enterprise account on GHE.com and a GitHub Enterprise Server instance.
* **Version requirement:** To enable GitHub Connect for GHE.com, your GitHub Enterprise Server instance must be on version 3.12 or later. Certain individual features of GitHub Connect require later versions. See [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/about-github-connect#github-connect-features).
* **Proxy configuration:** If using a proxy server, allow connectivity to the following GHE.com hostnames (replace SUBDOMAIN with your enterprise's subdomain).

   * `SUBDOMAIN.ghe.com`
   * `api.SUBDOMAIN.ghe.com`
   * `uploads.SUBDOMAIN.ghe.com`

   See [AUTOTITLE](/admin/configuring-settings/configuring-network-settings/configuring-an-outbound-web-proxy-server).

## Step 1: Enable connection to GHE.com

By default, GitHub Connect connects GitHub Enterprise Server to GitHub.com. You must enable your instance to connect to your enterprise's subdomain of GHE.com.

To enable the connection, someone with administrative SSH access to your GitHub Enterprise Server instance must complete the following tasks.

1. SSH into {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. If your instance comprises multiple nodes, for example if high availability or geo-replication are configured, SSH into the primary node. If you use a cluster, you can SSH into any node. Replace HOSTNAME with the hostname for your instance, or the hostname or IP address of a node. For more information, see [AUTOTITLE]({% ifversion not ghes %}/enterprise-server@latest{% endif %}/admin/administering-your-instance/administering-your-instance-from-the-command-line/accessing-the-administrative-shell-ssh).

   ```shell copy
   ssh -p 122 admin@HOSTNAME
   ```
1. To enable your instance to connect to GHE.com for GitHub Connect, run the following command. Replace SUBDOMAIN with the subdomain for your enterprise on GHE.com, for example `octocorp`.

   ```shell copy
   ghe-config app.github.github-connect-ghe-com-enabled true
   ghe-config app.github.github-connect-ghe-com-subdomain "SUBDOMAIN"
   ```

1. To apply the configuration, run the following command.

   >[!NOTE] During a configuration run, services on your GitHub Enterprise Server instance may restart, which can cause brief downtime for users.

    ```shell copy
    ghe-config-apply
    ```

After the run completes, you can configure GitHub Connect.

## Step 2: Enable GitHub Connect

To enable GitHub Connect, you must be an enterprise owner on both GitHub Enterprise Server and GitHub Enterprise Cloud.

People with a user account in both environments can connect the accounts from your GitHub Enterprise Server instance.

1. Sign in to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} and GHE.com.
{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: plug) GitHub Connect**.
1. Under "GitHub Connect is not enabled yet", click **Enable GitHub Connect**. By clicking **Enable GitHub Connect**, you agree to the [AUTOTITLE](/free-pro-team@latest/site-policy/github-terms/github-terms-for-additional-products-and-features#connect).
1. To the right of the enterprise account you'd like to connect, click **Connect**.
1. Choose which individual features of GitHub Connect you want to enable. See [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/about-github-connect#github-connect-features).

## Reenabling connections to GitHub.com

If you need to reenable GitHub Connect for GitHub.com, you must reconfigure your settings.

1. SSH into {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. If your instance comprises multiple nodes, for example if high availability or geo-replication are configured, SSH into the primary node. If you use a cluster, you can SSH into any node. Replace HOSTNAME with the hostname for your instance, or the hostname or IP address of a node. For more information, see [AUTOTITLE]({% ifversion not ghes %}/enterprise-server@latest{% endif %}/admin/administering-your-instance/administering-your-instance-from-the-command-line/accessing-the-administrative-shell-ssh).

   ```shell copy
   ssh -p 122 admin@HOSTNAME
   ```
1. Run the following command.

   ```shell copy
   ghe-config app.github.github-connect-ghe-com-enabled false
   ```

1. To apply the configuration, run the following command.

   >[!NOTE] During a configuration run, services on your GitHub Enterprise Server instance may restart, which can cause brief downtime for users.

    ```shell copy
    ghe-config-apply
    ```

1. Enable GitHub Connect on GitHub.com. See [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-github-connect-for-githubcom).
