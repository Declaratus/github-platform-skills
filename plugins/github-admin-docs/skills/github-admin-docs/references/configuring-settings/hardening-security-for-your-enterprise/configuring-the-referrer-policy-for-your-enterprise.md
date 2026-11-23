---
title: Configuring the referrer policy for your enterprise
shortTitle: Configure referrer policy
intro: You can increase the privacy of {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} by configuring the policy for cross-origin requests.
redirect_from:
  - /admin/configuration/configuring-your-enterprise/configuring-the-referrer-policy-for-your-enterprise
  - /admin/configuration/hardening-security-for-your-enterprise/configuring-the-referrer-policy-for-your-enterprise
versions:
  ghes: '*'
contentType: how-tos
category:
  - Secure and govern your enterprise
---

## About the referrer policy for your enterprise

The referrer policy controls the information that GitHub Enterprise Server transmits in HTTP headers when someone visits a link from {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to an external site.

By default, when a user on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} visits a link to another site from a file or comment on your instance, the request includes the hostname for your instance in plain text within the `Referer` header. If the link leads to an external website, the owner of the website could read the hostname for your instance in requests or log files.

You can control the information that GitHub Enterprise Server sends when a user visits a link from your instance.

## Enabling the `same-origin` referrer policy

You can enable the `same-origin` referrer policy to instruct modern browsers to exclude the hostname for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} from requests to external websites. The setting applies to all links from the web interface on your instance. By default, GitHub Enterprise Server uses the `origin-when-cross-origin` and `strict-origin-when-cross-origin` referrer policies, which means your instance's hostname will appear in HTTP and HTTPS requests to external websites.

> [!NOTE]
> Changing the referrer policy to `same-origin` can affect external sites that expect a hostname in the HTTP headers for a request.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. Under **(icon: gear) Settings**, click **Authentication security**.
1. Under "User Agent Referrer Policy", select **Enable same origin referrer policy for all organizations**.
1. Click **Save**.
