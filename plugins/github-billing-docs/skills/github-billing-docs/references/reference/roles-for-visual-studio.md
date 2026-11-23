---
title: Roles for Visual Studio subscriptions with GitHub Enterprise reference
shortTitle: Roles for Visual Studio
intro: 'Learn about the different roles required to set up Visual Studio subscriptions with GitHub Enterprise.'
versions:
  ghec: '*'
  ghes: '*'
permissions: '{% ifversion fpt %}Organization owners, billing managers, and personal account users {% elsif ghec %}Enterprise owners, organization owners, and billing managers {% endif %}'
product: 'The new billing platform is now available to all users.'
contentType: reference
category:
  - Manage enterprise licenses
---

Visual Studio subscriptions with GitHub Enterprise is a combined offering and knowledge of roles in both systems is useful.

## Visual Studio roles

| Role | Description | More information |
| :- | :- | :- |
| **Subscriptions admin** | Person who assigns licenses for Visual Studio subscription | [Overview of admin responsibilities](https://docs.microsoft.com/en-us/visualstudio/subscriptions/admin-responsibilities) in Microsoft Docs |
| **Subscriber** | Person who uses a license for Visual Studio subscription | [Visual Studio Subscriptions documentation](https://docs.microsoft.com/en-us/visualstudio/subscriptions/) in Microsoft Docs |

## GitHub roles

| Role | Description | More information |
| :- | :- | :- |
| **Enterprise owner** | Person who has a personal account that's an administrator of an enterprise on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} | [AUTOTITLE](/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-roles-in-your-enterprise/abilities-of-roles#enterprise-owners){% ifversion ghes %} in the GitHub Enterprise Cloud documentation.{% else %}.{% endif %} |
| **Organization owner** | Person who has a personal account that's an owner of an organization in your team's enterprise on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} | [AUTOTITLE](/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#organization-owners){% ifversion ghes %} in the GitHub Enterprise Cloud documentation.{% else %}.{% endif %} |
| **Enterprise member** | Person who has a personal account that's a member of an enterprise on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} | [AUTOTITLE](/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-roles-in-your-enterprise/abilities-of-roles#users)  |
