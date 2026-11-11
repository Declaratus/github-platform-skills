---
title: Managing policies and features for GitHub Copilot in your organization
intro: 'Control the availability of GitHub Copilot features and models for users granted a license by your organization.'
permissions: Organization owners
product: 'Organizations with a GitHub Copilot Business or GitHub Copilot Enterprise plan'
versions:
  feature: copilot
allowTitleToDifferFromFilename: true
redirect_from:
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization
  - /copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-business-in-your-organization
  - /copilot/managing-copilot-for-business/managing-policies-for-copilot-for-business-in-your-organization
  - /copilot/managing-copilot-business/managing-policies-for-copilot-business-in-your-organization
  - /copilot/managing-github-copilot-in-your-organization/managing-policies-and-features-for-copilot-in-your-organization
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-and-features-for-copilot-in-your-organization
  - /copilot/github-copilot-chat/copilot-chat-in-github-mobile/enabling-github-copilot-chat-for-github-mobile
  - /copilot/github-copilot-chat/github-copilot-extensions/managing-github-copilot-extensions
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/managing-policies-for-copilot-in-your-organization
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization
  - /copilot/how-tos/administer/organizations/managing-policies-for-copilot-in-your-organization
  - /copilot/how-tos/administer/organizations/manage-policies
  - /copilot/how-tos/administer/manage-for-organization/manage-policies
shortTitle: Manage policies
contentType: how-tos
category:
  - Manage Copilot for a team
---

Copilot policies are also managed at the enterprise level. If your enterprise owner has selected a specific policy, such as enabling a feature everywhere, disabling it everywhere, or enabling it for selected organizations only, you cannot override that setting at the organization level. For information on how policies combine, see [AUTOTITLE](/copilot/concepts/enterprise/policies).

> [!TIP]
> If your organization belongs to an enterprise, see [AUTOTITLE](/copilot/get-started/enterprise-ai-governance) for guidance on coordinating policies with broader governance and rollout decisions.

## Enabling Copilot features and models in your organization

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the sidebar, under "Code, planning, and automation", click **(icon: copilot) Copilot**.
   * Click **Policies** to edit the policies that control privacy and availability of features.
   * Click **Models** to edit the policies that control availability of models beyond the basic models provided with Copilot, which may incur additional costs.
1. For each policy you want to configure, click the dropdown menu and select an enforcement option.

> [!NOTE]
> The **MCP servers in Copilot** policy controls use where MCP server support is generally available (GA). This policy does not control access and permissions for the GitHub MCP server in third-party host applications (like Cursor, Windsurf or Claude). For more information on controlling access to the GitHub MCP server, see the [Policies and Governance](https://github.com/github/github-mcp-server/blob/main/docs/policies-and-governance.md#control-mechanisms) documentation in the GitHub MCP Server repository.

## Opting in to previews or feedback

If your organization has a Copilot Business or Copilot Enterprise plan and you enable "Copilot in GitHub.com", two additional options are displayed:

* **Opt in to user feedback collection:** If enabled, users will see options to provide feedback on selected Copilot features.
* **Opt in to preview features:** If enabled, users can test new Copilot features that are not yet generally available. Be aware that previews of features may have flaws, and the features may be changed or discontinued at any time.

## Further reading

* [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-organization/manage-default-models)
* [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-availability-of-default-models)
* [AUTOTITLE](/copilot/reference/supported-surfaces-for-policies)
