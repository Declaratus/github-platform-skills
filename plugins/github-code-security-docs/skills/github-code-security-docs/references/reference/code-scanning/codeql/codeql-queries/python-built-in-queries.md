---
title: Python queries for CodeQL analysis
shortTitle: Python queries
intro: Explore the queries that CodeQL uses to analyze code written in Python when you select the `default` or the `security-extended` query suite.
product: "CodeQL is available for the following repository types:\n\n{%- ifversion fpt %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghec %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{% endif %}"
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/managing-your-code-scanning-configuration/python-built-in-queries
  - /code-security/code-scanning/reference/code-ql-built-in-queries/python-built-in-queries
contentType: reference
category:
  - Find CodeQL CLI commands
---

CodeQL includes many queries for analyzing Python code. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [AUTOTITLE](/code-security/concepts/code-scanning/codeql/codeql-query-suites).

## Built-in queries for Python analysis

This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.

{% ifversion ghes %}

> [!NOTE]
> The initial release of GitHub Enterprise Server {{ allVersions[currentVersion].currentRelease }} included CodeQL action and CodeQL CLI {% ifversion ghes < 3.20 %}2.22.4{% elsif ghes < 3.21 %}2.23.9{% elsif ghes < 3.22 %}2.24.3{% elsif ghes < 3.23 %}2.25.6{% elsif ghes < 3.24 %}2.27.0{% endif %}, which may not include all of these queries. Your site administrator can update your CodeQL version to a newer release. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance).

{% endif %}

{% rowheaders %}

