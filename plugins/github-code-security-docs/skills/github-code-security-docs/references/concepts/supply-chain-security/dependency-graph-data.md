---
title: How the dependency graph recognizes dependencies
intro: 'The dependency graph automatically analyzes manifest files. You can submit data for dependencies that cannot be detected automatically.'
product: "{% ifversion fpt or ghec %}\n\nNot enabled by default. The dependency graph is available for the following repository types:\n\n* Public repositories\n* Private repositories\n* Forks\n\n{% elsif ghes %}\n\nThe dependency graph is available for all repositories.\n\n{% endif %}"
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Dependency graph data
contentType: concepts
category:
  - Secure your dependencies
---

The dependency graph can identify your project's dependencies using the following methods.

| Method | How it works |
| ------ | ------------ |
| **Static analysis** | Parses manifest and lock files in your repository |
| {% ifversion fpt or ghec %} |
| **Dependabot graph jobs** | Uses a Dependabot GitHub Actions workflow to generate dependency snapshots |
| {% endif %} |
| {% ifversion maven-transitive-dependencies %} |
| **Automatic submission** | Runs a built-in GitHub Actions workflow to resolve build-time dependencies |
| {% endif %}
| **Dependency submission API** | Accepts dependency data you submit programmatically |

Once dependencies are in the graph, you can receive Dependabot alerts and Dependabot security updates for any known vulnerabilities.

## Static analysis

When you enable the dependency graph, GitHub scans your repository for supported manifest files and parses each package's name and version. The graph updates when you change a supported manifest or lock file on your default branch{% ifversion fpt or ghec %}, or when a dependency changes in its own repository{% endif %}.

Static analysis can identify:

* **Direct dependencies** explicitly defined in a manifest or lock file
* **Indirect dependencies**—dependencies of these direct dependencies, also called "transitive dependencies"—but only if they are defined in a manifest or lock file, not if they are resolved at build time

For the most reliable graph, you should use lock files (or their equivalent), because they define exactly which versions of the direct and indirect dependencies you currently use. Lock files also ensure that all contributors to the repository are using the same versions, which will make it easier for you to test and debug code.{% ifversion fpt or ghec %} In addition, indirect dependencies inferred from manifest files (rather than lock files) are excluded from vulnerability checks.{% endif %}

{% ifversion maven-transitive-dependencies %}

## Automatic dependency submission

Some ecosystems resolve indirect dependencies at build time, so static analysis can't see the full dependency tree. When you enable automatic dependency submission for a repository, GitHub automatically identifies the transitive dependencies in the repository for supported ecosystems. See [AUTOTITLE](/code-security/reference/supply-chain-security/dependency-graph-supported-package-ecosystems).

In the background, automatic dependency submission runs a GitHub Actions workflow that generates the complete tree and uploads it using the dependency submission API.{% ifversion fpt or ghec %} Automatic dependency submission runs on GitHub-hosted runners by default and counts toward your GitHub Actions minutes. Optionally, you can choose to run it on self-hosted runners or larger runners.{% endif %}

To enable automatic dependency submission, see [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/submit-dependencies-automatically).

{% endif %}

{% ifversion fpt or ghec %}

## Dependabot graph jobs

Dependabot graph jobs use a special type of Dependabot job to build a dependency snapshot and upload it to the dependency submission API. Dependabot graph jobs are currently supported for **Go** and **Python** dependencies.

For supported ecosystems, Dependabot graph jobs provide:

* Full transitive dependency coverage, which means Dependabot can alert you to vulnerabilities in indirect dependencies that static analysis may miss.
* Private registry access through Dependabot secrets configured at the organization or repository level. For more information, see [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/configure-access-to-private-registries).
* Private packages that are not accessible through configured Dependabot secrets are gracefully omitted from the dependency graph without causing a failure.

This approach is similar to automatic dependency submission, but does not incur charges for GitHub Actions minutes. It can also access organization-wide configurations for private registries you've set up for Dependabot.

> [!NOTE] Dependabot graph jobs take precedence over automatic dependency submission. For example, if your Python repository previously used automatic dependency submission, those jobs will no longer run once Dependabot graph jobs are active. The only requirement is that the dependency graph is enabled for your repository.

{% endif %}

## The dependency submission API

You can call the dependency submission API in your own script or workflow. This is useful if:

* You need to submit transitive dependencies that cannot be detected from lock files.
* You need to create custom logic or are using an external CI/CD system.

Dependencies are submitted to the dependency submission API in the form of a snapshot. This is a list of dependencies associated with a commit SHA and other metadata, reflecting the current state of your repository.

If you are calling the API in a GitHub Actions workflow, you can use a pre-made action for your ecosystem that automatically gathers the dependencies and submits them to the API. Otherwise, you can write your own action or call the API from an external system.

Submitted dependencies {% ifversion fpt or ghec %}will be shown in dependency review, but {% endif %}are _not_ available in your organization's dependency insights.

{% ifversion ghes %}
{% else %}
> [!NOTE]
> The dependency review API and the dependency submission API work together. This means that the dependency review API will include dependencies submitted via the dependency submission API.
{% endif %}

For more information, see [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/use-dependency-submission-api).

## Prioritization

A repository can use multiple methods for dependency submission, which can cause the same package manifest to be scanned multiple times, potentially with different outputs from each scan. Dependency graph uses deduplication logic to parse the outputs, prioritizing the most accurate information for each manifest file.

Dependency graph displays only one instance of each manifest file using the following precedence rules.

1. **User submissions** take the highest priority, because they are usually created during artifact builds they have the most complete information.
   * If there are multiple manual snapshots from different detectors, they are sorted alphabetically by correlator and the first one used.
   * If there are two correlators with the same detector, the resolved dependencies are merged. For more information about correlators and detectors, see [AUTOTITLE](/rest/dependency-graph/dependency-submission).{% ifversion fpt or ghec %}
1. **Dependabot graph jobs** have the second-highest priority. For ecosystems where Dependabot graph jobs are available (currently Go and Python), they take precedence over automatic dependency submission.{% endif %}
1. **Automatic submissions** have the next priority since they are also created during artifact builds, but are not submitted by users.
1. **Static analysis results** are used when no other data is available.
