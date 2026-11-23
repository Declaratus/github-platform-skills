---
title: Editing a custom security configuration
shortTitle: Edit custom configuration
intro: Change the enablement settings in your custom security configuration to better meet the security needs of your repositories.
permissions: '{% ifversion fpt or ghec %}Enterprise owners and members with the **admin** role{% else %}Site administrators{% endif %}'
versions:
  feature: security-configuration-enterprise-level
redirect_from:
  - /admin/managing-code-security/securing-your-enterprise/editing-a-custom-security-configuration
  - /code-security/how-tos/secure-at-scale/configure-enterprise-security/manage-your-coverage/editing-a-custom-security-configuration
contentType: how-tos
category:
  - Secure at scale
---

## About editing a custom security configuration

After creating and applying a custom security configuration, you may need to edit the enablement settings for that configuration to better secure your repositories. Any changes you make to the enablement settings of a security configuration will automatically populate to all linked repositories.

## Modifying your custom security configuration

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. In the left sidebar, click **(icon: codescan) Advanced Security**.
1. In the "Configurations" section, click the name of the custom security configuration you want to edit.
1. Edit the name and description of your custom security configuration as desired.
1. Edit the enablement settings of your custom security configuration as desired.
1. In the "Policy" section, you can modify the configuration's enforcement status. {% ifversion security-configuration-enterprise-organization-enforcement %}{% ifversion fpt or ghec %}Enterprise owners and members with the **admin** role{% else %}Site administrators{% endif %} can block repository owners only, or both repository and organization owners, from changing features that are enabled or disabled by the configuration. Features that are not set aren't enforced. Select **Don't enforce**, **Enforce for repository owners**, or **Enforce for repository and organization owners** from the dropdown menu.{% else %}Enforcing a configuration will block repository owners from changing features that are enabled or disabled by the configuration, but features that are not set aren't enforced. Next to "Enforce configuration", select **Enforce** or **Don't enforce** from the dropdown menu.{% endif %}

    > [!NOTE] Some situations can break the enforcement of security configurations. See [AUTOTITLE](/code-security/reference/security-at-scale/configuration-enforcement).

1. To apply your changes, click **Update configuration**.