| Query name | Related CWEs | Default | Extended | Copilot Autofix |
| --- | --- | --- | --- | --- |
| ['input' function used in Python 2](https://codeql.github.com/codeql-query-help/python/py-use-of-input/) | 094, 095 | (icon: check) | (icon: check) | (icon: check) |
| [Accepting unknown SSH host keys when using Paramiko](https://codeql.github.com/codeql-query-help/python/py-paramiko-missing-host-key-validation/) | 295 | (icon: check) | (icon: check) | (icon: check) |
| [Bad HTML filtering regexp](https://codeql.github.com/codeql-query-help/python/py-bad-tag-filter/) | 116, 020, 185, 186 | (icon: check) | (icon: check) | (icon: check) |
| [Binding a socket to all network interfaces](https://codeql.github.com/codeql-query-help/python/py-bind-socket-all-network-interfaces/) | 200 | (icon: check) | (icon: check) | (icon: check) |
| [Clear-text logging of sensitive information](https://codeql.github.com/codeql-query-help/python/py-clear-text-logging-sensitive-data/) | 312, 359, 532 | (icon: check) | (icon: check) | (icon: check) |
| [Clear-text storage of sensitive information](https://codeql.github.com/codeql-query-help/python/py-clear-text-storage-sensitive-data/) | 312, 315, 359 | (icon: check) | (icon: check) | (icon: check) |
| [Code injection](https://codeql.github.com/codeql-query-help/python/py-code-injection/) | 094, 095, 116 | (icon: check) | (icon: check) | (icon: check) |
| [Construction of a cookie using user-supplied input](https://codeql.github.com/codeql-query-help/python/py-cookie-injection/) | 020 | (icon: check) | (icon: check) | (icon: check) |
| [CSRF protection weakened or disabled](https://codeql.github.com/codeql-query-help/python/py-csrf-protection-disabled/) | 352 | (icon: check) | (icon: check) | (icon: check) |
| [Default version of SSL/TLS may be insecure](https://codeql.github.com/codeql-query-help/python/py-insecure-default-protocol/) | 327 | (icon: check) | (icon: check) | (icon: check) |
| [Deserialization of user-controlled data](https://codeql.github.com/codeql-query-help/python/py-unsafe-deserialization/) | 502 | (icon: check) | (icon: check) | (icon: check) |
| [Failure to use secure cookies](https://codeql.github.com/codeql-query-help/python/py-insecure-cookie/) | 614 | (icon: check) | (icon: check) | (icon: check) |
| [Flask app is run in debug mode](https://codeql.github.com/codeql-query-help/python/py-flask-debug/) | 215, 489 | (icon: check) | (icon: check) | (icon: check) |
| [Full server-side request forgery](https://codeql.github.com/codeql-query-help/python/py-full-ssrf/) | 918 | (icon: check) | (icon: check) | (icon: check) |
| [HTTP Response Splitting](https://codeql.github.com/codeql-query-help/python/py-http-response-splitting/) | 113, 079 | (icon: check) | (icon: check) | (icon: check) |
| [Incomplete regular expression for hostnames](https://codeql.github.com/codeql-query-help/python/py-incomplete-hostname-regexp/) | 020 | (icon: check) | (icon: check) | (icon: check) |
| [Incomplete URL substring sanitization](https://codeql.github.com/codeql-query-help/python/py-incomplete-url-substring-sanitization/) | 020 | (icon: check) | (icon: check) | (icon: check) |
| [Inefficient regular expression](https://codeql.github.com/codeql-query-help/python/py-redos/) | 1333, 730, 400 | (icon: check) | (icon: check) | (icon: x) |
| [Information exposure through an exception](https://codeql.github.com/codeql-query-help/python/py-stack-trace-exposure/) | 209, 497 | (icon: check) | (icon: check) | (icon: check) |
| [Insecure temporary file](https://codeql.github.com/codeql-query-help/python/py-insecure-temporary-file/) | 377 | (icon: check) | (icon: check) | (icon: x) |
| [LDAP query built from user-controlled sources](https://codeql.github.com/codeql-query-help/python/py-ldap-injection/) | 090 | (icon: check) | (icon: check) | (icon: check) |
| [NoSQL Injection](https://codeql.github.com/codeql-query-help/python/py-nosql-injection/) | 943 | (icon: check) | (icon: check) | (icon: check) |
| [Overly permissive regular expression range](https://codeql.github.com/codeql-query-help/python/py-overly-large-range/) | 020 | (icon: check) | (icon: check) | (icon: x) |
| [PAM authorization bypass due to incorrect usage](https://codeql.github.com/codeql-query-help/python/py-pam-auth-bypass/) | 285 | (icon: check) | (icon: check) | (icon: check) |
| [Polynomial regular expression used on uncontrolled data](https://codeql.github.com/codeql-query-help/python/py-polynomial-redos/) | 1333, 730, 400 | (icon: check) | (icon: check) | (icon: x) |
| [Reflected server-side cross-site scripting](https://codeql.github.com/codeql-query-help/python/py-reflective-xss/) | 079, 116 | (icon: check) | (icon: check) | (icon: check) |
| [Regular expression injection](https://codeql.github.com/codeql-query-help/python/py-regex-injection/) | 730, 400 | (icon: check) | (icon: check) | (icon: check) |
| [Sensitive cookie missing `HttpOnly` attribute](https://codeql.github.com/codeql-query-help/python/py-client-exposed-cookie/) | 1004 | (icon: check) | (icon: check) | (icon: x) |
| [Sensitive cookie with `SameSite` attribute set to `None`](https://codeql.github.com/codeql-query-help/python/py-samesite-none-cookie/) | 1275 | (icon: check) | (icon: check) | (icon: x) |
| [Server Side Template Injection](https://codeql.github.com/codeql-query-help/python/py-template-injection/) | 074 | (icon: check) | (icon: check) | (icon: check) |
| [SQL query built from user-controlled sources](https://codeql.github.com/codeql-query-help/python/py-sql-injection/) | 089 | (icon: check) | (icon: check) | (icon: check) |
| [Uncontrolled command line](https://codeql.github.com/codeql-query-help/python/py-command-line-injection/) | 078, 088 | (icon: check) | (icon: check) | (icon: check) |
| [Uncontrolled data used in path expression](https://codeql.github.com/codeql-query-help/python/py-path-injection/) | 022, 023, 036, 073, 099 | (icon: check) | (icon: check) | (icon: check) |
| [URL redirection from remote source](https://codeql.github.com/codeql-query-help/python/py-url-redirection/) | 601 | (icon: check) | (icon: check) | (icon: check) |
| [Use of a broken or weak cryptographic algorithm](https://codeql.github.com/codeql-query-help/python/py-weak-cryptographic-algorithm/) | 327 | (icon: check) | (icon: check) | (icon: check) |
| [Use of a broken or weak cryptographic hashing algorithm on sensitive data](https://codeql.github.com/codeql-query-help/python/py-weak-sensitive-data-hashing/) | 327, 328, 916 | (icon: check) | (icon: check) | (icon: check) |
| [Use of insecure SSL/TLS version](https://codeql.github.com/codeql-query-help/python/py-insecure-protocol/) | 327 | (icon: check) | (icon: check) | (icon: check) |
| [Use of weak cryptographic key](https://codeql.github.com/codeql-query-help/python/py-weak-crypto-key/) | 326 | (icon: check) | (icon: check) | (icon: check) |
| [XML external entity expansion](https://codeql.github.com/codeql-query-help/python/py-xxe/) | 611, 827 | (icon: check) | (icon: check) | (icon: check) |
| [XML internal entity expansion](https://codeql.github.com/codeql-query-help/python/py-xml-bomb/) | 776, 400 | (icon: check) | (icon: check) | (icon: check) |
| [XPath query built from user-controlled sources](https://codeql.github.com/codeql-query-help/python/py-xpath-injection/) | 643 | (icon: check) | (icon: check) | (icon: check) |
| [Arbitrary file write during tarfile extraction](https://codeql.github.com/codeql-query-help/python/py-tarslip/) | 022 | (icon: x) | (icon: check) | (icon: check) |
| [Jinja2 templating with autoescape=False](https://codeql.github.com/codeql-query-help/python/py-jinja2-autoescape-false/) | 079 | (icon: x) | (icon: check) | (icon: check) |
| [Log Injection](https://codeql.github.com/codeql-query-help/python/py-log-injection/) | 117 | (icon: x) | (icon: check) | (icon: check) |
| [Overly permissive file permissions](https://codeql.github.com/codeql-query-help/python/py-overly-permissive-file/) | 732 | (icon: x) | (icon: check) | (icon: check) |
| [Partial server-side request forgery](https://codeql.github.com/codeql-query-help/python/py-partial-ssrf/) | 918 | (icon: x) | (icon: check) | (icon: check) |
| [Request without certificate validation](https://codeql.github.com/codeql-query-help/python/py-request-without-cert-validation/) | 295 | (icon: x) | (icon: check) | (icon: check) |
| [Unsafe shell command constructed from library input](https://codeql.github.com/codeql-query-help/python/py-shell-command-constructed-from-input/) | 078, 088, 073 | (icon: x) | (icon: check) | (icon: check) |

{% endrowheaders %}
