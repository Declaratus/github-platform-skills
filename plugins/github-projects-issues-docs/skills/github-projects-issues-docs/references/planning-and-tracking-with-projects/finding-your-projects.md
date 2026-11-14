---
title: Finding your projects
intro: Learn how to locate projects in your account, organizations, repositories, and teams.
redirect_from:
  - /issues/planning-and-tracking-with-projects/learning-about-projects/finding-your-projects
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
contentType: concepts
category:
  - Set up and manage projects
---

## Browsing all of your projects

You can browse all of your projects, regardless of where they are located. You can see the projects you have recently viewed and the projects you have created, and apply your own filters.

1. In the top left of any page, click (icon: three-bars) to open the global navigation menu.
1. In the menu, click **(icon: table) Projects**.
1. Optionally, in the text box above the list of projects, enter a filter to choose which projects are displayed. For more information on filter syntax, see [Syntax for filtering a list of projects](#syntax-for-filtering-a-list-of-projects) in this article.

   ![Screenshot of the main page for a team. In the horizontal navigation bar, the "Projects" tab is outlined in dark orange.](/assets/images/help/projects-v2/index-filter-box.png)

1. Click on the name of the project you want to open.

## Finding an organization's projects

You can view and filter all the projects owned by an organization that you have access to.

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Click the name of your organization.
1. Under the organization name, click **(icon: table) Projects**.
1. Optionally, in the text box above the list of projects, enter a filter to choose which projects are displayed. For more information on filter syntax, see [Syntax for filtering a list of projects](#syntax-for-filtering-a-list-of-projects) in this article.

   ![Screenshot of the main page for a team. In the horizontal navigation bar, the "Projects" tab is outlined in dark orange.](/assets/images/help/projects-v2/index-filter-box.png)

1. Click on the name of the project you want to open.

## Finding projects owned by your personal account

You can view and filter projects that you have created under your personal account.

1. In the top right corner of GitHub, click your profile picture, then click **Your profile**.

   ![Screenshot of the dropdown menu under @octocat's profile picture. "Your profile" is outlined in dark orange.](/assets/images/help/profile/profile-button-avatar-menu-global-nav-update.png)
1. On your profile, click **(icon: table) Projects**.
1. Optionally, in the text box above the list of projects, enter a filter to choose which projects are displayed. For more information on filter syntax, see [Syntax for filtering a list of projects](#syntax-for-filtering-a-list-of-projects) in this article.

   ![Screenshot of the main page for a team. In the horizontal navigation bar, the "Projects" tab is outlined in dark orange.](/assets/images/help/projects-v2/index-filter-box.png)

1. Click on the name of the project you want to open.

## Finding projects linked to a repository

Repositories can be linked to organization-level and user-level projects. You can browse and filter the projects that are linked to a specific repository. For more information on linking projects to a repository, see [AUTOTITLE](/issues/planning-and-tracking-with-projects/managing-your-project/adding-your-project-to-a-repository).

1. On GitHub, navigate to the main page of your repository.
1. Click **(icon: table) Projects**.

   ![Screenshot showing a repository's tabs. The "Projects" tab is highlighted with an orange outline.](/assets/images/help/projects-v2/repo-tab.png)

1. Optionally, in the text box above the list of projects, enter a filter to choose which projects are displayed. For more information on filter syntax, see [Syntax for filtering a list of projects](#syntax-for-filtering-a-list-of-projects) in this article.

   ![Screenshot of the main page for a team. In the horizontal navigation bar, the "Projects" tab is outlined in dark orange.](/assets/images/help/projects-v2/index-filter-box.png)

1. Click on the name of the project you want to open.

## Finding projects linked to a team

You can also link a project to specific teams in an organization and then browse and filter the projects that are associated with a particular team. For more information on linking projects, see [AUTOTITLE](/issues/planning-and-tracking-with-projects/managing-your-project/adding-your-project-to-a-team).

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Click the name of your organization.
1. Under your organization name, click **(icon: people) Teams**.

   ![Screenshot of the horizontal navigation bar for an organization. A tab, labeled with the people icon and "Teams," is outlined in dark orange.](/assets/images/help/organizations/organization-teams-tab.png)
1. Click the name of the team.
1. Click **(icon: project) Projects**.

   ![Screenshot of the main page for a team. In the horizontal navigation bar, the "Projects" tab is outlined in dark orange.](/assets/images/help/organizations/team-project-board-button.png)

1. Optionally, in the text box above the list of projects, enter a filter to choose which projects are displayed. For more information on filter syntax, see [Syntax for filtering a list of projects](#syntax-for-filtering-a-list-of-projects) in this article.

   ![Screenshot of the main page for a team. In the horizontal navigation bar, the "Projects" tab is outlined in dark orange.](/assets/images/help/projects-v2/index-filter-box.png)

1. Click on the name of the project you want to open.

## Syntax for filtering a list of projects

You can combine filters and even search project titles by including text. For example, `is:open creator:octocat game` will return open projects, created by the @octocat user, with the word "game" in the project title. You can use the search qualifiers in the following table to narrow down your search for a project.

| Qualifier  | Explanation
| ---------- | -------------
| `is:open` | Returns projects that are currently open. |
| `is:closed` | Returns projects that are currently closed. |
| `is:template` | Returns projects that are marked as a template. |
| `is:private` | Returns projects are set to private visibility. |
| `is:public` | Returns projects are set to public visibility. |
| `creator:USERNAME` | Returns projects created by USERNAME. For example, `creator:octocat` will return projects created by @octocat. |

You can also change how the projects are ordered.

| Qualifier  | Explanation
| ---------- | -------------
| `sort:title-asc` | Sort by project title. |
| `sort:updated-asc` or `sort:updated-desc`  | Sort by when the project was last updated. |
| `sort:created-asc` or `sort:created-desc`  | Sort by when the project was created. |
