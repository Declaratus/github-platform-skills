---
title: Using SAML for enterprise IAM
shortTitle: SAML for enterprise IAM
intro: 'You can centrally manage {% ifversion ghes %}accounts and {% endif %}access to {% ifversion ghes %}{% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}{% elsif ghec %}your enterprise''s resources{% endif %} with SAML single sign-on (SSO){% ifversion ghec %} and System for Cross-domain Identity Management (SCIM){% endif %}.'
versions:
  ghec: '*'
  ghes: '*'
redirect_from:
  - /github/setting-up-and-managing-your-enterprise/configuring-identity-and-access-management-for-your-enterprise-account
  - /admin/authentication/managing-identity-and-access-for-your-enterprise
  - /admin/authentication/configuring-authentication-and-provisioning-with-your-identity-provider
  - /enterprise/admin/articles/configuring-saml-authentication
  - /enterprise/admin/articles/about-saml-authentication
  - /enterprise/admin/user-management/using-saml
  - /enterprise/admin/authentication/using-saml
  - /admin/authentication/using-saml
  - /enterprise/admin/authentication/authenticating-users-for-your-github-enterprise-server-instance/using-saml
  - /admin/identity-and-access-management/authenticating-users-for-your-github-enterprise-server-instance/using-saml
  - /admin/identity-and-access-management/using-saml-for-enterprise-iam
children:
  - /deciding-whether-to-configure-saml-for-your-enterprise-or-your-organizations
  - /configuring-saml-single-sign-on-for-your-enterprise
  - /managing-team-synchronization-for-organizations-in-your-enterprise
  - /configuring-saml-single-sign-on-for-your-enterprise-using-okta
  - /disabling-saml-single-sign-on-for-your-enterprise
  - /enabling-encrypted-assertions
  - /updating-a-users-saml-nameid
  - /switching-your-saml-configuration-from-an-organization-to-an-enterprise-account
  - /troubleshooting-saml-authentication
---

{% ifversion ghec %}

> [!NOTE]
> If your enterprise uses Enterprise Managed Users, you must follow a different process to configure SAML single sign-on. For more information, see [AUTOTITLE](/admin/managing-iam/configuring-authentication-for-enterprise-managed-users/configuring-saml-single-sign-on-for-enterprise-managed-users).

{% endif %}
