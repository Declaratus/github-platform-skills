---
title: Uploading a new license to GitHub Enterprise Server
intro: 'You can upload your license file for GitHub Enterprise to your GitHub Enterprise Server instance to validate your application.'
versions:
  ghec: '*'
  ghes: '*'
shortTitle: Upload new license
redirect_from:
  - /billing/managing-your-license-for-github-enterprise/uploading-a-new-license-to-github-enterprise-server
contentType: how-tos
category:
  - Manage enterprise licenses
---

## About license files for GitHub Enterprise Server

When you purchase or download a new license for GitHub Enterprise Server you must upload the new license file to GitHub Enterprise Server to unlock your new user licenses.

If you use GitHub Enterprise Cloud, you can download a license from your enterprise. For more information, see [AUTOTITLE](/billing/concepts/enterprise-billing/ghes-license-files) and [AUTOTITLE](/billing/how-tos/manage-server-licenses/download-your-license).

If you'd like to renew or add user licenses to GitHub Enterprise, or if you have questions about your license, contact [GitHub's Sales team](https://github.com/enterprise/contact). Your new license file will be available for download immediately after you complete your order.

## Uploading your license from the Management Console

1. Sign into GitHub Enterprise Server as a site administrator.
{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. Under **(icon: gear) Settings**, click **{% ifversion fpt or ghec %}Licensing{% elsif ghes %}License{% endif %}**.
1. In the "User licenses" section, under "Quick links", click **Update license**. If prompted, enter the root password for your instance.

   ![Screenshot of the "User licenses" section of the "License" page. A link, labeled "Update license", is outlined in dark orange.](/assets/images/enterprise/management-console/update-license-link.png)
1. To upload your license, click **License file** and select your license file. Alternatively, drag your license file onto the **License file** upload area.

   ![Screenshot of the "License" page of the Management Console. The "License file" upload area is highlighted with an orange outline.](/assets/images/enterprise/management-console/upload-license.png)
1. Click **Upload**. Your license will be updated in the background. The change may take a few minutes before it is visible on your instance.

## Uploading your license with the REST API

You can use the REST API to upload a license to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. {% ifversion ghec %}See [AUTOTITLE](/enterprise-server@latest/rest/enterprise-admin/manage-ghes#upload-an-enterprise-license) in the documentation for GitHub Enterprise Server.{% elsif ghes %}See [AUTOTITLE](/rest/enterprise-admin/manage-ghes#upload-an-enterprise-license).{% endif %}

## Uploading a license with the GitHub CLI

You can import a license to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} using the `gh es` extension of the GitHub CLI. See the [usage instructions](https://github.com/github/gh-es/blob/main/USAGE.md#gh-es-config-import-license) in the `github/gh-es` repository on GitHub.com.

For more information about accessing your instance via the extension, {% ifversion ghec %}see [AUTOTITLE](/enterprise-server@latest/admin/administering-your-instance/administering-your-instance-from-the-command-line/administering-your-instance-using-the-github-cli) in the documentation for GitHub Enterprise Server.{% elsif ghes %}see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-command-line/administering-your-instance-using-the-github-cli).{% endif %}

## Uploading a license via SSH

You can upload and interact with your license from the command line via SSH. See the documentation for the `ghe-license` command in {% ifversion ghec %}[AUTOTITLE](/enterprise-server@latest/admin/administering-your-instance/administering-your-instance-from-the-command-line/command-line-utilities#ghe-license) in the documentation for GitHub Enterprise Server.{% elsif ghes %}[AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-command-line/command-line-utilities#ghe-license).{% endif %}

For more information about accessing your instance via SSH, see {% ifversion ghec %}[AUTOTITLE](/enterprise-server@latest/admin/administering-your-instance/administering-your-instance-from-the-command-line/accessing-the-administrative-shell-ssh) in the documentation for GitHub Enterprise Server.{% elsif ghes %}[AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-command-line/accessing-the-administrative-shell-ssh).{% endif %}
