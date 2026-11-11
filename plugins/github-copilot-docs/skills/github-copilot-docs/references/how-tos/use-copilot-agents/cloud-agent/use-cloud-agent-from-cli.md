---
title: Using Copilot cloud agent from the GitHub CLI
shortTitle: Use cloud agent from the GitHub CLI
intro: 'Start and track Copilot cloud agent sessions from the GitHub CLI.'
product: "Copilot cloud agent is available for all paid Copilot plans.\n\nThe agent is available in all repositories stored on GitHub, except repositories owned by managed user accounts and where it has been explicitly disabled.<br><a href=\"https://github.com/features/copilot/plans?ref_product=copilot&ref_type=purchase&ref_style=button\" target=\"_blank\" class=\"btn btn-primary mt-3 mr-3 no-underline\"><span>Sign up for Copilot</span> (icon: link-external)</a>"
versions:
  feature: copilot
contentType: how-tos
allowTitleToDifferFromFilename: true
category:
  - Author and optimize with Copilot
---

> [!NOTE]
> The `agent-task` command set is only available in v2.80.0 or later of the GitHub CLI. This command set is a public preview and is subject to change.

## Starting a session

You can start a new Copilot cloud agent session with the `gh agent-task create` command.

When you run the command without any arguments, you are asked to enter a prompt. Copilot cloud agent acts on the prompt and opens a pull request in the current repository.

You can use command line options to:

* Provide the prompt (`gh agent-task create "Example prompt"`)
* Choose a base branch, instead of using the repository's default branch (`--base`)
* Select a repository, instead of targeting the current repository (`--repo`)
* Follow the session log in real time (`--follow`)

To see all of the available options, run `gh agent-task create --help`.

## Tracking your sessions

You can see a list of your running and past agent sessions with the `gh agent-task list` command. The output will show a list of your recent sessions.

To see more information on a specific session, use the `gh agent-task view` command. For example, to view information about the session associated with pull request #123 in the `monalisa/bookstore` repository, run `gh agent-task view --repo monalisa/bookstore 123`.

To view the session logs, add the `--log` option. Optionally, use the `--follow` option to stream live logs as the agent works.

To see all of the available options, run `gh agent-task list --help` or `gh agent-task view --help`.

## Further reading

* [AUTOTITLE](/copilot/how-tos/copilot-on-github/use-copilot-agents/manage-and-track-agents)
* [AUTOTITLE](/copilot/tutorials/cloud-agent/get-the-best-results)
