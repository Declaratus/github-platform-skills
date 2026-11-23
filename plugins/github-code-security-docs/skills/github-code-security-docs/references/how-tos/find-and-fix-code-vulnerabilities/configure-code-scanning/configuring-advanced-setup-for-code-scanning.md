---
title: Configuring advanced setup for code scanning
shortTitle: Configure advanced setup
intro: You can configure advanced setup for a repository to find security vulnerabilities in your code using a highly customizable code scanning configuration.
permissions: 'Repository owners, organization owners, security managers, and users with the **admin** role'
product: "Code scanning is available for the following repository types:\n\n* Public repositories on GitHub.com\n* Organization-owned repositories on GitHub Team, GitHub Enterprise Cloud, or GitHub Enterprise Server, with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled."
redirect_from:
  - /code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/configuring-advanced-setup-for-code-scanning
  - /code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/configuring-advanced-setup-for-code-scanning
  - /code-security/code-scanning/creating-an-advanced-setup-for-code-scanning
  - /code-security/how-tos/scan-code-for-vulnerabilities/configure-code-scanning/configuring-advanced-setup-for-code-scanning
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
allowTitleToDifferFromFilename: true
contentType: how-tos
category:
  - Find and fix code vulnerabilities
---

{% ifversion ghes %}

> [!NOTE]
> Your site administrator must enable code scanning before you can use this feature. If you want to use GitHub Actions to scan your code, the site administrator must also enable GitHub Actions and set up the infrastructure required. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance).

{% endif %}

{% ifversion ghes %}

> [!NOTE]
> This article describes the features available with the version of the CodeQL action and associated CodeQL CLI bundle included in the initial release of this version of GitHub Enterprise Server. If your enterprise uses a more recent version of the CodeQL action, see the [GitHub Enterprise Cloud version](/enterprise-cloud@latest/{{ currentArticle }}) of this article for information on the latest features.
For information on using the latest version, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access).

{% endif %}

If you do not need a highly customizable code scanning configuration, consider using default setup for code scanning. For more information, see [AUTOTITLE](/code-security/concepts/code-scanning/setup-types).

## Prerequisites

Your repository is eligible for advanced setup if it meets these requirements.
* It uses CodeQL-supported languages or you plan to generate code scanning results with a third-party tool.
* GitHub Actions is enabled.{% ifversion fpt or ghec %}
* It is publicly visible, or GitHub Code Security is enabled.{%- elsif ghes %}
* GitHub Code Security is enabled.{% endif %}

{% ifversion ghes %}
If the server on which you are running GitHub Enterprise Server is not connected to the internet, your site administrator can enable CodeQL code scanning by making the CodeQL analysis bundle available on the server. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access).
{% endif %}

## Configuring advanced setup for code scanning with CodeQL

You can customize your CodeQL analysis by creating and editing a workflow file. Selecting advanced setup generates a basic workflow file for you to customize using standard workflow syntax and specifying options for the CodeQL action. See [AUTOTITLE](/actions/concepts/workflows-and-actions/workflows) and [AUTOTITLE](/code-security/reference/code-scanning/workflow-configuration-options).

{% ifversion fpt or ghec %}Using actions to run code scanning will use minutes. For more information, see [AUTOTITLE](/billing/concepts/product-billing/github-actions).{% endif %}

{% ifversion fpt %}

  > [!NOTE]
  > You can configure code scanning for any public repository where you have write access.

{% endif %}

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. In the "CodeQL analysis" row, select **Set up** (icon: triangle-down), then click **Advanced**.

   > [!NOTE]
   > If you are switching from default setup to advanced setup, in the "CodeQL analysis" row, select (icon: kebab-horizontal), then click **(icon: workflow) Switch to advanced**. In the pop-up window that appears, click **Disable CodeQL**.

1. To customize how code scanning scans your code, edit the workflow.

   Generally, you can commit the CodeQL analysis workflow without making any changes to it. However, many of the third-party workflows require additional configuration, so read the comments in the workflow before committing.

   For more information, see [AUTOTITLE](/code-security/reference/code-scanning/workflow-configuration-options) and [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/manage-your-configuration/codeql-for-compiled-languages).

1. Click **Commit changes...** to display the commit changes form.

   ![Screenshot of the form to create a new file. To the right of the file name, a green button, labeled "Commit changes...", is outlined in dark orange.](/assets/images/help/repository/start-commit-commit-new-file.png)
