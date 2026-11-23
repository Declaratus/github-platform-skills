---
title: Disabling unauthenticated sign-ups
redirect_from:
  - /enterprise/admin/articles/disabling-sign-ups
  - /enterprise/admin/user-management/disabling-unauthenticated-sign-ups
  - /enterprise/admin/authentication/disabling-unauthenticated-sign-ups
  - /admin/authentication/disabling-unauthenticated-sign-ups
  - /enterprise/admin/authentication/authenticating-users-for-your-github-enterprise-server-instance/disabling-unauthenticated-sign-ups
  - /admin/identity-and-access-management/authenticating-users-for-your-github-enterprise-server-instance/disabling-unauthenticated-sign-ups
  - /admin/identity-and-access-management/using-built-in-authentication/disabling-unauthenticated-sign-ups
intro: If you're using built-in authentication for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, you can block unauthenticated people from creating new user accounts on your instance.
permissions: Site administrators can disable unauthenticated sign-ups on a GitHub Enterprise Server instance.
versions:
  ghes: '*'
shortTitle: Block unauthenticated sign-up
contentType: how-tos
category:
  - Configure authentication
---

## About unauthenticated sign-ups

When you use built-in authentication for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, each person creates a personal account from an invitation or by signing up. By default, people who can access your instance while unauthenticated can create a new personal account on your instance. You can disable unauthenticated sign-ups and require an invitation to create a new user account on your instance.

Alternatively, you can configure external authentication for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. If you use external authentication, you must invite people to use your instance through your authentication provider. For more information, see [AUTOTITLE](/admin/concepts/identity-and-access-management/identity-and-access-management-fundamentals#external-authentication).

## Disabling unauthenticated sign-ups

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. In the "Settings" sidebar, click **Privacy** and uncheck **Private mode**.
1. Deselect **Enable sign-up**.
1. Under the "Settings" sidebar, click **Save settings**.

   > [!NOTE]
   > Saving settings in the Management Console restarts system services, which could result in user-visible downtime.

1. Wait for the configuration run to complete.
