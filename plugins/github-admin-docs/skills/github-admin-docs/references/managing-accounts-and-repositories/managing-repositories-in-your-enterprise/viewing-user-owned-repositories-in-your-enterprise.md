---
title: Viewing user-owned repositories in your enterprise
intro: You can view all repositories owned by users within your enterprise.
permissions: Enterprise owners can view user-owned repositories.
versions:
  feature: emu-owned-repos
shortTitle: View user-owned repositories
redirect_from:
  - /admin/user-management/managing-repositories-in-your-enterprise/viewing-user-owned-repositories-in-your-enterprise
contentType: how-tos
category:
  - Manage accounts and repositories
---

If your enterprise uses Enterprise Managed Users, and you've allowed users to create repositories owned by their user accounts, you can view all user-owned repositories within your enterprise.

You can also temporarily access any user-owned repository. For more information, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-repositories-in-your-enterprise/accessing-user-owned-repositories-in-your-enterprise).

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under "(icon: law) Policies", click **Member privileges**.
1. In the "Repository creation" section, under "Block the creation of user namespace repositories," click **View user namespace repositories in your enterprise**.

   ![Screenshot of a "Repository creation" section. A link labeled with an eye icon and "View user namespace repositories in your enterprise" is outlined.](/assets/images/help/business-accounts/view-user-namespace-repos.png)
