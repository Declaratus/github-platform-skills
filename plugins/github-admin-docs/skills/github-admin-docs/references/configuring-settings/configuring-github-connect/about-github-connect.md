---
title: About GitHub Connect
intro: 'GitHub Connect enhances GitHub Enterprise Server by giving you access to data and workflows from GitHub Enterprise Cloud.'
versions:
  ghes: '*'
redirect_from:
  - /admin/configuration/configuring-github-connect/about-github-connect
contentType: concepts
category:
  - Install and configure your instance
---

GitHub Connect allows {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to connect to your enterprise on GitHub Enterprise Cloud in limited ways.

After you enable GitHub Connect, you can choose which features to enable. For example, you can:

* Automatically sync license usage between environments
* Unify search results and user contribution data
* Enable features that rely on GitHub.com, such as Dependabot alerts for security vulnerabilities that are tracked in the GitHub Advisory Database

## About the connection

To enable GitHub Connect, you configure a connection between {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} and an enterprise account on **GitHub.com** or **GHE.com**. The connection uses HTTPS over ports 443 or 80 and is secured by TLS.

* GitHub Connect does not open {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to the public internet.
* None of your enterprise's private data is exposed to GitHub Enterprise Cloud users.
* GitHub Connect transmits only the limited data needed for the features you enable. Unless you enable license sync, no personal data is transmitted. For more information, see [Data transmission](#data-transmission).
* Enabling GitHub Connect will not allow GitHub Enterprise Cloud users to make changes to GitHub Enterprise Server.

## GitHub Connect features

After you configure the connection between {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} and GitHub Enterprise Cloud, you can enable individual features of GitHub Connect.

If you're connecting to an enterprise on **GHE.com**:

* Server Statistics is not available.
* Automatic user license sync requires GitHub Enterprise Server version 3.15 or later.
* Actions from GitHub.com require GitHub Enterprise Server version 3.20.6 or later, or any feature release from 3.21.0.

| Feature | Description | More information |
| ----------- | ----------- | ----------- |
| Automatic user license sync | Manage license usage across your GitHub Enterprise deployments by automatically syncing user licenses from {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to GitHub Enterprise Cloud. | [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-automatic-user-license-sync-for-your-enterprise) |
| Dependabot | Allow users to find and fix vulnerabilities in code dependencies. | [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-dependabot-for-your-enterprise) |
| GitHub.com actions | Allow users to use actions from GitHub.com in public workflow files. | [AUTOTITLE](/admin/managing-github-actions-for-your-enterprise/managing-access-to-actions-from-githubcom/enabling-automatic-access-to-githubcom-actions-using-github-connect) |
| Server Statistics | Analyze your own aggregate data from GitHub Enterprise Server, and help us improve GitHub products. | [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-server-statistics-for-your-enterprise) |
| Unified search | Allow users to include repositories on GitHub Enterprise Cloud in their search results when searching from {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. | [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-unified-search-for-your-enterprise) |
| Unified contributions | Allow users to include anonymized contribution counts for their work on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} in their contribution graphs on GitHub Enterprise Cloud. | [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-unified-contributions-for-your-enterprise) |

## Data transmission

When GitHub Connect is enabled, a record on GitHub Enterprise Cloud stores information about the connection. If you enable individual features of GitHub Connect, additional data is transmitted.

> [!NOTE]
> No repositories, issues, or pull requests are ever transmitted from GitHub Enterprise Server to GitHub Enterprise Cloud by GitHub Connect.

### Data transmitted when GitHub Connect is enabled

When you enable GitHub Connect or specific GitHub Connect features, a record on GitHub Enterprise Cloud stores the following information about the connection.
* The public key portion of your GitHub Enterprise Server license
* A hash of your GitHub Enterprise Server license
* The customer name on your GitHub Enterprise Server license
* The version of your GitHub Enterprise Server instance
* The hostname of {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}
* The enterprise account on GitHub Enterprise Cloud that's connected to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}
* The authentication token that's used by {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to make requests to GitHub Enterprise Cloud
* If Transport Layer Security (TLS) is enabled and configured on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}
* The GitHub Connect features that are enabled on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, and the date and time of enablement
* The dormancy threshold for your enterprise
* The number of dormant users for your enterprise
* A count of {% ifversion enterprise-licensing-language %}consumed licenses{% else %}license-consuming seats{% endif %}, which does not include suspended users

GitHub Connect syncs the above connection data between {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} and GitHub Enterprise Cloud weekly, starting from the day and approximate time that GitHub Connect was enabled.

### Data transmitted by individual features of GitHub Connect

Additional data is transmitted if you enable individual features of GitHub Connect.

| Feature | Data | Which way does the data flow? | Where is the data used? |
| ------- | ---- | --------- | ------ |
| Automatic user license sync | Each GitHub Enterprise Server user's user ID and email addresses{% ifversion ghas-in-license-sync %}, and whether the user consumes a license for GitHub Advanced Security, GitHub Code Security, or GitHub Secret Protection.{% endif %} | From GitHub Enterprise Server to GitHub Enterprise Cloud | GitHub Enterprise Cloud |
| Dependabot alerts | Vulnerability alerts | From GitHub.com to GitHub Enterprise Server | GitHub Enterprise Server |
| Dependabot updates | Dependencies and the metadata for each dependency's repository<br><br>If a dependency is stored in a private repository on GitHub.com, data will only be transmitted if Dependabot is configured and authorized to access that repository. | From GitHub.com to GitHub Enterprise Server | GitHub Enterprise Server |
| GitHub.com actions | Name of action, action (YAML file from GitHub Marketplace) | From GitHub.com to GitHub Enterprise Server<br><br>From GitHub Enterprise Server to GitHub.com | GitHub Enterprise Server |
| Server Statistics | Aggregate metrics about your usage of GitHub Enterprise Server. For the complete list of metrics, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/analyzing-how-your-team-works-with-server-statistics/about-server-statistics#server-statistics-data-collected). | From GitHub Enterprise Server to GitHub Enterprise Cloud | GitHub Enterprise Cloud |
| Unified search | Search terms, search results | From GitHub Enterprise Cloud to GitHub Enterprise Server<br><br>From GitHub Enterprise Server to GitHub Enterprise Cloud | GitHub Enterprise Server |
| Unified contributions | Contribution counts | From GitHub Enterprise Server to GitHub Enterprise Cloud | GitHub Enterprise Cloud |

## Enabling GitHub Connect

To enable GitHub Connect, see the article for your GitHub Enterprise Cloud environment.

* [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-github-connect-for-githubcom)
* [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-github-connect-for-ghecom)
