---
title: Configuring GitHub Pages for your enterprise
intro: You can enable or disable GitHub Pages for your enterprise and choose whether to make sites publicly accessible.
redirect_from:
  - /enterprise/admin/guides/installation/disabling-github-enterprise-pages
  - /enterprise/admin/guides/installation/configuring-github-enterprise-pages
  - /enterprise/admin/installation/configuring-github-pages-on-your-appliance
  - /enterprise/admin/configuration/configuring-github-pages-on-your-appliance
  - /admin/configuration/configuring-github-pages-on-your-appliance
  - /enterprise/admin/guides/installation/configuring-github-pages-for-your-enterprise
  - /admin/configuration/configuring-github-pages-for-your-enterprise
  - /admin/configuration/configuring-your-enterprise/configuring-github-pages-for-your-enterprise
  - /admin/configuration/configuring-user-applications-for-your-enterprise/configuring-github-pages-for-your-enterprise
versions:
  ghes: '*'
shortTitle: Configure GitHub Pages
contentType: how-tos
category:
  - Enable GitHub features for your enterprise
---

## Enabling public sites for GitHub Pages

If private mode is enabled on your enterprise, the public cannot access GitHub Pages sites hosted by your enterprise unless you enable public sites.

> [!WARNING]
> If you enable public sites for GitHub Pages, every site in every repository on your enterprise will be accessible to the public.

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. In the "Settings"" sidebar, click **Pages**.
1. Select **Public Pages**.
1. Under the "Settings" sidebar, click **Save settings**.

   > [!NOTE]
   > Saving settings in the Management Console restarts system services, which could result in user-visible downtime.

1. Wait for the configuration run to complete.

## Disabling GitHub Pages for your enterprise

If subdomain isolation is disabled for your enterprise, you should also disable GitHub Pages to protect yourself from potential security vulnerabilities. For more information, see [AUTOTITLE](/admin/configuring-settings/hardening-security-for-your-enterprise/enabling-subdomain-isolation).

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. In the "Settings"" sidebar, click **Pages**.
1. Deselect **Enable Pages**.
1. Under the "Settings" sidebar, click **Save settings**.

   > [!NOTE]
   > Saving settings in the Management Console restarts system services, which could result in user-visible downtime.

1. Wait for the configuration run to complete.

## Configuring GitHub Pages response headers for your enterprise

You can add or override response headers for GitHub Pages sites hosted by {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.

> [!WARNING]
> Ensure that your response headers are properly configured before saving. Improper configurations may negatively impact the security of {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. In the "Settings"" sidebar, click **Pages**.
1. Under "Http Header Name," type the header name. The length of header name should less than 128 characters.
1. Under "Http Header Value," type the header value. The length of header value should less than 300 characters.
1. Click **Add headers**.
1. Under the "Settings" sidebar, click **Save settings**.

   > [!NOTE]
   > Saving settings in the Management Console restarts system services, which could result in user-visible downtime.

1. Wait for the configuration run to complete.

## Further reading

* [AUTOTITLE](/admin/configuring-settings/hardening-security-for-your-enterprise/enabling-private-mode)
