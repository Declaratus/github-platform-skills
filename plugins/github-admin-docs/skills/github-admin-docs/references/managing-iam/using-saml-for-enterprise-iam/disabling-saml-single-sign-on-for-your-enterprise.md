---
title: Disabling SAML single sign-on for your enterprise
intro: You can disable SAML single sign-on (SSO) for your enterprise account.
versions:
  ghec: '*'
shortTitle: Disable SAML SSO
redirect_from:
  - /admin/identity-and-access-management/using-saml-for-enterprise-iam/disabling-saml-single-sign-on-for-your-enterprise
contentType: how-tos
category:
  - Configure authentication
---

## About disabled SAML SSO for your enterprise

After you disable SAML SSO for your enterprise, the following effects apply:

* All external identities for your enterprise will be removed. For more information, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/viewing-and-managing-a-users-saml-access-to-your-enterprise).
* Any SAML settings configured for individual organizations within the enterprise will take effect. For more information, see [AUTOTITLE](/organizations/managing-saml-single-sign-on-for-your-organization/enabling-and-testing-saml-single-sign-on-for-your-organization).

Disabling SAML SSO does not delete members' credentials. Their personal access tokens, SSH keys, and existing authorizations for OAuth apps and GitHub Apps remain valid, and their SSO authorizations are not revoked. If you enable SAML SSO again, members link their identity again the next time they sign in, but do not need to authorize their existing tokens and SSH keys again.

## Disabling SAML

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}

   > [!NOTE]
   > If you're unable to access the enterprise because your IdP is unavailable, you can use a recovery code to bypass SSO. For more information, see [AUTOTITLE](/admin/managing-iam/managing-recovery-codes-for-your-enterprise/accessing-your-enterprise-account-if-your-identity-provider-is-unavailable).

1. At the top of the page, click (icon: gear) **Settings**.
1. Under **(icon: gear) Settings**, click **Authentication security**.

1. Under "SAML single sign-on", deselect **Require SAML authentication**.
1. Click **Save**.

## Further reading

* [AUTOTITLE](/admin/managing-iam/configuring-authentication-for-enterprise-managed-users/disabling-authentication-and-provisioning-for-enterprise-managed-users)
