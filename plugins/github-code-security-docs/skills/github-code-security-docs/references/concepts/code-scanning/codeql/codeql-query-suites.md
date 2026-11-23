---
title: CodeQL query suites
shortTitle: CodeQL query suites
intro: You can choose from different built-in CodeQL query suites to use in your CodeQL code scanning setup.
product: "CodeQL is available for the following repository types:\n\n{%- ifversion fpt %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghec %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{% endif %}"
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/built-in-codeql-query-suites
  - /code-security/code-scanning/managing-your-code-scanning-configuration/built-in-codeql-query-suites
  - /code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites
contentType: concepts
category:
  - Customize vulnerability detection with CodeQL
---

## What are query suites?

Query suites allow you to pass multiple queries to CodeQL without having to specify the path to each query file individually. They provide a way of selecting queries based on their filename, metadata properties, or location on disk or in a CodeQL pack.

You should use query suites for the queries that you want to frequently use in your CodeQL analyses. You can use a built-in query suite available through GitHub, or you can create your own.

## Built-in CodeQL query suites

The built-in CodeQL query suites, `default`, `security-extended`, and `security-and-quality`, are created and maintained by GitHub. The `default` and `security-extended` query suites are available with default setup for every CodeQL-supported language.

Organization owners and security managers can recommend a query suite for use with default setup throughout their organization. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/configure-specific-tools/code-scanning-at-scale).

For a complete list of queries included in each query suite for every language, see [AUTOTITLE](/code-security/reference/code-scanning/codeql/codeql-queries).

### `default` query suite

* The `default` query suite is the group of queries run by default in CodeQL code scanning on GitHub.
* The queries in the `default` query suite are highly precise and return few false positive code scanning results. Relative to the `security-extended` query suite, the `default` suite returns fewer low-confidence code scanning results.
* This query suite is available for use with default setup for code scanning.

### `security-extended` query suite

* The `security-extended` query suite consists of all the queries in the `default` query suite, plus additional queries with slightly lower precision and severity.
* Relative to the `default` query suite, the `security-extended` suite may return a greater number of false positive code scanning results.
* This query suite is available for use with default setup for code scanning, and is referred to as the "Extended" query suite on GitHub.

### `security-and-quality` query suite

* The `security-and-quality` query suite consists of all the queries in the `security-extended` query suite, plus additional queries that identify maintainability and reliability issues.
* This query suite is available for use with advanced setup for code scanning. For more information, see [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configuring-advanced-setup-for-code-scanning).

## Custom query suites

To use a custom query suite, you must configure advanced setup for CodeQL code scanning. For more information, see [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configuring-advanced-setup-for-code-scanning).

Query suite definitions are stored in YAML files with the extension `.qls`. A suite definition is a sequence of instructions, where each instruction is a YAML mapping with (usually) a single key. The instructions are executed in the order they appear in the query suite definition. After all the instructions in the suite definition have been executed, the result is a set of selected queries. For more information, see [AUTOTITLE](/code-security/tutorials/customize-code-scanning/create-query-suites).

## Further reading

* [AUTOTITLE](/code-security/tutorials/customize-code-scanning/create-query-suites)
