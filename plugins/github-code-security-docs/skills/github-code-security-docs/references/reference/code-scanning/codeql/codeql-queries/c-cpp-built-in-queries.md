---
title: C and C++ queries for CodeQL analysis
shortTitle: C and C++ queries
intro: Explore the queries that CodeQL uses to analyze code written in C or C++ when you select the `default` or the `security-extended` query suite.
product: "CodeQL is available for the following repository types:\n\n{%- ifversion fpt %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghec %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{% endif %}"
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/managing-your-code-scanning-configuration/c-cpp-built-in-queries
  - /code-security/code-scanning/reference/code-ql-built-in-queries/c-cpp-built-in-queries
contentType: reference
category:
  - Find CodeQL CLI commands
---

CodeQL includes many queries for analyzing C and C++ code. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [AUTOTITLE](/code-security/concepts/code-scanning/codeql/codeql-query-suites).

## Built-in queries for C and C++ analysis

This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.

{% ifversion ghes %}

> [!NOTE]
> The initial release of GitHub Enterprise Server {{ allVersions[currentVersion].currentRelease }} included CodeQL action and CodeQL CLI {% ifversion ghes < 3.20 %}2.22.4{% elsif ghes < 3.21 %}2.23.9{% elsif ghes < 3.22 %}2.24.3{% elsif ghes < 3.23 %}2.25.6{% endif %}, which may not include all of these queries. Your site administrator can update your CodeQL version to a newer release. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance).

{% endif %}

{% rowheaders %}

