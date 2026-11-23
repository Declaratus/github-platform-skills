---
title: Placing a legal hold on a user or organization
intro: You can place a legal hold on a user or organization to ensure that repositories they own cannot be permanently removed from your enterprise.
redirect_from:
  - /enterprise/admin/user-management/placing-a-legal-hold-on-a-user-or-organization
  - /admin/user-management/placing-a-legal-hold-on-a-user-or-organization
  - /admin/user-management/managing-users-in-your-enterprise/placing-a-legal-hold-on-a-user-or-organization
versions:
  ghes: '*'
shortTitle: Place a legal hold
contentType: how-tos
category:
  - Manage accounts and repositories
---

Usually, if someone deletes a repository, it will be available on disk for 90 days and can be restored via the site admin dashboard. After 90 days the repository is purged and deleted forever. If you place a legal hold on a user or organization, repositories they own are available for restore indefinitely.

1. Sign in to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} at `http(s)://HOSTNAME/login`.
1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. Under "Search users, organizations, teams, repositories, gists, and applications", type the name of the user or organization in the text field. Then to the right of the field, click **Search**.
![Screenshot of the "Search" page of the "Site admin" settings. The button to search users and organizations, labeled "Search," is outlined.](/assets/images/enterprise/site-admin-settings/search-for-things.png)
1. In the search results, click the name of the user or organization.
![Screenshot of the "Accounts" search results. In the list of matches, "user1" is highlighted with an orange outline.](/assets/images/enterprise/site-admin-settings/click-user.png)
1. In the upper-right corner of the page, click **(icon: gear) Admin**.
![Screenshot of the header of the "Site admin" page for a user or repository. The "Admin" tab is highlighted with an orange outline.](/assets/images/enterprise/site-admin-settings/user/user-admin-tab-top.png)
1. Under "Legal hold", click **Place legal hold**.
