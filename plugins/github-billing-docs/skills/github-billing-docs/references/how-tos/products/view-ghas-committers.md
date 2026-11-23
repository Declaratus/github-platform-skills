---
title: Viewing committer information for Advanced Security licenses
intro: 'You can view information about the GitHub Secret Protection and GitHub Code Security committers for your enterprise and calculate the cost for additional committers with the site admin dashboard.'
permissions: Site administrators
product: "GitHub Code Security and GitHub Secret Protection are available for {% ifversion fpt or ghec %}accounts on GitHub Team and GitHub Enterprise Cloud{% elsif ghes %}accounts on GitHub Enterprise Server{% endif %}.\n\n{% ifversion fpt or ghec %} Some features are also available for free for public repositories on GitHub.com.{% endif %} For more information, see [AUTOTITLE](/get-started/learning-about-github/githubs-plans).\n\nFor information about GitHub Advanced Security for Azure DevOps, see [Configure GitHub Advanced Security for Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features) in Microsoft Learn."
versions:
  ghes: '*'
redirect_from:
  - /billing/managing-billing-for-github-advanced-security/viewing-committer-information-for-github-advanced-security
  - /billing/managing-billing-for-your-products/managing-billing-for-github-advanced-security/viewing-committer-information-for-github-advanced-security
shortTitle: View GHAS committers
contentType: how-tos
category:
  - Manage your plan and licenses
---

## About the "Advanced Security Committers" dashboard

You can estimate the number of licenses your enterprise might need for GitHub Secret Protection and GitHub Code Security with the "Advanced Security Committers" section of the site admin dashboard.

If you currently use Secret Protection or Code Security, this tool helps you understand how many committers are currently using licenses. It also helps you estimate how many additional licenses would be used if you enable Secret Protection or Code Security for more organizations and repositories.

If you're considering using Secret Protection or Code Security, you can use this tool to estimate potential costs to enable Secret Protection or Code Security.

For more information about billing for Advanced Security, see [AUTOTITLE](/billing/concepts/product-billing/github-advanced-security).

## Viewing committer information

1. In the upper-right corner of any page, click (icon: rocket) to display the "Site admin" pages.
1. In the left sidebar, click **Advanced Security Committers**. If this option is not displayed, at the top of the page, click (icon: rocket) **Site admin** to show the top-level "Site admin" page.

The page shows the number of licenses currently being used and the number of licenses you would use if you enabled Advanced Security for all repositories.

## Calculating the cost to add committers

Under "Calculate Additional Advanced Licenses", you can calculate how many more new or additional licenses will be used if you enable Secret Protection or Code Security for specific organizations and repositories.

1. In the upper-right corner of any page, click (icon: rocket) to display the "Site admin" pages.
1. In the left sidebar, click **Advanced Security Committers**. If this option is not displayed, at the top of the page, click (icon: rocket) **Site admin** to show the top-level "Site admin" page.
1. Under "Organizations and Repositories", enter or paste a list of organizations and repositories, with one organization or repository per line. For example:

   ```text
   example-org
   octo-org/octo-repo
   ```

1. Click **Recalculate**.
