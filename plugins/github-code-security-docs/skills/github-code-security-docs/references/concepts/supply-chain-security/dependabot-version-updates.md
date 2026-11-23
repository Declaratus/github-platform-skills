---
title: Dependabot version updates
intro: You can use Dependabot to keep the packages you use updated to the latest versions.
product: "Dependabot version updates is available for the following repositories:\n\n{% ifversion fpt or ghec %}\n\n* All repositories on GitHub\n\n{% else %}\n\n* All repositories on GitHub Enterprise Server\n\n{% endif %}"
redirect_from:
  - /github/administering-a-repository/about-dependabot
  - /github/administering-a-repository/about-github-dependabot
  - /github/administering-a-repository/about-github-dependabot-version-updates
  - /github/administering-a-repository/about-dependabot-version-updates
  - /code-security/supply-chain-security/about-dependabot-version-updates
  - /code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/upgrading-from-dependabotcom-to-github-native-dependabot
  - /code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates
  - /code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates
  - /code-security/dependabot/dependabot-version-updates
  - /code-security/supply-chain-security/keeping-your-dependencies-updated-automatically
  - /administering-a-repository/keeping-your-dependencies-updated-automatically
  - /code-security/concepts/supply-chain-security/about-dependabot-version-updates
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
shortTitle: Dependabot version updates
contentType: concepts
category:
  - Secure your dependencies
---

{% ifversion ghes %}

> [!NOTE]
> Your site administrator must set up Dependabot updates for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} before you can use this feature. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-dependabot-for-your-enterprise).{% ifversion security-feature-enablement-policies-dependabot %}
>
> You may not be able to enable or disable Dependabot updates if an enterprise owner has set a policy at the enterprise level. For more information, see [AUTOTITLE](/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise).
{% endif %}

{% endif %}

## About Dependabot version updates

Dependabot takes the effort out of maintaining your dependencies. You can use it to ensure that your repository automatically keeps up with the latest releases of the packages and applications it depends on.

When Dependabot raises pull requests, these pull requests could be for _security_ or _version_ updates:

* _Dependabot security updates_ are automated pull requests that help you update dependencies with known vulnerabilities.
* _Dependabot version updates_ are automated pull requests that keep your dependencies updated, even when they don’t have any vulnerabilities. To check the status of version updates, navigate to the **Insights** tab of your repository, then select **Dependency Graph**, and Dependabot.

You enable Dependabot version updates by checking a `dependabot.yml` configuration file into your repository.

{% ifversion fpt %}
Dependabot and all related features are covered by [GitHub's Terms of Service](/free-pro-team@latest/site-policy/github-terms/github-terms-of-service).
{% elsif ghec %}
Dependabot and all related features are covered by your license agreement. For more information, see [GitHub Enterprise Customer Terms](https://github.com/customer-terms).
{% endif %}

## Updates for packages

The `dependabot.yml` configuration file specifies the location of the manifest, or of other package definition files, stored in your repository. Dependabot uses this information to check for outdated packages and applications. Dependabot determines if there is a new version of a dependency by looking at the semantic versioning ([semver](https://semver.org/)) of the dependency to decide whether it should update to that version. For information on the supported repositories and ecosystems, see [AUTOTITLE](/code-security/reference/supply-chain-security/supported-ecosystems-and-repositories).

The `dependabot.yml` file can also be configured to tell Dependabot how to maintain your dependencies. For more information, see [AUTOTITLE](/code-security/concepts/supply-chain-security/about-the-dependabot-yml-file).

For certain package managers, Dependabot version updates also supports vendoring. Vendored (or cached) dependencies are dependencies that are checked in to a specific directory in a repository rather than referenced in a manifest. Vendored dependencies are available at build time even if package servers are unavailable. Dependabot version updates can be configured to check vendored dependencies for new versions and update them if necessary.

When Dependabot identifies an outdated dependency, it raises a pull request to update the manifest to the latest version of the dependency. For vendored dependencies, Dependabot raises a pull request to replace the outdated dependency with the new version directly. You check that your tests pass, review the changelog and release notes included in the pull request summary, and then merge it. For more information, see [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-version-updates).

{% ifversion dependabot-cooldown-default-days %}

By default, Dependabot applies a cooldown period of 3 days to version updates, so a new version is not considered for a version update until 3 days after its release. **This default cooldown does not apply to security updates.** This gives new releases time to stabilize before you receive a pull request. You can customize the cooldown periods, and the dependencies they apply to, with the `cooldown` option. For more information, see [AUTOTITLE](/code-security/reference/supply-chain-security/dependabot-options-reference#cooldown-).

{% endif %}

If you enable _security updates_, Dependabot also raises pull requests to update vulnerable dependencies. For more information, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-security-updates).

## Updates for actions

Actions are often updated with bug fixes and new features to make automated processes more reliable, faster, and safer. When you enable Dependabot version updates for GitHub Actions, Dependabot will help ensure that references to actions in a repository's _workflow.yml_ file and reusable workflows used inside workflows are kept up to date.

For each action in the file, Dependabot checks the action's reference (typically a version number or commit identifier associated with the action) against the latest version. If a more recent version of the action is available, Dependabot will send you a pull request that updates the reference in the workflow file to the latest version.

Dependabot also checks workflow files for uses of reusable workflows, and updates the Git reference for these called reusable workflows.

{% ifversion actions-workflow-lockfiles %}

If a workflow has been onboarded to a workflow dependency lockfile, Dependabot also regenerates the matching lockfile entry in the same pull request, so the pinned commit in the lockfile always matches the updated reference in the workflow file. This needs no additional configuration. For more information, see [AUTOTITLE](/actions/how-tos/secure-your-work/lock-workflow-dependencies).

{% endif %}

To enable this feature, see [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/auto-update-actions).

## About automatic deactivation of Dependabot updates

When maintainers of a repository stop interacting with Dependabot pull requests, Dependabot temporarily pauses its updates and lets you know, see [AUTOTITLE](/code-security/reference/supply-chain-security/troubleshoot-dependabot/dependabot-updates-stopped).

## About notifications for Dependabot version updates

You can filter your notifications on GitHub to show notifications for pull requests created by Dependabot. For more information, see [AUTOTITLE](/subscriptions-and-notifications/how-tos/viewing-and-triaging-notifications/managing-notifications-from-your-inbox).
