---
title: Dependabot auto-triage rules
intro: Control how Dependabot handles security alerts, including filtering, ignoring, snoozing, or triggering security updates.
product: "**GitHub presets** are available for all repository types.\n\n**Custom auto-triage rules** are available for the following repository types:\n\n{% ifversion fpt %}\n* Public repositories on GitHub.com\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{% ifversion ghec %}\n* Public repositories on GitHub.com\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{% ifversion ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}"
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
shortTitle: Dependabot auto-triage rules
redirect_from:
  - /code-security/dependabot/dependabot-alerts/using-alert-rules-to-prioritize-dependabot-alerts
  - /code-security/dependabot/dependabot-alert-rules/about-dependabot-alert-rules
  - /code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules
  - /code-security/dependabot/dependabot-auto-triage-rules
  - /code-security/concepts/supply-chain-security/about-dependabot-auto-triage-rules
contentType: concepts
category:
  - Secure your dependencies
---

## About Dependabot auto-triage rules

Dependabot auto-triage rules allow you to instruct Dependabot to automatically triage Dependabot alerts{% ifversion dependabot-malware-alerts %} and Dependabot malware alerts{% endif %}. You can use auto-triage rules to:
* Automatically dismiss or snooze certain alerts
* Specify the Dependabot alerts you want Dependabot to open pull requests for

Rules are applied before alert notifications are sent, so enabling rules that auto-dismiss low-risk alerts will help reduce notification noise.

There are two types of Dependabot auto-triage rules:

* GitHub presets
* Custom auto-triage rules

### About GitHub presets

GitHub presets are rules curated by GitHub that are available for all repositories.

#### Dismiss low impact issues for development-scoped dependencies

The `Dismiss low impact issues for development-scoped dependencies` rule is a GitHub preset that auto-dismisses certain types of vulnerabilities that are found in npm dependencies used in development. These alerts cover cases that feel like false alarms to most developers as the associated vulnerabilities:

* Are unlikely to be exploitable in a developer (non-production or runtime) environment.
* May relate to resource management, programming and logic, and information disclosure issues.
* At worst, have limited effects like slow builds or long-running tests.
* Are not indicative of issues in production.

The rule is enabled by default for public repositories and can be opted into for private repositories. For instructions, see [Enabling the `Dismiss low impact issues for development-scoped dependencies` rule for your private repository](/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/prioritize-with-preset-rules#enabling-github-preset-rules).

For more information about the criteria used by the rule, see [AUTOTITLE](/code-security/reference/supply-chain-security/criteria-for-preset-rules).

{% ifversion dependabot-malware-alerts %}

#### Dismiss package malware alerts

The `Dismiss package malware alerts` rule is a GitHub preset that auto-dismisses alerts that flag all versions of a package as malicious. If your project depends on an **internal** package with the same ecosystem and name as a malicious **public** package, Dependabot can generate a false positive alert, which the rule then auto-dismisses.

> [!IMPORTANT]
> Be aware that if a contributor adds a dependency that is truly malicious across all versions, this rule will auto-dismiss the related alert.

The `Dismiss package malware alerts` rule is disabled by default, but can be enabled for any repository using Dependabot malware alerts.

{% endif %}

### About custom auto-triage rules

> [!NOTE]
> {%- ifversion fpt %}
  Custom auto-triage rules for Dependabot alerts are available on public repositories and on any organization-owned repositories in GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled.
  
  {%- elsif ghec %}
  Custom auto-triage rules for Dependabot alerts are available on public repositories and on any organization-owned repositories in GitHub Team or GitHub Enterprise with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled.
  
  {%- elsif ghes %}
  Custom auto-triage rules for Dependabot alerts are available for organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled.
  
  {% endif %}

With custom auto-triage rules, you can create your own rules to automatically dismiss or reopen alerts based on targeted metadata, such as severity, package name, CWE, and more. You can also specify which Dependabot alerts you want Dependabot to open pull requests for. For more information, see [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/auto-triage-dependabot-alerts).

You can create custom rules from the **Settings** tab of the repository, provided the repository belongs to an organization that has a license for GitHub Code Security or GitHub Advanced Security. For more information, see [Adding custom auto-triage rules to your repository](/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/auto-triage-dependabot-alerts#adding-custom-auto-triage-rules-to-your-repository).

### About auto-dismissing alerts

Whilst you may find it useful to use auto-triage rules to auto-dismiss alerts, you can still reopen auto-dismissed alerts and filter to see which alerts have been auto-dismissed. For more information, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-dependabot-alerts/managing-automatically-dismissed-alerts).

Additionally, auto-dismissed alerts are still available for reporting and reviewing, and can be auto-reopened if the alert metadata changes, for example:
* If you change the scope of a dependency from development to production.
* If GitHub modifies certain metadata for the related advisory.

Auto-dismissed alerts are defined by the `resolution:auto-dismiss` close reason. Automatic dismissal activity is included in alert webhooks, REST and GraphQL APIs, and the audit log. For more information, see [AUTOTITLE](/rest/dependabot/alerts), and the "`repository_vulnerability_alert`" section in [AUTOTITLE](/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization).

## Next steps

To get started with Dependabot auto-triage rules, see [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/prioritize-with-preset-rules).

To customize your auto-triage experience, see [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/auto-triage-dependabot-alerts).
