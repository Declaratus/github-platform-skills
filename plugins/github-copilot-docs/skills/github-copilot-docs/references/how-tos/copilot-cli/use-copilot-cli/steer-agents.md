---
title: Steering agents in GitHub Copilot CLI
shortTitle: Steer agents
intro: Guide Copilot during task execution to keep work on track with your intent.
product: 'GitHub Copilot CLI is available with all Copilot plans. If you receive Copilot from an organization, the Copilot CLI policy must be enabled in the organization's settings.'
versions:
  feature: copilot
contentType: how-tos
redirect_from:
  - /copilot/how-tos/copilot-cli/use-copilot-cli-agents/steer-agents
category:
  - Build with Copilot CLI
docsTeamMetrics:
  - copilot-cli
---

## Steer the conversation while Copilot is thinking

While Copilot is working on a task, you can enter a new prompt at any time. By default, a plain prompt you send while Copilot is thinking is treated as steering and is considered in the context of the current task.

## Queue a prompt to be processed next

You can also queue a message instead of steering with it, by pressing <kbd>Ctrl</kbd>+<kbd>Enter</kbd> (or <kbd>Ctrl</kbd>+<kbd>Q</kbd>) instead of <kbd>Enter</kbd>. A queued message waits until the current task finishes, then runs as the next turn, instead of being folded into the task that's in progress. For information about canceling operations with queued prompts, see [AUTOTITLE](/copilot/how-tos/copilot-cli/use-copilot-cli/roll-back-changes#canceling-an-operation).

Steering lets you:

* Interrupt an agent that is heading in the wrong direction.
* Provide inline feedback when rejecting a tool permission request.
* Refine or clarify the task scope partway through execution.

## Next steps

To learn how to use Copilot CLI to get an AI-powered review of your code changes, see [AUTOTITLE](/copilot/how-tos/copilot-cli/use-copilot-cli/agentic-code-review).
