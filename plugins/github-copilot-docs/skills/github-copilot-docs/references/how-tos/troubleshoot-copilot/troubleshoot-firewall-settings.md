---
title: Troubleshooting firewall settings for GitHub Copilot
intro: Troubleshooting help for firewall-related errors.
versions:
  feature: copilot
shortTitle: Troubleshoot firewall settings
redirect_from:
  - /copilot/troubleshooting-github-copilot/troubleshooting-firewall-settings-for-github-copilot
  - /copilot/how-tos/troubleshoot/troubleshooting-firewall-settings-for-github-copilot
  - /copilot/how-tos/troubleshoot/troubleshoot-firewall-settings
contentType: how-tos
category:
  - Troubleshooting Copilot
---

## About the problem

If you or your company uses a firewall, Copilot may not function as expected. Copilot interacts with a remote machine learning model and checks for updates, and a firewall may block important traffic and degrade the user experience.

## Solving the problem

For an optimal Copilot experience, you should create an "allowlist" that lets certain URLs, ports, and protocols through your firewall. See [AUTOTITLE](/copilot/reference/copilot-allowlist-reference).
