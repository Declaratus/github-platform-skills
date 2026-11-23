---
title: Configuring Dependabot on self-hosted runners
intro: You can configure self-hosted runners that Dependabot uses to access your private registries and internal network resources.
shortTitle: Configure on self-hosted runners
permissions: 'Organization owners and repository administrators'
versions:
  feature: dependabot-on-actions-self-hosted
redirect_from:
  - /code-security/dependabot/working-with-dependabot/managing-dependabot-on-self-hosted-runners
  - /code-security/dependabot/maintain-dependencies/managing-dependabot-on-self-hosted-runners
  - /code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/managing-dependabot-on-self-hosted-runners
contentType: how-tos
category:
  - Secure your dependencies
---

## Prerequisites

* Dependabot is installed and enabled.
* GitHub Actions is enabled and in use.

{% ifversion ghec %}
When you enforce a policy to only allow actions and reusable workflows from your enterprise, and you enable Dependabot on GitHub Actions, Dependabot will not run. To enable Dependabot to run with your enterprise actions and reusable workflows, you should choose either to allow actions created by GitHub, or allow specified actions and reusable workflows. For more information, see [AUTOTITLE](/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise#controlling-access-to-public-actions-and-reusable-workflows).
{% endif %}

## Adding self-hosted runners for Dependabot updates

1. Provision self-hosted runners, at the repository or organization level. For more information, see [AUTOTITLE](/actions/concepts/runners/self-hosted-runners) and [AUTOTITLE](/actions/how-tos/manage-runners/self-hosted-runners/add-runners).
1. Configure your environment and runners to meet the requirements for Dependabot. See [Requirements for using Dependabot with self-hosted runners](/code-security/reference/supply-chain-security/dependabot-on-actions#requirements-for-using-dependabot-with-self-hosted-runners).{% ifversion dependabot-repository-runner-settings %}
1. Assign the default `dependabot` label or a custom label to each runner you want Dependabot to use. See [AUTOTITLE](/actions/how-tos/manage-runners/self-hosted-runners/apply-labels).{% elsif dependabot-self-hosted-labels %}
1. If you are configuring self-hosted runners for your organization, you can create and assign a custom label for your runners. Otherwise, if you are configuring self-hosted runners for a standalone repository, you need to apply the `dependabot` label. See [AUTOTITLE](/actions/how-tos/manage-runners/self-hosted-runners/apply-labels).{% else %}
1. Assign a `dependabot` label to each runner you want Dependabot to use. For more information, see [AUTOTITLE](/actions/how-tos/manage-runners/self-hosted-runners/apply-labels#assigning-a-label-to-a-self-hosted-runner).{% endif %}
1. Optionally, enable workflows triggered by Dependabot to use more than read-only permissions and to have access to any secrets that are normally available. For more information, see [AUTOTITLE](/code-security/reference/supply-chain-security/troubleshoot-dependabot/dependabot-on-actions).

## Configuring self-hosted runners for Dependabot updates

{% ifversion dependabot-repository-runner-settings %}
> [!WARNING]
> Before selecting **Labeled runner**, make sure a runner has the label you plan to use. If you specify a runner group, make sure the group exists and the repository can access it. See [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-on-actions#how-runner-settings-interact).

Once you have configured self-hosted runners for Dependabot updates, you can select them at the organization or repository level.
{% else %}
> [!WARNING]
> Before enabling "Dependabot on self-hosted runners", ensure that your self-hosted runners or larger runners are configured with the runner label used by Dependabot (by default, `dependabot`). When this setting is enabled, Dependabot jobs will only run on runners with this label. If no runners with this label are available, jobs will remain queued indefinitely. See [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-on-actions#how-runner-settings-interact).

Once you have configured self-hosted runners for Dependabot updates, you can enable or disable Dependabot updates on self-hosted runners at the organization or repository level.
{% endif %}

> [!NOTE]
> Changing the runner setting does not trigger a new Dependabot run.

### For your private{% ifversion ghec %} or internal{% endif %} repository

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
{% ifversion dependabot-repository-runner-settings %}
1. Under "Dependency scanning", in the "Dependabot version updates" section, next to "Runner type", click (icon: pencil).
1. From the "Runner type" dropdown menu, select **Labeled runner**.
1. Optionally, enter a runner group name and a custom runner label. If you do not enter a label, Dependabot uses the `dependabot` label.
1. Click **Save runner selection**.
{% else %}
1. Under "Dependabot", to the right of "Dependabot on self-hosted runners", click **Enable** to enable the feature or **Disable** to disable it.
{% endif %}

    > [!NOTE] If you cannot change the runner setting, your organization may restrict actions and self-hosted runners for the repository. Contact your organization owner for more information.

### For your organization

You can enable Dependabot on self-hosted runners for all existing private{% ifversion ghec %} or internal{% endif %} repositories in an organization. Only repositories already configured to run Dependabot on GitHub Actions will be updated to run Dependabot on self-hosted runners the next time a Dependabot job is triggered.

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the "(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security** then **Global settings**.{% ifversion dependabot-self-hosted-labels %}
1. In the "Dependabot" section, next to "Runner type", click (icon: pencil).
1. Select the "Runner type" dropdown menu, then click **Labeled runner** and provide any additional information. If you applied a custom label to your self-hosted runners, type that label in the "Runner label" text box.
1. To enable the feature for all new repositories in the organization, click **Save runner selection**.{% else %}
1. Under "Dependabot", select "Dependabot on self-hosted runners" to enable the feature for all new repositories in the organization.{% endif %}
