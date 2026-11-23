---
title: Upload fails because GitHub Code Security is disabled
shortTitle: 'GitHub Code Security disabled'
allowTitleToDifferFromFilename: true
intro: You can only upload SARIF results to {% ifversion fpt or ghec %}private or internal {% endif %}repositories where GitHub Code Security is enabled.
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/troubleshooting-sarif/ghas-required
  - /code-security/code-scanning/troubleshooting-sarif-uploads/ghas-required
  - /code-security/how-tos/scan-code-for-vulnerabilities/troubleshooting/troubleshooting-sarif-uploads/ghas-required
contentType: reference
category:
  - Troubleshoot security tools
---

## About this error

```text
GitHub Code Security or GitHub Advanced Security not enabled
GitHub Code Security or GitHub Advanced Security blocked by a policy
403: GitHub Code Security or GitHub Advanced Security is not enabled
```

This error is reported if a process attempts to upload a SARIF file to a repository where GitHub Code Security is not enabled or where use of this feature is blocked by a policy.

You will only see this error for SARIF files that contain results created using CodeQL{% ifversion fpt or ghec %} and for uploads to repositories with private or internal visibility. GitHub Code Security is enabled by default for all public repositories{% endif %}.

For information on how to confirm this error and fix the problem, see [AUTOTITLE](/code-security/reference/code-scanning/troubleshoot-analysis-errors/advanced-security-must-be-enabled).
