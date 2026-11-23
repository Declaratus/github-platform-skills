---
title: Configuring Proof of Presence
shortTitle: Proof of Presence
intro: 'Reduce the risk from compromised sessions by requiring people to reauthenticate with your identity provider before they perform high-impact actions in your enterprise.'
product: 'Enterprise accounts on GitHub Enterprise Cloud'
versions:
  feature: proof-of-presence
contentType: concepts
---

> [!NOTE]
> This feature is in public preview and is subject to change.

## About Proof of Presence

Proof of Presence (PoP) adds an identity-provider challenge to sudo mode for enterprises. When a member attempts a protected high-impact action, GitHub requires the member to reauthenticate through the enterprise's configured identity provider (IdP) before the action can proceed.

PoP uses the same session and timeout model as sudo mode, and the same protected actions that trigger sudo mode will trigger a PoP challenge. After a member successfully reauthenticates, the member can perform protected actions until the sudo-mode session expires. See [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/sudo-mode).

PoP can help you reduce the impact of a compromised session and meet compliance requirements for fresh authentication before sensitive operations. Before enabling PoP, make sure your IdP authentication policies provide the level of assurance that you require.

## Supported identity providers

During public preview, Proof of Presence supports **Microsoft Entra ID**.

## What members experience

When a member of your enterprise attempts a protected action and needs to reauthenticate, GitHub redirects the member to the enterprise's IdP. The member follows the IdP prompts, including any required multi-factor authentication, then returns to GitHub to complete the action.

If a member cannot complete the challenge, they should contact the enterprise administrator or IdP administrator who manages authentication for the enterprise.

## Prerequisites

Before you use PoP, configure SSO between your enterprise and a supported IdP. The configuration depends on your account and deployment type:

* For an enterprise that uses personal accounts, see [AUTOTITLE](/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise).
{% ifversion ghec %}
* For an enterprise that uses Enterprise Managed Users, see [AUTOTITLE](/admin/managing-iam/understanding-iam-for-enterprises/getting-started-with-enterprise-managed-users#configure-authentication).
{% endif %}

## Enabling Proof of Presence

When you enable Proof of Presence, this policy will apply across your enterprise.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. Under (icon: gear) **Settings**, click **Authentication security**.
1. From the **Proof of presence** dropdown menu, select an authentication requirement.

  Both options require the member to complete an authentication challenge through your IdP.

  * **Re-authentication**: Requires the member to authenticate again. Depending on your enterprise's authentication policy, the member may be able to satisfy the challenge with password-based authentication.
  * **MFA**: Requires the member to authenticate again and satisfy an additional multi-factor authentication challenge, such as using an authenticator app or biometric scan, as configured by your enterprise.
