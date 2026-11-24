---
title: Java and Kotlin queries for CodeQL analysis
shortTitle: Java and Kotlin queries
intro: Explore the queries that CodeQL uses to analyze code written in Java or Kotlin when you select the `default` or the `security-extended` query suite.
product: "CodeQL is available for the following repository types:\n\n{%- ifversion fpt %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghec %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{% endif %}"
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/code-scanning/managing-your-code-scanning-configuration/java-kotlin-built-in-queries
  - /code-security/code-scanning/reference/code-ql-built-in-queries/java-kotlin-built-in-queries
contentType: reference
category:
  - Find CodeQL CLI commands
---

CodeQL includes many queries for analyzing Java and Kotlin code. All queries in the `default` query suite are run by default. If you choose to use the `security-extended` query suite, additional queries are run. For more information, see [AUTOTITLE](/code-security/concepts/code-scanning/codeql/codeql-query-suites).

## Built-in queries for Java and Kotlin analysis

This table lists the queries available with the latest release of the CodeQL action and CodeQL CLI. For more information, see [CodeQL change logs](https://codeql.github.com/docs/codeql-overview/codeql-changelog/) in the CodeQL documentation site.

{% ifversion ghes %}

> [!NOTE]
> The initial release of GitHub Enterprise Server {{ allVersions[currentVersion].currentRelease }} included CodeQL action and CodeQL CLI {% ifversion ghes < 3.20 %}2.22.4{% elsif ghes < 3.21 %}2.23.9{% elsif ghes < 3.22 %}2.24.3{% elsif ghes < 3.23 %}2.25.6{% elsif ghes < 3.24 %}2.27.0{% endif %}, which may not include all of these queries. Your site administrator can update your CodeQL version to a newer release. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance).

{% endif %}

{% rowheaders %}

