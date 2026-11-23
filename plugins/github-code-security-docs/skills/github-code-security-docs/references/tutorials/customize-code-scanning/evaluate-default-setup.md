---
title: Evaluating default setup for code scanning
shortTitle: Evaluate default setup
intro: Learn how to assess how code scanning is working for you, and how you can customize your setup to best meet your needs.
permissions: 'Repository owners, organization owners, security managers, and users with the **admin** role'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/enabling-code-scanning/evaluating-default-setup-for-code-scanning
  - /code-security/tutorials/customize-code-scanning/evaluating-default-setup-for-code-scanning
contentType: tutorials
category:
  - Find and fix code vulnerabilities
---

When you first start using code scanning, you'll likely use default setup. This guide describes how to evaluate how default setup for code scanning is working for you, and what steps to take if something isn't working as you expect. This guide also describes how you can customize code scanning if you find that you have a specific use case that your new configuration doesn't fit.

## Customizing code scanning

When you first configure default setup, or after an initial analysis of your code, you can edit which languages default setup will analyze and the query suite run during analysis. The `default` query suite contains a set of queries that are carefully designed to look for the most relevant security issues, while minimizing false positive results. However, you can use the `security-extended` suite to run additional queries, which have slightly lower precision. For more information on the available query suites, see [AUTOTITLE](/code-security/concepts/code-scanning/codeql/codeql-query-suites).

For more information about customizing default setup, see [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/manage-your-configuration/edit-default-setup).

### Using advanced setup

If you've found that you still need more granular control over code scanning, you can use advanced setup. Advanced setup requires significantly more effort to configure, customize, and maintain, so we recommend enabling default setup first. For more information about advanced setup, see [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configuring-advanced-setup-for-code-scanning) and [AUTOTITLE](/code-security/reference/code-scanning/workflow-configuration-options).

## Evaluating code scanning with the tool status page

The tool status page shows useful information about all of your code scanning tools. You can use it to investigate whether individual tools are working for a repository, when files in the repository were first scanned and most recently scanned, and when upcoming scans are scheduled. It's also a useful starting point for debugging issues.

Using the tool status page, you can download the list of rules that code scanning is checking against, in CSV format. For integrated tools like CodeQL, you can also see more detailed information, including a percentage of files scanned and specific error messages.

If you find that default setup doesn't scan all your files, you may need to customize code scanning. For more information, see [Customizing code scanning](#customizing-code-scanning) in this article. Alternatively, or if something else isn't working as you expect, you may find our dedicated troubleshooting documentation useful. For more information, see [AUTOTITLE](/code-security/reference/code-scanning/troubleshoot-analysis-errors).

For more detailed information about the tool status page, see [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/manage-your-configuration/use-the-tools-status-page-for-code-scanning#viewing-the-tool-status-page-for-a-repository).
