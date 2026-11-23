---
title: Viewing people in your enterprise
intro: 'To audit access to enterprise-owned resources or user license usage, enterprise owners can view every administrator and member of the enterprise.'
permissions: Enterprise owners can view the people in an enterprise.
redirect_from:
  - /github/setting-up-and-managing-your-enterprise-account/viewing-people-in-your-enterprise-account
  - /articles/viewing-people-in-your-enterprise-account
  - /github/setting-up-and-managing-your-enterprise/viewing-people-in-your-enterprise
  - /github/setting-up-and-managing-your-enterprise/managing-users-in-your-enterprise/viewing-people-in-your-enterprise
  - /admin/user-management/managing-users-in-your-enterprise/viewing-people-in-your-enterprise
versions:
  ghec: '*'
  ghes: '*'
shortTitle: View people in your enterprise
category:
  - Manage accounts and repositories
---

{% ifversion repository-collaborators %}
>[!NOTE] If your enterprise uses managed user accounts, the outside collaborator role is called "repository collaborator." Generally, the documentation for outside collaborators also applies to repository collaborators. For the distinctions that apply, see [AUTOTITLE](/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#outside-collaborators-or-repository-collaborators).
{% endif %}

## About the list of people in your enterprise

To audit access to your enterprise's resources and manage license usage, you can see a list of all the people who have access to your enterprise.

You can see all current enterprise members and enterprise administrators{% ifversion ghec %}, as well as pending invitations to become members and administrators{% endif %}. To make it easier to consume this information, you can search and filter the lists. You can also view an overview of the number of members in your enterprise, grouped by role{% ifversion ghec %}, type of license, or type of deployment{% endif %}.

{% ifversion ghec %}

If GitHub Connect is configured for your enterprise, when you filter a list of people in your enterprise, the following limitations apply.

* The filter for two-factor authentication (2FA) status does not show people who only have an account on a GitHub Enterprise Server instance.
* If you combine the filter for accounts on GitHub Enterprise Server instances with either the filter for organizations or 2FA status, you will not see any results.

For more information about GitHub Connect, see [AUTOTITLE](/enterprise-server@latest/admin/configuring-settings/configuring-github-connect/about-github-connect) in the GitHub Enterprise Server documentation.

{% endif %}

{% ifversion enterprise-member-csv %}
You can also export membership information for your enterprise. For more information, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/exporting-membership-information-for-your-enterprise).
{% endif %}

## Viewing enterprise administrators

You can view all the current enterprise owners{% ifversion ghec %} and billing managers{% endif %} for your enterprise. You can see useful information about each administrator{% ifversion ghec %} and filter the list by role{% endif %}. You can find a specific person by searching for their username or display name.

{% ifversion ghes %}
Enterprise owners whose accounts are suspended are included in the list of enterprise administrators, and are identified as suspended. You should consider demoting any suspended owners you see. For more information, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/promoting-or-demoting-a-site-administrator#demoting-a-site-administrator-from-the-enterprise-settings).
{% endif %}

You can also remove an administrator. For more information, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/inviting-people-to-manage-your-enterprise#removing-an-enterprise-administrator-from-your-enterprise-account).

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: person) People**.
1. Under "(icon: person) People", click **Administrators**.

## Viewing members

You can see all the current members for your enterprise. You can see useful information about each account and filter the list in useful ways, such as by role. In addition to the list of members, you will see an overview of the number of members in your enterprise, grouped by role{% ifversion ghec %}, type of license, and type of deployment{% endif %}.

You can find a specific person by searching for the person's username or display name. To view more information about the person's access to your enterprise, such as the organizations the person belongs to, you can select the person's name.

{% ifversion remove-enterprise-members %}
You can also remove any enterprise member from all organizations owned by the enterprise. For more information, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/removing-a-member-from-your-enterprise).
{% endif %}

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: person) People**.
{% ifversion enterprise-member-csv %}
1. Optionally, to export the list of members as a CSV report, select **CSV report**. For more information about the information included in the report, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/exporting-membership-information-for-your-enterprise).{% endif %}

### About the membership overview

On the "Members" page, you will find an overview of the number of members in your enterprise, grouped by role{% ifversion ghec %}, type of license consumed, and the type of deployment the member is on{% endif %}. The following sections explain how the numbers in this overview are calculated.

