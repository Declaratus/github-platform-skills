---
title: Configuring SAML single sign-on for your enterprise
shortTitle: Configure SAML SSO
intro: You can control and secure access to {% ifversion ghec %}resources like repositories, issues, and pull requests within your enterprise's organizations{% elsif ghes %}{% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}{% endif %} by {% ifversion ghec %}enforcing{% elsif ghes %}configuring{% endif %} SAML single sign-on (SSO) through your identity provider (IdP).
permissions: '{% ifversion ghes %}Site administrators{% elsif ghec %}Enterprise owners{% endif %} can configure SAML SSO for {% ifversion ghec %}an enterprise on GitHub{% elsif ghes %}a GitHub Enterprise Server instance{% endif %}.'
versions:
  ghec: '*'
  ghes: '*'
redirect_from:
  - /admin/authentication/configuring-saml-single-sign-on-for-your-enterprise
  - /github/setting-up-and-managing-your-enterprise/enabling-saml-single-sign-on-for-organizations-in-your-enterprise-account
  - /github/setting-up-and-managing-your-enterprise/configuring-identity-and-access-management-for-your-enterprise-account/enabling-saml-single-sign-on-for-organizations-in-your-enterprise-account
  - /github/setting-up-and-managing-your-enterprise/configuring-identity-and-access-management-for-your-enterprise-account/enforcing-saml-single-sign-on-for-organizations-in-your-enterprise-account
  - /admin/authentication/managing-identity-and-access-for-your-enterprise/configuring-saml-single-sign-on-for-your-enterprise
  - /admin/identity-and-access-management/managing-iam-for-your-enterprise/configuring-saml-single-sign-on-for-your-enterprise
  - /admin/identity-and-access-management/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise
contentType: how-tos
category:
  - Configure authentication
---

{% ifversion ghec %}

**Before** following the steps in this article, make sure that your enterprise uses **personal accounts**. You can do so by checking whether your enterprise view has the "Users managed by ACCOUNT NAME" header bar at the top of the screen.

If you see this, your enterprise uses **managed users** and you must follow a different process to configure SAML single sign-on. See [AUTOTITLE](/admin/managing-iam/configuring-authentication-for-enterprise-managed-users/configuring-saml-single-sign-on-for-enterprise-managed-users).

{% endif %}

## About SAML SSO

{% ifversion ghec %}

Single sign-on (SSO) gives organization owners and enterprise owners a way to control and secure access to organization resources like repositories, issues, and pull requests.

If you configure SAML SSO, members of your organization will continue to sign into their personal accounts on GitHub.com. When a member accesses most resources within your organization, GitHub redirects the member to your IdP to authenticate. After successful authentication, your IdP redirects the member back to GitHub. For more information, see [AUTOTITLE](/enterprise-cloud@latest/authentication/authenticating-with-single-sign-on/about-authentication-with-single-sign-on).

> [!NOTE]
> SAML SSO does not replace the normal sign-in process for GitHub. Unless you use Enterprise Managed Users, members will continue to sign into their personal accounts on GitHub.com, and each personal account will be linked to an external identity in your IdP.

For more information, see [AUTOTITLE](/organizations/managing-saml-single-sign-on-for-your-organization/about-identity-and-access-management-with-saml-single-sign-on).

Enterprise owners can enable SAML SSO and centralized authentication through a SAML IdP across all organizations owned by an enterprise account. After you enable SAML SSO for your enterprise account, SAML SSO is enforced as a requirement for all enterprise members and all organizations owned by your enterprise account. All members will be required to authenticate using SAML SSO to gain access to the organizations where they are a member, and enterprise owners will be required to authenticate using SAML SSO when accessing an enterprise account.

To access each organization's resources on GitHub, the member must have an active SAML session in their browser.{% ifversion ghec %} To access each organization's protected resources using the API and Git, the member must use a personal access token or SSH key that the member has authorized for use with the organization.{% endif %} Enterprise owners can view and revoke a member's {% ifversion ghec %}linked identity, active sessions, or authorized credentials{% else %}active SAML sessions{% endif %} at any time.

