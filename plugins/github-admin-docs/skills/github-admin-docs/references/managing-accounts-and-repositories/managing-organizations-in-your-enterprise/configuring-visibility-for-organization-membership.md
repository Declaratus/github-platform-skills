---
title: Configuring visibility for organization membership
intro: You can set visibility for new organization members across your enterprise to public or private. You can also prevent members from changing their visibility from the default.
redirect_from:
  - /enterprise/admin/user-management/configuring-visibility-for-organization-membership
  - /admin/user-management/configuring-visibility-for-organization-membership
  - /admin/user-management/managing-organizations-in-your-enterprise/configuring-visibility-for-organization-membership
versions:
  ghes: '*'
shortTitle: Set membership visibility
contentType: how-tos
category:
  - Manage accounts and repositories
---
You can also enforce your default setting on all current organization members in your instance using a command-line utility. For example, if you'd like to require every organization member's visibility to be public, you can set the default to public and enforce the default for all new members in the admin settings, and then use the command-line utility to enforce the public setting on existing members.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under {% ifversion ghes %} **(icon: law) Policies**{% else %}"(icon: gear) Settings"{% endif %}, click **Options**.
1. Under "Default organization membership visibility", select the drop-down menu, and click **Private** or **Public**.
1. Optionally, to prevent members from changing their membership visibility from the default, select **Enforce for all enterprise members**.
   ![Screenshot of the "Default organization membership visibility" section. The "Enforce for all enterprise members" checkbox is outlined.](/assets/images/enterprise/site-admin-settings/enforce-default-org-membership-visibility-setting.png)
1. If you'd like to enforce your new visibility setting on all existing members, use the `ghe-org-membership-update` command-line utility. For more information, see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-command-line/command-line-utilities#ghe-org-membership-update).