If your enterprise uses both GitHub Enterprise Cloud and GitHub Enterprise Server, to get accurate data about your members and licenses across your deployments, you will need to enable GitHub Connect and synchronize license usage. For more information, see [AUTOTITLE](/enterprise-server@latest/admin/configuring-settings/configuring-github-connect/about-github-connect) in the GitHub Enterprise Server documentation.

#### Roles

The "Roles" column groups members by their role in the enterprise. For more information, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-roles-in-your-enterprise/abilities-of-roles).

If a user has multiple roles in an enterprise, the user is counted once for each role. For example, if the same user is a member of three organizations and an owner of two organizations, the user counts once towards "Organization member" and once towards "Organization owner."

An "outside collaborator" is a user who has access to a repository in an organization, but is not a member of the organization. The user might be an outside collaborator in one organization in your enterprise and a member of another organization. In this case, the user counts towards each total. For more information, see [AUTOTITLE](/organizations/managing-user-access-to-your-organizations-repositories/managing-outside-collaborators/adding-outside-collaborators-to-repositories-in-your-organization).

{% ifversion ghec %}

#### User licenses consumed

The "User licenses consumed" column shows you how licenses are consumed in your enterprise. For more information, see [AUTOTITLE](/billing/concepts/enterprise-billing/combined-enterprise-use).

If there are outside collaborators in your enterprise, the "total consumed" number of licenses may be larger than the number of people listed for your enterprise. An outside collaborator consumes a license, but is not counted in the total member count displayed next to "people in YOUR-ENTERPRISE". A pending invitation to an outside collaborator also consumes a license, but is not counted in the "By invitations" count in the overview.

For more information about how license usage is calculated across deployments, see [AUTOTITLE](/billing/how-tos/troubleshooting/enterprise-license-usage#about-the-calculation-of-consumed-licenses).

#### Deployment

The "Deployment" column groups users by the type of deployment they are using. For more information, see [AUTOTITLE](/admin/overview/about-github-for-enterprises#about-deployment-options).

"Cloud members" are a member or owner of any organization in your enterprise on GitHub Enterprise Cloud. "Server members" have an account on a GitHub Enterprise Server instance owned by your enterprise. "Members on cloud and server" are users who match both these criteria.
{% endif %}

{% ifversion ghec %}

## Viewing members' email addresses

You may be able to view the email addresses for members of your enterprise on either GitHub or an external identity system. The visibility of the email addresses depends on your enterprise's authentication method, domains, and potentially the member's user profile configuration.

* If you use Enterprise Managed Users and the `NameID` for your SAML configuration is an email address, you can view the `NameID` for each of your enterprise members.

* If you verify a domain for your enterprise, you can view members' email addresses for the verified domain. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-user-applications-for-your-enterprise/verifying-or-approving-a-domain-for-your-enterprise).

  > [!NOTE]
  > Email addresses for verified domains are not returned in a guaranteed order. If a member has email addresses for multiple verified domains, old or stale email addresses may remain after an IdP change. The list of verified domain email addresses cannot reliably identify the member's canonical or current corporate email address.

* If you don't use Enterprise Managed Users, and you also don't configure SAML single sign-on (SSO), members access your enterprise's resources on GitHub solely using a personal account. The owner of a personal account can choose whether or not to publicly display an email address. If a user chooses not to display the email address, you cannot view the email address. Without SAML, GitHub cannot display external identity information, like the `NameID`, which is typically an email address.

If you use Enterprise Managed Users, verify a domain, or configure SAML SSO for your enterprise, you may be able to view the email addresses in one or more of the following ways.

1. On your SAML Identity Provider (IdP), review the email addresses of users with access to your enterprise. For more information, see [AUTOTITLE](/admin/managing-iam/understanding-iam-for-enterprises/about-saml-for-enterprise-iam).
1. Export the membership report for your enterprise on GitHub. The report may contain the user's email address, stored as the following values.

   * `GitHub com saml name`: The `NameID` from the user's linked SAML identity, which is typically the user's email address (for more information, see [AUTOTITLE](/admin/managing-iam/iam-configuration-reference/saml-configuration-reference))
   * `GitHub com verified domain emails`: Email addresses for any verified domains (for more information, see [AUTOTITLE](/admin/configuring-settings/configuring-user-applications-for-your-enterprise/verifying-or-approving-a-domain-for-your-enterprise))

     The `GitHub com verified domain emails` value is unordered. Emails may be returned in a non-deterministic order, and you cannot request priority, sorting, or filtering for the user's current email address.

   For more information, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/exporting-membership-information-for-your-enterprise).
1. Use the GraphQL API to retrieve the `ExternalIdentity` for each member. For more information, see [AUTOTITLE](/graphql/overview/about-the-graphql-api) and [AUTOTITLE](/graphql/reference#externalidentity) in the GraphQL API documentation.

   > [!NOTE]
   > Access to external identities depends on whether SAML is configured at the organization or enterprise level. Organization-level external identities are available to organization owners, organization owner personal access tokens with the `read:org` or `admin:org` scope, and GitHub App installation tokens with read or write access to members when the app is installed on the organization. Enterprise-level external identities require an enterprise owner personal access token with the `read:enterprise` or `admin:enterprise` scope. GitHub Apps cannot access enterprise-level external identities, including enterprise-level SAML identities for GitHub Enterprise Cloud with personal user accounts.

{% endif %}

## Viewing outside collaborators

You can see all the current outside collaborators for your enterprise. You can see useful information about each collaborator and filter the list in useful ways, such as by organization. You can find a specific collaborator by searching for their username or display name.

You can view more information about the person's access to your enterprise, such as a list of all the repositories the collaborator has access to, by selecting the person's name.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: person) People**.
1. Under "People", select **Outside collaborators**.

{% ifversion ghec %}

## Viewing pending invitations

You can see all the pending invitations to become members, administrators, or outside collaborators in your enterprise. You can filter the list in useful ways, such as by license, by organization, or by source. You can find a specific person by searching for their username or display name.

In the list of pending members, for any individual account, you can cancel all invitations to join organizations owned by your enterprise. This does not cancel any invitations for that same person to become an enterprise administrator or outside collaborator.

> [!NOTE]
> If an invitation was provisioned via SCIM, you must cancel the invitation via your identity provider (IdP) instead of on GitHub.

If you use Visual Studio subscriptions with GitHub Enterprise, the list of pending invitations includes all Visual Studio subscribers that haven't joined any of your organizations on GitHub, even if the subscriber does not have a pending invitation to join an organization. For more information about how to get Visual Studio subscribers access to GitHub Enterprise, see [AUTOTITLE](/billing/how-tos/set-up-payment/set-up-vs-subscription).

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: person) People**.
1. Under "People", select **Invitations**.
1. Optionally, you can cancel all invitations for an account to join organizations owned by your enterprise. To the right of the account, select (icon: kebab-horizontal), then select **Cancel invitation**.

   ![Screenshot of a single invitation on the "Invitations" page. A button, titled "Cancel invitation", is highlighted with an orange outline.](/assets/images/help/enterprises/cancel-enterprise-member-invitation.png)
