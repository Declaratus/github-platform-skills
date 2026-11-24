---
title: Code scanning with CodeQL
shortTitle: CodeQL code scanning
intro: You can use CodeQL to identify vulnerabilities and errors in your code. The results are shown as code scanning alerts in GitHub.
product: "Code scanning is available for the following repository types:\n\n* Public repositories on GitHub.com\n* Organization-owned repositories on GitHub Team, GitHub Enterprise Cloud, or GitHub Enterprise Server, with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled."
redirect_from:
  - /code-security/secure-coding/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-code-scanning-with-codeql
  - /code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-code-scanning-with-codeql
  - /code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql
  - /code-security/concepts/code-scanning/codeql/about-code-scanning-with-codeql
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
contentType: concepts
category:
  - Find and fix code vulnerabilities
---

{% ifversion ghes %}

> [!NOTE]
> Your site administrator must enable code scanning before you can use this feature. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance).
>
> You may not be able to enable or disable code scanning if an enterprise owner has set a GitHub Code Security policy at the enterprise level. For more information, see [AUTOTITLE](/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise).

{% endif %}

CodeQL is the code analysis engine developed by GitHub to automate security checks. You can analyze your code using CodeQL and display the results as code scanning alerts.

There are three main ways to use CodeQL analysis for code scanning:

* Use default setup to quickly configure CodeQL analysis for code scanning on your repository. Default setup automatically chooses the languages to analyze, query suite to run, and events that trigger scans. If you prefer, you can manually select the query suite to run and languages to analyze. After you enable CodeQL, GitHub Actions will execute workflow runs to scan your code. For more information, see [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configure-code-scanning).
* Use advanced setup to add the CodeQL workflow to your repository. This generates a customizable workflow file which uses the [github/codeql-action](https://github.com/github/codeql-action/) to run the CodeQL CLI. For more information, see [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configuring-advanced-setup-for-code-scanning#configuring-advanced-setup-for-code-scanning-with-codeql).

* Run the CodeQL CLI directly in an external CI system and upload the results to GitHub. For more information, see [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/integrate-with-existing-tools/use-with-existing-ci-system).

{% ifversion ghes %}

> [!NOTE]
> On GitHub Enterprise Server {{ allVersions[currentVersion].currentRelease }}, the CodeQL action uses CodeQL CLI version {% ifversion ghes < 3.20 %}2.22.4{% elsif ghes < 3.21 %}2.23.9{% elsif ghes < 3.22 %}2.24.3{% elsif ghes < 3.23 %}2.25.6{% elsif ghes < 3.24 %}2.27.0{% endif %} by default. We recommend that you use the same version of the CodeQL CLI if you run analysis in an external CI system.

{% endif %}

For information about code scanning alerts, see [AUTOTITLE](/code-security/concepts/code-scanning/code-scanning-alerts).

## About CodeQL

CodeQL is a programming language and associated tools that treat code like data. It was created explicitly to make it easier to analyze code and find potential vulnerabilities in your code with greater confidence than traditional static analyzers.

1. You generate a CodeQL database to represent your codebase.
1. Then you run CodeQL queries on that database to identify problems in the codebase.
1. The query results are shown as code scanning alerts in GitHub when you use CodeQL with code scanning.

CodeQL supports both compiled and interpreted languages, and can find vulnerabilities and errors in code that's written in the supported languages.

CodeQL supports the following languages:

<!-- If you update the list of supported languages for CodeQL, update docs-internal/content/get-started/learning-about-github/github-language-support.md to reflect the changes. -->
* C/C++
* C#
* Go
* Java/Kotlin
* JavaScript/TypeScript
* Python
* Ruby{% ifversion codeql-rust-available %}
* Rust{% else ifversion codeql-rust-public-preview %}
* Rust (public preview){% endif %}
* Swift
* GitHub Actions workflows

> [!NOTE]
>
> * Use `java-kotlin` to analyze code written in Java, Kotlin or both.
> * Use `javascript-typescript` to analyze code written in JavaScript, TypeScript or both.

For more information, see the documentation on the CodeQL website: [Supported languages and frameworks](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/).

> [!IMPORTANT]
> CodeQL does **not** support languages that are not listed above. This includes, but is not limited to, **PHP**, **Scala**, and others. Attempting to use CodeQL with unsupported languages may result in no alerts being generated and incomplete analysis.

## Modeling custom or niche frameworks

GitHub experts, security researchers, and community contributors write libraries to model the flow of data in popular frameworks and libraries. If you use custom dependencies that aren't modeled, then you can use the CodeQL extension for Visual Studio Code to create models for these dependencies and use them to extend your analysis. For more information, see [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/scan-from-vs-code/use-the-model-editor).

## CodeQL queries

GitHub experts, security researchers, and community contributors write and maintain the default CodeQL queries used for code scanning. The queries are regularly updated to improve analysis and reduce any false positive results.{% ifversion ghes %} For details of the queries available in the default and extended packs, see [Queries included in the default and security-extended query suites](/code-security/concepts/code-scanning/codeql/codeql-query-suites#queries-included-in-the-default-and-security-extended-query-suites).{% endif %}

### Writing your own queries

The queries are open source, so you can view and contribute to the queries in the [github/codeql](https://github.com/github/codeql) repository. For more information, see [About CodeQL queries](https://codeql.github.com/docs/writing-codeql-queries/about-codeql-queries/) in the CodeQL documentation.

### Running additional queries

If you are scanning your code with advanced setup or an external CI system, you can run additional queries as part of your analysis.

These queries must belong to a published CodeQL query pack or a CodeQL pack in a repository.

* When a CodeQL query pack is published to the GitHub Container registry, all the transitive dependencies required by the queries and a compilation cache are included in the package. This improves performance and ensures that running the queries in the pack gives identical results every time until you upgrade to a new version of the pack or the CLI.

* CodeQL query packs can be downloaded from multiple GitHub container registries. For more information, see [AUTOTITLE](/code-security/reference/code-scanning/workflow-configuration-options#downloading-codeql-packs-from-github-enterprise-server).

For more information, see [AUTOTITLE](/code-security/tutorials/customize-code-scanning/customize-analysis).
