---
title: License troubleshooting information for GitHub Enterprise
intro: Troubleshoot license usage for your enterprise by understanding consumption criteria and auditing license reports.
versions:
  ghec: '*'
  ghes: '*'
shortTitle: Enterprise license troubleshooting
contentType: reference
redirect_from:
  - /billing/reference/license-usage-calculation
  - /billing/reference/license-usage-reference
category:
  - Manage enterprise licenses
---

## People who consume a license

A person consumes a license for GitHub Enterprise depending on specific criteria. If a user has not yet accepted an invitation to join your enterprise, the user still consumes a license. For more information about the people in your enterprise who consume a license, see [AUTOTITLE](/billing/reference/github-license-users).

## Visual Studio subscribers

If the verified email address for the personal account of an enterprise member on GitHub matches the User Principal Name (UPN) for a subscriber to your Visual Studio account, the Visual Studio subscriber will automatically consume one license for Visual Studio subscriptions with GitHub Enterprise Cloud.

> [!NOTE] For Enterprise Managed User only, to make sure a user account consumes a Visual Studio license, ensure the Visual Studio UPN matches the SCIM `userName` attribute or the email address from the linked identity on the GitHub account.

For more information, see [AUTOTITLE](/enterprise-cloud@latest/billing/concepts/enterprise-billing/visual-studio-subs).

## Users of GitHub Enterprise Cloud and GitHub Enterprise Server

For each user to consume a single {% ifversion enterprise-licensing-language %}license{% else %}seat{% endif %} regardless of how many deployments they use, you must synchronize license usage between GitHub Enterprise Server and GitHub Enterprise Cloud. For more information, see [AUTOTITLE](/billing/how-tos/manage-server-licenses/sync-license-usage).

After you synchronize license usage, GitHub matches user accounts on GitHub Enterprise Server with user accounts on GitHub Enterprise Cloud by email address.

1. We check the primary email address of each user on GitHub Enterprise Server.
1. We attempt to match that address with the email address for a user account on GitHub Enterprise Cloud.

### With SAML or SCIM

If your enterprise on GitHub Enterprise Cloud or any of the enterprise's organizations use SAML authentication or SCIM provisioning, we first check the linked SAML or SCIM identities to see if the identity contains one of the attributes below. We attempt to match the values of these attributes to the primary email address of each GitHub Enterprise Server user.

* `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name`
* `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`
* `username`
* `NameID`
* `emails`

### Without SAML or SCIM

If there is no match with a SAML or SCIM attribute, or if SAML authentication or SCIM provisioning is not in use, we attempt to match the primary email address on GitHub Enterprise Server with a verified email address for a user account on GitHub Enterprise Cloud. For more information about verification of email addresses on GitHub Enterprise Cloud, see [AUTOTITLE](/enterprise-cloud@latest/account-and-profile/how-tos/email-preferences/verifying-your-email-address){% ifversion ghes %} in the GitHub Enterprise Cloud documentation.{% else %}.{% endif %}

## Fields in the consumed license files

The GitHub Enterprise Cloud license usage report and GitHub Enterprise Server exported license usage file include a variety of fields to help you troubleshoot license usage for your enterprise.

For details of each field, see [AUTOTITLE](/billing/reference/license-reports#github-enterprise-cloud-license-report).

## Troubleshooting steps

For troubleshooting steps, see [AUTOTITLE](/billing/how-tos/troubleshooting/enterprise-license-usage).
