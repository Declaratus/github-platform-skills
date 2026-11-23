---
title: Deleting a custom security configuration
shortTitle: Delete custom configuration
intro: You can delete unnecessary custom security configurations in your enterprise.
permissions: '{% ifversion fpt or ghec %}Enterprise owners and members with the **admin** role{% else %}Site administrators{% endif %}'
versions:
  feature: security-configuration-enterprise-level
redirect_from:
  - /admin/managing-code-security/securing-your-enterprise/deleting-a-custom-security-configuration
  - /code-security/how-tos/secure-at-scale/configure-enterprise-security/manage-your-coverage/deleting-a-custom-security-configuration
contentType: how-tos
category:
  - Secure at scale
---

## About deleting a custom security configuration

If you no longer need a custom security configuration, you can delete that configuration to ensure it will not be applied to any repositories in the future. If you want to delete a custom security configuration because you want to change the security enablement settings in that configuration, consider editing the configuration instead. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/manage-your-coverage/edit-custom-configuration).

> [!WARNING]
> Deleting a custom security configuration will detach all repositories that are linked to that configuration. The existing security settings for those repositories will be unchanged, but you must apply a different security configuration or manage their security settings at the repository level to keep their settings up to date.

## Deleting a custom security configuration from your enterprise

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. In the left sidebar, click **(icon: codescan) Advanced Security**.
1. In the configurations table, click the name of the custom security configuration you want to delete.
1. In the "Edit configuration" page, scroll to the bottom of the page, then click **Delete configuration**.
1. Ensure you read the warning in the "Delete this configuration?" dialog, to confirm you are comfortable deleting the custom security configuration, then click **Delete configuration**.
