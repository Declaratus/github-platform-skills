---
title: Disabling GitHub Connect
shortTitle: Disable GitHub Connect
intro: 'You can disable GitHub Connect to stop the connection from {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to GitHub Enterprise Cloud.'
versions:
  ghes: '*'
permissions: 'Enterprise owners'
category:
  - Install and configure your instance
---

When you disconnect from GitHub Enterprise Cloud, the GitHub Connect GitHub App is deleted from your enterprise account and credentials stored on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} are deleted.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: plug) GitHub Connect**.
1. Under "GitHub Connect", to the right of the enterprise account you'd like to disconnect, click **Disable GitHub Connect**.
1. Read the information about disconnection, then click **Disable GitHub Connect**.
