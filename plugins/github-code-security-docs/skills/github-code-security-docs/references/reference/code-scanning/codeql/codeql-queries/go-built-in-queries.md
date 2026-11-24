---
title: Go queries for CodeQL analysis
shortTitle: Go queries
intro: Explore the queries that CodeQL uses to analyze code written in Go (Golang) when you select the `default` or the `security-extended` query suite.
product: "CodeQL is available for the following repository types:\n\n{%- ifversion fpt %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghec %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{% endif %}"
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/managing-your-code-scanning-configuration/go-built-in-queries
  - /code-security/code-scanning/reference/code-ql-built-in-queries/go-built-in-queries
contentType: reference
category:
  - Find CodeQL CLI commands
---

CodeQL includes many queries for analyzing Go code. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [AUTOTITLE](/code-security/concepts/code-scanning/codeql/codeql-query-suites).

## Built-in queries for Go analysis

This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.

{% ifversion ghes %}

> [!NOTE]
> The initial release of GitHub Enterprise Server {{ allVersions[currentVersion].currentRelease }} included CodeQL action and CodeQL CLI {% ifversion ghes < 3.20 %}2.22.4{% elsif ghes < 3.21 %}2.23.9{% elsif ghes < 3.22 %}2.24.3{% elsif ghes < 3.23 %}2.25.6{% elsif ghes < 3.24 %}2.27.0{% endif %}, which may not include all of these queries. Your site administrator can update your CodeQL version to a newer release. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance).

{% endif %}

{% rowheaders %}

