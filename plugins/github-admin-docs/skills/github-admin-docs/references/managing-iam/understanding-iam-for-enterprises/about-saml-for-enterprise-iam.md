---
title: About SAML for enterprise IAM
shortTitle: About SAML for IAM
intro: You can use SAML single sign-on (SSO) to centrally manage access {% ifversion ghec %}to organizations owned by your enterprise on GitHub.com{% elsif ghes %}to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}{% endif %}.
versions:
  ghec: '*'
  ghes: '*'
redirect_from:
  - /admin/authentication/about-identity-and-access-management-for-your-enterprise
  - /github/setting-up-and-managing-your-enterprise/about-identity-and-access-management-for-your-enterprise-account
  - /github/setting-up-and-managing-your-enterprise/configuring-identity-and-access-management-for-your-enterprise-account/about-identity-and-access-management-for-your-enterprise-account
  - /github/setting-up-and-managing-your-enterprise/about-user-provisioning-for-organizations-in-your-enterprise-account
  - /github/setting-up-and-managing-your-enterprise/configuring-saml-single-sign-on-and-scim-for-your-enterprise-account-using-okta
  - /admin/authentication/managing-identity-and-access-for-your-enterprise/about-identity-and-access-management-for-your-enterprise
  - /admin/identity-and-access-management/managing-iam-for-your-enterprise/about-identity-and-access-management-for-your-enterprise
  - /admin/identity-and-access-management/using-saml-for-enterprise-iam/about-identity-and-access-management-for-your-enterprise
  - /admin/identity-and-access-management/using-saml-for-enterprise-iam/about-saml-for-enterprise-iam
  - /admin/identity-and-access-management/managing-iam-for-your-enterprise/about-saml-for-enterprise-iam
  - /admin/identity-and-access-management/understanding-iam-for-enterprises/about-saml-for-enterprise-iam
contentType: concepts
category:
  - Configure authentication
---

## About SAML SSO for your enterprise

{% ifversion ghec %}

If your enterprise members manage their own user accounts on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, you can configure SAML authentication as an additional access restriction for your enterprise or organization. Single sign-on (SSO) gives organization owners and enterprise owners a way to control and secure access to organization resources like repositories, issues, and pull requests.

If you configure SAML SSO, members of your organization will continue to sign into their personal accounts on GitHub.com. When a member accesses most resources within your organization, GitHub redirects the member to your IdP to authenticate. After successful authentication, your IdP redirects the member back to GitHub. For more information, see [AUTOTITLE](/enterprise-cloud@latest/authentication/authenticating-with-single-sign-on/about-authentication-with-single-sign-on).

> [!NOTE]
> SAML SSO does not replace the normal sign-in process for GitHub. Unless you use Enterprise Managed Users, members will continue to sign into their personal accounts on GitHub.com, and each personal account will be linked to an external identity in your IdP.

Enterprise owners can enable SAML SSO and centralized authentication through a SAML IdP across all organizations owned by an enterprise account. After you enable SAML SSO for your enterprise account, SAML SSO is enforced as a requirement for all enterprise members and all organizations owned by your enterprise account. All members will be required to authenticate using SAML SSO to gain access to the organizations where they are a member, and enterprise owners will be required to authenticate using SAML SSO when accessing an enterprise account. For more information, see [AUTOTITLE](/admin/concepts/identity-and-access-management/identity-and-access-management-fundamentals) and [AUTOTITLE](/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise).

Alternatively, you can provision and manage the accounts of your enterprise members with Enterprise Managed Users. To help you determine whether SAML SSO or Enterprise Managed Users is better for your enterprise, see [AUTOTITLE](/admin/concepts/enterprise-fundamentals/choose-an-enterprise-type).

If a SAML configuration error or an issue with your identity provider (IdP) prevents you from using SAML SSO, you can use a recovery code to access your enterprise. For more information, see [AUTOTITLE](/admin/managing-iam/managing-recovery-codes-for-your-enterprise).

After you enable SAML SSO, depending on the IdP you use, you may be able to enable additional identity and access management features.

{% ifversion ghec %}

> [!NOTE]
> You cannot configure SCIM for your enterprise account unless your account was created for Enterprise Managed Users. For more information, see [AUTOTITLE](/admin/concepts/identity-and-access-management/enterprise-managed-users).
>
> If you do not use Enterprise Managed Users, and you want to use SCIM provisioning, you must configure SAML SSO at the organization level, not the enterprise level. For more information, see [AUTOTITLE](/organizations/managing-saml-single-sign-on-for-your-organization/about-identity-and-access-management-with-saml-single-sign-on).

{% endif %}

If you use Microsoft Entra ID (previously known as Azure AD) as your IdP, you can use team synchronization to manage team membership within each organization. If team sync is enabled for your organization or enterprise account, you can synchronize a GitHub team with an IdP group. When you do this, membership changes to the IdP group are reflected on GitHub automatically, reducing the need for manual updates and custom scripts. For more information, see [AUTOTITLE](/admin/managing-iam/using-saml-for-enterprise-iam/managing-team-synchronization-for-organizations-in-your-enterprise).

