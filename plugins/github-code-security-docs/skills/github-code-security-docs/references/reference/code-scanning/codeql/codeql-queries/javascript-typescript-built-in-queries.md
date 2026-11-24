---
title: JavaScript and TypeScript queries for CodeQL analysis
shortTitle: JavaScript and TypeScript queries
intro: Explore the queries that CodeQL uses to analyze code written in JavaScript or TypeScript when you select the `default` or the `security-extended` query suite.
product: "CodeQL is available for the following repository types:\n\n{%- ifversion fpt %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghec %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{% endif %}"
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/managing-your-code-scanning-configuration/javascript-typescript-built-in-queries
  - /code-security/code-scanning/reference/code-ql-built-in-queries/javascript-typescript-built-in-queries
contentType: reference
category:
  - Find CodeQL CLI commands
---

CodeQL includes many queries for analyzing JavaScript and TypeScript code. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [AUTOTITLE](/code-security/concepts/code-scanning/codeql/codeql-query-suites).

## Built-in queries for JavaScript and TypeScript analysis

This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.

{% ifversion ghes %}

> [!NOTE]
> The initial release of GitHub Enterprise Server {{ allVersions[currentVersion].currentRelease }} included CodeQL action and CodeQL CLI {% ifversion ghes < 3.20 %}2.22.4{% elsif ghes < 3.21 %}2.23.9{% elsif ghes < 3.22 %}2.24.3{% elsif ghes < 3.23 %}2.25.6{% elsif ghes < 3.24 %}2.27.0{% endif %}, which may not include all of these queries. Your site administrator can update your CodeQL version to a newer release. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance).

{% endif %}

{% rowheaders %}

