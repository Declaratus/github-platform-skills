---
title: Assigning issues and pull requests to other GitHub users
intro: Assignees clarify who is working on specific issues and pull requests.
permissions: 'Anyone with write access to a repository can assign issues and pull requests. {% ifversion ghec %} Members of an enterprise with managed users can only make changes in repositories that are part of their enterprise. {% endif %}'
redirect_from:
  - /github/managing-your-work-on-github/managing-your-work-with-issues-and-pull-requests/assigning-issues-and-pull-requests-to-other-github-users
  - /articles/assigning-issues-and-pull-requests-to-other-github-users
  - /github/managing-your-work-on-github/assigning-issues-and-pull-requests-to-other-github-users
  - /issues/tracking-your-work-with-issues/managing-issues/assigning-issues-and-pull-requests-to-other-github-users
  - /issues/tracking-your-work-with-issues/assigning-issues-and-pull-requests-to-other-github-users
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Assign issues & PRs
category:
  - Create and work with issues
---

## About issue and pull request assignees

You can assign multiple people to each issue or pull request, including: yourself, anyone who has commented on the issue or pull request, anyone with write permissions to the repository, and organization members with read permissions to the repository. For more information, see [AUTOTITLE](/get-started/learning-about-github/access-permissions-on-github).

{% ifversion copilot %}

You may also be able to assign Copilot to an issue, see [AUTOTITLE](/copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions).

{% endif %}

Both issues and pull requests support up to 10 assignees.

## Assigning an individual issue or pull request

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: issue-opened) Issues** or **(icon: git-pull-request) Pull requests**.

   ![Screenshot of the main page of a repository. In the horizontal navigation bar, the "Issues" and "Pull requests" tabs are outlined in orange.](/assets/images/help/repository/repo-settings-issues-pull-requests-global-nav-update.png)
1. Open the issue or pull request that you want to assign to someone.
1. In the right side menu, click **Assignees**.

   ![Screenshot of the right sidebar of an issue. A header, labeled "Assignees", is outlined in dark orange.](/assets/images/help/issues/assignee-menu.png)
1. To assign the issue or pull request to a user, start typing their username, then click their name when it appears. You can select and add up to ten assignees to an issue or pull request.

## Assigning multiple issues or pull requests

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: issue-opened) Issues** or **(icon: git-pull-request) Pull requests**.

   ![Screenshot of the main page of a repository. In the horizontal navigation bar, the "Issues" and "Pull requests" tabs are outlined in orange.](/assets/images/help/repository/repo-settings-issues-pull-requests-global-nav-update.png)
1. Select the items you want to assign to someone.

   ![Screenshot of the first two items in a list of issues. To the left of each issue, a checkbox is checked and outlined in dark orange.](/assets/images/help/issues/issues-assign-checkbox.png)
1. In the upper-right corner, click **Assign**.
1. To assign the items to a user, start typing their username, then click their name when it appears. You can select and add up to ten assignees to an issue or pull request.

{% ifversion copilot %}

## Assigning an issue to Copilot

If you assign an issue to Copilot, Copilot will work autonomously on the issue, creating a pull request and, when it has finished, requesting that you review the pull request. See [AUTOTITLE](/copilot/concepts/agents/cloud-agent/about-cloud-agent).

{% endif %}

## Further reading

* [AUTOTITLE](/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests)
