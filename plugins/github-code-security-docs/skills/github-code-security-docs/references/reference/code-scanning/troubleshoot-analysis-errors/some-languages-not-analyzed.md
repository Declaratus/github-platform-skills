---
title: Some languages were not analyzed with CodeQL advanced setup
shortTitle: Some languages not analyzed
allowTitleToDifferFromFilename: true
intro: If some languages were not analyzed, you can modify your code scanning workflow to add a matrix specifying the languages you want to analyze.
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/troubleshooting-code-scanning/some-languages-were-not-analyzed
  - /code-security/code-scanning/troubleshooting-code-scanning/some-languages-not-analyzed
  - /code-security/how-tos/scan-code-for-vulnerabilities/troubleshooting/troubleshooting-analysis-errors/some-languages-not-analyzed
contentType: reference
category:
  - Troubleshoot security tools
---

{% ifversion ghes %}

> [!NOTE]
> This article describes the features available with the version of the CodeQL action and associated CodeQL CLI bundle included in the initial release of this version of GitHub Enterprise Server. If your enterprise uses a more recent version of the CodeQL action, see the [GitHub Enterprise Cloud version](/enterprise-cloud@latest/{{ currentArticle }}) of this article for information on the latest features.
For information on using the latest version, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access).

{% endif %}

If you're using advanced setup and your workflow doesn't explicitly specify the languages to analyze, CodeQL implicitly detects the supported languages in your code base. In this configuration, out of the compiled languages C/C++, C#, Go, Java, Kotlin, {% ifversion codeql-rust-available %}Rust, {% else ifversion codeql-rust-public-preview %}Rust (public preview), {% endif %}and Swift, CodeQL only analyzes the language with the most source files. Edit the workflow and add a matrix specifying the languages you want to analyze. The default CodeQL analysis workflow uses such a matrix.

  The following extracts from a workflow show how you can use a matrix within the job strategy to specify languages, and then reference each language within the "Initialize CodeQL" step:

  ```yaml
  jobs:
    analyze:
      permissions:
        security-events: write
        actions: read
      # ...
      strategy:
        fail-fast: false
        matrix:
          language: ['csharp', 'c-cpp', 'javascript-typescript']

      steps:
      # ...
        - name: Initialize CodeQL
          uses: github/codeql-action/init@v4
          with:
            languages: {% raw %}${{ matrix.language }}{% endraw %}
  ```

  For more information about editing the workflow, see [AUTOTITLE](/code-security/reference/code-scanning/workflow-configuration-options).
