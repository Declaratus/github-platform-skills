---
title: Preventing users from creating organizations
redirect_from:
  - /enterprise/admin/articles/preventing-users-from-creating-organizations
  - /enterprise/admin/hidden/preventing-users-from-creating-organizations
  - /enterprise/admin/user-management/preventing-users-from-creating-organizations
  - /admin/user-management/preventing-users-from-creating-organizations
  - /admin/user-management/managing-organizations-in-your-enterprise/preventing-users-from-creating-organizations
intro: You can prevent users from creating organizations in your enterprise.
versions:
  ghes: '*'
shortTitle: Prevent organization creation
contentType: how-tos
category:
  - Manage accounts and repositories
---
{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under {% ifversion ghes %} **(icon: law) Policies**{% else %}"(icon: gear) Settings"{% endif %}, click **Options**.
1. Under "Users can create organizations", use the drop-down menu and click **Enabled** or **Disabled**.
