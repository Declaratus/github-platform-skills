---
title: Downloading your enterprise account's single sign-on recovery codes
shortTitle: Download recovery codes
intro: To ensure that you can access GitHub if your identity provider (IdP) is unavailable, you should download your enterprise account's single sign-on (SSO) recovery codes.
versions:
  ghec: '*'
redirect_from:
  - /admin/identity-and-access-management/managing-recovery-codes-for-your-enterprise/downloading-your-enterprise-accounts-saml-single-sign-on-recovery-codes
  - /admin/identity-and-access-management/managing-recovery-codes-for-your-enterprise/downloading-your-enterprise-accounts-single-sign-on-recovery-codes
permissions: Enterprise owners can download the SSO recovery codes for the enterprise account.
contentType: how-tos
category:
  - Configure authentication
---

In the event that your IdP is unavailable, you can use a recovery code to sign in and access your enterprise on GitHub. For more information, see [AUTOTITLE](/admin/managing-iam/managing-recovery-codes-for-your-enterprise/accessing-your-enterprise-account-if-your-identity-provider-is-unavailable).

If you did not save your recovery codes when you configured SSO, you can still access the codes from your enterprise's settings.

## Downloading codes for an enterprise with personal accounts

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. Under **(icon: gear) Settings**, click **Authentication security**.

1. Under "Require SAML authentication", click **Save your recovery codes**.

   ![Screenshot of the "Authentication security" screen. The "Save your recovery codes" hyperlink is highlighted with an orange outline.](/assets/images/help/enterprises/saml-recovery-codes-link.png)
1. To save your recovery codes, click **Download**, **Print**, or **Copy**.

## Downloading codes for an enterprise with Enterprise Managed Users

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **Identity provider**.
1. Under **Identity Provider**, click **Single sign-on configuration**.

1. Under either "SAML single sign-on" or "OIDC single sign-on", click **Save your recovery codes**.

1. To save your recovery codes, click **Download**, **Print**, or **Copy**.
