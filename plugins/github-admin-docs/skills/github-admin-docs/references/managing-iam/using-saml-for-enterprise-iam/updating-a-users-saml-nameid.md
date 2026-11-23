---
title: Updating a user's SAML NameID
shortTitle: Update SAML NameID
intro: When an account's `NameID` changes on your identity provider (IdP) and the person can no longer sign into {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, you must update the `NameID` mapping on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.
versions:
  ghes: '*'
redirect_from:
  - /admin/identity-and-access-management/using-saml-for-enterprise-iam/updating-a-users-saml-nameid
contentType: how-tos
category:
  - Configure authentication
---

## About updates to users' SAML `NameID`

In some situations, you may need to update values associated with a person's account on your SAML IdP. If that identifier is also the `NameID` that you use for authentication on GitHub, you must update the `NameID` mapping on your instance so the person can continue to authenticate successfully. For more information, see [AUTOTITLE](/admin/managing-iam/iam-configuration-reference/username-considerations-for-external-authentication).

To update user SAML `NameID` mappings in bulk, you can use the `ghe-saml-mapping-csv` command. For more information, see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-command-line/command-line-utilities#ghe-saml-mapping-csv).

When SCIM is enabled on your GitHub Enterprise Server instance, you cannot update user SAML `NameID` mappings.

## Updating a user's SAML `NameID`

Enterprise owners can update a user's SAML `NameID` on a GitHub instance.

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the left sidebar, click **All users**.
1. In the list of users, click the username you'd like to update the `NameID` mapping for.
1. In the upper-right corner of the page, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. To the right of "Update SAML NameID", click **Edit** .
1. In the "NameID" field, type the new `NameID` for the user.
1. Click **Update NameID**.
