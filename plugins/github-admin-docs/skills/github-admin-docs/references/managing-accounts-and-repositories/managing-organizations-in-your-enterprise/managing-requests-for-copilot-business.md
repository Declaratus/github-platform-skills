---
title: Managing requests for Copilot Business
intro: Meet your developers' needs by accepting Copilot requests from organizations in your enterprise.
permissions: Enterprise owners
product: Enterprise accounts with a subscription to GitHub Copilot Business.
versions:
  ghec: '*'
redirect_from:
  - /admin/managing-accounts-and-repositories/managing-organizations-in-your-enterprise/managing-requests-for-copilot-business-from-organizations-in-your-enterprise
shortTitle: Manage requests for Copilot
contentType: how-tos
category:
  - Manage accounts and repositories
---

Organization owners might not have the necessary permissions to satisfy requests from members. For example, if an organization owner is not an enterprise owner, and GitHub Copilot Business is not enabled for that organization, they will not have the permissions to approve requests for GitHub Copilot Business.

In these cases, when an organization member requests access to GitHub Copilot Business, the organization owner will be prompted to ask the enterprise owners to enable Copilot for the organization.

As an enterprise owner, you can view or dismiss these requests from your notifications page. You can approve the request by enabling Copilot for the organization.

## Approving requests for GitHub Copilot Business

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: copilot) AI controls**.
1. In the sidebar, click (icon: copilot) **Copilot**.
1. Click (icon: law) **Access management**.
1. In the "Copilot access" section, click the (icon: organization) **Organizations** tab.
1. Next to the organization you want to give access to, select the dropdown menu, then choose an access level.