1. In the commit message field, type a commit message.
1. Choose whether you'd like to commit directly to the default branch, or create a new branch and start a pull request.
1. Click **Commit new file** to commit the workflow file to the default branch or click **Propose new file** to commit the file to a new branch.
1. If you created a new branch, click **Create pull request** and open a pull request to merge your change into the default branch.

In the suggested CodeQL analysis workflow, code scanning is configured to analyze your code each time you either push a change to the default branch or any protected branches, or raise a pull request against the default branch. As a result, code scanning will now commence.

The `on:pull_request` and `on:push` triggers for code scanning are each useful for different purposes. See [AUTOTITLE](/code-security/reference/code-scanning/workflow-configuration-options#scan-frequency) and [AUTOTITLE](/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow).

For information on bulk enablement, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/configure-specific-tools/configuring-advanced-setup-for-code-scanning-with-codeql-at-scale).

{% ifversion fpt or ghec %}

### Keeping the CodeQL action up to date

We recommend referencing the CodeQL action using a major version tag (for example, `v4`) in your workflow file. This ensures your workflow automatically picks up the latest release within that major version, including bug fixes, new features, and updated CodeQL CLI versions.

Some CodeQL action features are enabled by server-side flags that may be removed over time, which can cause old versions to lose functionality. If you pin to a specific commit SHA or patch version tag, keep it updated, for example with Dependabot. See [AUTOTITLE](/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/auto-update-actions).

## Configuring code scanning using third-party actions

GitHub includes workflow templates for third-party actions, as well as the CodeQL action. Using a workflow template is much easier than writing a workflow unaided.

{% ifversion fpt or ghec %}Using actions to run code scanning will use minutes. For more information, see [AUTOTITLE](/billing/concepts/product-billing/github-actions).{% endif %}

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: play) Actions**.

   ![Screenshot of the tabs for the "github/docs" repository. The "Actions" tab is highlighted with an orange outline.](/assets/images/help/repository/actions-tab-global-nav-update.png)
1. If the repository has already at least one workflow configured and running, click **New workflow** to display workflow templates. If there are currently no workflows configured for the repository, go to the next step.

   ![Screenshot of the Actions tab for a repository. The "New workflow" button is outlined in dark orange.](/assets/images/help/security/actions-new-workflow-button.png)

1. In the "Choose a workflow" or "Get started with GitHub Actions" view, scroll down to the "Security" category and click **Configure** under the workflow you want to configure. You may need to click **View all** to find the security workflow you want to configure.

   ![Screenshot of the Security category of workflow templates. The Configure button and "View all" link are highlighted with an orange outline.](/assets/images/help/security/actions-workflows-security-section.png)

1. Follow any instructions in the workflow to customize it to your needs. For more general assistance about workflows, click **Documentation** on the right pane of the workflow page.

   ![Screenshot showing a workflow template file open for editing. The "Documentation" button is highlighted with an orange outline.](/assets/images/help/security/actions-workflows-documentation.png)

1. When you have finished defining your configuration, add the new workflow to your default branch.

   For more information, see [AUTOTITLE](/actions/how-tos/write-workflows/use-workflow-templates#choosing-and-using-a-workflow-template) and [AUTOTITLE](/code-security/reference/code-scanning/workflow-configuration-options).

{% endif %}

## Next steps

After your workflow runs successfully at least once, you are ready to start examining and resolving code scanning alerts. For more information on code scanning alerts, see [AUTOTITLE](/code-security/concepts/code-scanning/code-scanning-alerts) and [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/assess-alerts).

Learn how code scanning runs behave as checks on pull requests, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/triage-alerts-in-pull-requests).

You can find detailed information about your code scanning configuration, including timestamps for each scan and the percentage of files scanned, on the tool status page. For more information, see [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/manage-your-configuration/use-the-tools-status-page-for-code-scanning).

### Further reading

* [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/triage-alerts-in-pull-requests).
* [AUTOTITLE](/subscriptions-and-notifications/how-tos/managing-github-actions-notifications).
* [AUTOTITLE](/code-security/reference/code-scanning/workflow-configuration-options).
* [AUTOTITLE](/code-security/how-tos/view-and-interpret-data/view-code-scanning-logs).