{% ifversion ghes %}
>[!NOTE]
> This view is only enabled when SAML with SCIM is enabled.
{% endif %} For more information, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/viewing-and-managing-a-users-saml-access-to-your-enterprise).

{% ifversion ghec %}

> [!NOTE]
> You cannot configure SCIM for your enterprise account unless your account was created for Enterprise Managed Users. For more information, see [AUTOTITLE](/admin/concepts/identity-and-access-management/enterprise-managed-users).
>
> If you do not use Enterprise Managed Users, and you want to use SCIM provisioning, you must configure SAML SSO at the organization level, not the enterprise level. For more information, see [AUTOTITLE](/organizations/managing-saml-single-sign-on-for-your-organization/about-identity-and-access-management-with-saml-single-sign-on).

{% endif %}

When SAML SSO is disabled, all linked external identities are removed from GitHub.

After you enable SAML SSO, OAuth app and GitHub App authorizations may need to be revoked and reauthorized before they can access the organization. For more information, see [AUTOTITLE](/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps#oauth-apps-and-organizations).

{% elsif ghes %}

SAML SSO allows you to centrally control and secure access to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} from your SAML IdP.

If an unauthenticated user attempts to sign in to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} and you have disabled [built-in authentication](/admin/managing-iam/understanding-iam-for-enterprises/allowing-built-in-authentication-for-users-outside-your-provider), GitHub redirects the user to your SAML IdP for authentication. After the user successfully authenticates with an account on the IdP, the IdP redirects the user back to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. GitHub validates the response from your IdP, then grants access to the user. The user's SAML session is active in the browser for 24 hours. After that, the user must authenticate again with your IdP.

{% ifversion ghes %}

With JIT provisioning, if you remove a user from your IdP, you must also manually suspend the user's account on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. Otherwise, the account's owner can continue to authenticate using access tokens or SSH keys. For more information, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/suspending-and-unsuspending-users).

{% endif %}

{% endif %}

## Supported identity providers

