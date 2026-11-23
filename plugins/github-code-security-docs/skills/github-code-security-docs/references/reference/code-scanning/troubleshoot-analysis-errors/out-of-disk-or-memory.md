---
title: '"Out of disk" and "Out of memory" errors'
shortTitle: Out of disk or memory
intro: If you see one of these errors with GitHub Actions, {% ifversion ghes %}try reviewing the specifications of your self-hosted runners.{% else %}you can try alternative runners.{% endif %}
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/troubleshooting-code-scanning/out-of-disk-or-memory
  - /code-security/how-tos/scan-code-for-vulnerabilities/troubleshooting/troubleshooting-analysis-errors/out-of-disk-or-memory
contentType: reference
category:
  - Troubleshoot security tools
---

<!-- CodeQL CLI depends on a short URL generated from this article's URL. If this article's URL ever changes, make sure to update the short URL https://gh.io/troubleshooting-code-scanning/out-of-disk-or-memory. https://thehub.github.com/it/how-to/url-shortening -->

## About these errors

You may see these errors when running code scanning if {% ifversion ghes %}the runners you're using do not have sufficient free memory or disk space.{% else %}the runners you're using don't meet the recommended hardware requirements.{% endif %}

* `Out of disk`
* `Out of memory`

## Confirming the cause of the problem

You can review the recommended hardware resources for running CodeQL to make sure the runners that you use for code scanning meet those requirements. For more information, see [AUTOTITLE](/code-security/reference/code-scanning/codeql/hardware-resources-for-codeql).

## Fixing the problem

{% ifversion ghes %}

You may need to increase the memory or disk space available on the runners used for code scanning analysis.

{% else %}

If the runners you're using don't meet the recommended hardware requirements, consider using either larger runners or self-hosted runners.

Larger runners are GitHub-hosted runners with more RAM, CPU, and disk space than standard runners. These runners have the runner application and other tools preinstalled. For more information about larger runners and code scanning, see [AUTOTITLE](/actions/how-tos/manage-runners/larger-runners) and [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/manage-your-configuration/configure-larger-runners).

Self-hosted runners offer more control of hardware, operating system, and software tools than GitHub-hosted runners can provide. For more information, see [AUTOTITLE](/actions/concepts/runners/self-hosted-runners).
{% endif %}