| Query name | Related CWEs | Default | Extended | Copilot Autofix |
| --- | --- | --- | --- | --- |
| [Arbitrary file access during archive extraction ("Zip Slip")](https://codeql.github.com/codeql-query-help/javascript/js-zipslip/) | 022 | (icon: check) | (icon: check) | (icon: check) |
| [Bad HTML filtering regexp](https://codeql.github.com/codeql-query-help/javascript/js-bad-tag-filter/) | 020, 080, 116, 184, 185, 186 | (icon: check) | (icon: check) | (icon: check) |
| [Case-sensitive middleware path](https://codeql.github.com/codeql-query-help/javascript/js-case-sensitive-middleware-path/) | 178 | (icon: check) | (icon: check) | (icon: check) |
| [Clear text storage of sensitive information](https://codeql.github.com/codeql-query-help/javascript/js-clear-text-storage-of-sensitive-data/) | 312, 315, 359 | (icon: check) | (icon: check) | (icon: check) |
| [Clear text transmission of sensitive cookie](https://codeql.github.com/codeql-query-help/javascript/js-clear-text-cookie/) | 614, 311, 312, 319 | (icon: check) | (icon: check) | (icon: check) |
| [Clear-text logging of sensitive information](https://codeql.github.com/codeql-query-help/javascript/js-clear-text-logging/) | 312, 359, 532 | (icon: check) | (icon: check) | (icon: check) |
| [Client-side cross-site scripting](https://codeql.github.com/codeql-query-help/javascript/js-xss/) | 079, 116 | (icon: check) | (icon: check) | (icon: check) |
| [Client-side URL redirect](https://codeql.github.com/codeql-query-help/javascript/js-client-side-unvalidated-url-redirection/) | 079, 116, 601 | (icon: check) | (icon: check) | (icon: check) |
| [Code injection](https://codeql.github.com/codeql-query-help/javascript/js-code-injection/) | 094, 095, 079, 116 | (icon: check) | (icon: check) | (icon: check) |
| [CORS misconfiguration for credentials transfer](https://codeql.github.com/codeql-query-help/javascript/js-cors-misconfiguration-for-credentials/) | 346, 639, 942 | (icon: check) | (icon: check) | (icon: check) |
| [Creating biased random numbers from a cryptographically secure source](https://codeql.github.com/codeql-query-help/javascript/js-biased-cryptographic-random/) | 327 | (icon: check) | (icon: check) | (icon: check) |
| [Cross-window communication with unrestricted target origin](https://codeql.github.com/codeql-query-help/javascript/js-cross-window-information-leak/) | 201, 359 | (icon: check) | (icon: check) | (icon: check) |
| [Database query built from user-controlled sources](https://codeql.github.com/codeql-query-help/javascript/js-sql-injection/) | 089, 090, 943 | (icon: check) | (icon: check) | (icon: check) |
| [Dependency download using unencrypted communication channel](https://codeql.github.com/codeql-query-help/javascript/js-insecure-dependency/) | 300, 319, 494, 829 | (icon: check) | (icon: check) | (icon: check) |
| [Deserialization of user-controlled data](https://codeql.github.com/codeql-query-help/javascript/js-unsafe-deserialization/) | 502 | (icon: check) | (icon: check) | (icon: check) |
| [Disabling certificate validation](https://codeql.github.com/codeql-query-help/javascript/js-disabling-certificate-validation/) | 295, 297 | (icon: check) | (icon: check) | (icon: check) |
| [Disabling Electron webSecurity](https://codeql.github.com/codeql-query-help/javascript/js-disabling-electron-websecurity/) | 079 | (icon: check) | (icon: check) | (icon: check) |
| [Disabling SCE](https://codeql.github.com/codeql-query-help/javascript/js-angular-disabling-sce/) | 116 | (icon: check) | (icon: check) | (icon: check) |
| [DOM text reinterpreted as HTML](https://codeql.github.com/codeql-query-help/javascript/js-xss-through-dom/) | 079, 116 | (icon: check) | (icon: check) | (icon: check) |
| [Double compilation](https://codeql.github.com/codeql-query-help/javascript/js-angular-double-compilation/) | 1176 | (icon: check) | (icon: check) | (icon: check) |
| [Double escaping or unescaping](https://codeql.github.com/codeql-query-help/javascript/js-double-escaping/) | 116, 020 | (icon: check) | (icon: check) | (icon: check) |
| [Download of sensitive file through insecure connection](https://codeql.github.com/codeql-query-help/javascript/js-insecure-download/) | 829 | (icon: check) | (icon: check) | (icon: check) |
| [Enabling Electron allowRunningInsecureContent](https://codeql.github.com/codeql-query-help/javascript/js-enabling-electron-insecure-content/) | 494 | (icon: check) | (icon: check) | (icon: check) |
| [Exception text reinterpreted as HTML](https://codeql.github.com/codeql-query-help/javascript/js-xss-through-exception/) | 079, 116 | (icon: check) | (icon: check) | (icon: check) |
| [Exposure of private files](https://codeql.github.com/codeql-query-help/javascript/js-exposure-of-private-files/) | 200, 219, 548 | (icon: check) | (icon: check) | (icon: check) |
| [Host header poisoning in email generation](https://codeql.github.com/codeql-query-help/javascript/js-host-header-forgery-in-email-generation/) | 640 | (icon: check) | (icon: check) | (icon: check) |
| [Improper code sanitization](https://codeql.github.com/codeql-query-help/javascript/js-bad-code-sanitization/) | 094, 079, 116 | (icon: check) | (icon: check) | (icon: check) |
| [Inclusion of functionality from an untrusted source](https://codeql.github.com/codeql-query-help/javascript/js-functionality-from-untrusted-source/) | 830 | (icon: check) | (icon: check) | (icon: x) |
| [Incomplete HTML attribute sanitization](https://codeql.github.com/codeql-query-help/javascript/js-incomplete-html-attribute-sanitization/) | 079, 116, 020 | (icon: check) | (icon: check) | (icon: check) |
| [Incomplete multi-character sanitization](https://codeql.github.com/codeql-query-help/javascript/js-incomplete-multi-character-sanitization/) | 020, 080, 116 | (icon: check) | (icon: check) | (icon: check) |
| [Incomplete regular expression for hostnames](https://codeql.github.com/codeql-query-help/javascript/js-incomplete-hostname-regexp/) | 020 | (icon: check) | (icon: check) | (icon: check) |
| [Incomplete string escaping or encoding](https://codeql.github.com/codeql-query-help/javascript/js-incomplete-sanitization/) | 020, 080, 116 | (icon: check) | (icon: check) | (icon: check) |
| [Incomplete URL scheme check](https://codeql.github.com/codeql-query-help/javascript/js-incomplete-url-scheme-check/) | 020, 184 | (icon: check) | (icon: check) | (icon: check) |
| [Incomplete URL substring sanitization](https://codeql.github.com/codeql-query-help/javascript/js-incomplete-url-substring-sanitization/) | 020 | (icon: check) | (icon: check) | (icon: check) |
| [Incorrect suffix check](https://codeql.github.com/codeql-query-help/javascript/js-incorrect-suffix-check/) | 020 | (icon: check) | (icon: check) | (icon: check) |
| [Inefficient regular expression](https://codeql.github.com/codeql-query-help/javascript/js-redos/) | 1333, 730, 400 | (icon: check) | (icon: check) | (icon: check) |
| [Information exposure through a stack trace](https://codeql.github.com/codeql-query-help/javascript/js-stack-trace-exposure/) | 209, 497 | (icon: check) | (icon: check) | (icon: check) |
| [Insecure configuration of Helmet security middleware](https://codeql.github.com/codeql-query-help/javascript/js-insecure-helmet-configuration/) | 693, 1021 | (icon: check) | (icon: check) | (icon: check) |
| [Insecure randomness](https://codeql.github.com/codeql-query-help/javascript/js-insecure-randomness/) | 338 | (icon: check) | (icon: check) | (icon: check) |
| [Insecure URL whitelist](https://codeql.github.com/codeql-query-help/javascript/js-angular-insecure-url-whitelist/) | 183, 625 | (icon: check) | (icon: check) | (icon: check) |
| [JWT missing secret or public key verification](https://codeql.github.com/codeql-query-help/javascript/js-jwt-missing-verification/) | 347 | (icon: check) | (icon: check) | (icon: check) |
| [Loop bound injection](https://codeql.github.com/codeql-query-help/javascript/js-loop-bound-injection/) | 834, 730 | (icon: check) | (icon: check) | (icon: check) |
| [Missing CSRF middleware](https://codeql.github.com/codeql-query-help/javascript/js-missing-token-validation/) | 352 | (icon: check) | (icon: check) | (icon: check) |
| [Missing rate limiting](https://codeql.github.com/codeql-query-help/javascript/js-missing-rate-limiting/) | 770, 307, 400 | (icon: check) | (icon: check) | (icon: check) |
| [Overly permissive regular expression range](https://codeql.github.com/codeql-query-help/javascript/js-overly-large-range/) | 020 | (icon: check) | (icon: check) | (icon: check) |
| [Permissive CORS configuration](https://codeql.github.com/codeql-query-help/javascript/js-cors-permissive-configuration/) | 942 | (icon: check) | (icon: check) | (icon: x) |
| [Polynomial regular expression used on uncontrolled data](https://codeql.github.com/codeql-query-help/javascript/js-polynomial-redos/) | 1333, 730, 400 | (icon: check) | (icon: check) | (icon: x) |
| [Prototype-polluting assignment](https://codeql.github.com/codeql-query-help/javascript/js-prototype-polluting-assignment/) | 078, 079, 094, 400, 471, 915 | (icon: check) | (icon: check) | (icon: check) |
| [Prototype-polluting function](https://codeql.github.com/codeql-query-help/javascript/js-prototype-pollution-utility/) | 078, 079, 094, 400, 471, 915 | (icon: check) | (icon: check) | (icon: check) |
| [Prototype-polluting merge call](https://codeql.github.com/codeql-query-help/javascript/js-prototype-pollution/) | 078, 079, 094, 400, 471, 915 | (icon: check) | (icon: check) | (icon: check) |
| [Reflected cross-site scripting](https://codeql.github.com/codeql-query-help/javascript/js-reflected-xss/) | 079, 116 | (icon: check) | (icon: check) | (icon: check) |
| [Regular expression injection](https://codeql.github.com/codeql-query-help/javascript/js-regex-injection/) | 730, 400 | (icon: check) | (icon: check) | (icon: check) |
| [Replacement of a substring with itself](https://codeql.github.com/codeql-query-help/javascript/js-identity-replacement/) | 116 | (icon: check) | (icon: check) | (icon: check) |
| [Resource exhaustion](https://codeql.github.com/codeql-query-help/javascript/js-resource-exhaustion/) | 400, 770 | (icon: check) | (icon: check) | (icon: check) |
| [Resources exhaustion from deep object traversal](https://codeql.github.com/codeql-query-help/javascript/js-resource-exhaustion-from-deep-object-traversal/) | 400 | (icon: check) | (icon: check) | (icon: check) |
| [Second order command injection](https://codeql.github.com/codeql-query-help/javascript/js-second-order-command-line-injection/) | 078, 088 | (icon: check) | (icon: check) | (icon: check) |
| [Sensitive data read from GET request](https://codeql.github.com/codeql-query-help/javascript/js-sensitive-get-query/) | 598 | (icon: check) | (icon: check) | (icon: check) |
| [Sensitive server cookie exposed to the client](https://codeql.github.com/codeql-query-help/javascript/js-client-exposed-cookie/) | 1004 | (icon: check) | (icon: check) | (icon: check) |
| [Server crash](https://codeql.github.com/codeql-query-help/javascript/js-server-crash/) | 248, 730 | (icon: check) | (icon: check) | (icon: check) |
| [Server-side request forgery](https://codeql.github.com/codeql-query-help/javascript/js-request-forgery/) | 918 | (icon: check) | (icon: check) | (icon: check) |
| [Server-side URL redirect](https://codeql.github.com/codeql-query-help/javascript/js-server-side-unvalidated-url-redirection/) | 601 | (icon: check) | (icon: check) | (icon: check) |
| [Shell command built from environment values](https://codeql.github.com/codeql-query-help/javascript/js-shell-command-injection-from-environment/) | 078, 088 | (icon: check) | (icon: check) | (icon: check) |
| [Storage of sensitive information in build artifact](https://codeql.github.com/codeql-query-help/javascript/js-build-artifact-leak/) | 312, 315, 359 | (icon: check) | (icon: check) | (icon: check) |
| [Stored cross-site scripting](https://codeql.github.com/codeql-query-help/javascript/js-stored-xss/) | 079, 116 | (icon: check) | (icon: check) | (icon: check) |
| [System prompt injection](https://codeql.github.com/codeql-query-help/javascript/js-system-prompt-injection/) | 1427 | (icon: check) | (icon: check) | (icon: x) |
| [Template Object Injection](https://codeql.github.com/codeql-query-help/javascript/js-template-object-injection/) | 073, 094 | (icon: check) | (icon: check) | (icon: check) |
| [Type confusion through parameter tampering](https://codeql.github.com/codeql-query-help/javascript/js-type-confusion-through-parameter-tampering/) | 843 | (icon: check) | (icon: check) | (icon: check) |
| [Uncontrolled command line](https://codeql.github.com/codeql-query-help/javascript/js-command-line-injection/) | 078, 088 | (icon: check) | (icon: check) | (icon: check) |
| [Uncontrolled data used in path expression](https://codeql.github.com/codeql-query-help/javascript/js-path-injection/) | 022, 023, 036, 073, 099 | (icon: check) | (icon: check) | (icon: check) |
| [Unnecessary use of `cat` process](https://codeql.github.com/codeql-query-help/javascript/js-unnecessary-use-of-cat/) | 078 | (icon: check) | (icon: check) | (icon: check) |
| [Unsafe dynamic method access](https://codeql.github.com/codeql-query-help/javascript/js-unsafe-dynamic-method-access/) | 094 | (icon: check) | (icon: check) | (icon: check) |
| [Unsafe expansion of self-closing HTML tag](https://codeql.github.com/codeql-query-help/javascript/js-unsafe-html-expansion/) | 079, 116 | (icon: check) | (icon: check) | (icon: check) |
| [Unsafe HTML constructed from library input](https://codeql.github.com/codeql-query-help/javascript/js-html-constructed-from-input/) | 079, 116 | (icon: check) | (icon: check) | (icon: check) |
| [Unsafe jQuery plugin](https://codeql.github.com/codeql-query-help/javascript/js-unsafe-jquery-plugin/) | 079, 116 | (icon: check) | (icon: check) | (icon: check) |
| [Unsafe shell command constructed from library input](https://codeql.github.com/codeql-query-help/javascript/js-shell-command-constructed-from-input/) | 078, 088 | (icon: check) | (icon: check) | (icon: check) |
| [Untrusted domain used in script or other content](https://codeql.github.com/codeql-query-help/javascript/js-functionality-from-untrusted-domain/) | 830 | (icon: check) | (icon: check) | (icon: x) |
| [Unvalidated dynamic method call](https://codeql.github.com/codeql-query-help/javascript/js-unvalidated-dynamic-method-call/) | 754 | (icon: check) | (icon: check) | (icon: check) |
| [Use of a broken or weak cryptographic algorithm](https://codeql.github.com/codeql-query-help/javascript/js-weak-cryptographic-algorithm/) | 327, 328 | (icon: check) | (icon: check) | (icon: check) |
| [Use of a weak cryptographic key](https://codeql.github.com/codeql-query-help/javascript/js-insufficient-key-size/) | 326 | (icon: check) | (icon: check) | (icon: check) |
| [Use of externally-controlled format string](https://codeql.github.com/codeql-query-help/javascript/js-tainted-format-string/) | 134 | (icon: check) | (icon: check) | (icon: check) |
| [Use of password hash with insufficient computational effort](https://codeql.github.com/codeql-query-help/javascript/js-insufficient-password-hash/) | 916 | (icon: check) | (icon: check) | (icon: check) |
| [Useless regular-expression character escape](https://codeql.github.com/codeql-query-help/javascript/js-useless-regexp-character-escape/) | 020 | (icon: check) | (icon: check) | (icon: check) |
| [XML external entity expansion](https://codeql.github.com/codeql-query-help/javascript/js-xxe/) | 611, 827 | (icon: check) | (icon: check) | (icon: check) |
| [XML internal entity expansion](https://codeql.github.com/codeql-query-help/javascript/js-xml-bomb/) | 776, 400 | (icon: check) | (icon: check) | (icon: check) |
| [XPath injection](https://codeql.github.com/codeql-query-help/javascript/js-xpath-injection/) | 643 | (icon: check) | (icon: check) | (icon: check) |
| [Client-side request forgery](https://codeql.github.com/codeql-query-help/javascript/js-client-side-request-forgery/) | 918 | (icon: x) | (icon: check) | (icon: x) |
| [Empty password in configuration file](https://codeql.github.com/codeql-query-help/javascript/js-empty-password-in-configuration-file/) | 258, 862 | (icon: x) | (icon: check) | (icon: x) |
| [Failure to abandon session](https://codeql.github.com/codeql-query-help/javascript/js-session-fixation/) | 384 | (icon: x) | (icon: check) | (icon: x) |
| [File data in outbound network request](https://codeql.github.com/codeql-query-help/javascript/js-file-access-to-http/) | 200 | (icon: x) | (icon: check) | (icon: x) |
| [Hard-coded data interpreted as code](https://codeql.github.com/codeql-query-help/javascript/js-hardcoded-data-interpreted-as-code/) | 506 | (icon: x) | (icon: check) | (icon: x) |
| [Indirect uncontrolled command line](https://codeql.github.com/codeql-query-help/javascript/js-indirect-command-line-injection/) | 078, 088 | (icon: x) | (icon: check) | (icon: check) |
| [Insecure temporary file](https://codeql.github.com/codeql-query-help/javascript/js-insecure-temporary-file/) | 377, 378 | (icon: x) | (icon: check) | (icon: check) |
| [Log injection](https://codeql.github.com/codeql-query-help/javascript/js-log-injection/) | 117 | (icon: x) | (icon: check) | (icon: check) |
| [Missing origin verification in `postMessage` handler](https://codeql.github.com/codeql-query-help/javascript/js-missing-origin-check/) | 020, 940 | (icon: x) | (icon: check) | (icon: check) |
| [Missing regular expression anchor](https://codeql.github.com/codeql-query-help/javascript/js-regex-missing-regexp-anchor/) | 020 | (icon: x) | (icon: check) | (icon: check) |
| [Network data written to file](https://codeql.github.com/codeql-query-help/javascript/js-http-to-file-access/) | 912, 434 | (icon: x) | (icon: check) | (icon: x) |
| [Potential file system race condition](https://codeql.github.com/codeql-query-help/javascript/js-file-system-race/) | 367 | (icon: x) | (icon: check) | (icon: x) |
| [Remote property injection](https://codeql.github.com/codeql-query-help/javascript/js-remote-property-injection/) | 250, 400 | (icon: x) | (icon: check) | (icon: x) |
| [Sensitive cookie without SameSite restrictions](https://codeql.github.com/codeql-query-help/javascript/js-samesite-none-cookie/) | 1275 | (icon: x) | (icon: check) | (icon: check) |
| [Unsafe code constructed from library input](https://codeql.github.com/codeql-query-help/javascript/js-unsafe-code-construction/) | 094, 079, 116 | (icon: x) | (icon: check) | (icon: x) |
| [User-controlled bypass of security check](https://codeql.github.com/codeql-query-help/javascript/js-user-controlled-bypass/) | 807, 290 | (icon: x) | (icon: check) | (icon: x) |

{% endrowheaders %}
