---
title: Identity and access management fundamentals
shortTitle: Fundamentals
intro: 'Administrators must decide how users will access the enterprise''s resources on GitHub.'
versions:
  ghec: '*'
  ghes: '*'
contentType: concepts
redirect_from:
  - /admin/identity-and-access-management/managing-iam-for-your-enterprise/about-authentication-for-your-enterprise
  - /admin/identity-and-access-management/managing-iam-for-your-enterprise/about-identity-and-access-management
  - /admin/identity-and-access-management/understanding-iam-for-enterprises/about-identity-and-access-management
  - /admin/managing-iam/understanding-iam-for-enterprises/about-identity-and-access-management
category:
  - Configure authentication
---

## What is IAM for GitHub?

{% ifversion ghec %}

To control access to your enterprise's resources, you can allow people to use a personal account on GitHub.com and optionally configure additional SAML access restrictions, or you can provision and control the accounts for your enterprise using your identity provider (IdP) with Enterprise Managed Users.

After learning more about authentication and provisioning for each of these options, to determine which method is best for your enterprise, see [AUTOTITLE](/admin/concepts/enterprise-fundamentals/choose-an-enterprise-type).

{% elsif ghes %}

Administrators who configure a GitHub Enterprise Server instance can use local accounts and built-in authentication on the instance. Alternatively, to centralize identity and access for an enterprise's web applications, administrators can configure an external authentication method. If you use SAML, you can optionally provision user accounts on the instance from your identity provider (IdP) using System for Cross-domain Identity Management (SCIM).

{% endif %}

## Which authentication method are available to me?

{% ifversion ghec %}

When you create an enterprise on GitHub, you can decide how people authenticate to access your resources and who controls the user accounts.

* [Authentication through {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}](#authentication-through-githubcom)
* [Authentication through {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} with additional SAML access restriction](#authentication-through-githubcom-with-additional-saml-access-restriction)
* [Authentication with Enterprise Managed Users and federation](#authentication-with-enterprise-managed-users-and-federation)

### Authentication through {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}

With authentication solely through {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, each person you want to grant access to your enterprise must create and manage a personal account on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. After you grant access to your enterprise, the member can access your enterprise's resources after signing into the account on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. The member manages the account, and can contribute to other enterprises, organizations, and repositories on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. For more information about personal accounts, see [AUTOTITLE](/account-and-profile/how-tos/account-management/creating-an-account-on-github).

### Authentication through {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} with additional SAML access restriction

If you configure additional SAML access restriction, each person you want to grant access to your enterprise must create and manage a personal account on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. After you grant access to your enterprise, the member can access your enterprise's resources only after authenticating successfully for both the account on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} and for an account on your SAML identity provider (IdP). The member can contribute to other enterprises, organizations, and repositories on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} using their personal account. For more information about requiring SAML authentication for all access your enterprise's resources, see [AUTOTITLE](/admin/managing-iam/understanding-iam-for-enterprises/about-saml-for-enterprise-iam).

You can choose between configuring SAML at the enterprise level, which applies the same SAML configuration to all organizations within the enterprise, and configuring SAML separately for individual organizations. For more information, see [AUTOTITLE](/admin/managing-iam/using-saml-for-enterprise-iam/deciding-whether-to-configure-saml-for-your-enterprise-or-your-organizations).

### Authentication with Enterprise Managed Users and federation

If you need more control of the accounts for your enterprise members on GitHub, you can use Enterprise Managed Users. With Enterprise Managed Users, you provision and manage accounts for your enterprise members on GitHub using your IdP. Each member signs into an account that you create, and your enterprise manages the account. Contributions outside the enterprise are restricted. For more information, see [AUTOTITLE](/admin/concepts/identity-and-access-management/enterprise-managed-users).

{% elsif ghes %}

The following authentication methods are available for GitHub Enterprise Server.

* [Built-in authentication](#built-in-authentication)
* [External authentication](#external-authentication)

### Built-in authentication

When you use built-in authentication for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, each person creates a personal account from an invitation or by signing up. To access your instance, people authenticate with the credentials for the account. For more information, see [AUTOTITLE](/admin/managing-iam/using-built-in-authentication/configuring-built-in-authentication).

### External authentication

If you use an external directory or identity provider (IdP) to centralize access to multiple web applications, you may be able to configure external authentication for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. For more information, see the following articles.

* [AUTOTITLE](/admin/managing-iam/using-cas-for-enterprise-iam)
* [AUTOTITLE](/admin/managing-iam/using-ldap-for-enterprise-iam)
* [AUTOTITLE](/admin/managing-iam/using-saml-for-enterprise-iam)

> [!NOTE]
> You can use either SAML or LDAP, but not both.

If you choose to use external authentication, you can also configure fallback authentication for people who don't have an account on your external authentication provider. For example, you may want to grant access to a contractor or machine user. For more information, see [AUTOTITLE](/admin/managing-iam/understanding-iam-for-enterprises/allowing-built-in-authentication-for-users-outside-your-provider).

{% endif %}

## How does provisioning work?

{% ifversion ghec %}

If you use [authentication through {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} with additional SAML access restriction](#authentication-through-githubcom-with-additional-saml-access-restriction), people create personal accounts on GitHub.com, and you can grant those personal accounts access to resources in your enterprise. You do not provision accounts.

Alternatively, if you use [Enterprise Managed Users](#authentication-with-enterprise-managed-users-and-federation), you must configure your IdP to provision user accounts within your enterprise on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} using System for Cross-domain Identity Management (SCIM). For more information, see [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim).

{% elsif ghes %}

If you configure built-in authentication, CAS, LDAP, or SAML, GitHub Enterprise Server creates a user account when an authorized person signs into the instance, or "just in time" (JIT). Optionally, if you use SAML, you can provision user accounts from your identity provider (IdP) using SCIM. For more information, see [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/user-provisioning-with-scim-on-ghes).

{% endif %}

{% ifversion emu-public-scim-schema %}

## Which IdPs are supported?

If you choose to create an enterprise that uses personal accounts on GitHub.com, you can configure additional authentication with an external identity management system that adheres to the SAML 2.0 standard. GitHub also officially supports and tests some identity management systems. For more information, see [AUTOTITLE](/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise#supported-identity-providers).

GitHub partners with some developers of identity management systems to provide a "paved-path" integration with {% ifversion ghec %}Enterprise Managed Users{% else %}GitHub Enterprise Server{% endif %}. To simplify your configuration and ensure full support, **use a single partner IdP for both authentication and provisioning.** If you use a partner identity provider (IdP), you can configure one application on your IdP to provide authentication and provisioning. The IdP must support the SAML 2.0 standard. Alternatively, if you use Entra ID (previously known as Azure AD), you can configure OpenID Connect (OIDC) authentication. If you don't use a partner IdP, or if you only use a partner IdP for authentication, you can integrate IdPs that implement the SAML 2.0 and System for Cross-domain Identity Management (SCIM) 2.0 standards. For more information, see [AUTOTITLE](/admin/concepts/identity-and-access-management/enterprise-managed-users).

{% endif %}

## Further reading

* [AUTOTITLE](/admin/concepts/enterprise-fundamentals/enterprise-accounts)
{%- ifversion ghec %}
* [AUTOTITLE](/organizations/managing-membership-in-your-organization/can-i-create-accounts-for-people-in-my-organization)
{%- endif %}
