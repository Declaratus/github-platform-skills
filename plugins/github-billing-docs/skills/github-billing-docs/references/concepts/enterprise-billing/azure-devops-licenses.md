---
title: Combined use of GitHub Enterprise and Azure DevOps
intro: 'GitHub Enterprise Cloud customers who manage users with Entra ID can access Azure DevOps without additional cost.'
versions:
  fpt: '*'
  ghec: '*'
product: Enterprise accounts using Microsoft Entra ID as their identity provider, see [AUTOTITLE](/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim/configuring-scim-provisioning-for-users)
shortTitle: Azure DevOps licenses
contentType: concepts
category:
  - Manage enterprise licenses
---

GitHub Enterprise Cloud customers can use Azure DevOps without additional costs per user. For customers using Microsoft Entra, users can sign in with the same credentials on GitHub and Azure DevOps.

No additional setup is required for enterprises hosted on GitHub.com. GitHub Enterprise users are detected automatically when they sign in to Azure DevOps. See [User and permissions management](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/faq-user-and-permissions-management?view=azure-devops#github-enterprise) in the Microsoft Learn documentation.

GitHub Enterprise Cloud with data residency administrators need to link their instance of GHE.com to Azure DevOps before GitHub Enterprise users can be detected. See [How are GitHub Enterprise users in data residency regions identified?](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/faq-user-and-permissions-management?view=azure-devops#q--how-are-github-enterprise-users-in-data-residency-regions-identified-) in the Microsoft Learn documentation.
