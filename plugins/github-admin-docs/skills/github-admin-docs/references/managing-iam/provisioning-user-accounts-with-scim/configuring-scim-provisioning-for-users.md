---
title: Configuring SCIM provisioning {% ifversion ghec %}for Enterprise Managed Users{% else %}to manage users{% endif %}
shortTitle: Configure SCIM provisioning
intro: 'You can manage the lifecycle of your enterprise''s user accounts from your identity provider (IdP) using System for Cross-domain Identity Management (SCIM).'
allowTitleToDifferFromFilename: true
permissions: '{% ifversion scim-for-ghes-public-beta %}Site administrators{% endif %}'
product: "{% ifversion ghec %}\n\nEnterprise Managed Users is available for new enterprise accounts on GitHub Enterprise Cloud. See [AUTOTITLE](/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users).\n\n{% endif %}"
redirect_from:
  - /github/setting-up-and-managing-your-enterprise/managing-your-enterprise-users-with-your-identity-provider/configuring-scim-provisioning-for-enterprise-managed-users
  - /admin/authentication/managing-your-enterprise-users-with-your-identity-provider/configuring-scim-provisioning-for-enterprise-managed-users
  - /admin/identity-and-access-management/managing-iam-with-enterprise-managed-users/configuring-scim-provisioning-for-enterprise-managed-users
  - /admin/identity-and-access-management/using-enterprise-managed-users-and-saml-for-iam/configuring-scim-provisioning-for-enterprise-managed-users
  - /admin/identity-and-access-management/using-enterprise-managed-users-for-iam/configuring-scim-provisioning-for-enterprise-managed-users
  - /admin/identity-and-access-management/provisioning-user-accounts-for-enterprise-managed-users/configuring-scim-provisioning-for-enterprise-managed-users
  - /admin/managing-iam/provisioning-user-accounts-for-enterprise-managed-users/configuring-scim-provisioning-for-enterprise-managed-users
versions:
  ghec: '*'
  feature: scim-for-ghes-public-beta
category:
  - Provision and manage enterprise users
---

To create, manage, and deactivate user accounts for your enterprise members on GitHub, your IdP {% ifversion ghec %}must{% else %}can{% endif %} implement SCIM for communication with GitHub. SCIM is an open specification for management of user identities between systems. Different IdPs provide different experiences for the configuration of SCIM provisioning.

If you use a partner IdP, you can simplify the configuration of SCIM provisioning by using the partner IdP's application. If you don't use a partner IdP for provisioning, you can implement SCIM using calls to GitHub's REST API for SCIM. For more information, see {% ifversion ghec %}[AUTOTITLE](/admin/concepts/identity-and-access-management/enterprise-managed-users#how-does-emus-integrate-with-identity-management-systems).{% else %}[AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/user-provisioning-with-scim-on-ghes#supported-identity-providers).{% endif %}

> [!NOTE] GitHub does not test or validate identity provider (IdP) gallery applications for use in Government Cloud environments, including Microsoft Entra ID Government Cloud and Okta Government Cloud. Authentication and SCIM provisioning issues that involve gallery applications in these environments fall outside GitHub's [scope of support](/support/learning-about-github-support/about-github-support#scope-of-support).

{% ifversion ghes %}

## Who needs to follow these instructions?

Even if your instance already uses SAML authentication, or if you were enrolled in the SCIM private preview on a previous GitHub Enterprise Server version, you must ensure you have followed **all instructions in this guide** to enable SCIM in version 3.14 and later.

This guide applies in any of the following situations.

* You're **setting up SAML and SCIM for the first time**: you'll follow these instructions to get started.
* You **already use SAML authentication**: you'll need to enable SCIM on your instance, plus either reconfigure SAML with an IdP application that supports automated provisioning or set up a SCIM integration with the REST API.
* You were **enrolled in the SCIM private preview**: you'll need to reenable SCIM on your instance and, if you're using a partner IdP, reconfigure your settings on an updated IdP application.

{% endif %}

{% ifversion ghec %}

## About user lifecycle management with SCIM

