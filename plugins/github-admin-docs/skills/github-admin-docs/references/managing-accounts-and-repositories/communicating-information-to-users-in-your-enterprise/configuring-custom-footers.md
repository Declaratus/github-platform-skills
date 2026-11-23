---
title: Configuring custom footers
intro: You can give users easy access to enterprise-specific links by adding custom footers.
permissions: Enterprise owners can configure a custom footer.
versions:
  ghec: '*'
  ghes: '*'
shortTitle: Configure custom footers
redirect_from:
  - /admin/configuration/configuring-your-enterprise/configuring-custom-footers
contentType: how-tos
category:
  - Manage accounts and repositories
---

## About custom footers for your enterprise

You can configure the web UI for your enterprise to display a custom footer with up to five additional links. The custom footer appears above the default GitHub footer{% ifversion ghes %}, to all users and on all pages of your GitHub Enterprise Server instance{% elsif ghec %} to all enterprise members and collaborators, on all repository and organization pages for repositories and organizations that belong to the enterprise{% endif %}.

## Configuring custom footers

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. Under **(icon: gear) Settings**, click **General**.
1. Navigate to **Custom footer**.
1. Under each "Footer Link" heading, type a title and URL.
1. To save the content and display the custom footer, click **Update footer**.
