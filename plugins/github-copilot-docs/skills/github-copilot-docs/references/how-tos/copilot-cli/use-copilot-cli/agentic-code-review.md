---
title: Requesting a code review with GitHub Copilot CLI
shortTitle: Agentic code review
allowTitleToDifferFromFilename: true
intro: 'Use Copilot CLI to review your code changes directly from the terminal.'
product: "GitHub Copilot CLI is available with all Copilot plans. If you receive Copilot from an organization, the Copilot CLI policy must be enabled in the organization's settings."
versions:
  feature: copilot
contentType: how-tos
redirect_from:
  - /copilot/how-tos/copilot-cli/use-copilot-cli-agents/agentic-code-review
category:
  - Build with Copilot CLI
docsTeamMetrics:
  - copilot-cli
---

## About agentic code review

You can use the `/review` slash command to have Copilot analyze code changes without leaving the CLI. This lets you get quick feedback on your changes prior to committing.

1. Type `/review` and optionally specify a prompt, path, or file pattern to narrow the review scope, then press <kbd>Enter</kbd>.
1. If Copilot proposes running a command (for example, to inspect a diff or verify a file), review the command, then use the arrow keys to choose an option and press <kbd>Enter</kbd>.
   * Select **Yes** to run the command.
   * Select **No** to skip the command and tell Copilot what to do differently.
1. Read the feedback that Copilot provides about your changes and apply any suggested improvements in your code editor.

## Further reading

* [AUTOTITLE](/copilot/how-tos/copilot-cli/automate-copilot-cli/automate-with-actions)
* [AUTOTITLE](/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions)
