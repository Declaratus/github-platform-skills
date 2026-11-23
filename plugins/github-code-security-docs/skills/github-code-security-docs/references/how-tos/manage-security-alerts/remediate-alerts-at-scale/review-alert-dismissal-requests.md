---
title: Reviewing alert dismissal requests
shortTitle: Review alert dismissal requests
intro: Triage and resolve security alerts in your organization or enterprise by regularly reviewing alert dismissal requests.
permissions: "Access requires:\n* Organization views: **write** access to repositories in the organization\n* Enterprise views: organization owners and security managers"
product: Organizations or enterprises with GitHub Secret Protection, GitHub Code Security, or GitHub Advanced Security
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /code-security/security-overview/review-alert-dismissal-requests
contentType: how-tos
category:
  - Secure at scale
---

## Prerequisites

To receive and manage alert dismissal requests, you need to enable delegated alert dismissal. For an introduction to delegated alert dismissal and enablement instructions for specific features, see:
* [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-code-scanning-alerts/enable-delegated-alert-dismissal)
* [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-secret-scanning-alerts/enable-delegated-dismissal){% ifversion dependabot-delegated-alert-dismissal %}
* [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-dependabot-alerts/enable-delegated-alert-dismissal){% endif %}

## Reviewing requests for an organization

1. On GitHub, navigate to the main page of the organization.
1. Under your organization name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. In the "Requests" section of the sidebar, click any of the following options to review alert dismissal requests for the relevant feature:
    * (icon: key) **Secret scanning alert dismissal**
    * (icon: codescan) **Code scanning alert dismissal**{% ifversion dependabot-delegated-alert-dismissal %}
    * (icon: dependabot) **Dependabot alert dismissal**{% endif %}
1. Optionally, to filter requests by source repository, reviewer, requester, timeframe, or status, use the dropdown menus at the top of the list of requests.
1. Click the request you want to review.
1. Read the contents of the alert, as well as the requester's reasoning for the dismissal request.
1. Next to the dismissal request in the alert timeline, click **Review request**.
1. Provide any comments for the requester in the text box, then select either **Deny request** or **Approve request**.
1. Click **Submit review**.

## Reviewing requests across your enterprise

> [!NOTE] To review an alert dismissal request at the enterprise level, you must be an organization owner or security manager for the source organization, or be granted the necessary permissions through a custom role.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. In the "Requests" section of the sidebar, click any of the following options to review alert dismissal requests for the relevant feature:
    * (icon: key) **Secret scanning alert dismissal**
    * (icon: codescan) **Code scanning alert dismissal**{% ifversion dependabot-delegated-alert-dismissal %}
    * (icon: dependabot) **Dependabot alert dismissal**{% endif %}
1. Optionally, to filter requests by source organization, reviewer, requester, timeframe, or status, use the dropdown menus at the top of the list of requests.
1. Click the request you want to review.
1. Read the contents of the alert, as well as the requester's reasoning for the dismissal request.
1. Next to the dismissal request in the alert timeline, click **Review request**.
1. Provide any comments for the requester in the text box, then select either **Deny request** or **Approve request**.
1. Click **Submit review**.