1. Optionally, you can view pending invitations for enterprise administrators or outside collaborators. Under "Invitations", select **Administrators** or **Outside collaborators**.
1. Optionally, to filter the list of pending invitations by license, by organization, or by source, use the dropdown menus at the top of the list.

   ![Screenshot of the "Invitations" page. Three dropdown menus, titled "License", "Organizations", and "Source" are highlighted with an orange outline.](/assets/images/help/enterprises/enterprise-filter-pending-invitations.png)

{% endif %}

## Viewing suspended members

If your enterprise uses {% ifversion ghec %}Enterprise Managed Users{% else %}SCIM provisioning{% endif %}, you can view suspended users. Suspended users are members who have been deprovisioned after being unassigned from the application or deleted on the identity provider.{% ifversion ghec %} Currently, it is not possible to remove suspended users from an enterprise that uses Enterprise Managed Users.{% endif %}

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: person) People**.
1. Under "People", select **Suspended**.

## Viewing dormant users

You can view a list of all dormant users {% ifversion ghes %} who have not been suspended and {% endif %}who are not site administrators. {% ifversion not ghec %}By default, a{% else %}A{% endif %} user account is considered to be dormant if it has not been active for 30 days. {% ifversion not ghec %}You can configure the length of time a user must be inactive to be considered dormant{% ifversion ghes %} and choose to suspend dormant users to release user licenses{% endif %}.{% endif %} For more information, see [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/managing-dormant-users).

## Filtering by member type{% ifversion ghec %} in an enterprise with managed users{% endif %}

