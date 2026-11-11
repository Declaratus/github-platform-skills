---
title: Managing policies and features for GitHub Copilot in your enterprise
intro: 'Control the availability of features for GitHub Copilot in your enterprise using policies.'
permissions: Enterprise owners
product: 'Copilot Enterprise or Copilot Business'
versions:
  feature: copilot
allowTitleToDifferFromFilename: true
shortTitle: Manage enterprise policies
redirect_from:
  - /copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise
  - /copilot/how-tos/administer/enterprises/managing-policies-and-features-for-copilot-in-your-enterprise
  - /copilot/how-tos/administer/enterprises/manage-enterprise-policies
  - /copilot/how-tos/administer/manage-for-enterprise/manage-enterprise-policies
contentType: how-tos
category:
  - Manage Copilot for a team
---

When an organization owner assigns a Copilot license to a member of their organization, the availability of features and models is controlled by policies.

If you're setting up Copilot for the first time, see [AUTOTITLE](/copilot/tutorials/roll-out-at-scale/govern-at-scale/govern-for-adoption) for guidance on setting a governance posture that balances compliance with developer productivity.

## Defining policies for your enterprise

Enterprise owners can define a policy for the whole enterprise, or delegate the decision to individual organization owners. See [AUTOTITLE](/copilot/concepts/enterprise/policies).

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: copilot) AI controls**.
1. Navigate to the page containing the policies you want to manage:

   * To view policies for **AI agents**, in the sidebar, click (icon: agent) **Agents**.
   * To view administration, privacy, model, billing, and usage policies for **Copilot**, in the sidebar, click (icon: copilot) **Copilot**.
   * To view policies for **Copilot** features and clients, in the sidebar, click (icon: copilot) **Copilot**, then, under "Features & clients," click **Configure features & clients**.
   * To view policies for **Model Context Protocol (MCP)**, in the sidebar, click (icon: mcp) **MCP**.
1. Configure your policies as follows:
   * For policies with a **dropdown menu**, select the menu and click an enforcement option.
   * For policies with a **toggle**, click the toggle to set availability or enforcement.
   * For policies with **no visible dropdown menu or toggle**, click the name of the policy for configuration options.

> [!NOTE]
> The **MCP servers in Copilot** policy controls use where MCP server support is generally available (GA). This policy does not control access and permissions for the GitHub MCP server in third-party host applications (like Cursor, Windsurf or Claude). For more information on controlling access to the GitHub MCP server, see the [Policies and Governance](https://github.com/github/github-mcp-server/blob/main/docs/policies-and-governance.md#control-mechanisms) documentation in the GitHub MCP Server repository.

## Further reading

* [AUTOTITLE](/copilot/reference/enterprise-administrators/policy-conflicts)
* [AUTOTITLE](/copilot/reference/supported-surfaces-for-policies)