With SCIM, you manage the lifecycle of user accounts from your IdP:

* {% ifversion ghec %}After you configure provisioning for Enterprise Managed Users, your IdP uses SCIM to provision user accounts on GitHub and add the accounts to your enterprise.{% else %}When you provision a new user, your IdP will prompt {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to create an account and send an onboarding email to the user.{% endif %} If you assign a group to the application in your IdP, your IdP will provision accounts for all members of the group.
* When you update information associated with a user's identity on your IdP, your IdP will update the user's account on GitHub.
* When you unassign the user from the IdP application or deactivate a user's account on your IdP, your IdP will communicate with GitHub to invalidate any sessions and disable the member's account. The disabled account's information is maintained and their username is changed to a hash of their original username{% ifversion ghec %}, with the short code appended if applicable{% endif %}.
* If you reassign a user to the IdP application or reactivate their account on your IdP, the user account will be reactivated, and the username will be restored.

{% ifversion ghec or ghes %}
To configure team and organization membership, repository access, and permissions, you can use groups on your IdP. For more information, see [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/managing-team-memberships-with-identity-provider-groups).
{% endif %}

{% endif %}

## Prerequisites

{% ifversion ghec %}

If you're configuring SCIM provisioning for a new enterprise, make sure to complete all previous steps in the initial configuration process. See [AUTOTITLE](/admin/managing-iam/understanding-iam-for-enterprises/getting-started-with-enterprise-managed-users).

{% else %}

* SCIM is a server-to-server protocol. Your instance's REST API endpoints must be accessible to your SCIM provider.

This table contains the network requirements to configure GHES SCIM with an IdP:

| System | Direction | Purpose | Protocol / Port | Notes |
|------------|------------|----------|------------------|-------|
| GitHub Enterprise Server | Inbound | Receives SCIM API requests from IdP for users and groups | TCP 443 (HTTPS) | [AUTOTITLE](/rest/enterprise-admin/scim) must be reachable from IdP |
| Identity Provider (IdP) | Outbound | Sends SCIM provisioning requests to GitHub for users and groups | TCP 443 (HTTPS) | IdP acts as SCIM client, initiating outbound HTTPS connections to GitHub's SCIM API endpoints. |

* For authentication, your instance must use SAML SSO, or a mix of SAML and built-in authentication.
  * You cannot mix SCIM with other external authentication methods. If you use CAS or LDAP, you will need to migrate to SAML before using SCIM.
  * After you have configured SCIM, you must keep SAML authentication enabled to continue using SCIM.
* You must have administrative access on your IdP.
* You must have access to the Management Console on GitHub Enterprise Server.
* If you are configuring SCIM on an instance with existing users, ensure you have understood how SCIM will identify and update these users. See [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/user-provisioning-with-scim-on-ghes#what-will-happen-to-existing-users-on-my-instance).

{% endif %}

{% ifversion ghes %}

## 1. Create a built-in setup user

To ensure you can continue to sign in and configure settings when SCIM is enabled, you'll create an enterprise owner using built-in authentication.

1. Sign in to GitHub Enterprise Server as a user with access to the Management Console.
1. If you have **already enabled SAML authentication**, ensure your settings allow you to create and promote a built-in authentication user. Go to the "Authentication" section of the Management Console and enable the following settings:

   * Select **Allow creation of accounts with built-in authentication**, so you can create the user.
   * Select **Disable administrator demotion/promotion**, so admin permissions can be granted outside of your SAML provider.

   For help finding these settings, see [AUTOTITLE](/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise#configuring-saml-sso).

1. Create a built-in user account{% ifversion scim-for-ghes-ga %} with the username `scim-admin`{% endif %} to perform provisioning actions on your instance. See [AUTOTITLE](/admin/managing-iam/understanding-iam-for-enterprises/allowing-built-in-authentication-for-users-outside-your-provider#inviting-users-outside-your-provider-to-authenticate-to-your-instance).

   Ensure the user's email and username are different from any user you plan on provisioning through SCIM. If your email provider supports it, you can modify an email address by adding `+admin`, for example `johndoe+admin@example.com`.

   {% ifversion scim-for-ghes-ga %}You can use any username for your setup user, but we recommend using `scim-admin`. Although the `scim-admin` user consumes a license when first created, the license is freed once SCIM is enabled. With any other username, the user will continue to consume a license after SCIM is enabled.{% endif %}

1. Copy the password reset link after creating the user, and open it in a private browser window. Set a password for this user.

   > [!IMPORTANT]
   > As this user will act as a break-glass account, ensure you store the password securely in a password manager. Otherwise you risk losing access to this account.

1. Promote the user to an enterprise owner. See [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/promoting-or-demoting-a-site-administrator#promoting-a-user-from-the-enterprise-settings).

## 2. Create a personal access token

1. Sign in to your instance as the **built-in setup user** you created in the previous section.
1. Create a personal access token (classic). For instructions, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic).

   * The token must have the {% ifversion scim-enterprise-scope %}`scim:enterprise`{% else %}`admin:enterprise`{% endif %} scope.
   * The token must have **no expiration**. If you specify an expiration date, SCIM will no longer function after the expiration date passes.

1. Store the token securely in a password manager until you need the token again later in the setup process. You'll need the token to configure SCIM on your IdP.

## 3. Enable SAML on your instance

> [!NOTE] Complete this section if either of the following situations applies:
> * If you have **not already enabled SAML authentication**, you will need to do so before you can enable SCIM.
> * If you already use SAML authentication and want to use a **partner IdP for both authentication and provisioning**, or if you're **upgrading from the SCIM private preview**, you must reconfigure SAML using a new application.

1. Sign in to your instance as a user with access to the Management Console.
1. Go to the "Authentication" section of the Management Console. For instructions, see [AUTOTITLE](/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise#configuring-saml-sso).
1. Select **SAML**.
1. Configure the SAML settings according to your requirements and the IdP you're using.

   * So the built-in setup user can continue to authenticate, ensure you select the following settings:
     * **Allow creation of accounts with built-in authentication**
     * **Disable administrator demotion/promotion**
   * If you're using a partner IdP, to find the information you need to configure the settings, follow the "Configure SAML" section of the relevant guide.
     * [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/configuring-authentication-and-provisioning-with-entra-id#1-configure-saml)
     * [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/configuring-authentication-and-provisioning-with-pingfederate#1-configure-saml)
     * [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/configuring-scim-provisioning-with-okta#1-configure-saml)

1. Optionally, complete configuration of the SAML settings within the application in your IdP. Alternatively, you can leave this step until later.

## 4. Enable SCIM on your instance

1. Sign in to your instance as the **built-in setup user** you created earlier.
{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. Under **(icon: gear) Settings**, click **Authentication security**.
1. Under "SCIM Configuration", select **Enable SCIM configuration**.

You can confirm that SCIM is now enabled by checking your instance's [audit logs](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise). You should expect to see a "business.enable_open_scim" event, indicating that GitHub's [SCIM REST API](/admin/managing-iam/provisioning-user-accounts-with-scim/provisioning-users-and-groups-with-scim-using-the-rest-api) has been enabled on your instance.

{% endif %}

{% ifversion ghec %}

## Configuring user provisioning for Enterprise Managed Users

{% else %}

## 5. Configure your identity provider

{% endif %}

After completing the setup on GitHub, you can configure provisioning on your IdP. The instructions you should follow differ depending on whether you use a partner IdP's application for both authentication and provisioning.

* [Configuring provisioning if you use a partner IdP's application](#configuring-provisioning-if-you-use-a-partner-idps-application)
* [Configuring provisioning for other identity management systems](#configuring-provisioning-for-other-identity-management-systems)

### Configuring provisioning if you use a partner IdP's application

{% ifversion ghec %}

To use a partner IdP's application both authentication and provisioning, review the partner's instructions for configuring provisioning in the links in the following table.

{% rowheaders %}

| IdP | SSO method | Instructions |
|---|---|---|
| Microsoft Entra ID (previously known as Azure AD) | OIDC | [Tutorial: Configure GitHub Enterprise Managed User (OIDC) for automatic user provisioning](https://docs.microsoft.com/azure/active-directory/saas-apps/github-enterprise-managed-user-oidc-provisioning-tutorial) on Microsoft Learn |
| Entra ID | SAML | [Tutorial: Configure GitHub Enterprise Managed User for automatic user provisioning](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/github-enterprise-managed-user-provisioning-tutorial) on Microsoft Learn |
| Okta | SAML | [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/configuring-scim-provisioning-with-okta) |
| PingFederate | SAML | The "Prerequisites" and "2. Configure SCIM" sections in [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/configuring-authentication-and-provisioning-with-pingfederate) |

{% endrowheaders %}

{% else %}

To use a partner IdP's application for both authentication and provisioning, review the instructions that are linked below. Complete the steps for enabling SCIM, plus any SAML configuration that you haven't already performed.

* [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/configuring-authentication-and-provisioning-with-entra-id)
* [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/configuring-authentication-and-provisioning-with-pingfederate)
* [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/configuring-scim-provisioning-with-okta)

{% endif %}

### Configuring provisioning for other identity management systems

If you don't use a partner IdP, or if you only use a partner IdP for SAML authentication, you can manage the lifecycle of user accounts using GitHub's REST API endpoints for SCIM provisioning. See [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/provisioning-users-and-groups-with-scim-using-the-rest-api).

> [!NOTE]
> Use of the REST API for SCIM provisioning is not supported with enterprises enabled for OIDC.

GitHub does not expressly support mixing partner IdPs for authentication and provisioning and does not test all identity management systems. **GitHub's support team may not be able to assist you with issues related to mixed or untested systems.** If you need help, you must consult the system's documentation, support team, or other resources.

>[!IMPORTANT] The combination of **Okta and Entra ID** for SSO and SCIM (in either order) is explicitly **not supported**. GitHub's SCIM API will return an error to the identity provider on provisioning attempts if this combination is configured.

{% ifversion emu-public-scim-schema %}

1. Sign in as the setup user for your enterprise with the username **SHORTCODE_admin**, replacing SHORTCODE with your enterprise's shortcode.

   > [!NOTE]
   > If you need to reset the password for your setup user, contact GitHub Support through the [GitHub Support portal](https://support.github.com). The usual password reset option by providing your email address will not work.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **Identity provider**.
1. Under **Identity Provider**, click **Single sign-on configuration**.
1. Under "Open SCIM Configuration", select "Enable open SCIM configuration".
1. Manage the lifecycle of your users by making calls to the REST API endpoints for SCIM provisioning. See [AUTOTITLE](/admin/managing-iam/provisioning-user-accounts-with-scim/provisioning-users-and-groups-with-scim-using-the-rest-api).

{% endif %}

{% ifversion scim-for-ghes-public-beta %}

## 6. Update settings

After you have finished the configuration process, you should disable the following setting in the Management Console:

* **Disable administrator demotion/promotion**: Disable this setting to allow assignment of the enterprise owner role via SCIM. If this setting remains enabled, you will not be able to provision enterprise owners via SCIM.

Optionally, you can disable the following setting in the Management Console as well:

* **Allow creation of accounts with built-in authentication**: Disable this setting if you want all users to be provisioned from your IdP.

{% endif %}

## {% ifversion ghec %}Assigning{% else %}7. Assign{% endif %} users and groups

After you have configured authentication and provisioning, you will be able to provision new users on GitHub by assigning users or groups to the {% ifversion ghec %}GitHub Enterprise Managed User application{% else %}relevant application in your IdP{% endif %}.

When assigning users, you can use the "Roles" attribute in the application on your IdP to set a user's role in your enterprise. For more information about the roles available to assign, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-roles-in-your-enterprise/abilities-of-roles).

Entra ID does not support provisioning nested groups. For more information, see [How Application Provisioning works in Microsoft Entra ID](https://learn.microsoft.com/entra/identity/app-provisioning/how-provisioning-works#assignment-based-scoping) on Microsoft Learn.
