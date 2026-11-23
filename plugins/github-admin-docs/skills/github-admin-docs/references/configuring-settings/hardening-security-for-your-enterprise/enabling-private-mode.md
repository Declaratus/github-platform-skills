---
title: Enabling private mode
intro: In private mode, GitHub Enterprise Server requires every user to sign in to access the installation.
redirect_from:
  - /enterprise/admin/articles/private-mode
  - /enterprise/admin/guides/installation/security
  - /enterprise/admin/guides/installation/securing-your-instance
  - /enterprise/admin/installation/enabling-private-mode
  - /enterprise/admin/configuration/enabling-private-mode
  - /admin/configuration/enabling-private-mode
  - /admin/configuration/configuring-your-enterprise/enabling-private-mode
  - /admin/configuration/hardening-security-for-your-enterprise/enabling-private-mode
versions:
  ghes: '*'
contentType: how-tos
category:
  - Secure and govern your enterprise
---
You must enable private mode if {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} is publicly accessible over the Internet. In private mode, users cannot anonymously clone repositories. If built-in authentication is also enabled, an administrator must invite new users to create an account on the instance. For more information, see [AUTOTITLE](/admin/managing-iam/using-built-in-authentication/configuring-built-in-authentication).

> [!WARNING]
> If you add an image attachment to a pull request or issue comment, anyone can view the anonymized image URL without authentication{% ifversion ghes %}, even if the pull request is in a private repository, or if private mode is enabled. To prevent unauthorized access to the images, ensure that you restrict network access to the systems that serve the images, including {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}{% endif %}.

With private mode enabled, you can allow unauthenticated Git operations (and anyone with network access to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}) to read a public repository's code on your instance with anonymous Git read access enabled. For more information, see [AUTOTITLE](/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise).

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. Select **Private mode**.
1. Under the "Settings" sidebar, click **Save settings**.

   > [!NOTE]
   > Saving settings in the Management Console restarts system services, which could result in user-visible downtime.

1. Wait for the configuration run to complete.
