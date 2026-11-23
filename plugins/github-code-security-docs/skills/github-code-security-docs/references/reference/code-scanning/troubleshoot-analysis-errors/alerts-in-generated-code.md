---
title: Alerts found in generated code
shortTitle: Alerts in generated code
intro: When analyzing your code with code scanning, you may wish to build only the code which you wish to analyze.
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/troubleshooting-code-scanning/alerts-found-in-generated-code
  - /code-security/code-scanning/troubleshooting-code-scanning/alerts-in-generated-code
  - /code-security/how-tos/scan-code-for-vulnerabilities/troubleshooting/troubleshooting-analysis-errors/alerts-in-generated-code
contentType: reference
category:
  - Troubleshoot security tools
---

{% ifversion ghes %}

> [!NOTE]
> This article describes the features available with the version of the CodeQL action and associated CodeQL CLI bundle included in the initial release of this version of GitHub Enterprise Server. If your enterprise uses a more recent version of the CodeQL action, see the [GitHub Enterprise Cloud version](/enterprise-cloud@latest/{{ currentArticle }}) of this article for information on the latest features.
For information on using the latest version, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access).

{% endif %}
When using `build-mode: autobuild` or `build-mode: manual`, for compiled languages like Java, Kotlin, Go, C, C++, and C#, CodeQL analyzes all of the code which was built during the workflow run. To limit the amount of code being analyzed, build only the code which you wish to analyze by specifying your own build steps in a `run` block. You can combine specifying your own build steps with using the `paths` or `paths-ignore` filters on the `pull_request` and `push` events to ensure that your workflow only runs when specific code is changed. For more information, see [AUTOTITLE](/actions/reference/workflows-and-actions/workflow-syntax#onpushpull_requestpull_request_targetpathspaths-ignore).

For languages like JavaScript, Python, and TypeScript, that CodeQL analyzes without compiling the source code, or for a compiled language using `build-mode: none`, you can specify additional configuration options to limit the amount of code to analyze. For more information, see [AUTOTITLE](/code-security/reference/code-scanning/workflow-configuration-options#specifying-directories-to-scan).
