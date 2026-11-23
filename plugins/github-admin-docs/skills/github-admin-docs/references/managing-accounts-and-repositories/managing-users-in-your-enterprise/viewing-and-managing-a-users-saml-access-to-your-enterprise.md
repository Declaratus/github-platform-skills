---
title: Viewing and managing a user's SAML access to your enterprise
intro: 'You can view and revoke an enterprise member''s {% ifversion ghec %}linked identity, active sessions, and authorized credentials{% else %}active SAML sessions{% endif %}.'
permissions: Enterprise owners
product: '{% ifversion ghes %}Instances that have configured SCIM provisioning{% endif %}'
redirect_from:
  - /github/setting-up-and-managing-your-enterprise/viewing-and-managing-a-users-saml-access-to-your-enterprise-account
  - /github/setting-up-and-managing-your-enterprise-account/viewing-and-managing-a-users-saml-access-to-your-enterprise-account
  - /github/setting-up-and-managing-your-enterprise/viewing-and-managing-a-users-saml-access-to-your-enterprise
  - /github/setting-up-and-managing-your-enterprise/managing-users-in-your-enterprise/viewing-and-managing-a-users-saml-access-to-your-enterprise
  - /admin/user-management/managing-users-in-your-enterprise/viewing-and-managing-a-users-saml-access-to-your-enterprise
versions:
  ghec: '*'
  feature: scim-for-ghes-public-beta
shortTitle: View & manage SAML access
category:
  - Manage accounts and repositories
---

## About SAML access to your enterprise account

When you enable SAML single sign-on for your enterprise account, each enterprise member can link their external identity on your identity provider (IdP) to their existing account on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. To access each organization's resources on GitHub, the member must have an active SAML session in their browser.{% ifversion ghec %} To access each organization's protected resources using the API and Git, the member must use a personal access token or SSH key that the member has authorized for use with the organization.{% endif %} Enterprise owners can view and revoke a member's {% ifversion ghec %}linked identity, active sessions, or authorized credentials{% else %}active SAML sessions{% endif %} at any time.
                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                      {% ifversion ghes %}
                                                                                                                                                                                                                                      >[!NOTE]
                                                                                                                                                                                                                                      > This view is only enabled when SAML with SCIM is enabled.
                                                                                                                                                                                                                                      {% endif %}

{% ifversion ghec %}

If your enterprise uses Enterprise Managed Users, your members will use accounts provisioned through your IdP. Managed user accounts will not use their existing user account on GitHub. For more information, see [AUTOTITLE](/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users).

{% endif %}

{% ifversion ghec %}

## Viewing and revoking a linked identity

You can view the single sign-on identity that a member has linked to their account on GitHub.

If a member links the wrong identity to their account on GitHub, you can revoke the linked identity to allow the member to try again.

If your enterprise uses Enterprise Managed Users, you will not be able to deprovision or remove user accounts from the enterprise via GitHub. Any changes you need to make to your enterprise's managed user accounts should be made through your IdP.

> [!WARNING]
> If your organization uses team synchronization, revoking a person's SSO identity will remove that person from any teams mapped to IdP groups. For more information, see [AUTOTITLE](/organizations/organizing-members-into-teams/synchronizing-a-team-with-an-identity-provider-group).

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: person) People**.
1. Click on the name of the member whose linked identity you'd like to view or revoke.
1. In the left sidebar, click **SAML identity linked**.

   ![Screenshot of the people summary for @octocat. A link, labeled "SAML identity linked", is highlighted with an orange outline.](/assets/images/help/saml/saml-identity-linked.png)
1. Under "Linked SSO identity", view the linked SSO identity for the member.
1. To revoke the linked identity, to the right of the identity, click **Revoke**.
1. Read the information, then click **Revoke external identity**.

{% elsif scim-for-ghes-public-beta %}

## Viewing a linked identity

You can view the single sign-on identity that a member has linked to their account on GitHub.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: person) People**.
1. Click on the name of the member whose linked identity you'd like to view or revoke.
1. In the left sidebar, click **SAML identity linked**.

   ![Screenshot of the people summary for @octocat. A link, labeled "SAML identity linked", is highlighted with an orange outline.](/assets/images/help/saml/saml-identity-linked.png)
1. Under "Linked SSO identity", view the linked SSO identity for the member.

The identity data on this page will include the SCIM data that was sent to GitHub during user provisioning. This SCIM data is what GitHub uses when matching a SAML SSO request to the provisioned user. Note that GitHub does not use SAML mappings when SCIM is enabled. For more information on how GitHub maps SAML and SCIM data for users, please see [AUTOTITLE](/rest/enterprise-admin/scim?apiVersion=2022-11-28#mapping-of-saml-and-scim-data).

{% endif %}

## Viewing and revoking an active SAML session

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: person) People**.
1. Click on the name of the member whose SAML session you'd like to view or revoke.
1. In the left sidebar, click **SAML identity linked**.

   ![Screenshot of the people summary for @octocat. A link, labeled "SAML identity linked", is highlighted with an orange outline.](/assets/images/help/saml/saml-identity-linked.png)
1. Under "Active SAML sessions", view the active SAML sessions for the member.
1. To revoke a session, to the right of the session you'd like to revoke, click **Revoke**.

{% ifversion ghec %}

## Viewing and revoking authorized credentials

You can see each personal access token and SSH key that a member has authorized for API and Git access. Only the last several characters of each token or key are visible. If necessary, work with the member to determine which credentials you should revoke. Be aware that revoking a credential only removes the SAML authorization. It does not delete the underlying token or SSH key.

{% ifversion single_user_cred_revocation %}

> [!TIP] To respond to security incidents, enterprise and organization owners can also revoke all SSO authorizations at once for individual users, all users, or a specific credential type such as personal access tokens (classic). For enterprises with Enterprise Managed Users, you can delete credentials entirely. For more information, see [AUTOTITLE](/enterprise-cloud@latest/admin/managing-iam/respond-to-incidents/revoke-authorizations-or-tokens).

{% endif %}

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: person) People**.
1. Click on the name of the member whose authorized credentials you'd like to view or revoke.
1. In the left sidebar, click **SAML identity linked**.

   ![Screenshot of the people summary for @octocat. A link, labeled "SAML identity linked", is highlighted with an orange outline.](/assets/images/help/saml/saml-identity-linked.png)
1. Under "Authorized credentials", view the authorized credentials for the member.
1. To revoke credentials, to the right of the credentials you'd like to revoke, click **Revoke**.
1. Read the information, then click **I understand, revoke access for this token.**

## Further reading

* [AUTOTITLE](/organizations/granting-access-to-your-organization-with-saml-single-sign-on/viewing-and-managing-a-members-saml-access-to-your-organization)

{% endif %}
