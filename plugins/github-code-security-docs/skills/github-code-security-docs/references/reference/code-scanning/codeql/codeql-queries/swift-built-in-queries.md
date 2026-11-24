---
title: Swift queries for CodeQL analysis
shortTitle: Swift queries
intro: Explore the queries that CodeQL uses to analyze code written in Swift when you select the `default` or the `security-extended` query suite.
product: "CodeQL is available for the following repository types:\n\n{%- ifversion fpt %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghec %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{% endif %}"
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/managing-your-code-scanning-configuration/swift-built-in-queries
  - /code-security/code-scanning/reference/code-ql-built-in-queries/swift-built-in-queries
contentType: reference
category:
  - Find CodeQL CLI commands
---

CodeQL includes many queries for analyzing Swift code. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [AUTOTITLE](/code-security/concepts/code-scanning/codeql/codeql-query-suites).

## Built-in queries for Swift analysis

This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.

{% ifversion ghes %}

> [!NOTE]
> The initial release of GitHub Enterprise Server {{ allVersions[currentVersion].currentRelease }} included CodeQL action and CodeQL CLI {% ifversion ghes < 3.20 %}2.22.4{% elsif ghes < 3.21 %}2.23.9{% elsif ghes < 3.22 %}2.24.3{% elsif ghes < 3.23 %}2.25.6{% elsif ghes < 3.24 %}2.27.0{% endif %}, which may not include all of these queries. Your site administrator can update your CodeQL version to a newer release. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance).

{% endif %}

{% rowheaders %}

| Query name | Related CWEs | Default | Extended | Copilot Autofix |
| --- | --- | --- | --- | --- |
| [Bad HTML filtering regexp](https://codeql.github.com/codeql-query-help/swift/swift-bad-tag-filter/) | 116, 020, 185, 186 | (icon: check) | (icon: check) | (icon: check) |
| [Cleartext logging of sensitive information](https://codeql.github.com/codeql-query-help/swift/swift-cleartext-logging/) | 312, 359, 532 | (icon: check) | (icon: check) | (icon: check) |
| [Cleartext storage of sensitive information in a local database](https://codeql.github.com/codeql-query-help/swift/swift-cleartext-storage-database/) | 312 | (icon: check) | (icon: check) | (icon: check) |
| [Cleartext storage of sensitive information in an application preference store](https://codeql.github.com/codeql-query-help/swift/swift-cleartext-storage-preferences/) | 312 | (icon: check) | (icon: check) | (icon: check) |
| [Cleartext transmission of sensitive information](https://codeql.github.com/codeql-query-help/swift/swift-cleartext-transmission/) | 319 | (icon: check) | (icon: check) | (icon: x) |
| [Database query built from user-controlled sources](https://codeql.github.com/codeql-query-help/swift/swift-sql-injection/) | 089 | (icon: check) | (icon: check) | (icon: check) |
| [Encryption using ECB](https://codeql.github.com/codeql-query-help/swift/swift-ecb-encryption/) | 327 | (icon: check) | (icon: check) | (icon: check) |
| [Incomplete regular expression for hostnames](https://codeql.github.com/codeql-query-help/swift/swift-incomplete-hostname-regexp/) | 020 | (icon: check) | (icon: check) | (icon: check) |
| [Inefficient regular expression](https://codeql.github.com/codeql-query-help/swift/swift-redos/) | 1333, 730, 400 | (icon: check) | (icon: check) | (icon: x) |
| [Insecure TLS configuration](https://codeql.github.com/codeql-query-help/swift/swift-insecure-tls/) | 757 | (icon: check) | (icon: check) | (icon: check) |
| [Insufficient hash iterations](https://codeql.github.com/codeql-query-help/swift/swift-insufficient-hash-iterations/) | 916 | (icon: check) | (icon: check) | (icon: check) |
| [Missing regular expression anchor](https://codeql.github.com/codeql-query-help/swift/swift-missing-regexp-anchor/) | 020 | (icon: check) | (icon: check) | (icon: check) |
| [Predicate built from user-controlled sources](https://codeql.github.com/codeql-query-help/swift/swift-predicate-injection/) | 943 | (icon: check) | (icon: check) | (icon: check) |
| [Regular expression injection](https://codeql.github.com/codeql-query-help/swift/swift-regex-injection/) | 730, 400 | (icon: check) | (icon: check) | (icon: check) |
| [Resolving XML external entity in user-controlled data](https://codeql.github.com/codeql-query-help/swift/swift-xxe/) | 611, 776, 827 | (icon: check) | (icon: check) | (icon: check) |
| [Static initialization vector for encryption](https://codeql.github.com/codeql-query-help/swift/swift-static-initialization-vector/) | 329, 1204 | (icon: check) | (icon: check) | (icon: check) |
| [String length conflation](https://codeql.github.com/codeql-query-help/swift/swift-string-length-conflation/) | 135 | (icon: check) | (icon: check) | (icon: check) |
| [System command built from user-controlled sources](https://codeql.github.com/codeql-query-help/swift/swift-command-line-injection/) | 078, 088 | (icon: check) | (icon: check) | (icon: check) |
| [Uncontrolled data used in path expression](https://codeql.github.com/codeql-query-help/swift/swift-path-injection/) | 022, 023, 036, 073, 099 | (icon: check) | (icon: check) | (icon: check) |
| [Uncontrolled format string](https://codeql.github.com/codeql-query-help/swift/swift-uncontrolled-format-string/) | 134 | (icon: check) | (icon: check) | (icon: check) |
| [Unsafe WebView fetch](https://codeql.github.com/codeql-query-help/swift/swift-unsafe-webview-fetch/) | 079, 095, 749 | (icon: check) | (icon: check) | (icon: check) |
| [Use of a broken or weak cryptographic hashing algorithm on sensitive data](https://codeql.github.com/codeql-query-help/swift/swift-weak-sensitive-data-hashing/) | 327, 328 | (icon: check) | (icon: check) | (icon: check) |
| [Use of an inappropriate cryptographic hashing algorithm on passwords](https://codeql.github.com/codeql-query-help/swift/swift-weak-password-hashing/) | 327, 328, 916 | (icon: check) | (icon: check) | (icon: check) |
| [Use of constant salts](https://codeql.github.com/codeql-query-help/swift/swift-constant-salt/) | 760 | (icon: check) | (icon: check) | (icon: check) |
| [JavaScript Injection](https://codeql.github.com/codeql-query-help/swift/swift-unsafe-js-eval/) | 094, 095, 749 | (icon: x) | (icon: check) | (icon: check) |

{% endrowheaders %}
