---
title: Dependency graph
intro: You can use the dependency graph to identify all your project's dependencies. The dependency graph supports a range of popular package ecosystems.
product: "{% ifversion fpt or ghec %}\n\nNot enabled by default. The dependency graph is available for the following repository types:\n\n* Public repositories\n* Private repositories\n* Forks\n\n{% elsif ghes %}\n\nThe dependency graph is available for all repositories.\n\n{% endif %}"
redirect_from:
  - /github/visualizing-repository-data-with-graphs/about-the-dependency-graph
  - /code-security/supply-chain-security/about-the-dependency-graph
  - /code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph
  - /code-security/concepts/supply-chain-security/about-the-dependency-graph
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Dependency graph
contentType: concepts
category:
  - Secure your dependencies
---
<!--Marketing-LINK: From /features/security and /features/security/software-supply-chain pages "How GitHub's dependency graph is generated".-->

## About the dependency graph

The dependency graph is a summary of the manifest and lock files stored in a repository and any dependencies that are submitted for the repository using the dependency submission API. For each repository, it shows{% ifversion fpt or ghec %}:

* Dependencies, the ecosystems and packages it depends on
* Dependents, the repositories and packages that depend on it{% else %} dependencies, the ecosystems and packages it depends on.{% endif %}

For each dependency, you can see the version, {% ifversion fpt or ghec %}license information,{% endif %} the manifest file which included it, and whether it has known vulnerabilities. For package ecosystems supporting transitive dependencies, the relationship status will be displayed and you can click "(icon: kebab-horizontal)", then "Show paths", to see the transitive path which brought in the dependency.

You can also search for a specific dependency using the search bar. Dependencies are sorted automatically with vulnerable packages at the top.

{% ifversion ghes %}
GitHub does not retrieve license information for dependencies, and does not calculate information about dependents, the repositories and packages that depend on a repository.{% endif %}

For information on the supported ecosystems and manifest files, see [AUTOTITLE](/code-security/reference/supply-chain-security/dependency-graph-supported-package-ecosystems#supported-package-ecosystems).

When you create a pull request containing changes to dependencies that targets the default branch, GitHub uses the dependency graph to add dependency reviews to the pull request. These indicate whether the dependencies contain vulnerabilities and, if so, the version of the dependency in which the vulnerability was fixed. For more information, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependency-review).

## How the dependency graph is built

The dependency graph automatically parses dependencies by analyzing manifests and lock files in your repository. You can also submit data yourself. For more information, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependency-graph-data).

## Dependency graph availability

{% ifversion fpt or ghec %}
Repository administrators can enable or disable the dependency graph for repositories. For more information, see [AUTOTITLE](/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository).

Repository administrators can enable or disable the dependency graph for repositories. See [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/enable-dependency-graph).

{% endif %}

{% ifversion ghes %}
Enterprise owners can configure the dependency graph and Dependabot alerts for an enterprise. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/enable-dependency-graph) and [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-dependabot-for-your-enterprise).{% endif %}

{% ifversion ghes %}
For more information about configuration of the dependency graph, see [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/enable-dependency-graph).{% endif %}

{% ifversion fpt or ghec %}

## Dependents and "used by" data

For public repositories, the dependency graph lists dependents. These are other public repositories that depend on the repository or on packages that it publishes. This information is not reported for private repositories.

Some repositories have a "Used by" section in the sidebar of the **Code** tab. This section shows the number of public references to a package that were found, and displays the avatars of some of the owners of the dependent projects. Clicking any item in this section takes you to the **Dependents** tab of the dependency graph.

Your repository will have a "Used by" section if:
* The dependency graph is enabled for the repository.
* Your repository contains a package that is published on a supported package ecosystem. See [AUTOTITLE](/code-security/reference/supply-chain-security/dependency-graph-supported-package-ecosystems#supported-package-ecosystems).
* Within the ecosystem, your package has a link to a _public_ repository where the source is stored.
* More than 100 repositories depend on your package.

![Screenshot of the "Used by" section for a repository showing the summary of "13.4m" with details of 8 avatars and "+13,435,819."](/assets/images/help/repository/used-by-section.png)

The "Used by" section represents a single package from the repository. If you have admin permissions to a repository that contains multiple packages, you can choose which package the "Used by" section represents. See [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/change-used-by-data).

{% endif %}

## What you can do with the dependency graph

You can use the dependency graph to:

* Explore the repositories your code depends on{% ifversion fpt or ghec %}, and those that depend on it{% endif %}. For more information, see [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/explore-dependencies). {% ifversion fpt or ghec %}
* View a summary of the dependencies used in your organization's repositories in a single dashboard. For more information, see [AUTOTITLE](/organizations/collaborating-with-groups-in-organizations/viewing-insights-for-dependencies-in-your-organization#viewing-organization-dependency-insights).{% endif %}
* View and update vulnerable dependencies for your repository. For more information, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-alerts).
* See information about vulnerable dependencies in pull requests. For more information, see [AUTOTITLE](/pull-requests/how-tos/review-pull-requests/reviewing-dependency-changes-in-a-pull-request).
* Export a software bill of materials (SBOM) for audit or compliance purposes. This is a formal, machine-readable inventory of a project's dependencies. See [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/establish-provenance-and-integrity/export-dependencies-as-sbom).

## Further reading

* [Dependency graph](https://en.wikipedia.org/wiki/Dependency_graph) on Wikipedia
* [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/explore-dependencies)
* [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-dependabot-alerts/view-dependabot-alerts)
* [AUTOTITLE](/code-security/reference/supply-chain-security/troubleshoot-dependabot/vulnerability-detection)
