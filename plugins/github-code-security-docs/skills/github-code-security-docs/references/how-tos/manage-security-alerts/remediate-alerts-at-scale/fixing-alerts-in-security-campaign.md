---
title: Fixing alerts in a security campaign
shortTitle: Fix alerts in campaign
intro: Learn how to find and fix alerts in a security campaign.
allowTitleToDifferFromFilename: true
permissions: 'Users with **write** access'
product: "{% ifversion fpt %}\nOrganizations on GitHub Team with [GitHub Secret Protection or GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{% ifversion ghec %}\nOrganizations on GitHub Team or GitHub Enterprise Cloud with [GitHub Secret Protection or GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{% ifversion ghes %}\nOrganizations with [{% ifversion security-campaigns %}GitHub Code Security{% elsif security-campaigns-secrets %}GitHub Secret Protection or GitHub Code Security{% endif %}](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}"
contentType: how-tos
versions:
  feature: security-campaigns
redirect_from:
  - /code-security/code-scanning/managing-code-scanning-alerts/fixing-alerts-in-security-campaign
category:
  - Secure at scale
---

## Viewing alerts in a security campaign

When a campaign targets security alerts in a repository that you have write access to, you can navigate to the list of repository alerts in the campaign.

* Display the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab for the repository and click one of the campaigns under "Campaigns" in the sidebar.
* If you have write access to more than one repository in the organization, display the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab for the organization and click one of the campaigns under "Campaigns" in the sidebar.
* Alternatively, click **View security campaign** in the campaign's email notification.

This view shows the alerts in the current repository for a campaign called "SQL injection (CWE-89)" (highlighted gray) that is managed by "octocat" (outlined in dark orange).

![Screenshot of repository campaign view with "SQL injection (CWE-89)" campaign displayed and the "Campaign manager" outlined in dark orange.](/assets/images/help/security/builder-sec-campaign.png)

## Fixing alerts in a security campaign

If you want to see the code that triggered the security alert and the suggested fix, click on the alert name to show the alert view.

{% ifversion copilot %}If agentic autofix is enabled, the fastest way to resolve alerts is to assign them to Copilot. Agentic Autofix explores the codebase, generates and validates a fix, and opens a pull request. See [Assigning alerts to Copilot](#assigning-alerts-to-copilot) below. The following steps describe how to fix alerts yourself instead.{% endif %}

1. When you are ready to work on one or more security alerts, check whether they are already assigned to Copilot or whether someone else is working on them. Open any linked work to check whether a fix is already in progress:
   * (icon: git-pull-request-draft) an open draft pull request may fix this alert.
   * (icon: git-pull-request) an open pull request may fix this alert.
   * (icon: git-branch) a branch may contain changes to fix this alert.

1. In the campaign view for the repository, select the alerts that you want to fix.{% ifversion security-campaigns-autofix %}
1. Connect the security alerts to a working branch:
   * If at least one "Autofix" suggestion is available for the selected alerts, click **Commit autofix** and commit the changes either to a new branch or to an existing branch.
   * If no autofix suggestions are available for the selected alerts, click **Create new branch** to create a new branch where you will work on fixing the alerts.{% elsif ghes %}
1. Click **Create new branch** to create a new branch where you will work on fixing the alerts.{% endif %}
1. When you have finished fixing the alerts and testing your solutions, create a pull request for your changes and request a review from the campaign manager.

> [!TIP] If you have write permission for more than one repository in the campaign, click the link in the "Campaign progress" box in your repository to show the organization-level view of the campaign. When you open a repository from this view, the campaign alerts view is displayed.

{% ifversion copilot %}

## Assigning alerts to Copilot

Before you assign alerts, agentic autofix must be enabled for the repository. See [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/managing-access-to-agentic-autofix-for-code-scanning).

Agentic Autofix consumes AI credits and GitHub Actions minutes.

You can assign between 1 and 25 alerts from the campaign view. One assignment creates one agent session and one pull request for the selected alerts. It also adds you as a requested reviewer.

1. In the repository's campaign view, select the alerts that you want to assign.
1. Above the list of alerts, click **(icon: copilot) Assign to Copilot**.

Typically within a few minutes, Copilot opens a pull request that addresses the assigned alerts. The pull request summarizes the fixes and changes, and appears next to each assigned alert.

For more information about reviewing the session and pull request, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/resolve-alerts#fixing-alerts-with-copilot).

{% endif %}

{% ifversion copilot %}

## Using GitHub Copilot Chat for secure coding

If you have access to Copilot Chat then you can ask the AI questions about the vulnerability, the suggested fix, and how to test that the fix is comprehensive.

> [!TIP]
> Copilot's ability to answer natural language questions like these in a repository context is optimized when the semantic code search index for the repository is up to date. For more information, see [AUTOTITLE](/copilot/concepts/prompting-and-context/repository-indexing).

{% endif %}
