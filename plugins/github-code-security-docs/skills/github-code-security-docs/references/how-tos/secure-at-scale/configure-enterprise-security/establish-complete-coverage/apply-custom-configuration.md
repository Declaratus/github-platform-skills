---
title: Applying a custom security configuration to your enterprise
shortTitle: Apply custom configuration
intro: You can apply your custom security configuration to organizations and repositories in your organization to meet the specific security needs of your enterprise.
permissions: '{% ifversion fpt or ghec %}Enterprise owners and members with the **admin** role{% else %}Site administrators{% endif %}'
versions:
  feature: security-configuration-enterprise-level
redirect_from:
  - /admin/managing-code-security/securing-your-enterprise/applying-a-custom-security-configuration-to-your-enterprise
  - /code-security/how-tos/secure-at-scale/configure-enterprise-security/establish-complete-coverage/applying-a-custom-security-configuration-to-your-enterprise
contentType: how-tos
category:
  - Secure at scale
---

## About applying a custom security configuration

After you create a custom security configuration, you need to apply it to repositories in your enterprise to enable the configuration's settings on those repositories.

The repository list displays each repository's configuration status. For the full list of statuses and recommended actions, see [AUTOTITLE](/code-security/reference/security-at-scale/configuration-statuses).

{% ifversion fpt or ghec %}
>[!NOTE] Some features enabled in security configurations may use GitHub Actions runner compute. GitHub will let you know if that's the case when you apply the configuration to a repository. For more information about billing for GitHub Actions, see [AUTOTITLE](/billing/concepts/product-billing/github-actions).
{% endif %}

## Applying your custom security configuration to repositories in your enterprise

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. In the left sidebar, click **(icon: codescan) Advanced Security**.
1. To the right of the configuration you want to apply, select the **Apply to** (icon: triangle-down) dropdown menu, then click **All repositories** or **All repositories without configurations**.
<!--Based on testing on 2025-03-31 this additional option is available only when you apply configurations at the enterprise level.-->
1. Optionally, in the confirmation dialog, you can choose to automatically apply the security configuration to newly created repositories depending on their visibility. Select the **None** (icon: triangle-down) dropdown menu, then click **Public**, or **Private and internal**, or both.

1. Review the detailed information about how your changes will affect GitHub Secret Protection, GitHub Code Security, or GitHub Advanced Security license consumption. To apply the security configuration, click **Apply**.

The security configuration is applied to both active and archived repositories because some security features run on archived repositories, for example, secret scanning. In addition, if a repository is later unarchived you can be confident that it is protected by the chosen security configuration.

If security configurations fail to apply to some organizations in your enterprise, GitHub will display a banner on the UI to let you know. You can click the links on the banner to get more information about the organizations and repositories involved.

## Next steps

To learn how to edit your custom security configuration, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/manage-your-coverage/edit-custom-configuration).