| Query name | Related CWEs | Default | Extended | Copilot Autofix |
| --- | --- | --- | --- | --- |
| [Arbitrary file access during archive extraction ("Zip Slip")](https://codeql.github.com/codeql-query-help/go/go-zipslip/) | 022 | (icon: check) | (icon: check) | (icon: check) |
| [Arbitrary file write extracting an archive containing symbolic links](https://codeql.github.com/codeql-query-help/go/go-unsafe-unzip-symlink/) | 022 | (icon: check) | (icon: check) | (icon: check) |
| [Bad redirect check](https://codeql.github.com/codeql-query-help/go/go-bad-redirect-check/) | 601 | (icon: check) | (icon: check) | (icon: check) |
| [Clear-text logging of sensitive information](https://codeql.github.com/codeql-query-help/go/go-clear-text-logging/) | 312, 315, 359 | (icon: check) | (icon: check) | (icon: check) |
| [Command built from user-controlled sources](https://codeql.github.com/codeql-query-help/go/go-command-injection/) | 078 | (icon: check) | (icon: check) | (icon: x) |
| [Cookie 'HttpOnly' attribute is not set to true](https://codeql.github.com/codeql-query-help/go/go-cookie-httponly-not-set/) | 1004 | (icon: check) | (icon: check) | (icon: x) |
| [Cookie 'Secure' attribute is not set to true](https://codeql.github.com/codeql-query-help/go/go-cookie-secure-not-set/) | 614 | (icon: check) | (icon: check) | (icon: x) |
| [Cross-site scripting via HTML template escaping bypass](https://codeql.github.com/codeql-query-help/go/go-html-template-escaping-bypass-xss/) | 079, 116 | (icon: check) | (icon: check) | (icon: x) |
| [Database query built from user-controlled sources](https://codeql.github.com/codeql-query-help/go/go-sql-injection/) | 089 | (icon: check) | (icon: check) | (icon: check) |
| [Disabled TLS certificate check](https://codeql.github.com/codeql-query-help/go/go-disabled-certificate-check/) | 295 | (icon: check) | (icon: check) | (icon: check) |
| [Email content injection](https://codeql.github.com/codeql-query-help/go/go-email-injection/) | 640 | (icon: check) | (icon: check) | (icon: check) |
| [Incomplete regular expression for hostnames](https://codeql.github.com/codeql-query-help/go/go-incomplete-hostname-regexp/) | 020 | (icon: check) | (icon: check) | (icon: check) |
| [Incomplete URL scheme check](https://codeql.github.com/codeql-query-help/go/go-incomplete-url-scheme-check/) | 020 | (icon: check) | (icon: check) | (icon: check) |
| [Incorrect conversion between integer types](https://codeql.github.com/codeql-query-help/go/go-incorrect-integer-conversion/) | 190, 681 | (icon: check) | (icon: check) | (icon: check) |
| [Information exposure through a stack trace](https://codeql.github.com/codeql-query-help/go/go-stack-trace-exposure/) | 209, 497 | (icon: check) | (icon: check) | (icon: check) |
| [Insecure TLS configuration](https://codeql.github.com/codeql-query-help/go/go-insecure-tls/) | 327 | (icon: check) | (icon: check) | (icon: check) |
| [Missing JWT signature check](https://codeql.github.com/codeql-query-help/go/go-missing-jwt-signature-check/) | 347 | (icon: check) | (icon: check) | (icon: check) |
| [Missing regular expression anchor](https://codeql.github.com/codeql-query-help/go/go-regex-missing-regexp-anchor/) | 020 | (icon: check) | (icon: check) | (icon: check) |
| [Open URL redirect](https://codeql.github.com/codeql-query-help/go/go-unvalidated-url-redirection/) | 601 | (icon: check) | (icon: check) | (icon: check) |
| [Potentially unsafe quoting](https://codeql.github.com/codeql-query-help/go/go-unsafe-quoting/) | 078, 089, 094 | (icon: check) | (icon: check) | (icon: check) |
| [Reflected cross-site scripting](https://codeql.github.com/codeql-query-help/go/go-reflected-xss/) | 079, 116 | (icon: check) | (icon: check) | (icon: check) |
| [Size computation for allocation may overflow](https://codeql.github.com/codeql-query-help/go/go-allocation-size-overflow/) | 190 | (icon: check) | (icon: check) | (icon: check) |
| [Slice memory allocation with excessive size value](https://codeql.github.com/codeql-query-help/go/go-uncontrolled-allocation-size/) | 770 | (icon: check) | (icon: check) | (icon: check) |
| [Suspicious characters in a regular expression](https://codeql.github.com/codeql-query-help/go/go-suspicious-character-in-regex/) | 020 | (icon: check) | (icon: check) | (icon: check) |
| [Uncontrolled data used in network request](https://codeql.github.com/codeql-query-help/go/go-request-forgery/) | 918 | (icon: check) | (icon: check) | (icon: x) |
| [Uncontrolled data used in path expression](https://codeql.github.com/codeql-query-help/go/go-path-injection/) | 022, 023, 036, 073, 099 | (icon: check) | (icon: check) | (icon: check) |
| [Use of a broken or weak cryptographic algorithm](https://codeql.github.com/codeql-query-help/go/go-weak-cryptographic-algorithm/) | 327, 328 | (icon: check) | (icon: check) | (icon: x) |
| [Use of a broken or weak cryptographic hashing algorithm on sensitive data](https://codeql.github.com/codeql-query-help/go/go-weak-sensitive-data-hashing/) | 327, 328, 916 | (icon: check) | (icon: check) | (icon: x) |
| [Use of a weak cryptographic key](https://codeql.github.com/codeql-query-help/go/go-weak-crypto-key/) | 326 | (icon: check) | (icon: check) | (icon: check) |
| [Use of constant `state` value in OAuth 2.0 URL](https://codeql.github.com/codeql-query-help/go/go-constant-oauth2-state/) | 352 | (icon: check) | (icon: check) | (icon: check) |
| [Use of insecure HostKeyCallback implementation](https://codeql.github.com/codeql-query-help/go/go-insecure-hostkeycallback/) | 322 | (icon: check) | (icon: check) | (icon: check) |
| [Use of insufficient randomness as the key of a cryptographic algorithm](https://codeql.github.com/codeql-query-help/go/go-insecure-randomness/) | 338 | (icon: check) | (icon: check) | (icon: check) |
| [XPath injection](https://codeql.github.com/codeql-query-help/go/go-xml-xpath-injection/) | 643 | (icon: check) | (icon: check) | (icon: check) |
| [Log entries created from user input](https://codeql.github.com/codeql-query-help/go/go-log-injection/) | 117 | (icon: x) | (icon: check) | (icon: check) |

{% endrowheaders %}
