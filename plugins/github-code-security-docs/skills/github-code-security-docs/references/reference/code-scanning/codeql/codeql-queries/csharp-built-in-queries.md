---
title: C# queries for CodeQL analysis
shortTitle: C# queries
intro: Explore the queries that CodeQL uses to analyze code written in C# when you select the `default` or the `security-extended` query suite.
product: "CodeQL is available for the following repository types:\n\n{%- ifversion fpt %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghec %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{% endif %}"
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/managing-your-code-scanning-configuration/csharp-built-in-queries
  - /code-security/code-scanning/reference/code-ql-built-in-queries/csharp-built-in-queries
contentType: reference
category:
  - Find CodeQL CLI commands
---

CodeQL includes many queries for analyzing C# code. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [AUTOTITLE](/code-security/concepts/code-scanning/codeql/codeql-query-suites).

## Built-in queries for C# analysis

This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.

{% ifversion ghes %}

> [!NOTE]
> The initial release of GitHub Enterprise Server {{ allVersions[currentVersion].currentRelease }} included CodeQL action and CodeQL CLI {% ifversion ghes < 3.20 %}2.22.4{% elsif ghes < 3.21 %}2.23.9{% elsif ghes < 3.22 %}2.24.3{% elsif ghes < 3.23 %}2.25.6{% elsif ghes < 3.24 %}2.27.0{% endif %}, which may not include all of these queries. Your site administrator can update your CodeQL version to a newer release. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance).

{% endif %}

{% rowheaders %}

