---
title: Enabling unified contributions for your enterprise
shortTitle: Unified contributions
intro: You can allow users to include anonymized contribution counts for their work on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} in their contribution graphs on GitHub Enterprise Cloud.
redirect_from:
  - /enterprise/admin/guides/developer-workflow/enabling-unified-contributions-between-github-enterprise-and-github-com
  - /enterprise/admin/guides/developer-workflow/enabling-unified-contributions-between-github-enterprise-server-and-github-com
  - /enterprise/admin/developer-workflow/enabling-unified-contributions-between-github-enterprise-server-and-githubcom
  - /enterprise/admin/installation/enabling-unified-contributions-between-github-enterprise-server-and-githubcom
  - /enterprise/admin/configuration/enabling-unified-contributions-between-github-enterprise-server-and-githubcom
  - /admin/configuration/enabling-unified-contributions-between-github-enterprise-server-and-githubcom
  - /admin/configuration/managing-connections-between-github-enterprise-server-and-github-enterprise-cloud/enabling-unified-contributions-between-github-enterprise-server-and-githubcom
  - /admin/configuration/managing-connections-between-your-enterprise-accounts/enabling-unified-contributions-between-your-enterprise-account-and-githubcom
  - /admin/configuration/configuring-github-connect/enabling-unified-contributions-for-your-enterprise
permissions: Enterprise owners
versions:
  ghes: '*'
contentType: how-tos
category:
  - Install and configure your instance
---

## About unified contributions

As an enterprise owner, you can allow end users to send anonymized contribution counts for their work from {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to their contribution graph on GitHub.com or GHE.com.

After you enable unified contributions, before individual users can send contribution counts from {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to GitHub Enterprise Cloud, each user must also connect their user account on GitHub Enterprise Server with an account on GitHub Enterprise Cloud. For more information, see [AUTOTITLE](/account-and-profile/how-tos/contribution-settings/sharing-contributions-from-github-enterprise-server).

GitHub requests updates hourly using GitHub Connect.

If the enterprise owner disables the functionality or individual users opt out of the connection, the contribution counts from GitHub Enterprise Server will be deleted on GitHub Enterprise Cloud. If the user reconnects their profiles after disabling them, the contribution counts for the past 90 days are restored.

GitHub Enterprise Server **only** sends the contribution count and source (GitHub Enterprise Server) for connected users. It does not send any information about the contribution or how it was made.

## Enabling unified contributions

Before enabling unified contributions on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, you must enable GitHub Connect. See [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-github-connect-for-ghecom) or [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-github-connect-for-githubcom).

1. Sign in to GitHub Enterprise Server and GitHub Enterprise Cloud.
1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the left sidebar, click **Enterprise{% ifversion ghes %} overview{% endif %}**.
1. At the top of the page, click **(icon: plug) GitHub Connect**.
1. To the right of "Unified contributions", click **Enable**.

   ![Screenshot of the "Unified contributions" option on the GitHub Connect page. The "Enable" button is highlighted with an orange outline.](/assets/images/enterprise/site-admin-settings/dotcom-ghe-connection-request-access.png)
1. [Sign in](https://enterprise.github.com/login) to the GitHub Enterprise Server site to receive further instructions.

When you request access, we may redirect you to the GitHub Enterprise Server site to check your current terms of service.
