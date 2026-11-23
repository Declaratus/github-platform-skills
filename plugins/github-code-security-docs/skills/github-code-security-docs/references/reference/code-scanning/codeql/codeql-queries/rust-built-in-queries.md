---
title: Rust queries for CodeQL analysis
shortTitle: Rust queries
intro: Explore the queries that CodeQL uses to analyze code written in Rust when you select the `default` or the `security-extended` query suite.
product: "CodeQL is available for the following repository types:\n\n{%- ifversion fpt %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghec %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{% endif %}"
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/managing-your-code-scanning-configuration/rust-built-in-queries
  - /code-security/code-scanning/reference/code-ql-built-in-queries/rust-built-in-queries
contentType: reference
category:
  - Find CodeQL CLI commands
---

CodeQL includes many queries for analyzing Rust code. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [AUTOTITLE](/code-security/concepts/code-scanning/codeql/codeql-query-suites).

## Built-in queries for Rust analysis

This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.

{% ifversion ghes %}

> [!NOTE]
> The initial release of GitHub Enterprise Server {{ allVersions[currentVersion].currentRelease }} included CodeQL action and CodeQL CLI {% ifversion ghes < 3.20 %}2.22.4{% elsif ghes < 3.21 %}2.23.9{% elsif ghes < 3.22 %}2.24.3{% elsif ghes < 3.23 %}2.25.6{% endif %}, which may not include all of these queries. Your site administrator can update your CodeQL version to a newer release. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance).

{% endif %}

{% rowheaders %}

| Query name | Related CWEs | Default | Extended | Copilot Autofix |
| --- | --- | --- | --- | --- |
| ['Secure' attribute is not set to true](https://codeql.github.com/codeql-query-help/rust/rust-insecure-cookie/) | 319, 614 | (icon: check) | (icon: check) | (icon: x) |
| [Access of invalid pointer](https://codeql.github.com/codeql-query-help/rust/rust-access-invalid-pointer/) | 476, 825 | (icon: check) | (icon: check) | (icon: x) |
| [Cleartext logging of sensitive information](https://codeql.github.com/codeql-query-help/rust/rust-cleartext-logging/) | 312, 359, 532 | (icon: check) | (icon: check) | (icon: x) |
| [Cleartext storage of sensitive information in a database](https://codeql.github.com/codeql-query-help/rust/rust-cleartext-storage-database/) | 312 | (icon: check) | (icon: check) | (icon: x) |
| [Cleartext transmission of sensitive information](https://codeql.github.com/codeql-query-help/rust/rust-cleartext-transmission/) | 319 | (icon: check) | (icon: check) | (icon: x) |
| [Cross-site scripting](https://codeql.github.com/codeql-query-help/rust/rust-xss/) | 079, 116 | (icon: check) | (icon: check) | (icon: x) |
| [Database query built from user-controlled sources](https://codeql.github.com/codeql-query-help/rust/rust-sql-injection/) | 089 | (icon: check) | (icon: check) | (icon: x) |
| [Disabled TLS certificate check](https://codeql.github.com/codeql-query-help/rust/rust-disabled-certificate-check/) | 295 | (icon: check) | (icon: check) | (icon: x) |
| [Failure to use HTTPS URLs](https://codeql.github.com/codeql-query-help/rust/rust-non-https-url/) | 319, 345 | (icon: check) | (icon: check) | (icon: x) |
| [Hard-coded cryptographic value](https://codeql.github.com/codeql-query-help/rust/rust-hard-coded-cryptographic-value/) | 259, 321, 798, 1204 | (icon: check) | (icon: check) | (icon: x) |
| [Regular expression injection](https://codeql.github.com/codeql-query-help/rust/rust-regex-injection/) | 020, 074 | (icon: check) | (icon: check) | (icon: x) |
| [Server-side request forgery](https://codeql.github.com/codeql-query-help/rust/rust-request-forgery/) | 918 | (icon: check) | (icon: check) | (icon: x) |
| [Uncontrolled allocation size](https://codeql.github.com/codeql-query-help/rust/rust-uncontrolled-allocation-size/) | 770, 789 | (icon: check) | (icon: check) | (icon: x) |
| [Uncontrolled command line](https://codeql.github.com/codeql-query-help/rust/rust-command-line-injection/) | 078, 088 | (icon: check) | (icon: check) | (icon: x) |
| [Uncontrolled data used in path expression](https://codeql.github.com/codeql-query-help/rust/rust-path-injection/) | 022, 023, 036, 073, 099 | (icon: check) | (icon: check) | (icon: x) |
| [Use of a broken or weak cryptographic algorithm](https://codeql.github.com/codeql-query-help/rust/rust-weak-cryptographic-algorithm/) | 327 | (icon: check) | (icon: check) | (icon: x) |
| [Use of a broken or weak cryptographic hashing algorithm on sensitive data](https://codeql.github.com/codeql-query-help/rust/rust-weak-sensitive-data-hashing/) | 327, 328, 916 | (icon: check) | (icon: check) | (icon: x) |
| [Access of a pointer after its lifetime has ended](https://codeql.github.com/codeql-query-help/rust/rust-access-after-lifetime-ended/) | 825 | (icon: x) | (icon: check) | (icon: x) |
| [Log injection](https://codeql.github.com/codeql-query-help/rust/rust-log-injection/) | 117 | (icon: x) | (icon: check) | (icon: x) |

{% endrowheaders %}