| Query name | Related CWEs | Default | Extended | Copilot Autofix |
| --- | --- | --- | --- | --- |
| [`TrustManager` that accepts all certificates](https://codeql.github.com/codeql-query-help/java/java-insecure-trustmanager/) | 295 | (icon: check) | (icon: check) | (icon: check) |
| [Android `WebView` that accepts all certificates](https://codeql.github.com/codeql-query-help/java/java-improper-webview-certificate-validation/) | 295 | (icon: check) | (icon: check) | (icon: check) |
| [Android debuggable attribute enabled](https://codeql.github.com/codeql-query-help/java/java-android-debuggable-attribute-enabled/) | 489 | (icon: check) | (icon: check) | (icon: check) |
| [Android fragment injection](https://codeql.github.com/codeql-query-help/java/java-android-fragment-injection/) | 470 | (icon: check) | (icon: check) | (icon: check) |
| [Android fragment injection in PreferenceActivity](https://codeql.github.com/codeql-query-help/java/java-android-fragment-injection-preference-activity/) | 470 | (icon: check) | (icon: check) | (icon: check) |
| [Android Intent redirection](https://codeql.github.com/codeql-query-help/java/java-android-intent-redirection/) | 926, 940 | (icon: check) | (icon: check) | (icon: check) |
| [Android Webview debugging enabled](https://codeql.github.com/codeql-query-help/java/java-android-webview-debugging-enabled/) | 489 | (icon: check) | (icon: check) | (icon: check) |
| [Arbitrary file access during archive extraction ("Zip Slip")](https://codeql.github.com/codeql-query-help/java/java-zipslip/) | 022 | (icon: check) | (icon: check) | (icon: check) |
| [Cleartext storage of sensitive information in cookie](https://codeql.github.com/codeql-query-help/java/java-cleartext-storage-in-cookie/) | 315 | (icon: check) | (icon: check) | (icon: check) |
| [Cross-site scripting](https://codeql.github.com/codeql-query-help/java/java-xss/) | 079 | (icon: check) | (icon: check) | (icon: check) |
| [Depending upon JCenter/Bintray as an artifact repository](https://codeql.github.com/codeql-query-help/java/java-maven-dependency-upon-bintray/) | 1104 | (icon: check) | (icon: check) | (icon: check) |
| [Deserialization of user-controlled data](https://codeql.github.com/codeql-query-help/java/java-unsafe-deserialization/) | 502 | (icon: check) | (icon: check) | (icon: x) |
| [Detect JHipster Generator Vulnerability CVE-2019-16303](https://codeql.github.com/codeql-query-help/java/java-jhipster-prng/) | 338 | (icon: check) | (icon: check) | (icon: check) |
| [Disabled Netty HTTP header validation](https://codeql.github.com/codeql-query-help/java/java-netty-http-request-or-response-splitting/) | 093, 113 | (icon: check) | (icon: check) | (icon: check) |
| [Disabled Spring CSRF protection](https://codeql.github.com/codeql-query-help/java/java-spring-disabled-csrf-protection/) | 352 | (icon: check) | (icon: check) | (icon: check) |
| [Exposed Spring Boot actuators](https://codeql.github.com/codeql-query-help/java/java-spring-boot-exposed-actuators/) | 200 | (icon: check) | (icon: check) | (icon: x) |
| [Exposed Spring Boot actuators in configuration file](https://codeql.github.com/codeql-query-help/java/java-spring-boot-exposed-actuators-config/) | 200 | (icon: check) | (icon: check) | (icon: x) |
| [Expression language injection (JEXL)](https://codeql.github.com/codeql-query-help/java/java-jexl-expression-injection/) | 094 | (icon: check) | (icon: check) | (icon: check) |
| [Expression language injection (MVEL)](https://codeql.github.com/codeql-query-help/java/java-mvel-expression-injection/) | 094 | (icon: check) | (icon: check) | (icon: check) |
| [Expression language injection (Spring)](https://codeql.github.com/codeql-query-help/java/java-spel-expression-injection/) | 094 | (icon: check) | (icon: check) | (icon: check) |
| [Failure to use HTTPS or SFTP URL in Maven artifact upload/download](https://codeql.github.com/codeql-query-help/java/java-maven-non-https-url/) | 300, 319, 494, 829 | (icon: check) | (icon: check) | (icon: check) |
| [Failure to use secure cookies](https://codeql.github.com/codeql-query-help/java/java-insecure-cookie/) | 614 | (icon: check) | (icon: check) | (icon: check) |
| [Groovy Language injection](https://codeql.github.com/codeql-query-help/java/java-groovy-injection/) | 094 | (icon: check) | (icon: check) | (icon: check) |
| [HTTP response splitting](https://codeql.github.com/codeql-query-help/java/java-http-response-splitting/) | 113 | (icon: check) | (icon: check) | (icon: check) |
| [Implicit narrowing conversion in compound assignment](https://codeql.github.com/codeql-query-help/java/java-implicit-cast-in-compound-assignment/) | 190, 192, 197, 681 | (icon: check) | (icon: check) | (icon: check) |
| [Implicitly exported Android component](https://codeql.github.com/codeql-query-help/java/java-android-implicitly-exported-component/) | 926 | (icon: check) | (icon: check) | (icon: check) |
| [Improper verification of intent by broadcast receiver](https://codeql.github.com/codeql-query-help/java/java-improper-intent-verification/) | 925 | (icon: check) | (icon: check) | (icon: check) |
| [Inefficient regular expression](https://codeql.github.com/codeql-query-help/java/java-redos/) | 1333, 730, 400 | (icon: check) | (icon: check) | (icon: x) |
| [Information exposure through a stack trace](https://codeql.github.com/codeql-query-help/java/java-stack-trace-exposure/) | 209, 497 | (icon: check) | (icon: check) | (icon: check) |
| [Information exposure through an error message](https://codeql.github.com/codeql-query-help/java/java-error-message-exposure/) | 209 | (icon: check) | (icon: check) | (icon: check) |
| [Insecure Bean Validation](https://codeql.github.com/codeql-query-help/java/java-insecure-bean-validation/) | 094 | (icon: check) | (icon: check) | (icon: check) |
| [Insecure LDAP authentication](https://codeql.github.com/codeql-query-help/java/java-insecure-ldap-auth/) | 522, 319 | (icon: check) | (icon: check) | (icon: check) |
| [Insecure local authentication](https://codeql.github.com/codeql-query-help/java/java-android-insecure-local-authentication/) | 287 | (icon: check) | (icon: check) | (icon: check) |
| [Insecure randomness](https://codeql.github.com/codeql-query-help/java/java-insecure-randomness/) | 330, 338 | (icon: check) | (icon: check) | (icon: check) |
| [Intent URI permission manipulation](https://codeql.github.com/codeql-query-help/java/java-android-intent-uri-permission-manipulation/) | 266, 926 | (icon: check) | (icon: check) | (icon: check) |
| [JNDI lookup with user-controlled name](https://codeql.github.com/codeql-query-help/java/java-jndi-injection/) | 074 | (icon: check) | (icon: check) | (icon: check) |
| [LDAP query built from user-controlled sources](https://codeql.github.com/codeql-query-help/java/java-ldap-injection/) | 090 | (icon: check) | (icon: check) | (icon: check) |
| [Missing JWT signature check](https://codeql.github.com/codeql-query-help/java/java-missing-jwt-signature-check/) | 347 | (icon: check) | (icon: check) | (icon: check) |
| [OGNL Expression Language statement with user-controlled input](https://codeql.github.com/codeql-query-help/java/java-ognl-injection/) | 917 | (icon: check) | (icon: check) | (icon: check) |
| [Overly permissive regular expression range](https://codeql.github.com/codeql-query-help/java/java-overly-large-range/) | 020 | (icon: check) | (icon: check) | (icon: check) |
| [Partial path traversal vulnerability from remote](https://codeql.github.com/codeql-query-help/java/java-partial-path-traversal-from-remote/) | 023 | (icon: check) | (icon: check) | (icon: check) |
| [Polynomial regular expression used on uncontrolled data](https://codeql.github.com/codeql-query-help/java/java-polynomial-redos/) | 1333, 730, 400 | (icon: check) | (icon: check) | (icon: x) |
| [Query built from user-controlled sources](https://codeql.github.com/codeql-query-help/java/java-sql-injection/) | 089, 564 | (icon: check) | (icon: check) | (icon: check) |
| [Reading from a world writable file](https://codeql.github.com/codeql-query-help/java/java-world-writable-file-read/) | 732 | (icon: check) | (icon: check) | (icon: check) |
| [Regular expression injection](https://codeql.github.com/codeql-query-help/java/java-regex-injection/) | 730, 400 | (icon: check) | (icon: check) | (icon: x) |
| [Resolving XML external entity in user-controlled data](https://codeql.github.com/codeql-query-help/java/java-xxe/) | 611, 776, 827 | (icon: check) | (icon: check) | (icon: check) |
| [Sensitive cookies without the HttpOnly response header set](https://codeql.github.com/codeql-query-help/java/java-sensitive-cookie-not-httponly/) | 1004 | (icon: check) | (icon: check) | (icon: x) |
| [Server-side request forgery](https://codeql.github.com/codeql-query-help/java/java-ssrf/) | 918 | (icon: check) | (icon: check) | (icon: check) |
| [Server-side template injection](https://codeql.github.com/codeql-query-help/java/java-server-side-template-injection/) | 1336, 094 | (icon: check) | (icon: check) | (icon: check) |
| [Uncontrolled command line](https://codeql.github.com/codeql-query-help/java/java-command-line-injection/) | 078, 088 | (icon: check) | (icon: check) | (icon: check) |
| [Uncontrolled data used in content resolution](https://codeql.github.com/codeql-query-help/java/java-android-unsafe-content-uri-resolution/) | 441, 610 | (icon: check) | (icon: check) | (icon: check) |
| [Uncontrolled data used in path expression](https://codeql.github.com/codeql-query-help/java/java-path-injection/) | 022, 023, 036, 073 | (icon: check) | (icon: check) | (icon: check) |
| [Unsafe hostname verification](https://codeql.github.com/codeql-query-help/java/java-unsafe-hostname-verification/) | 297 | (icon: check) | (icon: check) | (icon: check) |
| [URL forward from a remote source](https://codeql.github.com/codeql-query-help/java/java-unvalidated-url-forward/) | 552 | (icon: check) | (icon: check) | (icon: check) |
| [URL redirection from remote source](https://codeql.github.com/codeql-query-help/java/java-unvalidated-url-redirection/) | 601 | (icon: check) | (icon: check) | (icon: check) |
| [Use of a broken or risky cryptographic algorithm](https://codeql.github.com/codeql-query-help/java/java-weak-cryptographic-algorithm/) | 327, 328 | (icon: check) | (icon: check) | (icon: check) |
| [Use of a cryptographic algorithm with insufficient key size](https://codeql.github.com/codeql-query-help/java/java-insufficient-key-size/) | 326 | (icon: check) | (icon: check) | (icon: check) |
| [Use of a predictable seed in a secure random number generator](https://codeql.github.com/codeql-query-help/java/java-predictable-seed/) | 335, 337 | (icon: check) | (icon: check) | (icon: check) |
| [Use of externally-controlled format string](https://codeql.github.com/codeql-query-help/java/java-tainted-format-string/) | 134 | (icon: check) | (icon: check) | (icon: check) |
| [Use of implicit PendingIntents](https://codeql.github.com/codeql-query-help/java/java-android-implicit-pendingintents/) | 927 | (icon: check) | (icon: check) | (icon: check) |
| [Use of RSA algorithm without OAEP](https://codeql.github.com/codeql-query-help/java/java-rsa-without-oaep/) | 780 | (icon: check) | (icon: check) | (icon: check) |
| [User-controlled data in numeric cast](https://codeql.github.com/codeql-query-help/java/java-tainted-numeric-cast/) | 197, 681 | (icon: check) | (icon: check) | (icon: check) |
| [User-controlled data used in permissions check](https://codeql.github.com/codeql-query-help/java/java-tainted-permissions-check/) | 807, 290 | (icon: check) | (icon: check) | (icon: check) |
| [Using a static initialization vector for encryption](https://codeql.github.com/codeql-query-help/java/java-static-initialization-vector/) | 329, 1204 | (icon: check) | (icon: check) | (icon: check) |
| [XPath injection](https://codeql.github.com/codeql-query-help/java/java-xml-xpath-injection/) | 643 | (icon: check) | (icon: check) | (icon: check) |
| [XSLT transformation with user-controlled stylesheet](https://codeql.github.com/codeql-query-help/java/java-xslt-injection/) | 074 | (icon: check) | (icon: check) | (icon: check) |
| [Access Java object methods through JavaScript exposure](https://codeql.github.com/codeql-query-help/java/java-android-webview-addjavascriptinterface/) | 079 | (icon: x) | (icon: check) | (icon: x) |
| [Android APK installation](https://codeql.github.com/codeql-query-help/java/java-android-arbitrary-apk-installation/) | 094 | (icon: x) | (icon: check) | (icon: x) |
| [Android missing certificate pinning](https://codeql.github.com/codeql-query-help/java/java-android-missing-certificate-pinning/) | 295 | (icon: x) | (icon: check) | (icon: check) |
| [Android sensitive keyboard cache](https://codeql.github.com/codeql-query-help/java/java-android-sensitive-keyboard-cache/) | 524 | (icon: x) | (icon: check) | (icon: check) |
| [Android WebSettings file access](https://codeql.github.com/codeql-query-help/java/java-android-websettings-file-access/) | 200 | (icon: x) | (icon: check) | (icon: check) |
| [Android WebView JavaScript settings](https://codeql.github.com/codeql-query-help/java/java-android-websettings-javascript-enabled/) | 079 | (icon: x) | (icon: check) | (icon: check) |
| [Android WebView settings allows access to content links](https://codeql.github.com/codeql-query-help/java/java-android-websettings-allow-content-access/) | 200 | (icon: x) | (icon: check) | (icon: check) |
| [Application backup allowed](https://codeql.github.com/codeql-query-help/java/java-android-backup-enabled/) | 312 | (icon: x) | (icon: check) | (icon: check) |
| [Building a command line with string concatenation](https://codeql.github.com/codeql-query-help/java/java-concatenated-command-line/) | 078, 088 | (icon: x) | (icon: check) | (icon: x) |
| [Building a command with an injected environment variable](https://codeql.github.com/codeql-query-help/java/java-exec-tainted-environment/) | 078, 088, 454 | (icon: x) | (icon: check) | (icon: check) |
| [Cleartext storage of sensitive information in the Android filesystem](https://codeql.github.com/codeql-query-help/java/java-android-cleartext-storage-filesystem/) | 312 | (icon: x) | (icon: check) | (icon: check) |
| [Cleartext storage of sensitive information using 'Properties' class](https://codeql.github.com/codeql-query-help/java/java-cleartext-storage-in-properties/) | 313 | (icon: x) | (icon: check) | (icon: check) |
| [Cleartext storage of sensitive information using `SharedPreferences` on Android](https://codeql.github.com/codeql-query-help/java/java-android-cleartext-storage-shared-prefs/) | 312 | (icon: x) | (icon: check) | (icon: check) |
| [Cleartext storage of sensitive information using a local database on Android](https://codeql.github.com/codeql-query-help/java/java-android-cleartext-storage-database/) | 312 | (icon: x) | (icon: check) | (icon: x) |
| [Comparison of narrow type with wide type in loop condition](https://codeql.github.com/codeql-query-help/java/java-comparison-with-wider-type/) | 190, 197 | (icon: x) | (icon: check) | (icon: check) |
| [Executing a command with a relative path](https://codeql.github.com/codeql-query-help/java/java-relative-path-command/) | 078, 088 | (icon: x) | (icon: check) | (icon: check) |
| [Exposure of sensitive information to notifications](https://codeql.github.com/codeql-query-help/java/java-android-sensitive-notification/) | 200 | (icon: x) | (icon: check) | (icon: check) |
| [Exposure of sensitive information to UI text views](https://codeql.github.com/codeql-query-help/java/java-android-sensitive-text/) | 200 | (icon: x) | (icon: check) | (icon: check) |
| [HTTP request type unprotected from CSRF](https://codeql.github.com/codeql-query-help/java/java-csrf-unprotected-request-type/) | 352 | (icon: x) | (icon: check) | (icon: check) |
| [Improper validation of user-provided array index](https://codeql.github.com/codeql-query-help/java/java-improper-validation-of-array-index/) | 129 | (icon: x) | (icon: check) | (icon: check) |
| [Improper validation of user-provided size used for array construction](https://codeql.github.com/codeql-query-help/java/java-improper-validation-of-array-construction/) | 129 | (icon: x) | (icon: check) | (icon: check) |
| [Insecure basic authentication](https://codeql.github.com/codeql-query-help/java/java-insecure-basic-auth/) | 522, 319 | (icon: x) | (icon: check) | (icon: check) |
| [Insecure JavaMail SSL Configuration](https://codeql.github.com/codeql-query-help/java/java-insecure-smtp-ssl/) | 297 | (icon: x) | (icon: check) | (icon: check) |
| [Insecurely generated keys for local authentication](https://codeql.github.com/codeql-query-help/java/java-android-insecure-local-key-gen/) | 287 | (icon: x) | (icon: check) | (icon: check) |
| [Insertion of sensitive information into log files](https://codeql.github.com/codeql-query-help/java/java-sensitive-log/) | 532 | (icon: x) | (icon: check) | (icon: check) |
| [Leaking sensitive information through a ResultReceiver](https://codeql.github.com/codeql-query-help/java/java-android-sensitive-result-receiver/) | 927 | (icon: x) | (icon: check) | (icon: check) |
| [Leaking sensitive information through an implicit Intent](https://codeql.github.com/codeql-query-help/java/java-android-sensitive-communication/) | 927 | (icon: x) | (icon: check) | (icon: x) |
| [Local information disclosure in a temporary directory](https://codeql.github.com/codeql-query-help/java/java-local-temp-file-or-directory-information-disclosure/) | 200, 732 | (icon: x) | (icon: check) | (icon: check) |
| [Log Injection](https://codeql.github.com/codeql-query-help/java/java-log-injection/) | 117 | (icon: x) | (icon: check) | (icon: check) |
| [Loop with unreachable exit condition](https://codeql.github.com/codeql-query-help/java/java-unreachable-exit-in-loop/) | 835 | (icon: x) | (icon: check) | (icon: x) |
| [Missing read or write permission in a content provider](https://codeql.github.com/codeql-query-help/java/java-android-incomplete-provider-permissions/) | 926 | (icon: x) | (icon: check) | (icon: check) |
| [Partial path traversal vulnerability](https://codeql.github.com/codeql-query-help/java/java-partial-path-traversal/) | 023 | (icon: x) | (icon: check) | (icon: check) |
| [Query built by concatenation with a possibly-untrusted string](https://codeql.github.com/codeql-query-help/java/java-concatenated-sql-query/) | 089, 564 | (icon: x) | (icon: check) | (icon: check) |
| [Race condition in socket authentication](https://codeql.github.com/codeql-query-help/java/java-socket-auth-race-condition/) | 421 | (icon: x) | (icon: check) | (icon: check) |
| [Time-of-check time-of-use race condition](https://codeql.github.com/codeql-query-help/java/java-toctou-race-condition/) | 367 | (icon: x) | (icon: check) | (icon: check) |
| [Trust boundary violation](https://codeql.github.com/codeql-query-help/java/java-trust-boundary-violation/) | 501 | (icon: x) | (icon: check) | (icon: check) |
| [Uncontrolled data in arithmetic expression](https://codeql.github.com/codeql-query-help/java/java-uncontrolled-arithmetic/) | 190, 191 | (icon: x) | (icon: check) | (icon: check) |
| [Unreleased lock](https://codeql.github.com/codeql-query-help/java/java-unreleased-lock/) | 764, 833 | (icon: x) | (icon: check) | (icon: x) |
| [Unsafe certificate trust](https://codeql.github.com/codeql-query-help/java/java-unsafe-cert-trust/) | 273 | (icon: x) | (icon: check) | (icon: check) |
| [Unsafe resource fetching in Android WebView](https://codeql.github.com/codeql-query-help/java/java-android-unsafe-android-webview-fetch/) | 749, 079 | (icon: x) | (icon: check) | (icon: x) |
| [Use of a potentially broken or risky cryptographic algorithm](https://codeql.github.com/codeql-query-help/java/java-potentially-weak-cryptographic-algorithm/) | 327, 328 | (icon: x) | (icon: check) | (icon: check) |
| [Use of a potentially dangerous function](https://codeql.github.com/codeql-query-help/java/java-potentially-dangerous-function/) | 676 | (icon: x) | (icon: check) | (icon: x) |
| [User-controlled bypass of sensitive method](https://codeql.github.com/codeql-query-help/java/java-user-controlled-bypass/) | 807, 290 | (icon: x) | (icon: check) | (icon: x) |
| [User-controlled data in arithmetic expression](https://codeql.github.com/codeql-query-help/java/java-tainted-arithmetic/) | 190, 191 | (icon: x) | (icon: check) | (icon: check) |

{% endrowheaders %}
