---
title: Reviewing changes to content exclusions for GitHub Copilot
shortTitle: Review changes
intro: You can monitor changes to content exclusions in your repositories and organizations.
permissions: Organization owners
product: 'Organizations{% ifversion ghec %} and enterprises{% endif %} with a Copilot Business or Copilot Enterprise plan.'
versions:
  feature: copilot
redirect_from:
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-changes-to-content-exclusions-for-github-copilot
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-github-copilot-features-in-your-organization/reviewing-changes-to-content-exclusions-for-github-copilot
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/reviewing-changes-to-content-exclusions-for-github-copilot
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/reviewing-changes-to-content-exclusions-for-github-copilot
  - /copilot/managing-copilot/configuring-and-auditing-content-exclusion/reviewing-changes-to-content-exclusions-for-github-copilot
  - /copilot/how-tos/content-exclusion/reviewing-changes-to-content-exclusions-for-github-copilot
  - /copilot/how-tos/content-exclusion/review-changes
contentType: how-tos
category:
  - Configure Copilot
---

Organization and repository settings include the ability to exclude content from being used by GitHub Copilot. You can review any changes that are made to these content exclusion settings.

## Reviewing changes in your repository

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)

1. In the sidebar, under "Code, planning, and automation", click **(icon: copilot) Copilot**.
1. Scroll to the bottom of the page.

   You will see the name of the person who last changed the content exclusion settings, and information about when they made this change.
1. Click the time of the last change.

   ![Screenshot of the last edited information. The time of change link is highlighted with a dark orange outline.](/assets/images/help/copilot/content-exclusions-last-edited-by.png)

   The "Audit log" page for the organization is displayed, showing the most recently logged occurrences of the `copilot.content_exclusion_changed` action in the repository.
1. Click the ellipsis (...) at the end of each entry to see more details.

   If the "excluded_paths" entry is truncated, hover over the truncated value to show the full entry. This displays the content of the exclusion settings after the change was saved.

   ![Screenshot of audit log details for the 'copilot.content_exclusion_changed' action. The ellipsis button is highlighted.](/assets/images/help/copilot/copilot-audit-log.png)

## Reviewing changes in your organization

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)

1. In the left sidebar, click **(icon: copilot) Copilot** then click **Content exclusion**.
1. Scroll to the bottom of the page.

   You will see the name of the person who last changed the content exclusion settings, and information about when they made this change.
1. Click the time of the last change.

   ![Screenshot of the last edited information. The time of change link is highlighted with a dark orange outline.](/assets/images/help/copilot/content-exclusions-last-edited-by.png)

   The "Audit log" page for the organization is displayed, showing the most recently logged occurrences of the `copilot.content_exclusion_changed` action.

   Changes made at either the repository or organization level are listed.

1. Click the ellipsis (...) at the end of each entry to see more details.

   If the "excluded_paths" entry is truncated, hover over the truncated value to show the full entry. This displays the content of the exclusion settings after the change was saved.

   ![Screenshot of audit log details for the 'copilot.content_exclusion_changed' action. The ellipsis button is highlighted.](/assets/images/help/copilot/copilot-audit-log.png)

{% ifversion ghec %}

## Reviewing changes in your enterprise

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: copilot) AI controls**.
1. In the sidebar, click (icon: copilot) **Copilot**.
1. Click (icon: circle-slash) **Content exclusion**.
1. At the bottom of the page, you'll see the name of the person who last changed the content exclusion settings, and information about when they made this change. Click the time of the last change.

   ![Screenshot of the last edited information. The time of change link is highlighted with a dark orange outline.](/assets/images/help/copilot/content-exclusions-last-edited-by.png)

   The "Audit log" page for the organization is displayed, showing the most recently logged occurrences of the `copilot.content_exclusion_changed` action.

   Changes made at the repository, organization, and enterprise level are listed.

1. Click the ellipsis (...) at the end of each entry to see more details.

   If the "excluded_paths" entry is truncated, hover over the truncated value to show the full entry. This displays the content of the exclusion settings after the change was saved.

   ![Screenshot of audit log details for the 'copilot.content_exclusion_changed' action. The ellipsis button is highlighted.](/assets/images/help/copilot/copilot-audit-log.png)

{% endif %}

## Further reading

* [AUTOTITLE](/copilot/concepts/context/content-exclusion)
