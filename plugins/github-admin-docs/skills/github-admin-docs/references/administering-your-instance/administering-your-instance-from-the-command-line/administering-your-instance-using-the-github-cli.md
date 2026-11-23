---
title: Administering your instance using the GitHub CLI
intro: You can administer your GitHub Enterprise Server instance using the GitHub CLI extension for GHES Manage API.
versions:
  feature: ghes-manage-api-cli-extension
shortTitle: Using the GitHub CLI
contentType: how-tos
category:
  - Install and configure your instance
---
## About the `gh es` extension for GitHub CLI

GitHub CLI is an open source tool for using GitHub from your computer's command line. When you're working from the command line, you can use the GitHub CLI to save time and avoid switching context. For more information about the GitHub CLI, see [AUTOTITLE](/github-cli/github-cli/about-github-cli).

`gh es` is a GitHub CLI extension that allows you to perform administrative tasks on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} by using the instance's REST API endpoints. For more information about GitHub CLI extensions, see [AUTOTITLE](/github-cli/github-cli/using-github-cli-extensions).

You can use the `gh es` extension to manage the root site administrator password, configure maintenance mode, view metadata and status information for your instance's nodes, and more. For installation and usage instructions, see the [github/gh-es repository](https://github.com/github/gh-es) on GitHub.com.

## Further reading

* [AUTOTITLE](/rest/enterprise-admin/manage-ghes)
