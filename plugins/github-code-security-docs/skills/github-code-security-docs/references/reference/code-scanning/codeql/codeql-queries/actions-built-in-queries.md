---
title: GitHub Actions queries for CodeQL analysis
shortTitle: Actions queries
intro: Explore the queries that CodeQL uses to analyze code written in GitHub Actions workflow files when you select the `default` or the `security-extended` query suite.
product: "CodeQL is available for the following repository types:\n\n{%- ifversion fpt %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghec %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{% endif %}"
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/managing-your-code-scanning-configuration/actions-built-in-queries
  - /code-security/code-scanning/managing-your-code-scanning-configuration/github-actions-built-in-queries
  - /code-security/code-scanning/reference/code-ql-built-in-queries/actions-built-in-queries
contentType: reference
category:
  - Find CodeQL CLI commands
---

CodeQL includes many queries for analyzing GitHub Actions workflows. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [AUTOTITLE](/code-security/concepts/code-scanning/codeql/codeql-query-suites).

## Built-in queries for GitHub Actions analysis

This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.

{% ifversion ghes %}

> [!NOTE]
> The initial release of GitHub Enterprise Server {{ allVersions[currentVersion].currentRelease }} included CodeQL action and CodeQL CLI {% ifversion ghes < 3.20 %}2.22.4{% elsif ghes < 3.21 %}2.23.9{% elsif ghes < 3.22 %}2.24.3{% elsif ghes < 3.23 %}2.25.6{% endif %}, which may not include all of these queries. Your site administrator can update your CodeQL version to a newer release. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance).

{% endif %}

{% rowheaders %}

| Query name | Related CWEs | Default | Extended | Copilot Autofix |
| --- | --- | --- | --- | --- |
| [Artifact poisoning](https://codeql.github.com/codeql-query-help/actions/actions-artifact-poisoning-critical/) | 829 | (icon: check) | (icon: check) | (icon: check) |
| [Cache Poisoning via caching of untrusted files](https://codeql.github.com/codeql-query-help/actions/actions-cache-poisoning-direct-cache/) | 349 | (icon: check) | (icon: check) | (icon: check) |
| [Cache Poisoning via code injection](https://codeql.github.com/codeql-query-help/actions/actions-cache-poisoning-code-injection/) | 349, 094 | (icon: check) | (icon: check) | (icon: check) |
| [Cache Poisoning via execution of untrusted code](https://codeql.github.com/codeql-query-help/actions/actions-cache-poisoning-poisonable-step/) | 349 | (icon: check) | (icon: check) | (icon: check) |
| [Checkout of untrusted code in a privileged context](https://codeql.github.com/codeql-query-help/actions/actions-untrusted-checkout-high/) | 829 | (icon: check) | (icon: check) | (icon: x) |
| [Checkout of untrusted code in a privileged context](https://codeql.github.com/codeql-query-help/actions/actions-untrusted-checkout-critical/) | 829 | (icon: check) | (icon: check) | (icon: x) |
| [Code injection](https://codeql.github.com/codeql-query-help/actions/actions-code-injection-critical/) | 094, 095, 116 | (icon: check) | (icon: check) | (icon: check) |
| [Environment variable built from user-controlled sources](https://codeql.github.com/codeql-query-help/actions/actions-envvar-injection-critical/) | 077, 020 | (icon: check) | (icon: check) | (icon: check) |
| [Excessive Secrets Exposure](https://codeql.github.com/codeql-query-help/actions/actions-excessive-secrets-exposure/) | 312 | (icon: check) | (icon: check) | (icon: check) |
| [Improper Access Control](https://codeql.github.com/codeql-query-help/actions/actions-improper-access-control/) | 285 | (icon: check) | (icon: check) | (icon: check) |
| [PATH environment variable built from user-controlled sources](https://codeql.github.com/codeql-query-help/actions/actions-envpath-injection-critical/) | 077, 020 | (icon: check) | (icon: check) | (icon: check) |
| [Storage of sensitive information in GitHub Actions artifact](https://codeql.github.com/codeql-query-help/actions/actions-secrets-in-artifacts/) | 312 | (icon: check) | (icon: check) | (icon: check) |
| [Unmasked Secret Exposure](https://codeql.github.com/codeql-query-help/actions/actions-unmasked-secret-exposure/) | 312 | (icon: check) | (icon: check) | (icon: check) |
| [Untrusted Checkout TOCTOU](https://codeql.github.com/codeql-query-help/actions/actions-untrusted-checkout-toctou-high/) | 367 | (icon: check) | (icon: check) | (icon: check) |
| [Untrusted Checkout TOCTOU](https://codeql.github.com/codeql-query-help/actions/actions-untrusted-checkout-toctou-critical/) | 367 | (icon: check) | (icon: check) | (icon: check) |
| [Use of a known vulnerable action](https://codeql.github.com/codeql-query-help/actions/actions-vulnerable-action/) | 1395 | (icon: check) | (icon: check) | (icon: check) |
| [Workflow does not contain permissions](https://codeql.github.com/codeql-query-help/actions/actions-missing-workflow-permissions/) | 275 | (icon: check) | (icon: check) | (icon: check) |
| [Artifact poisoning](https://codeql.github.com/codeql-query-help/actions/actions-artifact-poisoning-medium/) | 829 | (icon: x) | (icon: check) | (icon: check) |
| [Checkout of untrusted code in a non-privileged context](https://codeql.github.com/codeql-query-help/actions/actions-untrusted-checkout-medium/) | 829 | (icon: x) | (icon: check) | (icon: check) |
| [Code injection](https://codeql.github.com/codeql-query-help/actions/actions-code-injection-medium/) | 094, 095, 116 | (icon: x) | (icon: check) | (icon: check) |
| [Environment variable built from user-controlled sources](https://codeql.github.com/codeql-query-help/actions/actions-envvar-injection-medium/) | 077, 020 | (icon: x) | (icon: check) | (icon: check) |
| [PATH environment variable built from user-controlled sources](https://codeql.github.com/codeql-query-help/actions/actions-envpath-injection-medium/) | 077, 020 | (icon: x) | (icon: check) | (icon: check) |
| [Unpinned tag for a non-immutable Action or reusable workflow](https://codeql.github.com/codeql-query-help/actions/actions-unpinned-tag/) | 829 | (icon: x) | (icon: check) | (icon: x) |

{% endrowheaders %}
