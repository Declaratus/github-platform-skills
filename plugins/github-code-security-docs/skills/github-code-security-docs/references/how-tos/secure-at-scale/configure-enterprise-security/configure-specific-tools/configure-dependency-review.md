---
title: Configuring dependency review for your appliance
shortTitle: Configure dependency review
intro: To help users understand dependency changes when reviewing pull requests, you can enable, configure, and disable dependency review for GitHub Enterprise Server.
product: "Dependency review is available for the following repository types:\n\n{%- ifversion fpt %}\n* Public repositories on GitHub.com\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{%- ifversion ghec %}\n* Public repositories on GitHub.com\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{%- ifversion ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}"
versions:
  ghes: '*'
redirect_from:
  - /admin/code-security/managing-github-advanced-security-for-your-enterprise/configuring-dependency-review-for-your-appliance
  - /admin/managing-code-security/managing-github-advanced-security-for-your-enterprise/configuring-dependency-review-for-your-appliance
  - /code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-dependency-review-for-your-appliance
contentType: how-tos
category:
  - Secure your dependencies
---

## About dependency review

Dependency review helps you understand dependency changes and the security impact of these changes at every pull request. It provides an easily understandable visualization of dependency changes with a rich diff on the "Files Changed" tab of a pull request. Dependency review informs you of:
* Which dependencies were added, removed, or updated, along with the release dates
* How many projects use these components
* Vulnerability data for these dependencies

Some additional features, such as license checks, blocking of pull requests, and CI/CD integration, are available with the [dependency review action](https://github.com/actions/dependency-review-action).

## Checking whether your license includes Advanced Security

You can identify if your enterprise has a license for Advanced Security products by reviewing your enterprise settings. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/establish-complete-coverage/enabling-github-advanced-security-for-your-enterprise#checking-whether-your-license-includes-advanced-security).

## Prerequisites for dependency review

* A license for GitHub Code Security or GitHub Advanced Security (see [AUTOTITLE](/billing/concepts/product-billing/github-advanced-security)).

* The dependency graph enabled for the instance. Site administrators can enable the dependency graph via the management console or the administrative shell (see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/enable-dependency-graph)).

* GitHub Connect enabled to download and synchronize vulnerabilities from the GitHub Advisory Database. This is usually configured as part of setting up Dependabot (see [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-dependabot-for-your-enterprise)).

## Enabling and disabling dependency review

To enable or disable dependency review, you need to enable or disable the dependency graph for your instance.

For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/enable-dependency-graph).

## Running dependency review using GitHub Actions

> [!NOTE]
> The dependency review action is currently in public preview and subject to change.

The dependency review action is included in your installation of GitHub Enterprise Server. It is available for all repositories that have GitHub Code Security or GitHub Advanced Security and dependency graph enabled.

The dependency review action scans your pull requests for dependency changes and raises an error if any new dependencies have known vulnerabilities. The action is supported by an API endpoint that compares the dependencies between two revisions and reports any differences.

For more information about the action and the API endpoint, see the [`dependency-review-action`](https://github.com/actions/dependency-review-action) documentation, and [AUTOTITLE](/rest/dependency-graph/dependency-review).

Users run the dependency review action using a GitHub Actions workflow. If you have not already set up runners for GitHub Actions, you must do this to enable users to run workflows. You can provision self-hosted runners at the repository, organization, or enterprise account level. For information, see [AUTOTITLE](/actions/concepts/runners/self-hosted-runners) and [AUTOTITLE](/actions/how-tos/manage-runners/self-hosted-runners/add-runners).
