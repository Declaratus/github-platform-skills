---
title: About using actions in your enterprise
intro: 'GitHub Enterprise Server includes most GitHub-authored actions, and has options for enabling access to other actions from GitHub.com and GitHub Marketplace.'
redirect_from:
  - /enterprise/admin/github-actions/about-using-githubcom-actions-on-github-enterprise-server
  - /admin/github-actions/about-using-githubcom-actions-on-github-enterprise-server
  - /admin/github-actions/about-using-actions-on-github-enterprise-server
  - /admin/github-actions/about-using-actions-in-your-enterprise
  - /admin/github-actions/managing-access-to-actions-from-githubcom/about-using-actions-in-your-enterprise
versions:
  ghes: '*'
shortTitle: About actions in your enterprise
contentType: concepts
category:
  - Enable GitHub features for your enterprise
---

{% ifversion ghes %}

> [!NOTE]
> GitHub Enterprise Server users should use self-hosted runners. GitHub-hosted runners are **not** supported.

{% endif %}

## About actions on GitHub Enterprise Server

GitHub Actions workflows can use _actions_, which are individual tasks that you can combine to create jobs and customize your workflow. You can create your own actions, or use and customize actions shared by the GitHub community.

GitHub Actions on GitHub Enterprise Server is designed to work in environments without full internet access. By default, workflows cannot use actions from GitHub.com and [GitHub Marketplace](https://github.com/marketplace?type=actions). You can restrict your developers to using actions that are stored on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, which includes most official GitHub-authored actions, as well as any actions your developers create. Alternatively, to allow your developers to benefit from the full ecosystem of actions built by industry leaders and the open source community, you can configure access to other actions from GitHub.com.

We recommend allowing automatic access to all actions from GitHub.com. However, this does require GitHub Enterprise Server to make outbound connections to GitHub.com. If you don't want to allow these connections, or you want to have greater control over which actions are used on your enterprise, you can manually sync specific actions from GitHub.com.

## Official actions bundled with your enterprise instance

Most official GitHub-authored actions are automatically bundled with GitHub Enterprise Server, and are captured at a point in time from GitHub Marketplace.

The bundled official actions include the following, among others.
* `actions/checkout`
* `actions/upload-artifact`
* `actions/download-artifact`
* `actions/labeler`
* Various `actions/setup-` actions

To see all the official actions included on your enterprise instance, browse to the `actions` organization on your instance: <code>https://<em>HOSTNAME</em>/actions</code>.

There is no connection required between {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} and GitHub.com to use these actions.

Each action is a repository in the `actions` organization, and each action repository includes the necessary tags, branches, and commit SHAs that your workflows can use to reference the action. For information on how to update the bundled official actions, see [AUTOTITLE](/admin/managing-github-actions-for-your-enterprise/managing-access-to-actions-from-githubcom/using-the-latest-version-of-the-official-bundled-actions).

> [!NOTE]
> * When using setup actions (such as `actions/setup-LANGUAGE`) on GitHub Enterprise Server with self-hosted runners, you might need to set up the tools cache on runners that do not have internet access. For more information, see [AUTOTITLE](/admin/managing-github-actions-for-your-enterprise/managing-access-to-actions-from-githubcom/setting-up-the-tool-cache-on-self-hosted-runners-without-internet-access).
> * All `actions/setup-LANGUAGE` action repositories currently support three platforms: macOS, Windows, and Ubuntu.
> * When GitHub Enterprise Server is updated, bundled actions are automatically replaced with default versions in the upgrade package.
> * Being bundled with GitHub Enterprise Server means the action is available within that environment, but it doesn’t automatically guarantee compatibility with all platforms or self-hosted runners.

## Configuring access to actions on GitHub.com

If users in your enterprise need access to other actions from GitHub.com or GitHub Marketplace, there are a few configuration options.

The recommended approach is to enable automatic access to all actions from GitHub.com. You can do this by using GitHub Connect to integrate GitHub Enterprise Server with GitHub Enterprise Cloud. For more information, see [AUTOTITLE](/admin/managing-github-actions-for-your-enterprise/managing-access-to-actions-from-githubcom/enabling-automatic-access-to-githubcom-actions-using-github-connect).

> [!NOTE]
> Before you can configure access to actions on GitHub.com, you must configure {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to use GitHub Actions. For more information, see [AUTOTITLE](/admin/managing-github-actions-for-your-enterprise/getting-started-with-github-actions-for-your-enterprise/getting-started-with-github-actions-for-github-enterprise-server).

To use actions from GitHub.com,{% ifversion ghes %} both GitHub Enterprise Server and{% endif %} your self-hosted runners must be able to make outbound connections to GitHub.com. No inbound connections from GitHub.com are required. For more information, see [AUTOTITLE](/actions/reference/runners/self-hosted-runners#communication-with-githubcom).

After you enable GitHub Connect, you can use policies to restrict which public actions can be used in repositories in your enterprise. For more information, see [AUTOTITLE](/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise).

Alternatively, if you want stricter control over which actions are allowed in your enterprise, or you do not want to allow outbound connections to GitHub.com, you can manually download and sync actions onto your enterprise instance using the `actions-sync` tool. For more information, see [AUTOTITLE](/admin/managing-github-actions-for-your-enterprise/managing-access-to-actions-from-githubcom/manually-syncing-actions-from-githubcom).
