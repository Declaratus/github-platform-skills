---
title: Reviewing audit logs for GitHub Copilot
shortTitle: Review audit logs
intro: Check for changes to settings or licenses in your Copilot plan.
product: 'Copilot Business or Copilot Enterprise'
permissions: Enterprise owners or users with the "Read enterprise audit logs" custom role
redirect_from:
  - /copilot/managing-copilot-for-business/reviewing-your-organization-or-enterprises-audit-logs-for-copilot-for-business
  - /copilot/managing-copilot-business/reviewing-your-organization-or-enterprises-audit-logs-for-copilot-business
  - /copilot/managing-github-copilot-in-your-organization/reviewing-your-organization-or-enterprises-audit-logs-for-copilot-business
  - /copilot/managing-github-copilot-in-your-organization/reviewing-audit-logs-for-copilot-business
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-audit-logs-for-copilot-business
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-github-copilot-activity-in-your-organization/reviewing-audit-logs-for-copilot-business
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/reviewing-audit-logs-for-copilot-business
  - /copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-audit-logs-for-copilot-business
  - /copilot/how-tos/administer/organizations/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-audit-logs-for-copilot-business
  - /copilot/how-tos/administer/organizations/reviewing-activity-related-to-github-copilot-in-your-organization/review-audit-logs
  - /copilot/how-tos/administer/organizations/review-activity/review-audit-logs
  - /copilot/how-tos/administer/manage-for-organization/review-activity/review-audit-logs
  - /copilot/how-tos/administer-copilot/manage-for-organization/review-activity/review-audit-logs
versions:
  feature: copilot
contentType: how-tos
category:
  - Manage Copilot for a team
docsTeamMetrics:
  - ai-governance
---

You can use the audit log to review actions taken in your enterprise. The audit log includes a record of:

* Changes to your Copilot plan, such as changes to settings and policies or a user losing or receiving a license
* Agent activity on the GitHub website

The audit log does **not** include client session data, such as the prompts a user sends to Copilot locally. A custom solution is required to access this data: for example, some companies use custom hooks to send Copilot CLI events to their own logging service.

## Viewing your enterprise's audit logs

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. Under "Settings", click **Audit log**.

## Searching audit log events

Use the `action:copilot` search term to view all events related to your Copilot plan.

You can also filter by a specific event. For example, `action:copilot.cfb_seat_assignment_created` returns events related to a license being assigned to a new user. For a full list of Copilot events, see [AUTOTITLE](/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise) or [AUTOTITLE](/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/audit-log-events-for-your-organization).

To view a record of agent activity, use the `actor:Copilot` search term. See [AUTOTITLE](/copilot/reference/enterprise-administrators/agentic-audit-log-events).

> [!NOTE]
> For team-based seat assignments, the `copilot.cfb_seat_added` event's actor may not be the account that performed the membership change. See [AUTOTITLE](/copilot/reference/copilot-billing/seat-assignment#seat-assignment-management).

## Retaining audit log history

The audit log retains events for the last 180 days. We recommend streaming the audit log to a Security Information and Event Management (SIEM) platform, where you can view long-term history and set up alerts for anomalous activity. See [AUTOTITLE](/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise).
