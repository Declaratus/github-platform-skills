---
title: Tracking security campaigns
shortTitle: Track security campaign
intro: Use the campaign tracking views to monitor remediation progress, identify stalled work, and measure campaign impact across your organization.
allowTitleToDifferFromFilename: true
permissions: 'Organization owners, security managers, and organization members with the **admin** role'
product: "{% ifversion fpt %}\nOrganizations on GitHub Team with [GitHub Secret Protection or GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{% ifversion ghec %}\nOrganizations on GitHub Team or GitHub Enterprise Cloud with [GitHub Secret Protection or GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{% ifversion ghes %}\nOrganizations with [{% ifversion security-campaigns %}GitHub Code Security{% elsif security-campaigns-secrets %}GitHub Secret Protection or GitHub Code Security{% endif %}](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}"
audience:
  - driver
contentType: how-tos
versions:
  feature: security-campaigns
redirect_from:
  - /code-security/securing-your-organization/fixing-security-alerts-at-scale/tracking-security-campaigns
category:
  - Secure at scale
---

{% ifversion security-campaigns-secrets %}

> [!NOTE]
> Campaigns for secret scanning alerts are currently in public preview and are subject to change.

{% endif %}

## Tracking campaigns across your organization

The tracking view helps you quickly assess the health of your organization’s campaigns. You can use it to identify campaigns with a high number of open alerts, check whether work has started, and determine whether campaigns are on track to meet their due dates.

To display the campaign tracking view, navigate to the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab for the organization, then in the left sidebar click **(icon: goal) Campaigns**. {% ifversion security-campaigns-secrets %}To display campaigns for secrets, click the **Secrets** tab at the top of the page.

![Screenshot of the security campaigns overview page. The "Secrets" campaign tab is outlined in orange.](/assets/images/help/security/security-campaigns-tracking-overview-2tabs.png)

{% else %}

![Screenshot of the security campaigns overview page.](/assets/images/help/security/security-campaigns-tracking-overview-code-only.png)

{% endif %}

The tracking view shows you a summary of "Open" and "Closed" campaigns, with the total alert count across all campaigns of that type. The view breaks down the total alert count into the following alert statuses:

* **Open**: the alert is still active and has not yet been addressed.
* **In progress** (code campaigns only): work has started to fix the alert—at least one branch or pull request has been created from the campaign view or alert page.
* **Fixed**: the alert has been resolved, either within or outside of the campaign workflow.
* **Dismissed**: the alert was reviewed but intentionally not fixed; it has been dismissed.

Review the proportion of alerts in each status to understand where action is needed. A high number of **Open** alerts may indicate that remediation has not yet started, while a low number of **In progress** alerts could signal that teams need additional guidance or prioritization.

## Tracking a single campaign

You can similarly track how a single campaign is progressing by viewing the campaign's own tracking page.

To display the tracking page for a campaign, navigate to the "Campaigns" page, {% ifversion security-campaigns-secrets %}select **Code** or **Secrets** campaigns, {% endif %}and then select the campaign you want to view from the list of campaigns.

![Screenshot of campaign tracking view for "Testing Campaigns for CodeQL". The campaign progress is outlined in dark orange.](/assets/images/help/security/driver-sec-campaign-view.png)

The tracking view for a single campaign helps you evaluate whether remediation is progressing as expected and whether additional follow-up is required.

The following indicators help you evaluate whether remediation is progressing as expected and whether additional follow-up is required.

* **Campaign progress**: how many alerts are closed (fixed or dismissed), in progress, or still left to review.
* **Status**: how the campaign is progressing towards its due date.
* **Copilot Autofix** (code campaigns only): number of alerts where Copilot Autofix can generate a fix to resolve the alert.

For example, if many alerts remain open as the due date approaches, you may need to follow up with repository owners or adjust the campaign timeline.

You can also explore campaign repositories and alerts to identify which teams are actively addressing alerts and which may need follow-up.

* **Repository details:** you can expand any repository to show the progress in alert remediation.
* **Alert details:** you can set the "Group by" option to **None** to show a list of all alerts.

You can filter both of these views to focus on a subset of repositories or alerts. For code campaigns, any alerts that are in progress are listed first.
