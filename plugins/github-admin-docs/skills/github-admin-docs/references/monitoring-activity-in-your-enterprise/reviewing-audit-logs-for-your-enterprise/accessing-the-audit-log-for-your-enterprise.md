---
title: Accessing the audit log for your enterprise
intro: You can view aggregated actions from all of the organizations owned by an enterprise account in the enterprise's audit log.
shortTitle: Access audit logs
permissions: Enterprise owners {% ifversion ghes %}and site administrators {% endif %}can access the audit log.
redirect_from:
  - /github/setting-up-and-managing-your-enterprise/managing-organizations-in-your-enterprise-account/viewing-the-audit-logs-for-organizations-in-your-enterprise-account
  - /articles/viewing-the-audit-logs-for-organizations-in-your-business-account
  - /articles/viewing-the-audit-logs-for-organizations-in-your-enterprise-account
  - /github/setting-up-and-managing-your-enterprise-account/viewing-the-audit-logs-for-organizations-in-your-enterprise-account
  - /github/setting-up-and-managing-your-enterprise/viewing-the-audit-logs-for-organizations-in-your-enterprise-account
  - /admin/user-management/managing-organizations-in-your-enterprise/viewing-the-audit-logs-for-organizations-in-your-enterprise
versions:
  ghec: '*'
  ghes: '*'
contentType: how-tos
category:
  - Monitor and audit your enterprise
---

{% ifversion ghec %}

There are several ways to access and retain audit log data for your enterprise:

* **Web interface**: View recent activity in your enterprise settings. See [Viewing the enterprise's audit log via the web interface](#viewing-the-enterprises-audit-log-via-the-web-interface).
* **JSON/CSV exports**: Download a file of audit log activity. See [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/exporting-audit-log-activity-for-your-enterprise).
* **REST API endpoint**: Query audit log events programmatically. See [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/using-the-audit-log-api-for-your-enterprise).
* **Streaming to an external system**: Deliver events continuously to a system that your incident responders can access and query. See [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise).

Each method exposes a different subset of your audit log data. For the full list of events, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise).

## Audit log data available by access method

{% rowheaders %}

| Data available | Web interface | JSON/CSV exports | REST API endpoint | Streaming to an external system |
| :- | :-: | :-: | :-: | :-: |
| Range of web events | 180 days | 180 days | 180 days | Determined by the retention policy of your external system |
| [API request events](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise#api) | (icon: x) | (icon: x) | (icon: x) | (icon: check) (If enabled) |
| [Git events](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise#git) | (icon: x) | (icon: check) (JSON only). The audit log retains Git events for seven days. | (icon: check). The audit log retains Git events for seven days. | (icon: check) |
| Single sign-on responses (organization and enterprise) | (icon: x) | (icon: check) | (icon: check) | (icon: check) |
| [Created and completed workflow runs](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise#workflows) | (icon: x) | (icon: check) | (icon: check) | (icon: check) |
| [Started workflow jobs, including the secrets provided to each job](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise#workflows) | (icon: x) | (icon: check) | (icon: check) | (icon: check) |
| Online and offline self-hosted runners | (icon: x) | (icon: check) | (icon: check) | (icon: check) |

{% endrowheaders %}

For enterprises that use Enterprise Managed Users, the enterprise audit log also includes user events. For a list of these user events, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/security-log-events).

To retain Git events beyond their availability in the audit log, save them to external storage before they expire. Configure audit log streaming in advance to collect events continuously.

Git event exports do not include events initiated through the web interface or the REST or GraphQL APIs. For example, when someone merges a pull request in the web interface, the resulting push to the base branch is missing from the export.

`api.request` events are available only in streamed enterprise audit logs, and only when the option to stream API request events has been enabled. For more information, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#enabling-audit-log-streaming-of-api-requests). 

> [!IMPORTANT]
> Audit log streaming only includes activity from the time you enable it. Enabling it during an incident will not recover earlier activity.

## Preparing for an incident response

Enable enterprise audit log streaming, API request event streaming, and source IP address disclosure to prepare for incident response. Without all three features enabled, responders will have critical visibility gaps when investigating incidents affecting your enterprise or its organizations. Set an appropriate retention period for the streamed logs and ensure incident responders can access them.

For setup instructions, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#setting-up-audit-log-streaming), [Enabling audit log streaming of API requests](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#enabling-audit-log-streaming-of-api-requests), and [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/displaying-ip-addresses-in-the-audit-log-for-your-enterprise).

**During a security incident**, GitHub Support can answer questions about features and available data, but does not investigate on your behalf or preserve logs for your investigation. For more information, see [AUTOTITLE](/support/learning-about-github-support/understanding-how-github-support-can-help-during-a-security-incident).

{% endif %}

## Viewing the enterprise's audit log via the web interface

The audit log lists events triggered by activities that affect your enterprise{% ifversion ghes %}. Audit logs for GitHub are retained indefinitely, unless an enterprise owner configured a different retention period. See [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/configuring-the-audit-log-for-your-enterprise).{% else %} within the last 180 days. The audit log retains Git events for seven days.{% endif %}

By default, only events from the past three months are displayed. To view older events, you must specify a date range with the `created` parameter. See [AUTOTITLE](/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates).
{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. Under "Settings", click **Audit log**.
