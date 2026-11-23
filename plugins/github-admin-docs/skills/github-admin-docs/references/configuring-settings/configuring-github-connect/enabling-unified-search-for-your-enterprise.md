---
title: Enabling unified search for your enterprise
shortTitle: Unified search
intro: You can allow users to include repositories on GitHub Enterprise Cloud in their search results when searching from {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.
redirect_from:
  - /enterprise/admin/guides/developer-workflow/enabling-unified-search-between-github-enterprise-and-github-com
  - /enterprise/admin/guides/developer-workflow/enabling-unified-search-between-github-enterprise-server-and-github-com
  - /enterprise/admin/developer-workflow/enabling-unified-search-between-github-enterprise-server-and-githubcom
  - /enterprise/admin/installation/enabling-unified-search-between-github-enterprise-server-and-githubcom
  - /enterprise/admin/configuration/enabling-unified-search-between-github-enterprise-server-and-githubcom
  - /admin/configuration/enabling-unified-search-between-github-enterprise-server-and-githubcom
  - /admin/configuration/managing-connections-between-github-enterprise-server-and-github-enterprise-cloud/enabling-unified-search-between-github-enterprise-server-and-githubcom
  - /admin/configuration/managing-connections-between-your-enterprise-accounts/enabling-unified-search-between-your-enterprise-account-and-githubcom
  - /admin/configuration/configuring-github-connect/enabling-unified-search-for-your-enterprise
permissions: Enterprise owners
versions:
  ghes: '*'
contentType: how-tos
category:
  - Install and configure your instance
---

## About unified search

When you enable unified search, users can view search results from content on GitHub.com or GHE.com when searching from {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.

You can choose to allow search results for public repositories on GitHub.com, and you can separately choose to allow search results for private repositories on GitHub Enterprise Cloud. If you enable unified search for private repositories, users can only search private repositories that they have access to and that are owned by the connected enterprise account. For more information, see [AUTOTITLE](/search-github/getting-started-with-searching-on-github/about-searching-on-github#searching-across-github-enterprise-and-githubcom-simultaneously).

Users will never be able to search {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} from GitHub Enterprise Cloud, even if they have access to both environments.

After you enable unified search for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, before individual users can see search results from private repositories on GitHub Enterprise Cloud in {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, each user must also connect their user account on GitHub Enterprise Server with a user account on GitHub Enterprise Cloud. For more information, see [AUTOTITLE](/search-github/getting-started-with-searching-on-github/enabling-repository-search-across-environments).

Searching via the REST and GraphQL APIs does not include GitHub Enterprise Cloud search results. Advanced search and searching for wikis in GitHub Enterprise Cloud are not supported.

## Enabling unified search

Before you can enable unified search, you must enable GitHub Connect. See [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-github-connect-for-ghecom) or [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-github-connect-for-githubcom).

1. Sign in to GitHub Enterprise Server and GitHub Enterprise Cloud.
1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the left sidebar, click **Enterprise{% ifversion ghes %} overview{% endif %}**.
1. At the top of the page, click **(icon: plug) GitHub Connect**.
1. To the right of "Unified search", click **Enable**.

   ![Screenshot of the "Unified search" for public repositories option. The "Enable" button is outlined in orange.](/assets/images/enterprise/site-admin-settings/github-dotcom-enable-search.png)
1. Optionally, to the right of "Users can search private repositories on ENTERPRISE ACCOUNT when searching from Enterprise Server", click **Enable**.

   ![Screenshot of the "Unified search" option for private repositories. To the right of the setting, the "Enable" button is outlined in orange.](/assets/images/enterprise/site-admin-settings/enable-private-search.png)
