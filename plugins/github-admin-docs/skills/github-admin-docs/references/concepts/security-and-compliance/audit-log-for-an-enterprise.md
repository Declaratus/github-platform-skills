---
title: Audit log for an enterprise
intro: 'To support debugging and internal and external compliance, GitHub provides logs of audited{% ifversion ghes %} system,{% endif %} user, organization, and repository events.'
shortTitle: Audit logs
redirect_from:
  - /enterprise/admin/articles/audit-logging
  - /enterprise/admin/installation/audit-logging
  - /enterprise/admin/user-management/audit-logging
  - /admin/user-management/audit-logging
  - /admin/user-management/monitoring-activity-in-your-enterprise/audit-logging
  - /github/setting-up-and-managing-your-enterprise/managing-your-enterprise-users-with-your-identity-provider/auditing-activity-in-your-enterprise
  - /admin/authentication/managing-your-enterprise-users-with-your-identity-provider/auditing-activity-in-your-enterprise
  - /admin/identity-and-access-management/managing-iam-with-enterprise-managed-users/auditing-activity-in-your-enterprise
  - /admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/about-the-audit-log-for-your-enterprise
  - /enterprise-onboarding/feature-enhancements/about-the-audit-log-for-your-enterprise
  - /enterprise-onboarding/govern-people-and-repositories/using-the-audit-log-for-your-enterprise
versions:
  ghes: '*'
  ghec: '*'
contentType: concepts
category:
  - Secure and govern your enterprise
docsTeamMetrics:
  - enterprise-onboarding
---

## What are audit logs?

> [!NOTE]
> Webhooks might be a good alternative to the audit log or API polling for certain use cases. Webhooks are a way for GitHub to notify your server when specific events occur for a repository, organization, or enterprise. Compared to the API or searching the audit log, webhooks can be more efficient if you just want to learn and possibly log when certain events occur on your enterprise, organization, or repository. See [AUTOTITLE](/webhooks).

The audit log lists events triggered by activities that affect your enterprise{% ifversion ghes %}. Audit logs for GitHub are retained indefinitely, unless an enterprise owner configured a different retention period. See [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/configuring-the-audit-log-for-your-enterprise).{% else %} within the last 180 days. The audit log retains Git events for seven days.{% endif %}

By default, only events from the past three months are displayed. To view older events, you must specify a date range with the `created` parameter. See [AUTOTITLE](/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates).

The name for each audit log entry is composed of a category of events, followed by an operation type. For example, the `repo.create` entry refers to the `create` operation on the `repo` category.

Each audit log entry shows applicable information about an event, such as:

* The {% ifversion ghec or ghes %}enterprise or {% endif %}organization an action was performed in
* The user (actor) who performed the action
* The user affected by the action
* Which repository an action was performed in
* The action that was performed
* Which country the action took place in
* The date and time the action occurred
{%- ifversion ghec or ghes %}
* The SAML SSO and SCIM identity of the user (actor) who performed the action
{%- endif %}
{%- ifversion ghec or ghes %}
* For actions outside of the web UI, how the user (actor) authenticated
{%- endif %}
{%- ifversion enterprise-audit-log-ip-addresses %}
* Optionally, the source IP address for the user (actor) who performed the action
{%- endif %}

{% ifversion ghes %}Site administrators can review the audit log for an instance, which contains a wider range of events including system administrative events. To access the instance-level audit log:

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the left menu, click **Audit log**.{% endif %}

In addition to viewing your audit log, you can monitor activity in your enterprise in other ways, such as {% ifversion ghes %}viewing push logs and {% endif %}managing global webhooks. For more information, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/exploring-user-activity-in-your-enterprise). You can also use the audit log, and other tools, to monitor the actions taken in response to security alerts. For more information, see [AUTOTITLE](/code-security/concepts/security-at-scale/audit-security-alerts).

## How to use audit logs

As an enterprise owner{% ifversion ghes %} or site administrator{% endif %}, you can interact with the audit log data for your enterprise in several ways:
* You can view the audit log for your enterprise. For more information, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/accessing-the-audit-log-for-your-enterprise).
* You can search the audit log for specific events{% ifversion ghec %} and export audit log data{% endif %}. For more information, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/searching-the-audit-log-for-your-enterprise){% ifversion ghec %} and [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/exporting-audit-log-activity-for-your-enterprise){% endif %}.
* You can identify all events that were performed by a specific access token. For more information, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/identifying-audit-log-events-performed-by-an-access-token).{% ifversion ghes %}
* You can configure settings, such as the retention period for audit log events and whether Git events are included. For more information, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/configuring-the-audit-log-for-your-enterprise).{% endif %}
{%- ifversion enterprise-audit-log-ip-addresses %}
* You can display the IP address associated with events in the audit log. For more information, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/displaying-ip-addresses-in-the-audit-log-for-your-enterprise).
{%- endif %}
* You can stream audit and Git events data from GitHub to an external data management system. For more information, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise).
{%- ifversion ghes %}
* You can forward audit and system logs from your enterprise to a third-party hosted monitoring system. For more information, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/exploring-user-activity-in-your-enterprise/log-forwarding).
{%- endif %}
* You can use the Audit log API to view actions performed in your enterprise. For more information, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/using-the-audit-log-api-for-your-enterprise).

For a full list of audit log actions that may appear in your enterprise audit log, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise).

## Further reading

* [AUTOTITLE](/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization)
{%- ifversion ghes %}
* [AUTOTITLE](/admin/monitoring-and-managing-your-instance/monitoring-your-instance/about-system-logs)
{%- endif %}
