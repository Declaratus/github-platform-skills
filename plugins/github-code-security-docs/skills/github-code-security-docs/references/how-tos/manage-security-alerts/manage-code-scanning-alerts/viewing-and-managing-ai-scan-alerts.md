---
title: Viewing and managing AI Scan alerts on your repository''s default branch
shortTitle: 'Manage AI Scan backlog alerts'
intro: 'Run an AI Scan, review the alerts in your code scanning backlog, and check fixes for security vulnerabilities.'
allowTitleToDifferFromFilename: true
permissions: 'Users with **write** access'
versions:
  feature: ai-scan-for-repositories
contentType: how-tos
category:
  - Find and fix code vulnerabilities
---

> [!NOTE]
> AI Scan for repositories is in public preview and subject to change.

## Prerequisites

AI Scan for repositories must be enabled for your repository. See [AUTOTITLE](/code-security/concepts/code-scanning/ai-scan-for-repositories#enabling-ai-scan-for-repositories).

## Running a scan

Scans analyze your repository's default branch.

1. On GitHub, navigate to the main page of the repository.
1. Under the repository name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab. If you cannot see the "(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" tab, select the **(icon: kebab-horizontal)** dropdown menu, and then click **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}**.
1. In the left sidebar, click **(icon: codescan) Code scanning**.
1. In the top right corner, select the **AI Scan** dropdown.
1. From the dropdown, to the right of **Standard scan**, click to start the scan.
1. Wait for the scan to complete.

## Viewing AI Scan alerts

When the scan finishes, its findings appear in the code scanning alert list. Filter the list by the **AI Scan** tool to review them.

Use the existing alert assessment and remediation workflows:

* To review and prioritize findings, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/assess-alerts).
* To fix alerts manually or with Copilot, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/resolve-alerts).

## Checking fixes and closing alerts

After a potential fix is merged into the default branch, repeat the steps in [Running a scan](#running-a-scan). Merging a fix does not automatically trigger another AI Scan.

During public preview, an alert only closes automatically after a new scan if the fix changes the exact line of code that triggered the alert. Otherwise, you must manually close the alert.