---
title: Configuring built-in authentication
intro: When you use the default authentication method, all authentication details are stored on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.
permissions: Site administrators can configure authentication for a GitHub Enterprise Server instance.
redirect_from:
  - /enterprise/admin/user-management/using-built-in-authentication
  - /enterprise/admin/authentication/using-built-in-authentication
  - /admin/authentication/using-built-in-authentication
  - /enterprise/admin/authentication/authenticating-users-for-your-github-enterprise-server-instance/using-built-in-authentication
  - /admin/identity-and-access-management/authenticating-users-for-your-github-enterprise-server-instance/using-built-in-authentication
  - /admin/identity-and-access-management/using-built-in-authentication/configuring-built-in-authentication
versions:
  ghes: '*'
shortTitle: Configure built-in authentication
contentType: how-tos
category:
  - Configure authentication
---

## About built-in authentication

By default, GitHub Enterprise Server uses built-in authentication. Each person creates a user account on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} from an invitation or by signing up, and then authenticates with the credentials for the account to access your instance. Your GitHub Enterprise Server instance stores the authentication information for the account.

By default, users can use passkeys for built-in authentication, but you can disable passkeys for your instance. See [AUTOTITLE](/admin/managing-iam/using-built-in-authentication/disabling-passkeys-for-your-instance).

You can prevent unauthenticated people from creating new user accounts on your instance. For more information, see [AUTOTITLE](/admin/managing-iam/using-built-in-authentication/disabling-unauthenticated-sign-ups).

Alternatively, you can configure external authentication for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. If you use external authentication, you must invite people to use your instance through your authentication provider. For more information, see [AUTOTITLE](/admin/concepts/identity-and-access-management/identity-and-access-management-fundamentals#external-authentication).

## Configuring built-in authentication

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. In the "Settings" sidebar, click **Authentication**.
1. Under "Authentication," select **Built in authentication**.
### Two-factor authentication
When using LDAP or built-in authentication, two-factor authentication is supported. Organization owners can require members to have two-factor authentication enabled.

## Creating your account

Once your instance has been created, you'll need to create your own admin account.

1. On the "Create Admin Account" page at `http(s)://[hostname]/join`, type your username, password, and email address, then click **Create an account**.
1. Sign in to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} at `http(s)://HOSTNAME/login`.

## Next steps

<a name="inviting-users"></a>

After you configure built-in authentication and create your administrative account, you can invite people to create accounts and use your instance. For more information, see [AUTOTITLE](/admin/managing-iam/using-built-in-authentication/inviting-people-to-use-your-instance).

## Further reading

* [AUTOTITLE](/admin/configuring-settings/configuring-user-applications-for-your-enterprise/configuring-email-for-notifications)
