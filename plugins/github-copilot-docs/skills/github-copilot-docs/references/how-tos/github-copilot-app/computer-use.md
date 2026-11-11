---
title: Using the GitHub Copilot app to interact with desktop applications
shortTitle: Computer use
intro: 'With computer use, allow Copilot to interact with local desktop applications from the GitHub Copilot app.'
product: 'The GitHub Copilot app is available for all Copilot plans.<br><a href="https://github.com/features/ai/github-app?utm_source=app-download-docs&utm_medium=docs&utm_campaign=universe-2026" target="_blank" class="btn btn-primary mt-3 mr-3 no-underline js-os-download" data-os-download-mac="https://gh.io/copilot-app-mac" data-os-download-mac-intel="https://gh.io/copilot-app-mac-intel" data-os-download-windows="https://gh.io/copilot-app-win64" data-os-download-windows-arm="https://gh.io/copilot-app-win-arm" data-os-download-linux="https://gh.io/copilot-app-linux" data-os-download-linux-arm="https://github.com/github/app/releases/latest/download/GitHub-Copilot-linux-arm64.AppImage">(icon: desktop-download) <span class="js-os-download-label">Download the GitHub Copilot app</span></a>'
versions:
  feature: copilot
contentType: how-tos
category:
  - Author and optimize with Copilot
---

> [!NOTE]
> Computer use is in public preview and subject to change.

## About computer use

Copilot can interact with desktop applications on your behalf by reading accessible application content and visual context, clicking controls, entering and editing text, pressing keys, scrolling, dragging, and navigating workflows across applications.

This capability is useful for workflows in legacy and GUI-only software that do not provide an API, command-line interface, or MCP integration. It is available for local sessions on macOS and Windows.

Copilot interacts with applications in the background so you can continue working in other applications. On Windows, it brings the target application into focus only when needed, then restores the previously active window.

For information about its capabilities, controls, and limitations, see [AUTOTITLE](/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/computer-use).

## Enabling computer use

1. Open the settings for the GitHub Copilot app.
1. In the sidebar, select **Computer Use**.
1. Under **Enable Computer Use**, turn on **Enable Computer Use**.
1. On macOS, under **Prerequisites**, grant both required permissions:
   * Grant **Accessibility** permission to allow computer use to interact with application controls.
   * Grant **Screen Recording** permission to allow computer use to inspect application windows when visual context is needed.
1. On macOS, if a permission change is not detected, click **Check again**.

You can also use the `/computer on` command in a session. To check the current plugin and MCP status, use `/computer show`.

## Using computer use

Computer use works best when you describe the outcome you want, the applications involved, and any important constraints.

For example:

```text copy
Open APP_NAME and summarize the status information shown in the
main window. Do not change any values or submit any forms.
```

Replace `APP_NAME` with the name of an application installed on your computer.

Computer use follows the app's **Tool Permissions** setting. This setting determines whether Copilot asks for approval before controlling an application. To review or change the setting, open the app settings and select **Sessions**. When approval is required, check that the requested application and action match your prompt. Then choose **Allow** to grant access for the current computer-use session, **Always allow** to save the approval for future sessions, or decline or cancel the request.

To interrupt an active operation, click **Stop** or press <kbd>Esc</kbd>.

## Reviewing always allowed applications

If you choose **Always allow** in the GitHub Copilot app or GitHub Copilot CLI, the approval is saved and applies to both surfaces on the same computer.

1. Open the settings for the GitHub Copilot app.
1. In the sidebar, select **Computer Use**.
1. Under **Always allowed apps**, click the delete icon next to the application.

Removing an application deletes its saved approval for future sessions in both the app and CLI. It does not revoke access already granted in a running session. Click **Stop** or press <kbd>Esc</kbd> to stop the current operation. End the session to revoke application access granted to that session.

## Disabling computer use

Open the settings for the GitHub Copilot app. In the sidebar, select **Computer Use**, then turn off **Enable Computer Use**.

You can also use `/computer off` in a session.

## Troubleshooting computer use

* If the **Computer Use** settings page is not available, confirm that the feature is available for your account and operating system.
* On macOS, if computer use cannot interact with applications, confirm that both **Accessibility** and **Screen Recording** show **Granted** under **Prerequisites**.