| Query name | Related CWEs | Default | Extended | Copilot Autofix |
| --- | --- | --- | --- | --- |
| [Bad check for overflow of integer addition](https://codeql.github.com/codeql-query-help/cpp/cpp-bad-addition-overflow-check/) | 190, 192 | (icon: check) | (icon: check) | (icon: check) |
| [Badly bounded write](https://codeql.github.com/codeql-query-help/cpp/cpp-badly-bounded-write/) | 120, 787, 805 | (icon: check) | (icon: check) | (icon: check) |
| [Call to `memset` may be deleted](https://codeql.github.com/codeql-query-help/cpp/cpp-memset-may-be-deleted/) | 014 | (icon: check) | (icon: check) | (icon: check) |
| [Call to alloca in a loop](https://codeql.github.com/codeql-query-help/cpp/cpp-alloca-in-loop/) | 770 | (icon: check) | (icon: check) | (icon: check) |
| [Call to function with fewer arguments than declared parameters](https://codeql.github.com/codeql-query-help/cpp/cpp-too-few-arguments/) | 234, 685 | (icon: check) | (icon: check) | (icon: check) |
| [Cast between HRESULT and a Boolean type](https://codeql.github.com/codeql-query-help/cpp/cpp-hresult-boolean-conversion/) | 253 | (icon: check) | (icon: check) | (icon: check) |
| [Cast from char* to wchar_t*](https://codeql.github.com/codeql-query-help/cpp/cpp-incorrect-string-type-conversion/) | 704 | (icon: check) | (icon: check) | (icon: x) |
| [CGI script vulnerable to cross-site scripting](https://codeql.github.com/codeql-query-help/cpp/cpp-cgi-xss/) | 079 | (icon: check) | (icon: check) | (icon: check) |
| [Cleartext storage of sensitive information in file](https://codeql.github.com/codeql-query-help/cpp/cpp-cleartext-storage-file/) | 260, 313 | (icon: check) | (icon: check) | (icon: check) |
| [Cleartext transmission of sensitive information](https://codeql.github.com/codeql-query-help/cpp/cpp-cleartext-transmission/) | 319, 359 | (icon: check) | (icon: check) | (icon: check) |
| [Comparison of narrow type with wide type in loop condition](https://codeql.github.com/codeql-query-help/cpp/cpp-comparison-with-wider-type/) | 190, 197, 835 | (icon: check) | (icon: check) | (icon: check) |
| [Dangerous use of 'cin'](https://codeql.github.com/codeql-query-help/cpp/cpp-dangerous-cin/) | 676 | (icon: check) | (icon: check) | (icon: check) |
| [Exposure of system data to an unauthorized control sphere](https://codeql.github.com/codeql-query-help/cpp/cpp-system-data-exposure/) | 497 | (icon: check) | (icon: check) | (icon: x) |
| [Failure to use HTTPS URLs](https://codeql.github.com/codeql-query-help/cpp/cpp-non-https-url/) | 319, 345 | (icon: check) | (icon: check) | (icon: check) |
| [File opened with O_CREAT flag but without mode argument](https://codeql.github.com/codeql-query-help/cpp/cpp-open-call-with-mode-argument/) | 732 | (icon: check) | (icon: check) | (icon: check) |
| [Incorrect return-value check for a 'scanf'-like function](https://codeql.github.com/codeql-query-help/cpp/cpp-incorrectly-checked-scanf/) | 253 | (icon: check) | (icon: check) | (icon: check) |
| [Iterator to expired container](https://codeql.github.com/codeql-query-help/cpp/cpp-iterator-to-expired-container/) | 416, 664 | (icon: check) | (icon: check) | (icon: check) |
| [Likely overrunning write](https://codeql.github.com/codeql-query-help/cpp/cpp-very-likely-overrunning-write/) | 120, 787, 805 | (icon: check) | (icon: check) | (icon: check) |
| [Mismatching new/free or malloc/delete](https://codeql.github.com/codeql-query-help/cpp/cpp-new-free-mismatch/) | 762 | (icon: check) | (icon: check) | (icon: check) |
| [Multiplication result converted to larger type](https://codeql.github.com/codeql-query-help/cpp/cpp-integer-multiplication-cast-to-long/) | 190, 192, 197, 681 | (icon: check) | (icon: check) | (icon: check) |
| [No space for zero terminator](https://codeql.github.com/codeql-query-help/cpp/cpp-no-space-for-terminator/) | 131, 120, 122 | (icon: check) | (icon: check) | (icon: check) |
| [Pointer overflow check](https://codeql.github.com/codeql-query-help/cpp/cpp-pointer-overflow-check/) | 758 | (icon: check) | (icon: check) | (icon: check) |
| [Potential double free](https://codeql.github.com/codeql-query-help/cpp/cpp-double-free/) | 415 | (icon: check) | (icon: check) | (icon: x) |
| [Potential use after free](https://codeql.github.com/codeql-query-help/cpp/cpp-use-after-free/) | 416 | (icon: check) | (icon: check) | (icon: check) |
| [Potentially overflowing call to snprintf](https://codeql.github.com/codeql-query-help/cpp/cpp-overflowing-snprintf/) | 190, 253 | (icon: check) | (icon: check) | (icon: check) |
| [Potentially unsafe call to strncat](https://codeql.github.com/codeql-query-help/cpp/cpp-unsafe-strncat/) | 788, 676, 119, 251 | (icon: check) | (icon: check) | (icon: check) |
| [Redundant null check due to previous dereference](https://codeql.github.com/codeql-query-help/cpp/cpp-redundant-null-check-simple/) | 476 | (icon: check) | (icon: check) | (icon: check) |
| [Returning stack-allocated memory](https://codeql.github.com/codeql-query-help/cpp/cpp-return-stack-allocated-memory/) | 825 | (icon: check) | (icon: check) | (icon: check) |
| [Setting a DACL to NULL in a SECURITY_DESCRIPTOR](https://codeql.github.com/codeql-query-help/cpp/cpp-unsafe-dacl-security-descriptor/) | 732 | (icon: check) | (icon: check) | (icon: check) |
| [Signed overflow check](https://codeql.github.com/codeql-query-help/cpp/cpp-signed-overflow-check/) | 128, 190 | (icon: check) | (icon: check) | (icon: check) |
| [Static array access may cause overflow](https://codeql.github.com/codeql-query-help/cpp/cpp-static-buffer-overflow/) | 119, 131 | (icon: check) | (icon: check) | (icon: check) |
| [Suspicious add with sizeof](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-add-sizeof/) | 468 | (icon: check) | (icon: check) | (icon: check) |
| [Time-of-check time-of-use filesystem race condition](https://codeql.github.com/codeql-query-help/cpp/cpp-toctou-race-condition/) | 367 | (icon: check) | (icon: check) | (icon: check) |
| [Too few arguments to formatting function](https://codeql.github.com/codeql-query-help/cpp/cpp-wrong-number-format-arguments/) | 234, 685 | (icon: check) | (icon: check) | (icon: check) |
| [Uncontrolled data in arithmetic expression](https://codeql.github.com/codeql-query-help/cpp/cpp-uncontrolled-arithmetic/) | 190, 191 | (icon: check) | (icon: check) | (icon: check) |
| [Uncontrolled data in SQL query](https://codeql.github.com/codeql-query-help/cpp/cpp-sql-injection/) | 089 | (icon: check) | (icon: check) | (icon: x) |
| [Uncontrolled data used in OS command](https://codeql.github.com/codeql-query-help/cpp/cpp-command-line-injection/) | 078, 088 | (icon: check) | (icon: check) | (icon: x) |
| [Uncontrolled format string](https://codeql.github.com/codeql-query-help/cpp/cpp-tainted-format-string/) | 134 | (icon: check) | (icon: check) | (icon: check) |
| [Unsafe use of this in constructor](https://codeql.github.com/codeql-query-help/cpp/cpp-unsafe-use-of-this/) | 670 | (icon: check) | (icon: check) | (icon: check) |
| [Unsigned difference expression compared to zero](https://codeql.github.com/codeql-query-help/cpp/cpp-unsigned-difference-expression-compared-zero/) | 191 | (icon: check) | (icon: check) | (icon: check) |
| [Upcast array used in pointer arithmetic](https://codeql.github.com/codeql-query-help/cpp/cpp-upcast-array-pointer-arithmetic/) | 119, 843 | (icon: check) | (icon: check) | (icon: check) |
| [Use of a broken or risky cryptographic algorithm](https://codeql.github.com/codeql-query-help/cpp/cpp-weak-cryptographic-algorithm/) | 327 | (icon: check) | (icon: check) | (icon: x) |
| [Use of a cryptographic algorithm with insufficient key size](https://codeql.github.com/codeql-query-help/cpp/cpp-insufficient-key-size/) | 326 | (icon: check) | (icon: check) | (icon: check) |
| [Use of a version of OpenSSL with Heartbleed](https://codeql.github.com/codeql-query-help/cpp/cpp-openssl-heartbleed/) | 327, 788 | (icon: check) | (icon: check) | (icon: check) |
| [Use of dangerous function](https://codeql.github.com/codeql-query-help/cpp/cpp-dangerous-function-overflow/) | 242, 676 | (icon: check) | (icon: check) | (icon: check) |
| [Use of expired stack-address](https://codeql.github.com/codeql-query-help/cpp/cpp-using-expired-stack-address/) | 825 | (icon: check) | (icon: check) | (icon: check) |
| [Use of string after lifetime ends](https://codeql.github.com/codeql-query-help/cpp/cpp-use-of-string-after-lifetime-ends/) | 416, 664 | (icon: check) | (icon: check) | (icon: check) |
| [Use of unique pointer after lifetime ends](https://codeql.github.com/codeql-query-help/cpp/cpp-use-of-unique-pointer-after-lifetime-ends/) | 416, 664 | (icon: check) | (icon: check) | (icon: check) |
| [Wrong type of arguments to formatting function](https://codeql.github.com/codeql-query-help/cpp/cpp-wrong-type-format-argument/) | 686 | (icon: check) | (icon: check) | (icon: check) |
| [XML external entity expansion](https://codeql.github.com/codeql-query-help/cpp/cpp-external-entity-expansion/) | 611 | (icon: check) | (icon: check) | (icon: check) |
| [Array offset used before range check](https://codeql.github.com/codeql-query-help/cpp/cpp-offset-use-before-range-check/) | 120, 125 | (icon: x) | (icon: check) | (icon: check) |
| [Authentication bypass by spoofing](https://codeql.github.com/codeql-query-help/cpp/cpp-user-controlled-bypass/) | 290 | (icon: x) | (icon: check) | (icon: x) |
| [boost::asio TLS settings misconfiguration](https://codeql.github.com/codeql-query-help/cpp/cpp-boost-tls-settings-misconfiguration/) | 326 | (icon: x) | (icon: check) | (icon: check) |
| [boost::asio use of deprecated hardcoded protocol](https://codeql.github.com/codeql-query-help/cpp/cpp-boost-use-of-deprecated-hardcoded-security-protocol/) | 327 | (icon: x) | (icon: check) | (icon: check) |
| [Call to memory access function may overflow buffer](https://codeql.github.com/codeql-query-help/cpp/cpp-overflow-buffer/) | 119, 121, 122, 126 | (icon: x) | (icon: check) | (icon: check) |
| [Certificate not checked](https://codeql.github.com/codeql-query-help/cpp/cpp-certificate-not-checked/) | 295 | (icon: x) | (icon: check) | (icon: check) |
| [Certificate result conflation](https://codeql.github.com/codeql-query-help/cpp/cpp-certificate-result-conflation/) | 295 | (icon: x) | (icon: check) | (icon: check) |
| [Cleartext storage of sensitive information in an SQLite database](https://codeql.github.com/codeql-query-help/cpp/cpp-cleartext-storage-database/) | 313 | (icon: x) | (icon: check) | (icon: check) |
| [Cleartext storage of sensitive information in buffer](https://codeql.github.com/codeql-query-help/cpp/cpp-cleartext-storage-buffer/) | 312 | (icon: x) | (icon: check) | (icon: check) |
| [Comma before misleading indentation](https://codeql.github.com/codeql-query-help/cpp/cpp-comma-before-misleading-indentation/) | 1078, 670 | (icon: x) | (icon: check) | (icon: check) |
| [File created without restricting permissions](https://codeql.github.com/codeql-query-help/cpp/cpp-world-writable-file-creation/) | 732 | (icon: x) | (icon: check) | (icon: check) |
| [Incorrect 'not' operator usage](https://codeql.github.com/codeql-query-help/cpp/cpp-incorrect-not-operator-usage/) | 480 | (icon: x) | (icon: check) | (icon: check) |
| [Incorrect allocation-error handling](https://codeql.github.com/codeql-query-help/cpp/cpp-incorrect-allocation-error-handling/) | 570, 252, 755 | (icon: x) | (icon: check) | (icon: check) |
| [Invalid pointer dereference](https://codeql.github.com/codeql-query-help/cpp/cpp-invalid-pointer-deref/) | 119, 125, 193, 787 | (icon: x) | (icon: check) | (icon: check) |
| [Missing return-value check for a 'scanf'-like function](https://codeql.github.com/codeql-query-help/cpp/cpp-missing-check-scanf/) | 252, 253 | (icon: x) | (icon: check) | (icon: check) |
| [Non-constant format string](https://codeql.github.com/codeql-query-help/cpp/cpp-non-constant-format/) | 134 | (icon: x) | (icon: check) | (icon: check) |
| [Not enough memory allocated for array of pointer type](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-allocation-size/) | 131, 122 | (icon: x) | (icon: check) | (icon: check) |
| [Not enough memory allocated for pointer type](https://codeql.github.com/codeql-query-help/cpp/cpp-allocation-too-small/) | 131, 122 | (icon: x) | (icon: check) | (icon: check) |
| [NULL application name with an unquoted path in call to CreateProcess](https://codeql.github.com/codeql-query-help/cpp/cpp-unsafe-create-process-call/) | 428 | (icon: x) | (icon: check) | (icon: check) |
| [Overrunning write](https://codeql.github.com/codeql-query-help/cpp/cpp-overrun-write/) | 119, 131 | (icon: x) | (icon: check) | (icon: check) |
| [Possibly wrong buffer size in string copy](https://codeql.github.com/codeql-query-help/cpp/cpp-bad-strncpy-size/) | 676, 119, 251 | (icon: x) | (icon: check) | (icon: check) |
| [Potential exposure of sensitive system data to an unauthorized control sphere](https://codeql.github.com/codeql-query-help/cpp/cpp-potential-system-data-exposure/) | 497 | (icon: x) | (icon: check) | (icon: check) |
| [Potentially overrunning write](https://codeql.github.com/codeql-query-help/cpp/cpp-overrunning-write/) | 120, 787, 805 | (icon: x) | (icon: check) | (icon: check) |
| [Potentially overrunning write with float to string conversion](https://codeql.github.com/codeql-query-help/cpp/cpp-overrunning-write-with-float/) | 120, 787, 805 | (icon: x) | (icon: check) | (icon: check) |
| [Potentially uninitialized local variable](https://codeql.github.com/codeql-query-help/cpp/cpp-uninitialized-local/) | 665, 457 | (icon: x) | (icon: check) | (icon: check) |
| [Potentially unsafe use of strcat](https://codeql.github.com/codeql-query-help/cpp/cpp-unsafe-strcat/) | 676, 120, 251 | (icon: x) | (icon: check) | (icon: check) |
| [Suspicious 'sizeof' use](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-sizeof/) | 467 | (icon: x) | (icon: check) | (icon: check) |
| [Suspicious pointer scaling](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-pointer-scaling/) | 468 | (icon: x) | (icon: check) | (icon: x) |
| [Suspicious pointer scaling to void](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-pointer-scaling-void/) | 468 | (icon: x) | (icon: check) | (icon: check) |
| [Type confusion](https://codeql.github.com/codeql-query-help/cpp/cpp-type-confusion/) | 843 | (icon: x) | (icon: check) | (icon: check) |
| [Unbounded write](https://codeql.github.com/codeql-query-help/cpp/cpp-unbounded-write/) | 120, 787, 805 | (icon: x) | (icon: check) | (icon: check) |
| [Uncontrolled allocation size](https://codeql.github.com/codeql-query-help/cpp/cpp-uncontrolled-allocation-size/) | 190, 789 | (icon: x) | (icon: check) | (icon: check) |
| [Uncontrolled data used in path expression](https://codeql.github.com/codeql-query-help/cpp/cpp-path-injection/) | 022, 023, 036, 073 | (icon: x) | (icon: check) | (icon: check) |
| [Uncontrolled process operation](https://codeql.github.com/codeql-query-help/cpp/cpp-uncontrolled-process-operation/) | 073, 078, 114 | (icon: x) | (icon: check) | (icon: check) |
| [Unterminated variadic call](https://codeql.github.com/codeql-query-help/cpp/cpp-unterminated-variadic-call/) | 121 | (icon: x) | (icon: check) | (icon: check) |
| [Untrusted input for a condition](https://codeql.github.com/codeql-query-help/cpp/cpp-tainted-permissions-check/) | 807 | (icon: x) | (icon: check) | (icon: check) |
| [Use of potentially dangerous function](https://codeql.github.com/codeql-query-help/cpp/cpp-potentially-dangerous-function/) | 676 | (icon: x) | (icon: check) | (icon: check) |

{% endrowheaders %}
