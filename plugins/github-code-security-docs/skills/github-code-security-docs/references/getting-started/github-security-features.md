---
title: GitHub security features
intro: An overview of GitHub's security features.
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
contentType: get-started
category:
  - Plan your security strategy
---

## About GitHub's security features

GitHub's security features help keep your code and secrets secure in repositories and across organizations.

{% ifversion fpt or ghec %}

* Some features are available for all GitHub plans.
* Additional features are available to organizations {% ifversion ghec %}and enterprises{% endif %} on GitHub Team and GitHub Enterprise Cloud that purchase a GitHub Advanced Security product:
  * [GitHub Secret Protection](#available-with-github-secret-protection)
  * [GitHub Code Security](#available-with-github-code-security)
* In addition, a number of GitHub Secret Protection and GitHub Code Security features can be run on public repositories for free.{% endif %}

{%- ifversion ghes %}

* Some features are available for all repositories by default.
* Additional features are available to enterprises that purchase a GitHub Advanced Security product:
  * [GitHub Secret Protection](#available-with-github-secret-protection)
  * [GitHub Code Security](#available-with-github-code-security){% endif %}

## Available for all GitHub plans

The following security features are available for you to use, regardless of the GitHub plan you are on. You don't need to purchase GitHub Secret Protection or GitHub Code Security to use these features.

{% ifversion fpt or ghec %}

Most of these features are available for public{% ifversion ghec %}, internal,{% endif %} and private repositories.
Some features are _only_ available for public repositories.

{% endif %}

### Security policy

Make it easy for your users to confidentially report security vulnerabilities they've found in your repository. For more information, see [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/add-security-policy).

### Dependency graph

The dependency graph allows you to explore the ecosystems and packages that your repository depends on and the repositories and packages that depend on your repository.

You can find the dependency graph on the **Insights** tab for your repository. For more information, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependency-graph).

### Software Bill of Materials (SBOM)

You can export the dependency graph of your repository as an SPDX-compatible, Software Bill of Materials (SBOM). For more information, see [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/export-dependencies-as-sbom).

### GitHub Advisory Database

The GitHub Advisory Database contains a curated list of security vulnerabilities that you can view, search, and filter. For more information, see [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/browse-advisory-database).

### Dependabot alerts and security updates

View alerts about dependencies that are known to contain security vulnerabilities, and choose whether to have pull requests generated automatically to update these dependencies. For more information, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-alerts)
and [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-security-updates).

You can also use default Dependabot auto-triage rules curated by GitHub to automatically filter out a substantial amount of false positives.

For an overview of the different features offered by Dependabot and instructions on how to get started, see [AUTOTITLE](/code-security/tutorials/secure-your-dependencies/dependabot-quickstart).

{% ifversion dependabot-malware-alerts %}

#### Dependabot malware alerts

On GitHub.com and GitHub Enterprise Server 3.22+, you can view alerts for malicious dependencies in your repository. See [AUTOTITLE](/code-security/concepts/supply-chain-security/malware-alerts).

{% endif %}

### Dependabot version updates

Use Dependabot to automatically raise pull requests to keep your dependencies up-to-date. This helps reduce your exposure to older versions of dependencies. Using newer versions makes it easier to apply patches if security vulnerabilities are discovered, and also makes it easier for Dependabot security updates to successfully raise pull requests to upgrade vulnerable dependencies. You can also customize Dependabot version updates to streamline their integration into your repositories. For more information, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-version-updates).

{% ifversion fpt or ghec %}

### Security advisories

Privately discuss and fix security vulnerabilities in your public repository's code. You can then publish a security advisory to alert your community to the vulnerability and encourage community members to upgrade. For more information, see [AUTOTITLE](/code-security/concepts/vulnerability-reporting-and-management/repository-security-advisories).

{% endif %}

### Repository rulesets

Enforce consistent code standards, security, and compliance across branches and tags. For more information, see [AUTOTITLE](/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).

{% ifversion fpt or ghec %}

### Artifact attestations

Create unfalsifiable provenance and integrity guarantees for the software you build. For more information, see [AUTOTITLE](/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations).

{% ifversion fpt %}

> [!NOTE]
> If you are on a GitHub Free, GitHub Pro, or GitHub Team plan, artifact attestations are only available for public repositories. To use artifact attestations in private or internal repositories, you must be on a GitHub Enterprise Cloud plan.{% endif %}

### Secret scanning alerts for partners

When GitHub detects a leaked secret in a public repository, or a public npm packages, GitHub informs the relevant service provider that the secret may be compromised. For details of the supported secrets and service providers, see [AUTOTITLE](/code-security/reference/secret-security/supported-secret-scanning-patterns#supported-provider-patterns).

{% ifversion secret-scanning-push-protection-for-users %}

### Push protection for users

Push protection for users automatically protects you from accidentally committing secrets to public repositories, regardless of whether the repository itself has secret scanning enabled. Push protection for users is on by default, but you can disable the feature at any time through your personal account settings. For more information, see [AUTOTITLE](/code-security/how-tos/secure-your-secrets/prevent-future-leaks/manage-user-push-protection).

{% endif %}

{% endif %}

## Available with GitHub Secret Protection

For accounts on {% ifversion fpt or ghec %}GitHub Team and GitHub Enterprise Cloud{% endif %}{% ifversion ghes %} GitHub Enterprise Server{% endif %}, you can access additional security features when you purchase **GitHub Secret Protection**.

GitHub Secret Protection includes features that help you detect and prevent credential leaks and secret sprawl, such as secret scanning for detecting hardcoded credentials and push protection for blocking them before they reach your repository.

These features are available for all repository types. {% ifversion fpt or ghec %}Some of these features are available for public repositories free of charge, meaning that you don't need to purchase GitHub Secret Protection to enable the feature on a public repository.{% endif %}

<!--Hiding information on setting up a trial for now, as there is no available link for fpt yet. Needs versioning for fpt, ghec and ghes.
For information about how you can try GitHub Secret Protection for free, see [AUTOTITLE](/code-security/tutorials/trialing-github-advanced-security/trial-advanced-security).
-->

### {% ifversion fpt or ghec %}Secret scanning alerts for users{% else %}Secret scanning{% endif %}

Automatically detect hardcoded credentials that have been checked into a repository. You can view alerts for any secrets that GitHub finds in your code, in the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab of your repository, so you can respond to credential leaks quickly. For more information, see [AUTOTITLE](/code-security/concepts/secret-security/secret-scanning).

{% ifversion fpt or ghec %}

Available for public repositories by default.

{% endif %}

{% ifversion secret-scanning-ai-generic-secret-detection %}

### AI-detected secrets

AI-detected secrets's generic secret detection is an AI-powered expansion of secret scanning that identifies unstructured secrets (passwords) in your source code and then generates an alert.{% ifversion fpt or ghec %} For more information, see [AUTOTITLE](/code-security/responsible-use/security-and-quality-ai-features).{% endif %}

{% endif %}

### Push protection

Push protection proactively scans your code, and any repository contributors' code, for hardcoded secrets during the push process and blocks the push if any credential leaks are detected. If a contributor bypasses the block, an alert is generated. For more information, see [AUTOTITLE](/code-security/concepts/secret-security/push-protection).

{% ifversion fpt or ghec %}

Available for public repositories by default.

{% endif %}

### Delegated bypass for push protection

Delegated bypass for push protection lets you control which individuals, roles, and teams:
* Can bypass push protection{% ifversion push-protection-org-enterprise-exemptions %}
* Are exempt from push protection{% endif %}
* Can review bypass requests from other contributors

For more information, see [AUTOTITLE](/code-security/concepts/secret-security/delegated-bypass).

### Custom patterns

You can define custom patterns to identify secrets that are not detected by the default patterns supported by secret scanning, such as patterns that are internal to your organization. For more information, see [AUTOTITLE](/code-security/how-tos/secure-your-secrets/customize-leak-detection/define-custom-patterns).

<!--Hiding security overview for earlier GHES versions, so it isn't duplicated below-->

### Security overview

Security overview allows you to review the overall security landscape of your organization, view trends and other insights, and manage security configurations, making it easy to monitor your organization's security status and identify the repositories and organizations at greatest risk. For more information, see [AUTOTITLE](/code-security/concepts/security-at-scale/security-overview).

## Available with GitHub Code Security

For accounts on {% ifversion fpt or ghec %}GitHub Team and GitHub Enterprise Cloud{% endif %}{% ifversion ghes %} GitHub Enterprise Server{% endif %}, you can access additional security features when you purchase **GitHub Code Security**.

GitHub Code Security includes features that help you find and fix vulnerabilities, like code scanning, premium Dependabot features, and dependency review.

These features are available for all repository types. {% ifversion fpt or ghec %}Some of these features are available for public repositories free of charge, meaning that you don't need to purchase GitHub Code Security to enable the feature on a public repository.{% endif %}

<!--Hiding information on setting up a trial for now, as there is no available link for fpt yet. Needs versioning for fpt, ghec & ghes.

For information about how you can try GitHub Code Security for free, see [AUTOTITLE](/code-security/tutorials/trialing-github-advanced-security/trial-advanced-security).

-->

### Code scanning

Automatically detect security vulnerabilities and coding errors in new or modified code. Potential problems are highlighted, with detailed information, allowing you to fix the code before it's merged into your default branch. For more information, see [AUTOTITLE](/code-security/concepts/code-scanning/code-scanning).

{% ifversion fpt or ghec %}

Available for public repositories by default.

{% endif %}

### CodeQL CLI

Run CodeQL processes locally on software projects or to generate code scanning results for upload to GitHub. For more information, see [AUTOTITLE](/code-security/concepts/code-scanning/codeql/codeql-cli).

{% ifversion fpt or ghec %}

Available for public repositories by default.

{% endif %}

{% ifversion code-scanning-autofix %}

### Copilot Autofix

Get automatically generated fixes for code scanning alerts. For more information, see [AUTOTITLE](/code-security/responsible-use/security-and-quality-ai-features).

{% ifversion fpt or ghec %}

Available for public repositories by default.

{% endif %}

{% endif %}

{% ifversion ai-powered-security-detections %}

### AI Scan

Find vulnerabilities in languages and frameworks not covered by CodeQL with an AI-based scanning engine that runs during pull request review. See [AUTOTITLE](/code-security/concepts/code-scanning/ai-powered-security-detections).

{% endif %}

### Custom auto-triage rules for Dependabot

Help you manage your Dependabot alerts at scale. With custom auto-triage rules you have control over the alerts you want to ignore, snooze, or trigger a Dependabot security update for. For more information, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-alerts) and [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/auto-triage-dependabot-alerts).

### Dependency review

Show the full impact of changes to dependencies and see details of any vulnerable versions before you merge a pull request. For more information, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependency-review).

