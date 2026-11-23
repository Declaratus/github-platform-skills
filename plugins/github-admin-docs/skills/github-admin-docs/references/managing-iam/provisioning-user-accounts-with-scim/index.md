---
title: 'Provisioning accounts{% ifversion ghec %} for Enterprise Managed Users{% else %} with SCIM{% endif %}'
shortTitle: 'Provision{% ifversion ghec %} managed user accounts{% else %} accounts with SCIM{% endif %}'
product: "{% ifversion ghec %}\n\nEnterprise Managed Users is available for new enterprise accounts on GitHub Enterprise Cloud. See [AUTOTITLE](/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users).\n\n{% endif %}"
intro: 'Learn how to provision accounts and manage organization and team membership for users{% ifversion ghec %} of your enterprise with managed users{% elsif ghes %} on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}{% endif %}.'
versions:
  ghec: '*'
  ghes: '*'
children:
  - /user-provisioning-with-scim-on-ghes
  - /configuring-scim-provisioning-for-users
  - /migrating-from-ldap-to-saml-with-scim
  - /configuring-authentication-and-provisioning-with-entra-id
  - /configuring-authentication-and-provisioning-with-pingfederate
  - /configuring-scim-provisioning-with-okta
  - /disabling-scim-provisioning-for-users
  - /provisioning-users-and-groups-with-scim-using-the-rest-api
  - /managing-team-memberships-with-identity-provider-groups
  - /deprovisioning-and-reinstating-users
  - /troubleshooting-team-membership-with-identity-provider-groups
redirect_from:
  - /admin/identity-and-access-management/provisioning-user-accounts-for-enterprise-managed-users
  - /admin/managing-iam/provisioning-user-accounts-for-enterprise-managed-users
---

