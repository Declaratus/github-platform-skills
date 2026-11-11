---
title: Finding existing vulnerabilities in code
shortTitle: Find vulnerabilities
intro: Copilot Chat can help find common vulnerabilities in your code and suggest fixes.
redirect_from:
  - /copilot/example-prompts-for-github-copilot-chat/security-analysis/finding-existing-vulnerabilities-in-code
  - /copilot/copilot-chat-cookbook/security-analysis/finding-existing-vulnerabilities-in-code
  - /copilot/tutorials/copilot-chat-cookbook/security-analysis/finding-existing-vulnerabilities-in-code
  - /copilot/tutorials/copilot-chat-cookbook/security-analysis/find-vulnerabilities
  - /copilot/tutorials/copilot-chat-cookbook/analyze-security/find-vulnerabilities
versions:
  feature: copilot
category:
  - Security analysis
  - Author and optimize with Copilot
  - Improve quality and maintainability
surface:
  - Chat
octicon: code
contentType: tutorials
---

While they may be considered "common knowledge" by many developers, the vast majority of newly introduced security weaknesses are due to vulnerabilities like cross-site scripting (XSS), SQL injection, and cross-site request forgery (CSRF). These vulnerabilities can be mitigated by following secure coding practices, such as using parameterized queries, input validation, and avoiding hard-coded sensitive data. GitHub Copilot can help detect and resolve these issues.

> [!NOTE] While Copilot Chat can help find some common security vulnerabilities and help you fix them, you should not rely on Copilot for a comprehensive security analysis. Using code scanning will more thoroughly ensure your code is secure. For more information on setting up code scanning, see [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configure-code-scanning).

## Example scenario

The JavaScript code below has a potential XSS vulnerability that could be exploited if the `name` parameter is not properly sanitized before being displayed on the page.

```javascript id=potential-xss
function displayName(name) {
  const nameElement = document.getElementById('name-display');
  nameElement.innerHTML = `Showing results for "${name}"`
}
```

## Example prompt

You can ask Copilot Chat to analyze code for common security vulnerabilities and provide explanations and fixes for the issues it finds.

```copilot copy prompt ref=potential-xss
Analyze this code for potential security vulnerabilities and suggest fixes.
```

## Example response

> [!NOTE] The following response is an example. Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.

Copilot responds with an explanation of the vulnerability, and suggested changes to the code to fix it.

```javascript
function displayName(name) {
  const nameElement = document.getElementById('name-display');
  nameElement.textContent = `Showing results for "${name}"`;
}
```

## Further reading

* [AUTOTITLE](/copilot/concepts/prompting-and-context/prompt-engineering)
* [AUTOTITLE](/copilot/get-started/best-practices)
* [AUTOTITLE](/code-security/concepts/code-scanning/code-scanning)