{% ifversion ghec %}If your enterprise uses Enterprise Managed Users, you{% elsif ghes %}You{% endif %} can filter the member list of an organization by type to determine if memberships are managed through an IdP or managed directly. Memberships managed through an IdP were added through an IdP group, and the IdP group was connected to a team within the organization. Memberships managed directly were added to the organization manually. The way a membership is managed in an organization determines how it must be removed. You can use this filter to determine how members were added to an organization, so you know how to remove them.{% ifversion ghec %} For more information, see [AUTOTITLE](/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users#about-organization-membership-management).{% endif %}

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. Under "Organizations", in the search bar, begin typing the organization's name until it appears in the search results.
1. Select the name of the organization.
1. Above the organization name, select **(icon: person) People**.

   ![Screenshot of the tabs above an organization name. The "People" tab is highlighted with an orange outline.](/assets/images/help/enterprises/emu-organization-people-tab.png)
1. Above the list of members, select **Type**, then select the type of members you want to view.
   ![Screenshot of the list of members. A dropdown menu labeled "Type" is outlined and expanded.](/assets/images/help/enterprises/filter-by-member-type.png)

{% ifversion scim-for-ghes-public-beta %}

## Filtering by account type (SAML and SCIM)

If you use SAML authentication and SCIM provisioning, you can filter members based on how they authenticate and how their account was created.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: person) People**.
1. Select **Account Type**, then choose from the following options.

   * **Built-in:** Users with local accounts on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} who authenticate with a username and password.
{% ifversion scim-for-ghes-ga %}
   * **SAML JIT provisioned:** Users who authenticate with SAML via an identity provider and were created through just-in-time (JIT) provisioning when they first signed in. These users are not linked to SCIM identities.
   * **SCIM provisioned:** Users who were created and managed through SCIM provisioning from your identity provider. These users are linked to SCIM identities.
{% else %}
   * **SAML linked:** Users who authenticate with SAML via an identity provider, but were not provisioned by SCIM.
   * **SAML and SCIM linked:** Users who authenticate with SAML via an identity provider, and were provisioned by SCIM.
{% endif %}

{% endif %}

{% ifversion scim-for-ghes-ga %}
Enterprise administrators with CLI access can export a full CSV of SCIM provisioned user identities using the [ghe-scim-identities-csv](/admin/administering-your-instance/administering-your-instance-from-the-command-line/command-line-utilities#ghe-scim-identities-csv) tool.
{% endif %}

## Viewing members without an email address from a verified domain

You can view a list of members in your enterprise who don't have an email address from a verified domain associated with their user account.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. Under "Settings", click **Verified & approved domains**.
1. Under "Notification preferences", select the **(icon: eye) View enterprise members without an approved or verified domain email** link.

## Viewing whether members in your enterprise have 2FA enabled

{% ifversion ghec %}

You can see which people in your enterprise have enabled two-factor authentication.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: person) People**.
1. To view the two-factor authentication security levels of enterprise members, on the right, select **Two-factor authentication**, then select **Secure**, **Insecure**, or **Disabled**.

   ![Screenshot of the list of enterprise members. A dropdown menu, labeled "Two-factor authentication", is expanded and outlined in orange.](/assets/images/help/2fa/filter-enterprise-members-by-2fa.png)

{% else %}

You can see which people in your enterprise have enabled two-factor authentication{% ifversion mandatory-2fa-required-overview %} or are required to do so{% endif %}.

{% ifversion mandatory-2fa-required-overview %}
> [!NOTE]
> As of March 2023, GitHub required all users who contribute code on GitHub.com to enable one or more forms of two-factor authentication (2FA). If you were in an eligible group, you would have received a notification email when that group was selected for enrollment, marking the beginning of a 45-day 2FA enrollment period, and you would have seen banners asking you to enroll in 2FA on GitHub.com. If you didn't receive a notification, then you were not part of a group required to enable 2FA, though we strongly recommend it.
>
> For more information about the 2FA enrollment rollout, see [this blog post](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13).
{% endif %}

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: person) People**.
1. To view enterprise members who have enabled or disabled two-factor authentication, on the right, select **Two-factor authentication**, then select **Secure** or **Disabled**.

   ![Screenshot of the list of organization members. A dropdown menu, labeled "Two-factor Authentication", is expanded and outlined in orange.](/assets/images/help/2fa/ghes-filter-org-members-by-2fa.png)

{% endif %}

## Further reading

* [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-roles-in-your-enterprise/abilities-of-roles)