| Query name | Related CWEs | Default | Extended | Copilot Autofix |
| --- | --- | --- | --- | --- |
| ['requireSSL' attribute is not set to true](https://codeql.github.com/codeql-query-help/csharp/cs-web-requiressl-not-set/) | 319, 614 | (icon: check) | (icon: check) | (icon: check) |
| [Arbitrary file access during archive extraction ("Zip Slip")](https://codeql.github.com/codeql-query-help/csharp/cs-zipslip/) | 022 | (icon: check) | (icon: check) | (icon: check) |
| [ASP.NET config file enables directory browsing](https://codeql.github.com/codeql-query-help/csharp/cs-web-directory-browse-enabled/) | 548 | (icon: check) | (icon: check) | (icon: check) |
| [Assembly path injection](https://codeql.github.com/codeql-query-help/csharp/cs-assembly-path-injection/) | 073, 114 | (icon: check) | (icon: check) | (icon: check) |
| [Clear text storage of sensitive information](https://codeql.github.com/codeql-query-help/csharp/cs-cleartext-storage-of-sensitive-information/) | 312, 315, 359 | (icon: check) | (icon: check) | (icon: check) |
| [Cookie 'HttpOnly' attribute is not set to true](https://codeql.github.com/codeql-query-help/csharp/cs-web-cookie-httponly-not-set/) | 1004 | (icon: check) | (icon: check) | (icon: x) |
| [Cookie 'Secure' attribute is not set to true](https://codeql.github.com/codeql-query-help/csharp/cs-web-cookie-secure-not-set/) | 319, 614 | (icon: check) | (icon: check) | (icon: x) |
| [Cookie security: overly broad domain](https://codeql.github.com/codeql-query-help/csharp/cs-web-broad-cookie-domain/) | 287 | (icon: check) | (icon: check) | (icon: check) |
| [Cookie security: overly broad path](https://codeql.github.com/codeql-query-help/csharp/cs-web-broad-cookie-path/) | 287 | (icon: check) | (icon: check) | (icon: check) |
| [Cookie security: persistent cookie](https://codeql.github.com/codeql-query-help/csharp/cs-web-persistent-cookie/) | 539 | (icon: check) | (icon: check) | (icon: check) |
| [Creating an ASP.NET debug binary may reveal sensitive information](https://codeql.github.com/codeql-query-help/csharp/cs-web-debug-binary/) | 011, 532 | (icon: check) | (icon: check) | (icon: check) |
| [Cross-site scripting](https://codeql.github.com/codeql-query-help/csharp/cs-web-xss/) | 079, 116 | (icon: check) | (icon: check) | (icon: check) |
| [Denial of Service from comparison of user input against expensive regex](https://codeql.github.com/codeql-query-help/csharp/cs-redos/) | 1333, 730, 400 | (icon: check) | (icon: check) | (icon: check) |
| [Deserialization of untrusted data](https://codeql.github.com/codeql-query-help/csharp/cs-unsafe-deserialization-untrusted-input/) | 502 | (icon: check) | (icon: check) | (icon: check) |
| [Deserialized delegate](https://codeql.github.com/codeql-query-help/csharp/cs-deserialized-delegate/) | 502 | (icon: check) | (icon: check) | (icon: check) |
| [Encryption using ECB](https://codeql.github.com/codeql-query-help/csharp/cs-ecb-encryption/) | 327 | (icon: check) | (icon: check) | (icon: check) |
| [Exposure of private information](https://codeql.github.com/codeql-query-help/csharp/cs-exposure-of-sensitive-information/) | 359 | (icon: check) | (icon: check) | (icon: check) |
| [Failure to abandon session](https://codeql.github.com/codeql-query-help/csharp/cs-session-reuse/) | 384 | (icon: check) | (icon: check) | (icon: check) |
| [Header checking disabled](https://codeql.github.com/codeql-query-help/csharp/cs-web-disabled-header-checking/) | 113 | (icon: check) | (icon: check) | (icon: check) |
| [Improper control of generation of code](https://codeql.github.com/codeql-query-help/csharp/cs-code-injection/) | 094, 095, 096 | (icon: check) | (icon: check) | (icon: check) |
| [Information exposure through an exception](https://codeql.github.com/codeql-query-help/csharp/cs-information-exposure-through-exception/) | 209, 497 | (icon: check) | (icon: check) | (icon: check) |
| [Information exposure through transmitted data](https://codeql.github.com/codeql-query-help/csharp/cs-sensitive-data-transmission/) | 201 | (icon: check) | (icon: check) | (icon: check) |
| [Insecure randomness](https://codeql.github.com/codeql-query-help/csharp/cs-insecure-randomness/) | 338 | (icon: check) | (icon: check) | (icon: check) |
| [LDAP query built from user-controlled sources](https://codeql.github.com/codeql-query-help/csharp/cs-ldap-injection/) | 090 | (icon: check) | (icon: check) | (icon: check) |
| [Log entries created from user input](https://codeql.github.com/codeql-query-help/csharp/cs-log-forging/) | 117 | (icon: check) | (icon: check) | (icon: check) |
| [Missing clickjacking protection](https://codeql.github.com/codeql-query-help/csharp/cs-web-missing-x-frame-options/) | 451, 829 | (icon: check) | (icon: check) | (icon: x) |
| [Missing cross-site request forgery token validation](https://codeql.github.com/codeql-query-help/csharp/cs-web-missing-token-validation/) | 352 | (icon: check) | (icon: check) | (icon: check) |
| [Missing global error handler](https://codeql.github.com/codeql-query-help/csharp/cs-web-missing-global-error-handler/) | 012, 248 | (icon: check) | (icon: check) | (icon: check) |
| [Page request validation is disabled](https://codeql.github.com/codeql-query-help/csharp/cs-web-request-validation-disabled/) | 016 | (icon: check) | (icon: check) | (icon: check) |
| [Regular expression injection](https://codeql.github.com/codeql-query-help/csharp/cs-regex-injection/) | 730, 400 | (icon: check) | (icon: check) | (icon: check) |
| [Resource injection](https://codeql.github.com/codeql-query-help/csharp/cs-resource-injection/) | 099 | (icon: check) | (icon: check) | (icon: check) |
| [SQL query built from user-controlled sources](https://codeql.github.com/codeql-query-help/csharp/cs-sql-injection/) | 089 | (icon: check) | (icon: check) | (icon: check) |
| [Uncontrolled command line](https://codeql.github.com/codeql-query-help/csharp/cs-command-line-injection/) | 078, 088 | (icon: check) | (icon: check) | (icon: check) |
| [Uncontrolled data used in path expression](https://codeql.github.com/codeql-query-help/csharp/cs-path-injection/) | 022, 023, 036, 073, 099 | (icon: check) | (icon: check) | (icon: check) |
| [Uncontrolled format string](https://codeql.github.com/codeql-query-help/csharp/cs-uncontrolled-format-string/) | 134 | (icon: check) | (icon: check) | (icon: check) |
| [Untrusted XML is read insecurely](https://codeql.github.com/codeql-query-help/csharp/cs-xml-insecure-dtd-handling/) | 611, 827, 776 | (icon: check) | (icon: check) | (icon: check) |
| [Unvalidated local pointer arithmetic](https://codeql.github.com/codeql-query-help/csharp/cs-unvalidated-local-pointer-arithmetic/) | 119, 120, 122, 788 | (icon: check) | (icon: check) | (icon: check) |
| [URL redirection from remote source](https://codeql.github.com/codeql-query-help/csharp/cs-web-unvalidated-url-redirection/) | 601 | (icon: check) | (icon: check) | (icon: check) |
| [User-controlled bypass of sensitive method](https://codeql.github.com/codeql-query-help/csharp/cs-user-controlled-bypass/) | 807, 247, 350 | (icon: check) | (icon: check) | (icon: check) |
| [Weak encryption](https://codeql.github.com/codeql-query-help/csharp/cs-weak-encryption/) | 327 | (icon: check) | (icon: check) | (icon: check) |
| [Weak encryption: inadequate RSA padding](https://codeql.github.com/codeql-query-help/csharp/cs-inadequate-rsa-padding/) | 327, 780 | (icon: check) | (icon: check) | (icon: check) |
| [Weak encryption: Insufficient key size](https://codeql.github.com/codeql-query-help/csharp/cs-insufficient-key-size/) | 326 | (icon: check) | (icon: check) | (icon: check) |
| [XML injection](https://codeql.github.com/codeql-query-help/csharp/cs-xml-injection/) | 091 | (icon: check) | (icon: check) | (icon: check) |
| [XPath injection](https://codeql.github.com/codeql-query-help/csharp/cs-xml-xpath-injection/) | 643 | (icon: check) | (icon: check) | (icon: check) |
| [Empty password in configuration file](https://codeql.github.com/codeql-query-help/csharp/cs-empty-password-in-configuration/) | 258, 862 | (icon: x) | (icon: check) | (icon: x) |
| [Insecure Direct Object Reference](https://codeql.github.com/codeql-query-help/csharp/cs-web-insecure-direct-object-reference/) | 639 | (icon: x) | (icon: check) | (icon: check) |
| [Insecure SQL connection](https://codeql.github.com/codeql-query-help/csharp/cs-insecure-sql-connection/) | 327 | (icon: x) | (icon: check) | (icon: check) |
| [Missing function level access control](https://codeql.github.com/codeql-query-help/csharp/cs-web-missing-function-level-access-control/) | 285, 284, 862 | (icon: x) | (icon: check) | (icon: check) |
| [Missing XML validation](https://codeql.github.com/codeql-query-help/csharp/cs-xml-missing-validation/) | 112 | (icon: x) | (icon: check) | (icon: check) |
| [Serialization check bypass](https://codeql.github.com/codeql-query-help/csharp/cs-serialization-check-bypass/) | 020 | (icon: x) | (icon: check) | (icon: check) |
| [Thread-unsafe capturing of an ICryptoTransform object](https://codeql.github.com/codeql-query-help/csharp/cs-thread-unsafe-icryptotransform-captured-in-lambda/) | 362 | (icon: x) | (icon: check) | (icon: check) |
| [Thread-unsafe use of a static ICryptoTransform field](https://codeql.github.com/codeql-query-help/csharp/cs-thread-unsafe-icryptotransform-field-in-class/) | 362 | (icon: x) | (icon: check) | (icon: check) |
| [Use of file upload](https://codeql.github.com/codeql-query-help/csharp/cs-web-file-upload/) | 434 | (icon: x) | (icon: check) | (icon: check) |
| [Value shadowing](https://codeql.github.com/codeql-query-help/csharp/cs-web-ambiguous-client-variable/) | 348 | (icon: x) | (icon: check) | (icon: check) |
| [Value shadowing: server variable](https://codeql.github.com/codeql-query-help/csharp/cs-web-ambiguous-server-variable/) | 348 | (icon: x) | (icon: check) | (icon: check) |

{% endrowheaders %}
