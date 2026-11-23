---
title: Enabling the dependency graph
intro: You can allow users to identify their projects' dependencies by enabling the dependency graph.
permissions: "{% ifversion fpt or ghec %}\n\nRepository owners, organization owners, security managers, and users with the **admin** role\n\n{% elsif ghes %}\n\nEnterprise owners\n\n{% endif %}"
redirect_from:
  - /code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph#enabling-the-dependency-graph
  - /code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-graph
  - /code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configuring-the-dependency-graph
  - /code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/enabling-the-dependency-graph
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Enable dependency graph
contentType: how-tos
category:
  - Secure your dependencies
---

The dependency graph is a summary of the manifest and lock files stored in a repository and any dependencies that are submitted for the repository using the dependency submission API. For more information, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependency-graph).

When the dependency graph is first enabled, any manifest and lock files for supported ecosystems are parsed immediately. The graph is usually populated within minutes but this may take longer for repositories with many dependencies. Once enabled, the graph is automatically updated with every push to the repository{% ifversion fpt or ghec %} and every push to other repositories in the graph{% endif %}.

{% ifversion ghes %}

## Enabling the dependency graph for a GitHub Enterprise Server instance

If the dependency graph is not available on your GitHub Enterprise Server instance, ask an enterprise owner to enable it. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/enable-dependency-graph).

{% else %}

## Enabling the dependency graph for a repository

Enabling the dependency graph gives GitHub read-only access to the dependency manifest and lock files for a repository.

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. Read the message about granting GitHub read-only access to the repository data to enable the dependency graph, then next to "Dependency Graph", click **Enable**.

   You can disable the dependency graph at any time by clicking **Disable** next to "Dependency Graph" on the settings page for "Advanced Security".

## Enabling the dependency graph for multiple repositories

You can enable or disable the dependency graph for all repositories owned by your user account, regardless of their visibility. See [AUTOTITLE](/account-and-profile/how-tos/account-settings/managing-security-and-analysis-features).

You can also enable the dependency graph for multiple repositories in an organization at the same time. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security).

{% endif %}

## Next steps

You can use the dependency submission API to submit dependencies from the package manager or ecosystem of your choice, even if the ecosystem is not supported by dependency graph for manifest or lock file analysis.
Dependencies submitted to a project using the dependency submission API will show which detector was used for their submission and when they were submitted. For more information on the dependency submission API, see [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/use-dependency-submission-api).

For more information on viewing the dependency graph, see [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/explore-dependencies).

## Further reading

{%- ifversion maven-transitive-dependencies %}
* [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/submit-dependencies-automatically){%- endif %}
{%- ifversion fpt or ghec %}
* [AUTOTITLE](/organizations/collaborating-with-groups-in-organizations/viewing-insights-for-dependencies-in-your-organization){%- endif %}
* [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-dependabot-alerts/view-dependabot-alerts)
* [AUTOTITLE](/code-security/reference/supply-chain-security/troubleshoot-dependabot/vulnerability-detection)
