---
title: Inviting people to use your instance
intro: When you use built-in authentication for GitHub Enterprise Server, you can invite people by email address to create a user account on your instance.
versions:
  ghes: '*'
permissions: Enterprise owners can invite people to create a user account on a GitHub Enterprise Server instance.
shortTitle: Invite people
redirect_from:
  - /admin/identity-and-access-management/using-built-in-authentication/inviting-people-to-use-your-instance
contentType: how-tos
category:
  - Configure authentication
---

## About invitations for new users

When you use built-in authentication for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, each person creates a personal account from an invitation or by signing up. By default, people who can access your instance while unauthenticated can create a new personal account on your instance.

You can disable unauthenticated sign-ups and require an invitation to create a new user account on your instance. For more information, see [AUTOTITLE](/admin/managing-iam/using-built-in-authentication/disabling-unauthenticated-sign-ups).

Alternatively, you can configure external authentication for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. If you use external authentication, you must invite people to use your instance through your authentication provider. For more information, see [AUTOTITLE](/admin/concepts/identity-and-access-management/identity-and-access-management-fundamentals#external-authentication).

## Inviting people to create a user account

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the left sidebar, click **Invite user**.
1. Type the username and email address for each of the user accounts that you'd like to create, then click **Generate a password reset link**.

If you've configured email for notifications on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, your instance will send the invitation to the provided email address. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-user-applications-for-your-enterprise/configuring-email-for-notifications).
