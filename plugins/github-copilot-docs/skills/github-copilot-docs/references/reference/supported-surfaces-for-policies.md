---
title: Supported surfaces for GitHub Copilot policies
shortTitle: Supported surfaces for policies
allowTitleToDifferFromFilename: true
intro: 'Which policies affect which Copilot features and surfaces?'
versions:
  feature: copilot
category:
  - Manage Copilot for a team
contentType: reference
---

GitHub Copilot is available across various surfaces: in IDEs, in the CLI, and as multiple agents and chat interfaces on the GitHub website.

A dedicated policy exists to enable or disable each supported feature or surface. Additionally, you can set various policies to customize or control the Copilot experience. However, not every policy applies to every available surface.

## Supported surfaces

{% rowheaders %}

| Policy name | IDEs | Copilot in the cloud (sandbox) | Copilot in the cloud (GitHub Actions) | Copilot CLI | The GitHub Copilot app | Copilot code review |
| --- | --- | --- | --- | --- | --- | --- |
| Editor preview features | (icon: check) | (icon: x) | (icon: x) | (icon: x) | (icon: x) | (icon: x) |
| Copilot can search the web | (icon: check) | (icon: check) | (icon: x) | (icon: x) | (icon: x) | (icon: x) |
| Configure custom models | (icon: check) | (icon: x) | (icon: x) | (icon: check) | (icon: check) | (icon: x) |
| Suggestions matching public code | (icon: check) | (icon: x) | (icon: check)[^1] | (icon: x) | (icon: x) | (icon: x) |
| MCP servers in Copilot | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Restrict MCP access to registry servers | (icon: check) | (icon: x) | (icon: x) | (icon: check) | (icon: check) | (icon: x) |
| Content exclusion | (icon: check)[^4] | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Configure models | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: x) |
| Copilot Memory | (icon: check)[^2] | (icon: check) | (icon: check) | (icon: check) | (icon: check)[^3] | (icon: check) |

{% endrowheaders %}

[^1]: Only supported in annotate mode. See [AUTOTITLE](/copilot/responsible-use/agents#7-limitations).

[^2]: Supported in Copilot sessions that run in Visual Studio Code's **Local Agent Host**. The application also requires its own Copilot Memory setting to be enabled. See [AUTOTITLE](/copilot/how-tos/use-copilot-agents/copilot-memory/manage-for-yourself#copilot-memory-in-visual-studio-code).

[^3]: In the GitHub Copilot app, this policy applies where Copilot Memory is available for the user's account. The app's separate project **Memory** setting is not the same feature. See [AUTOTITLE](/copilot/concepts/prompting-and-context/copilot-memory#where-copilot-memory-is-available).

[^4] For a detailed breakdown by IDE, see [AUTOTITLE](/copilot/concepts/security-governance-and-network-settings/content-exclusion#availability-of-content-exclusion).

## More information on Copilot in the cloud

"Copilot in the cloud" refers to cloud sessions running on cloud sandboxes or GitHub Actions. Users can start cloud sessions from local clients. The columns for local clients in the table refer to local sessions in those clients.

Coverage of policies and enterprise managed settings currently varies between environments. Where users can choose between these environments, cloud sandboxes are the default. However, currently, some interfaces can only run on GitHub Actions (such as assigning an issue to Copilot or mentioning `@Copilot` in a pull request).