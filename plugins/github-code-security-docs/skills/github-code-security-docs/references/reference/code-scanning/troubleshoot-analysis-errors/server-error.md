---
title: 'Error: "Server error"'
shortTitle: Server error
intro: If you see this error, it may be transient. Check the current GitHub Actions service status, and try running your workflow again.
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/troubleshooting-code-scanning/server-error
  - /code-security/how-tos/scan-code-for-vulnerabilities/troubleshooting/troubleshooting-analysis-errors/server-error
contentType: reference
category:
  - Troubleshoot security tools
---

## About this error

```text
Server error
```

If the run of a workflow for code scanning fails due to a server error, this may be due to a transient communication issue.

## Confirming the cause of the error

You can check the current "Actions" service status on the [Status Dashboard](https://www.githubstatus.com/).

## Fixing the problem

Try running the workflow again. If the problem persists, contact {% ifversion fpt or ghec %}us through the [GitHub Support portal](https://support.github.com){% elsif ghes %}your site administrator{% endif %}.
