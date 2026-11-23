---
title: Working with push protection and the GitHub MCP server
shortTitle: Push protection and the GitHub MCP server
intro: Learn how you are protected from leaking secrets during interactions with the GitHub MCP server, and how to bypass a push protection block if you need to.
product: Public repositories on GitHub.com
permissions: 'Users with **write** access'
versions:
  feature: copilot
redirect_from:
  - /code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-and-the-github-mcp-server
  - /code-security/concepts/secret-security/working-with-push-protection-and-the-github-mcp-server
  - /code-security/concepts/secret-security/push-protection-with-the-github-mcp-server
contentType: concepts
category:
  - Protect your secrets
---

## About push protection and the GitHub MCP server

Push protection prevents you from inadvertently exposing secrets, such as tokens, keys and credentials, in your repository.

When you're interacting with the GitHub MCP server, push protection blocks secrets in AI-generated responses as well as preventing secrets from being included in any actions you perform, such as creating an issue.

This protection is on by default for all interactions between the GitHub MCP server and **public repositories**; and between the GitHub MCP server and private repositories covered by GitHub Advanced Security, regardless of whether push protection is enabled on the repository's security settings page.

## Resolving a block

To resolve the block, you can either:

* **Remove** the secret from the content of your request before trying again.
* **Bypass the block.** If push protection is enabled for the repository, or you have push protection enabled for your personal account, you'll see an option to bypass the push protection block. You should carefully evaluate if it's safe to include the secret in your request before continuing.

## Further reading

* [AUTOTITLE](/code-security/concepts/secret-security/push-protection)
* [About the GitHub MCP server](/copilot/concepts/customizations/mcp#about-the-github-mcp-server)
* [AUTOTITLE](/code-security/how-tos/use-ghas-with-ai-coding-agents/scan-for-secrets-with-github-mcp-server)