{% ifversion fpt or ghec %}

Available for public repositories by default.

{% endif %}

{% ifversion security-campaigns %}

### Security campaigns

Fix security alerts at scale by creating security campaigns and collaborating with developers to reduce your security backlog. For more information, see [AUTOTITLE](/code-security/concepts/security-at-scale/about-security-campaigns).

{% endif %}

### Security overview

Security overview allows you to review the overall security landscape of your organization, view trends and other insights, and manage security configurations, making it easy to monitor your organization's security status and identify the repositories and organizations at greatest risk. For more information, see [AUTOTITLE](/code-security/concepts/security-at-scale/security-overview).

{% ifversion copilot-chat-ghas-alerts %}

## Leveraging GitHub Copilot Chat to understand security alerts

With a GitHub Copilot Enterprise license, you can also ask GitHub Copilot Chat for help to better understand security alerts in repositories in your organization from GitHub Advanced Security features (code scanning, secret scanning, and Dependabot alerts). For more information, see [AUTOTITLE](/copilot/how-tos/copilot-on-github/chat-with-copilot/chat-in-github).

{% endif %}

## Further reading

* [AUTOTITLE](/get-started/learning-about-github/githubs-plans)
* [AUTOTITLE](/get-started/learning-about-github/about-github-advanced-security)
* [AUTOTITLE](/get-started/learning-about-github/github-language-support)