There are special considerations when enabling SAML SSO for your enterprise account if any of the organizations owned by the enterprise account are already configured to use SAML SSO. For more information, see [AUTOTITLE](/admin/managing-iam/using-saml-for-enterprise-iam/switching-your-saml-configuration-from-an-organization-to-an-enterprise-account).

{% elsif ghes %}

SAML SSO allows people to authenticate and access {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} through an external system for identity management.

SAML is an XML-based standard for authentication and authorization. When you configure SAML for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, the external system for authentication is called an identity provider (IdP). Your instance acts as a SAML service provider (SP). For more information about the SAML standard, see [Security Assertion Markup Language](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language) on Wikipedia.

> [!NOTE]
> You can use either SAML or LDAP, but not both.

{% endif %}

{% ifversion ghes %}

When using SAML or CAS, two-factor authentication is not supported or managed on the GitHub Enterprise Server instance, but may be supported by the external authentication provider. Two-factor authentication enforcement on organizations is not available. For more information about enforcing two-factor authentication on organizations, see [AUTOTITLE](/organizations/keeping-your-organization-secure/managing-two-factor-authentication-for-your-organization/requiring-two-factor-authentication-in-your-organization).

After you configure SAML, people who use {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} must use a personal access token to authenticate API requests. For more information, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

If you want to allow authentication for some people who don't have an account on your external authentication provider, you can allow fallback authentication to local accounts on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. For more information, see [AUTOTITLE](/admin/managing-iam/understanding-iam-for-enterprises/allowing-built-in-authentication-for-users-outside-your-provider).

{% endif %}

For more information about the configuration of SAML SSO on GitHub, see [AUTOTITLE](/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise).

{% ifversion ghes %}

## About creation of user accounts

By default, your IdP does not communicate with GitHub automatically when you assign or unassign the application. GitHub {% ifversion fpt or ghec %}provisions access to your resources on {% else %}creates a user account {% endif %}using SAML Just-in-Time (JIT) provisioning the first time someone navigates to {% ifversion fpt or ghec %}your enterprise's resources on GitHub{% else %}your GitHub Enterprise Server instance{% endif %} and signs in by authenticating through your IdP. You may need to manually notify users when you grant access to GitHub, and you must manually {% ifversion fpt or ghec %}deprovision access {% else %}deactivate the user account on {% endif %}GitHub during offboarding.

Alternatively, instead of SAML JIT provisioning, you can use SCIM to {% ifversion ghec %}provision or deprovision{% elsif ghes %}create or suspend{% endif %} {% ifversion fpt or ghec %}access to organizations owned by your enterprise on GitHub {% else %}user accounts and grant or deny access to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} {% endif %}automatically after you assign or unassign the application on your IdP.{% ifversion ghes %} SCIM for GitHub Enterprise Server is currently in {% ifversion scim-for-ghes-public-beta %}public{% else %}private{% endif %} public preview and is subject to change.{% endif %} For more information, see [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/user-provisioning-with-scim-on-ghes).

{% ifversion ghes %}

With JIT provisioning, if you remove a user from your IdP, you must also manually suspend the user's account on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. Otherwise, the account's owner can continue to authenticate using access tokens or SSH keys. For more information, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/suspending-and-unsuspending-users).

{% endif %}

{% endif %}

## Supported IdPs

{% ifversion ghec %}

We test and officially support the following IdPs. For SAML SSO, we offer limited support for all identity providers that implement the SAML 2.0 standard. For more information, see the [SAML Wiki](https://wiki.oasis-open.org/security) on the OASIS website.

IdP | SAML | Team synchronization |
--- | :--: | :-------: |
Active Directory Federation Services (AD FS) | (icon: check) | (icon: x) |
Entra ID | (icon: check) | (icon: check) |
Okta | (icon: check) | (icon: x) |
OneLogin | (icon: check) | (icon: x) |
PingOne | (icon: check) | (icon: x) |
Shibboleth | (icon: check) | (icon: x) |

{% elsif ghes %}

GitHub supports SAML SSO with IdPs that implement the SAML 2.0 standard. For more information, see the [SAML Wiki](https://wiki.oasis-open.org/security) on the OASIS website.

GitHub officially supports and internally tests the following IdPs for SAML.{% ifversion ghes %} For more information about the IdPs that are supported for SCIM on GitHub Enterprise Server, see [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/user-provisioning-with-scim-on-ghes#supported-identity-providers).{% endif %}

* Microsoft Active Directory Federation Services (AD FS)
* Microsoft Entra ID (previously known as Azure AD)
* Okta
* OneLogin
* PingOne
* Shibboleth

If your IdP supports encrypted assertions, you can configure encrypted assertions on GitHub Enterprise Server for increased security during the authentication process.

GitHub does not support SAML Single Logout. To terminate an active SAML session, users should log out directly on your SAML IdP.

{% endif %}

## Further reading

* [AUTOTITLE](/admin/managing-iam/using-saml-for-enterprise-iam)
* [SAML Wiki](https://wiki.oasis-open.org/security) on the OASIS website
* [System for Cross-domain Identity Management: Protocol (RFC 7644)](https://tools.ietf.org/html/rfc7644) on the IETF website
