---
title: Managing labels
intro: You can classify {% ifversion fpt or ghec %}issues, pull requests, and discussions{% else %}issues and pull requests{% endif %} by creating, editing, applying, and deleting labels.
permissions: '{% ifversion ghec %} Members of an enterprise with managed users can only make changes in repositories that are part of their enterprise. {% endif %}'
redirect_from:
  - /github/managing-your-work-on-github/managing-your-work-with-issues-and-pull-requests/managing-labels
  - /articles/managing-Labels
  - /articles/labeling-issues-and-pull-requests
  - /github/managing-your-work-on-github/labeling-issues-and-pull-requests
  - /articles/about-labels
  - /github/managing-your-work-on-github/about-labels
  - /articles/creating-and-editing-labels-for-issues-and-pull-requests
  - /articles/creating-a-label
  - /github/managing-your-work-on-github/creating-a-label
  - /articles/customizing-issue-labels
  - /articles/applying-labels-to-issues-and-pull-requests
  - /github/managing-your-work-on-github/applying-labels-to-issues-and-pull-requests
  - /articles/editing-a-label
  - /github/managing-your-work-on-github/editing-a-label
  - /articles/deleting-a-label
  - /github/managing-your-work-on-github/deleting-a-label
  - /github/managing-your-work-on-github/managing-labels
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
contentType: how-tos
category:
  - Triage and organize issues
---
## About labels

You can manage your work on GitHub by creating labels to categorize {% ifversion fpt or ghec %}issues, pull requests, and discussions{% else %}issues and pull requests{% endif %}. You can apply labels in the repository the label was created in. Once a label exists, you can use the label on any {% ifversion fpt or ghec %}issue, pull request, or discussion{% else %}issue or pull request{% endif %} within that repository. Addition, modification, or deletion of labels in one repository has no effect on labels belonging to other repositories.

## About default labels

GitHub provides default labels in every new repository. You can use these default labels to help create a standard workflow in a repository.

Label | Description
---  | ---
`accessibility` | Indicates a barrier affecting people with disabilities
`bug` | Indicates an unexpected problem or unintended behavior
`documentation` | Indicates a need for improvements or additions to documentation
`duplicate` | Indicates similar {% ifversion fpt or ghec %}issues, pull requests, or discussions{% else %}issues or pull requests{% endif %}
`enhancement` | Indicates new feature requests
`good first issue` | Indicates a good issue for first-time contributors
`help wanted` | Indicates that a maintainer wants help on an issue or pull request
`invalid` | Indicates that an {% ifversion fpt or ghec %}issue, pull request, or discussion{% else %}issue or pull request{% endif %} is no longer relevant
`question` | Indicates that an {% ifversion fpt or ghec %}issue, pull request, or discussion{% else %}issue or pull request{% endif %} needs more information
`wontfix` | Indicates that work won't continue on an {% ifversion fpt or ghec %}issue, pull request, or discussion{% else %}issue or pull request{% endif %}

Default labels are included in every new repository when the repository is created, but you can edit or delete the labels later.

Issues with the `good first issue` label are used to populate the repository's `contribute` page. For an example of a `contribute` page, see [github/docs/contribute](https://github.com/github/docs/contribute).

Organization owners can customize the default labels for repositories in their organization. For more information, see [AUTOTITLE](/organizations/managing-organization-settings/managing-default-labels-for-repositories-in-your-organization).

## Creating a label

Anyone with write access to a repository can create a label.

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: issue-opened) Issues** or **(icon: git-pull-request) Pull requests**.

   ![Screenshot of the main page of a repository. In the horizontal navigation bar, the "Issues" and "Pull requests" tabs are outlined in orange.](/assets/images/help/repository/repo-settings-issues-pull-requests-global-nav-update.png)
1. Above the list of issues or pull requests, click **Labels**.

   ![Screenshot of the list of issues for a repository. Above the list, a button, labeled with a label icon and "Labels", is outlined in dark orange.](/assets/images/help/issues/issues-labels-button.png)
1. To the right of the search field, click **New label**.
1. Under "Label name", type a name for your label.
1. Under "Description", type a description to help others understand and use your label.
1. Optionally, to customize the color of your label, edit the hexadecimal number, or, for another random selection, click (icon: sync).
1. To save the new label, click **Create label**.

## Applying a label

Anyone with triage access to a repository can apply and dismiss labels.

1. Navigate to the {% ifversion fpt or ghec %}issue, pull request, or discussion{% else %}issue or pull request{% endif %}.
1. In the right sidebar, click **Labels**, then click a label.

## Editing a label

Anyone with write access to a repository can edit existing labels.

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: issue-opened) Issues** or **(icon: git-pull-request) Pull requests**.

   ![Screenshot of the main page of a repository. In the horizontal navigation bar, the "Issues" and "Pull requests" tabs are outlined in orange.](/assets/images/help/repository/repo-settings-issues-pull-requests-global-nav-update.png)
1. Above the list of issues or pull requests, click **Labels**.

   ![Screenshot of the list of issues for a repository. Above the list, a button, labeled with a label icon and "Labels", is outlined in dark orange.](/assets/images/help/issues/issues-labels-button.png)
1. In the labels list, to the right of the label you want to edit, click **Edit**.
1. Under "Label name", type a name for your label.
1. Under "Description", type a description to help others understand and use your label.
1. Optionally, to customize the color of your label, edit the hexadecimal number, or, for another random selection, click (icon: sync).
1. Click **Save changes**.

## Deleting a label

Anyone with write access to a repository can delete existing labels.

Deleting a label will remove the label from issues and pull requests.

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: issue-opened) Issues** or **(icon: git-pull-request) Pull requests**.

   ![Screenshot of the main page of a repository. In the horizontal navigation bar, the "Issues" and "Pull requests" tabs are outlined in orange.](/assets/images/help/repository/repo-settings-issues-pull-requests-global-nav-update.png)
1. Above the list of issues or pull requests, click **Labels**.

   ![Screenshot of the list of issues for a repository. Above the list, a button, labeled with a label icon and "Labels", is outlined in dark orange.](/assets/images/help/issues/issues-labels-button.png)
1. In the labels list, to the right of the label you want to delete, click **Delete**.

## Further reading

* [AUTOTITLE](/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests)
* [AUTOTITLE](/organizations/managing-organization-settings/managing-default-labels-for-repositories-in-your-organization){% ifversion fpt or ghec %}
* [AUTOTITLE](/communities/setting-up-your-project-for-healthy-contributions/encouraging-helpful-contributions-to-your-project-with-labels){% endif %}
* [AUTOTITLE](/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#using-emojis)
