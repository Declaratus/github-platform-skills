---
title: Restrict MCP server access to a custom registry
intro: You can configure an MCP registry URL and access control policy to determine which MCP servers developers can discover and use in supported IDEs and Copilot CLI.
permissions: Enterprise owners and organization owners
product: 'Copilot Enterprise or Copilot Business'
versions:
  feature: copilot
shortTitle: Restrict based on registry
redirect_from:
  - /copilot/how-tos/administer-copilot/configure-mcp-server-access
  - /copilot/how-tos/administer-copilot/manage-for-organization/set-extension-permissions
  - /copilot/how-tos/administer-copilot/manage-mcp-usage/configure-mcp-server-access
contentType: how-tos
category:
  - Manage Copilot for a team
---

> [!IMPORTANT] This feature is in public preview and is not the recommended method for restricting access to MCP servers. The more secure, generally available method is to define settings in your enterprise's `managed-settings.json` file. See [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-enterprise-allowlist).

## Prerequisites

Before you can fully configure MCP server access for your company, you need to create an MCP registry. See [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-mcp-registry).

## Configuring the MCP allowlist policy for an enterprise

To ensure uniform access, you can set and maintain your MCP registry URL and allowlist policy at the enterprise level. Otherwise, if your teams have different needs, you should configure separate policies for each organization.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: copilot) AI controls**.
1. In the sidebar, click (icon: mcp) **MCP**.
1. Ensure **MCP servers in Copilot** is set to **Enabled everywhere**.
1. In the **MCP Registry URL** section, enter the URL of your registry, then click **Save**.

    > [!NOTE]
    > If you set up your MCP registry using Azure API Center, enter the base URL for your API Center, including the workspace path, in the format:
    >
    > ```text
    > https://SERVICE-NAME.data.REGION.azure-apicenter.ms/workspaces/WORKSPACE-NAME
    > ```
    >
    > For example:
    >
    > ```text
    > https://contoso-apic.data.eastus.azure-apicenter.ms/workspaces/default
    > ```
    >
    > Including additional route suffixes like `/v0.1/servers` will cause the registry to error out, because GitHub Copilot appends the MCP v0.1 path automatically.

1. In the **Restrict MCP access to registry servers** section, select the dropdown menu, then click one of the following options:
   * **Allow all**: No restrictions. All MCP servers can be used.
   * **Registry only**: Only servers from the registry may run, so users can't use Copilot connectors. To allow connectors, select **Allow all**.

    Your chosen policy will immediately apply to developers in your enterprise.

## Configuring the MCP allowlist policy for an organization

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the sidebar, under "Code, planning, and automation", click **(icon: copilot) Copilot**, then click **Policies**.
1. In the "Features" section, ensure **MCP servers in Copilot** is set to **Enabled**.
1. In the **MCP Registry URL (optional)** field, enter the URL of your registry, then click **Save**.

    > [!NOTE]
    > If you set up your MCP registry using Azure API Center, enter the base URL for your API Center, including the workspace path, in the format:
    >
    > ```text
    > https://SERVICE-NAME.data.REGION.azure-apicenter.ms/workspaces/WORKSPACE-NAME
    > ```
    >
    > For example:
    >
    > ```text
    > https://contoso-apic.data.eastus.azure-apicenter.ms/workspaces/default
    > ```
    >
    > Including additional route suffixes like `/v0.1/servers` will cause the registry to error out, because GitHub Copilot appends the MCP v0.1 path automatically.

1. In the **Restrict MCP access to registry servers** section, select the dropdown menu, then click one of the following options:
   * **Allow all**: No restrictions. All MCP servers can be used.
   * **Registry only**: Only servers from the registry may run, so users can't use Copilot connectors. To allow connectors, select **Allow all**.

    Your chosen policy will immediately apply to developers in your organization.

## Next steps

For detailed information on MCP allowlist enforcement and limitations, see [AUTOTITLE](/copilot/reference/enterprise-administrators/mcp-private-registry-enforcement).

## Further reading

* [AUTOTITLE](/copilot/reference/supported-surfaces-for-policies)
