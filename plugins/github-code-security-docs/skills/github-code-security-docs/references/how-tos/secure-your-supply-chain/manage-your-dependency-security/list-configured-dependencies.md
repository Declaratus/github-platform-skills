---
title: Listing dependencies configured for version updates
intro: You can view the dependencies that Dependabot monitors for updates.
permissions: 'Users with **write** access'
redirect_from:
  - /github/administering-a-repository/listing-dependencies-configured-for-version-updates
  - /code-security/supply-chain-security/listing-dependencies-configured-for-version-updates
  - /code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/listing-dependencies-configured-for-version-updates
  - /code-security/dependabot/dependabot-version-updates/listing-dependencies-configured-for-version-updates
  - /code-security/dependabot/troubleshooting-dependabot/listing-dependencies-configured-for-version-updates
  - /code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/listing-dependencies-configured-for-version-updates
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
shortTitle: List configured dependencies
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

## Viewing dependencies monitored by Dependabot

After you've enabled version updates, you can confirm that your configuration is correct using the **Dependabot** tab in the dependency graph for the repository. For more information, see [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-version-updates).

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: graph) Insights**.

   ![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled with a graph icon and "Insights," is outlined in orange.](/assets/images/help/repository/repo-nav-insights-tab.png)
1. In the left sidebar, click **Dependency graph**.
![Screenshot of the "Dependency graph" tab. The tab is highlighted with an orange outline.](/assets/images/help/graphs/graphs-sidebar-dependency-graph.png)
1. Under "Dependency graph", click **Dependabot**.
1. Optionally, to view the files monitored for a package manager, to the right of the package manager, click (icon: kebab-horizontal).

   ![Screenshot of the Dependabot tab under "Insights". A dropdown menu, labeled with a kebab icon, is highlighted with an orange outline.](/assets/images/help/dependabot/monitored-dependency-files.png)

If any dependencies are missing, check the log files for errors. If any package managers are missing, review the configuration file.

For information about Dependabot job logs, see [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/view-dependabot-logs).
