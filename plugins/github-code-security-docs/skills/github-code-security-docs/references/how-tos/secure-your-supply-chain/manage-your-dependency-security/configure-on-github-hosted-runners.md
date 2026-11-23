---
title: Configuring Dependabot on GitHub-hosted runners
intro: Enable Dependabot on GitHub-hosted runners to more easily identify Dependabot job errors and manually detect and troubleshoot failed runs.
shortTitle: Configure on GitHub-hosted runners
permissions: 'Organization owners and repository administrators'
versions:
  feature: dependabot-on-actions-opt-in
contentType: how-tos
category:
  - Secure your dependencies
---

## Enabling or disabling Dependabot on standard GitHub-hosted runners

You can configure Dependabot on standard GitHub-hosted runners:
* [For your repository](#for-your-repository)
* [For your organization](#for-your-organization)

If you restrict access to your organization's or repository's private resources, you may need to update your list of allowed IP addresses prior to enabling Dependabot on GitHub Actions runners. You can update your IP allow list to use the GitHub-hosted runners IP addresses (instead of the Dependabot IP addresses), sourced from the [meta](/rest/meta) REST API endpoint.

> [!WARNING] You should not rely on the GitHub Actions IP addresses for authentication to private registries. These GitHub Actions addresses are not only used by GitHub, and should not be trusted for authentication. Instead, use a self-hosted runner to ensure greater control over your network access. For more information, see [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/configure-on-self-hosted-runners).

### For your repository

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
{% ifversion dependabot-repository-runner-settings %}
1. Under "Dependency scanning", in the "Dependabot version updates" section, next to "Runner type", click (icon: pencil).
1. From the "Runner type" dropdown menu, select **Standard GitHub runner**.
1. Click **Save runner selection**.
{% else %}
1. Under "Dependabot", to the right of "Dependabot on Actions runners", click **Enable** to enable the feature or **Disable** to disable it.
{% endif %}

    > [!NOTE]
    > Dependabot on GitHub Actions relies on the `ubuntu-latest` label to select the appropriate runner. To ensure Dependabot runs on GitHub-hosted runners, you should not use the label `ubuntu-latest` for self-hosted runners.

### For your organization

Only repositories meeting the following criteria will be updated to run Dependabot on GitHub Actions the next time a Dependabot job is triggered.

  * Dependabot is enabled in the repository.
  * GitHub Actions is enabled in the repository.

If a repository in your organization has Dependabot enabled but GitHub Actions disabled, Dependabot will not run on GitHub Actions, but will continue to run using the built-in Dependabot application.

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the "(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security** then **Global settings**.{% ifversion dependabot-self-hosted-labels %}
1. In the "Dependabot" section, next to "Runner type", confirm that you have selected "Standard GitHub runner". If not, click (icon: pencil) and update your configuration.{% else %}
1. Under "Dependabot", select "Dependabot on Actions runners" to enable the feature or deselect to disable it.{% endif %}

    > [!NOTE]
    > Dependabot on GitHub Actions relies on the `ubuntu-latest` label to select the appropriate runner. To ensure Dependabot runs on GitHub-hosted runners, you should not use the label `ubuntu-latest` for self-hosted runners.

## Enabling or disabling Dependabot on larger runners

If you run into Dependabot timeouts and out-of-memory errors, you may want to use larger runners, as you can configure these runners to have more resources. You can only enable larger runners for Dependabot **for an organization**.

Using larger runners can help update jobs finish within the 55-minute time limit, but does not increase the limit.

1. Add a larger runner to your organization and ensure the name specified is `dependabot`. For more information, see [AUTOTITLE](/actions/how-tos/manage-runners/larger-runners/manage-larger-runners#adding-a-larger-runner-to-an-organization).
1. Opt in the organization to self-hosted runners. For more information, see [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/configure-on-self-hosted-runners#for-your-organization). This step is required, as it ensures that future Dependabot jobs will run on the larger GitHub-hosted runner that has the `dependabot` name.

    > [!NOTE]
    > Dependabot on GitHub Actions relies on the `ubuntu-latest` label to select the appropriate runner. To ensure Dependabot runs on GitHub-hosted runners, you should not use the label `ubuntu-latest` for self-hosted runners.
