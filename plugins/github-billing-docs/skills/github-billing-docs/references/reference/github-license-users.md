---
title: People who consume a license in an organization
intro: Learn how consumption of GitHub licenses is determined for paid organizations and enterprises.
shortTitle: GitHub license users
redirect_from:
  - /github/setting-up-and-managing-billing-and-payments-on-github/about-per-user-pricing
  - /articles/about-per-user-pricing
  - /github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-your-github-account/about-per-user-pricing
  - /github/billing/managing-billing-for-your-github-account/about-per-user-pricing
  - /billing/managing-the-plan-for-your-github-account/about-per-user-pricing
  - /billing/concepts/license-consumption
  - /billing/reference/license-consumption
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
contentType: reference
category:
  - Manage your plan and licenses
---

The bill for each account on GitHub consists of the account's plan, plus other any other subscriptions and usage-based billing for the account. For organizations and enterprises, the "plan" component of the bill is based on the number of licensed seats you use.

## Organizations on GitHub Team

GitHub bills for the following people:

* Organization members, including owners
* Outside collaborators on private repositories owned by your organization, excluding forks
  * GitHub counts each outside collaborator once, even if the user account has access to multiple repositories in your organization.
* Anyone with a pending invitation to become an outside collaborator on private repositories owned by your organization, excluding forks
  * Inviting an outside collaborator to a repository using their email address temporarily uses an available seat, even if they already have access to other repositories. After they accept the invite, the seat will be freed up again. Inviting them using their username does not temporarily use a seat.
* Dormant users

### People who don't consume a license

* Billing managers
* Anyone with a pending invitation to become a billing manager
* Anyone with a pending invitation to become an outside collaborator on a public repository owned by your organization
* Anyone with a failed invitation to become an organization member or an outside collaborator on a repository owned by your organization

## Organizations on GitHub Enterprise Cloud

{% ifversion repository-collaborators %}
>[!NOTE] If your enterprise uses managed user accounts, the outside collaborator role is called "repository collaborator." Generally, the documentation for outside collaborators also applies to repository collaborators. For the distinctions that apply, see [AUTOTITLE](/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization#outside-collaborators-or-repository-collaborators).
{% endif %}

GitHub bills for each of the following accounts on GitHub Enterprise Cloud:

* Enterprise owners who are a member or owner of at least one organization in the enterprise
* Organization members, including owners
* Outside collaborators on private or internal repositories owned by your organization, excluding forks
  * GitHub counts each outside collaborator once, even if the user account has access to multiple repositories in your organization.
* Dormant users who are a member or owner of at least one organization in the enterprise

> [!IMPORTANT]
> With usage-based billing, changes to license consumption during a billing cycle are reflected in your next bill. A user who consumed a license at any point during the cycle, for example before being suspended or removed, remains billable for that cycle. See [AUTOTITLE](/billing/concepts/enterprise-billing/usage-based-licenses#how-are-metered-licenses-measured).

If your enterprise does not use Enterprise Managed Users or usage-based billing, you will also be billed for each of the following accounts. Under usage-based billing, pending invitations do not consume a license. See [AUTOTITLE](/billing/concepts/enterprise-billing/usage-based-licenses).

* Anyone with a pending invitation to become an organization owner or member
  * If the invited user already consumes an enterprise license, a pending organization invitation won't use an additional license—as long as the invitation is sent to their GitHub username or a verified email address on their account. 
* Anyone with a pending invitation to become an outside collaborator on private or internal repositories owned by your organization, excluding forks
  * If an invitee does not accept the invitation within seven days, the pending invitation expires automatically. {% ifversion ghec %}If a SCIM request from your identity provider (IdP) generates the invitation, the invitation will not expire.{% endif %}
  * If the invited user already consumes an enterprise license because they're a collaborator on an internal or private repository in the enterprise, a pending collaborator invitation using their email address for another repository in the enterprise consumes an available seat. After they accept the invite, the seat will be freed up again. Inviting them using their username does not temporarily use a seat.

### People who don't consume licenses

* Suspended Managed user accounts
* Enterprise owners who are not a member or owner of at least one organization in the enterprise
* The setup user for an enterprise that uses Enterprise Managed Users (see [AUTOTITLE](/enterprise-cloud@latest/admin/concepts/identity-and-access-management/setup-user))
* Enterprise billing managers
* Billing managers for individual organizations
* Anyone with a pending invitation to become a billing manager
* Anyone who is an outside collaborator on a public repository owned by your organization, or who has a pending invitation to become one
* Anyone with a failed invitation to become an organization member or an outside collaborator on a repository owned by your organization
* Guest collaborators who are not organization members or repository collaborators (see [AUTOTITLE](/enterprise-cloud@latest/admin/managing-accounts-and-repositories/managing-roles-in-your-enterprise/abilities-of-roles#guest-collaborators))
* Users of Visual Studio subscriptions with GitHub Enterprise whose accounts on GitHub are not linked, and who do not meet any of the other criteria for per-user pricing
* Unaffiliated users: people who have been added to the enterprise, but are not members of any organizations in the enterprise
  * However, these users consume a bundled Visual Studio license if they are linked with a Visual Studio subscription

## Organizations on GitHub Enterprise Server

* Any active user who has successfully authenticated to your GitHub Enterprise Server instance
* Dormant users (administrators can suspend dormant users to free licenses, see [Managing dormant users]({% ifversion not ghes %}/enterprise-server@latest{% endif %}/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/managing-dormant-users){% ifversion not ghes %} in the GitHub Enterprise Server documentation{% endif %})

### People who don't consume a license

* Suspended users (see [Suspending and unsuspending users]({% ifversion not ghes %}/enterprise-server@latest{% endif %}/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/suspending-and-unsuspending-users){% ifversion not ghes %} in the GitHub Enterprise Server documentation{% else %}.{% endif %})
* If you have enabled SCIM on your GitHub Enterprise Server instance, the built-in setup user you create, provided you use the `scim-admin` username.
* Users who already consume a license on GitHub Enterprise Cloud, provided you sync license usage between environments. See [AUTOTITLE](/billing/concepts/enterprise-billing/combined-enterprise-use).

## Further reading

{%- ifversion not fpt %}
* [AUTOTITLE](/admin/concepts/enterprise-fundamentals/enterprise-accounts)
* [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-roles-in-your-enterprise/abilities-of-roles)
{%- endif %}
* [AUTOTITLE](/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization)
* [AUTOTITLE](/organizations/managing-user-access-to-your-organizations-repositories/managing-outside-collaborators/adding-outside-collaborators-to-repositories-in-your-organization)
