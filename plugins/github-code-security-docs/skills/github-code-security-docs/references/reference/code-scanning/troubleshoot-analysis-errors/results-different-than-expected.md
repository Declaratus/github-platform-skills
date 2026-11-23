---
title: Results are different than expected
shortTitle: Results different than expected
intro: If your code scanning results are different than you expected, you can check which configurations are active.
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/troubleshooting-code-scanning/results-are-different-than-expected
  - /code-security/code-scanning/troubleshooting-code-scanning/results-different-than-expected
  - /code-security/how-tos/scan-code-for-vulnerabilities/troubleshooting/troubleshooting-analysis-errors/results-different-than-expected
contentType: reference
category:
  - Troubleshoot security tools
---

If your code scanning results are different than you expected, you may have both default and advanced setup configured for your repository. When you enable default setup, this disables the existing CodeQL workflow file and blocks any CodeQL API analysis from uploading results.

To check if default setup is enabled, navigate to the main page of the repository, then click **(icon: gear) Settings**. In the "Security" section of the sidebar, click **(icon: codescan) Advanced Security**. In the "Code scanning" section of the page, next to "CodeQL analysis", click (icon: kebab-horizontal). If there is a **(icon: workflow) Switch to advanced** option, you are currently using default setup.

If you want to return to using advanced setup and get code scanning results from your custom workflow file, click **(icon: stop) Disable CodeQL** to disable default setup. Then you should re-enable your pre-existing workflows to start triggering and uploading results from advanced setup. For more information, see [AUTOTITLE](/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows) and [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configuring-advanced-setup-for-code-scanning).

In some cases, your repository may use multiple code scanning configurations. These configurations can generate duplicate alerts. Additionally, stale configurations that no longer run will display outdated alert statuses, and the stale alerts will stay open indefinitely. To avoid outdated alerts, you should remove stale code scanning configurations from a branch. For more information on multiple configurations and deleting stale configurations, see [AUTOTITLE](/code-security/concepts/code-scanning/code-scanning-alerts#about-alerts-from-multiple-configurations) and [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/resolve-alerts#removing-stale-configurations-and-alerts-from-a-branch).