GitHub supports SAML SSO with IdPs that implement the SAML 2.0 standard. For more information, see the [SAML Wiki](https://wiki.oasis-open.org/security) on the OASIS website.

GitHub officially supports and internally tests the following IdPs for SAML.{% ifversion ghes %} For more information about the IdPs that are supported for SCIM on GitHub Enterprise Server, see [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/user-provisioning-with-scim-on-ghes#supported-identity-providers).{% endif %}

* Microsoft Active Directory Federation Services (AD FS)
* Microsoft Entra ID (previously known as Azure AD)
* Okta
* OneLogin
* PingOne
* Shibboleth

{% ifversion ghec %}

For more information about connecting Microsoft Entra ID (previously known as Azure AD) to your enterprise, see [Tutorial: Microsoft Entra SSO integration with GitHub Enterprise Cloud - Enterprise Account](https://learn.microsoft.com/en-us/entra/identity/saas-apps/github-enterprise-cloud-enterprise-account-tutorial) in Microsoft Docs.

> [!NOTE] GitHub does not test or validate identity provider (IdP) gallery applications for use in Government Cloud environments, including Microsoft Entra ID Government Cloud and Okta Government Cloud. Authentication and SCIM provisioning issues that involve gallery applications in these environments fall outside GitHub's [scope of support](/support/learning-about-github-support/about-github-support#scope-of-support).

{% elsif ghes %}

For more information about connecting Entra ID to your enterprise, see [Tutorial: Microsoft Entra SSO integration with GitHub Enterprise Server](https://learn.microsoft.com/en-us/entra/identity/saas-apps/github-ae-tutorial) in Microsoft Docs.

> [!NOTE] GitHub does not test or validate identity provider (IdP) gallery applications for use in Government Cloud environments, including Microsoft Entra ID Government Cloud and Okta Government Cloud. Authentication and SCIM provisioning issues that involve gallery applications in these environments fall outside GitHub's [scope of support](/support/learning-about-github-support/about-github-support#scope-of-support).

## Username considerations with SAML

GitHub normalizes a value from your {% ifversion ghec %}IdP{% elsif ghes %}external authentication provider{% endif %} to determine the username for each new personal account {% ifversion ghec %}in your enterprise on GitHub{% elsif ghes %}on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}{% endif %}. For more information, see [AUTOTITLE](/admin/managing-iam/iam-configuration-reference/username-considerations-for-external-authentication).

{% endif %}

{% ifversion ghec %}

## Enforcing SAML single-sign on for organizations in your enterprise account

When you enforce SAML SSO for your enterprise, the enterprise configuration will override any existing organization-level SAML configurations. There are special considerations when enabling SAML SSO for your enterprise account if any of the organizations owned by the enterprise account are already configured to use SAML SSO. For more information, see [AUTOTITLE](/admin/managing-iam/using-saml-for-enterprise-iam/switching-your-saml-configuration-from-an-organization-to-an-enterprise-account).

When you enforce SAML SSO for an organization, GitHub removes any members of the organization that have not authenticated successfully with your SAML IdP. When you require SAML SSO for your enterprise, GitHub does not remove members of the enterprise that have not authenticated successfully with your SAML IdP. The next time a member accesses the enterprise's resources, the member must authenticate with your SAML IdP.

For more detailed information about how to enable SAML using Okta, see [AUTOTITLE](/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise-using-okta).

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. Under **(icon: gear) Settings**, click **Authentication security**.

1. Optionally, to view the current configuration for all organizations in the enterprise account before you change the setting, click **(icon: eye) View your organizations' current configurations**.
   
      ![Screenshot of a policy in the enterprise settings. A link, labeled "View your organizations' current configurations", is outlined.](/assets/images/help/business-accounts/view-current-policy-implementation-link.png)
1. Under "SAML single sign-on", select **Require SAML authentication**.
1. In the **Sign on URL** field, type the HTTPS endpoint of your IdP for single sign-on requests. This value is available in your IdP configuration.
1. Optionally, in the **Issuer** field, type your SAML issuer URL to verify the authenticity of sent messages.
1. Under **Public Certificate**, paste a certificate to verify SAML responses. This is the public key corresponding to the private key used to sign SAML responses.

   > [!NOTE]
   > GitHub does not enforce the expiration of this SAML IdP certificate. This means that even if this certificate expires, your SAML authentication will continue to work. However, if your IdP administrator regenerates the SAML certificate, and you don't update it on the GitHub side, users will encounter a `digest mismatch` error during SAML authentication attempts due to the certificate mismatch. See [Error: Digest mismatch](/admin/managing-iam/using-saml-for-enterprise-iam/troubleshooting-saml-authentication#error-digest-mismatch).

   To find the certificate, refer to the documentation for your IdP. Some IdPs call this an X.509 certificate.

1. Under your public certificate, to the right of the current signature and digest methods, click (icon: pencil).

   ![Screenshot of the current signature method and digest method in the SAML settings. The pencil icon is highlighted with an orange outline.](/assets/images/help/saml/edit-signature-digest-method.png)
1. Select the **Signature Method** and **Digest Method** dropdown menus, then click the hashing algorithm used by your SAML issuer.

1. Before enabling SAML SSO for your enterprise, to ensure that the information you've entered is correct, click **Test SAML configuration** . This test uses Service Provider initiated (SP-initiated) authentication and must be successful before you can save the SAML settings.
1. Click **Save**.
1. To ensure you can still access your enterprise on GitHub if your IdP is unavailable in the future, click **Download**, **Print**, or **Copy** to save your recovery codes. For more information, see [AUTOTITLE](/admin/managing-iam/managing-recovery-codes-for-your-enterprise/downloading-your-enterprise-accounts-single-sign-on-recovery-codes).

{% elsif ghes %}

## Configuring SAML SSO

You can enable or disable SAML authentication for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, or you can edit an existing configuration. You can view and edit authentication settings in the Management Console. For more information, see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-web-ui).

> [!NOTE]
> GitHub strongly recommends that you verify any new configuration for authentication in a staging environment. An incorrect configuration could result in downtime for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. For more information, see [AUTOTITLE](/admin/installing-your-enterprise-server/setting-up-a-github-enterprise-server-instance/setting-up-a-staging-instance).

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. In the "Settings" sidebar, click **Authentication**.

1. Under "Authentication", select **SAML**.
1. Optionally, to allow people without an account on your external authentication system to sign in with built-in authentication, select **Allow built-in authentication**. For more information, see [AUTOTITLE](/admin/managing-iam/understanding-iam-for-enterprises/allowing-built-in-authentication-for-users-outside-your-provider).
1. Optionally, to enable unsolicited response SSO, select **IdP initiated SSO**. By default, GitHub Enterprise Server will reply to an unsolicited Identity Provider (IdP) initiated request with an `AuthnRequest` back to the IdP.

   > [!TIP]
   > We recommend keeping this value **unselected**. You should enable this feature **only** in the rare instance that your SAML implementation does not support service provider initiated SSO, and when advised by GitHub Enterprise Support.

1. Optionally, if you do not want your SAML provider to determine administrator rights for users on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, select **Disable administrator demotion/promotion**
1. Optionally, to allow {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to receive encrypted assertions from your SAML IdP, select **Require encrypted assertions**.

   You must ensure that your IdP supports encrypted assertions and that the encryption and key transport methods in the management console match the values configured on your IdP. You must also provide {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}'s public certificate to your IdP. For more information, see [AUTOTITLE](/admin/managing-iam/using-saml-for-enterprise-iam/enabling-encrypted-assertions).

1. In the **Single sign-on URL** field, type the HTTP or HTTPS endpoint on your IdP for single sign-on requests. This value is provided by your IdP configuration. If the host is only available from your internal network, you may need to [configure {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to use internal nameservers](/admin/configuring-settings/configuring-network-settings/configuring-dns-nameservers).
1. Optionally, in the **Issuer** field, type your SAML issuer's name. This verifies the authenticity of messages sent to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.
1. Select the **Signature Method** and **Digest Method** dropdown menus, then click the hashing algorithm used by your SAML issuer to verify the integrity of the requests from {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.
1. Select the **Name Identifier Format** dropdown menu, then click a format.
1. Under "Verification certificate", click **Choose File**, then choose a certificate to validate SAML responses from the IdP.

   > [!NOTE]
   > GitHub does not enforce the expiration of this SAML IdP certificate. This means that even if this certificate expires, your SAML authentication will continue to work. However, if your IdP administrator regenerates the SAML certificate, and you don't update it on the GitHub side, users will encounter a `digest mismatch` error during SAML authentication attempts due to the certificate mismatch. See [Error: Digest mismatch](/admin/managing-iam/using-saml-for-enterprise-iam/troubleshooting-saml-authentication#error-digest-mismatch).

1. Under "User attributes", modify the SAML attribute names to match your IdP if needed, or accept the default names.

{% endif %}

{% ifversion proof-of-presence %}

## Enabling Proof of Presence

After you configure SAML SSO, your enterprise can use Proof of Presence to require reauthentication through your IdP before high-impact actions. During public preview, Proof of Presence supports **Microsoft Entra ID**. For more information, see [AUTOTITLE](/admin/configuring-settings/hardening-security-for-your-enterprise/configuring-proof-of-presence).

{% endif %}

## Further reading

{%- ifversion ghec %}

* [AUTOTITLE](/organizations/managing-saml-single-sign-on-for-your-organization)
{%- endif %}
{%- ifversion ghes %}
* [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/promoting-or-demoting-a-site-administrator)
{% ifversion scim-for-ghes-public-beta %}* [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/configuring-scim-provisioning-for-users){% endif %}
{%- endif %}
