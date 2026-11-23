---
title: Managing pull requests for dependency updates
intro: You manage pull requests raised by Dependabot in much the same way as other pull requests, but there are some extra options.
permissions: 'Users with **write** access'
redirect_from:
  - /github/administering-a-repository/managing-pull-requests-for-dependency-updates
  - /code-security/supply-chain-security/managing-pull-requests-for-dependency-updates
  - /code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/managing-pull-requests-for-dependency-updates
  - /code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates
  - /code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/managing-pull-requests-for-dependency-updates
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
shortTitle: Manage Dependabot PRs
contentType: how-tos
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

## Viewing Dependabot pull requests

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: git-pull-request) Pull requests**.
1. Any pull requests for security or version updates are easy to identify.
    * The author is {% ifversion fpt or ghec %}[dependabot](https://github.com/dependabot){% else %}dependabot{% endif %}, the bot account used by Dependabot.
    * By default, they have the `dependencies` label.

## Changing the rebase strategy for Dependabot pull requests

By default, Dependabot automatically rebases pull requests to resolve any conflicts. If a pull request has not been merged for 30 days, Dependabot will stop rebasing the pull request. You can still manually rebase and merge the pull request. If you'd prefer to handle merge conflicts manually, you can disable this using the `rebase-strategy` option. For details, see [AUTOTITLE](/code-security/reference/supply-chain-security/dependabot-options-reference#rebase-strategy--).

## Allowing Dependabot to rebase and force push over extra commits

By default, Dependabot will stop rebasing a pull request once extra commits have been pushed to it. To allow Dependabot to force push over commits added to its branches, include any of the following strings: `[dependabot skip]` , `[skip dependabot]`, `[dependabot-skip]`, or `[skip-dependabot]`, in either lower or uppercase, to the commit message.

## Managing Dependabot pull requests with comment commands

You can use comment commands on Dependabot pull requests to manage and customize your dependency updates. For details, see [AUTOTITLE](/code-security/reference/supply-chain-security/dependabot-pull-request-comment-commands).

Dependabot will react with a "thumbs up" emoji to acknowledge the command, and may respond with a comment on the pull request. While Dependabot usually responds quickly, some commands may take several minutes to complete if Dependabot is busy processing other updates or commands.

If you run any of the commands for ignoring dependencies or versions, Dependabot stores the preferences for the repository centrally. While this is a quick solution, for repositories with more than one contributor it is better to explicitly define the dependencies and versions to ignore in the configuration file. This makes it easy for all contributors to see why a particular dependency isn't being updated automatically.

For more information, see [AUTOTITLE](/code-security/reference/supply-chain-security/dependabot-options-reference#ignore--).
