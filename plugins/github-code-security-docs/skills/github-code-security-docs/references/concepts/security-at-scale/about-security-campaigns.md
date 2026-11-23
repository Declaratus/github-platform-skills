---
title: About security campaigns
shortTitle: Security campaigns
intro: You can fix security alerts at scale by creating security campaigns and collaborating with developers to burn down your security backlog.
product: "{% ifversion fpt %}\nOrganizations on GitHub Team with [GitHub Secret Protection or GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{% ifversion ghec %}\nOrganizations on GitHub Team or GitHub Enterprise Cloud with [GitHub Secret Protection or GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{% ifversion ghes %}\nOrganizations with [{% ifversion security-campaigns %}GitHub Code Security{% elsif security-campaigns-secrets %}GitHub Secret Protection or GitHub Code Security{% endif %}](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}"
allowTitleToDifferFromFilename: true
audience:
  - driver
contentType: concepts
versions:
  feature: security-campaigns
redirect_from:
  - /code-security/securing-your-organization/fixing-security-alerts-at-scale/about-security-campaigns
category:
  - Secure at scale
---

Once you have identified security alerts the next step is to identify the most urgent alerts and get them fixed. Security campaigns are a way to group alerts and share them with developers, so you can collaborate to remediate vulnerabilities in the code{% ifversion security-campaigns-secrets %} and any exposed secrets{% endif %}.

## Security campaigns in your day-to-day work

You can use security campaigns to support many of your aims as a security leader.

* Improving the security posture of the company by leading work to remediate alerts.
* Reinforcing security training for developers by creating a campaign of related, code scanning alerts to fix collaboratively.{% ifversion security-campaigns-secrets %}
* Ensuring that secret scanning alerts are resolved within your remediation target.{% endif %}
* Building collaborative relationships between the security team and developers to promote shared ownership of security alerts.
* Providing clarity to developers on the most urgent alerts to fix and monitoring alert remediation.

## Benefits of using security campaigns

A security campaign has many benefits over other ways of encouraging developers to remediate security alerts. In particular,

* Developers are notified about any security campaigns that they can contribute to.
* Developers can see the alerts you've highlighted for remediation without leaving their normal workflows.
* Each campaign has a named point of contact for questions, reviews, and collaboration.  {% ifversion security-campaigns-autofix %}
* For code scanning alerts, GitHub Copilot Autofix is automatically triggered to suggest a resolution. {% endif %}
{%- ifversion code-secret-alert-assignees %}
* You can assign both code scanning and secret scanning alerts in a campaign to users with write access.{% ifversion copilot %} If agentic autofix is enabled, you can also assign code scanning alerts to Copilot to automatically generate a pull request with fixes.{% endif %}
{%- endif %}

You can use one of the templates to select a group of closely related alerts for a campaign. This allows developers to build on the knowledge gained by resolving one alert and use it to fix several more, providing them with an incentive to fix multiple alerts.

In addition, you can use the REST API to create and interact with campaigns more efficiently and at scale. For more information, see [AUTOTITLE](/rest/campaigns/campaigns).

{% ifversion security-campaigns-secrets %}

## Differences between code and secret campaigns

{% ifversion security-campaigns-secrets %}

> [!NOTE]
> Campaigns for secret scanning alerts are currently in public preview and are subject to change.

{% endif %}

The creation workflow is the same for all campaigns, but you will notice a few differences in progress tracking and developer experience.

{% rowheaders %}

| Property | Code | Secret |
|--|--|--|
| Alerts available for inclusion | (icon: check) Default branch only | (icon: check)
| Repository tracking issues | (icon: check) | (icon: x) |
| Developer notifications | (icon: check) Requires write access to repository | (icon: check) Requires view access to alerts list |
| {% ifversion code-secret-alert-assignees %} |
| Alert assignment | (icon: check) | (icon: check) May raise permissions |
| {% endif %} |
| Automatic remediation support | (icon: check) GitHub Copilot Autofix | (icon: x) |

{% endrowheaders %}

{% endif %}

{% ifversion code-secret-alert-assignees %}

## About assigning alerts

{% ifversion code-secret-alert-assignees-ga %}{% elsif ghes = 3.20 %}

>[!NOTE]
> The option to assign code scanning and secret scanning alerts is currently in public preview and is subject to change.

{% endif %}

You can assign a code scanning or secret scanning alert to any user who has **write** access for the repository.

If the assignee for a secret scanning alert **cannot view the alert list**, their permissions are temporarily raised for that alert. Any additional permissions are revoked when they are unassigned from the alert.

{% ifversion code-secret-alert-assignees-ga %}

GitHub notifies users:

* When they are assigned to an alert
* When that alert is dismissed

For code scanning, you can also perform some of these operations programmatically using the REST API, such as assigning or unassigning users to alerts, and filtering alerts by assignee. For more information, see [AUTOTITLE](/rest/code-scanning/code-scanning) in the REST API documentation. Additionally, webhooks are available to notify you when an alert is assigned or an assignment is removed.

{% endif %}

{% ifversion security-campaigns-assign-to-cca %}

If agentic autofix is enabled for a repository, you can select up to 25 code scanning alerts in a security campaign and assign them to Copilot. One assignment starts one agent session and creates one pull request for the selected alerts. See [AUTOTITLE](/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/fixing-alerts-in-security-campaign#assigning-alerts-to-copilot).

{% endif %}

{% endif %}

## Next steps

* [AUTOTITLE](/code-security/tutorials/secure-your-organization/best-practice-fix-alerts-at-scale)
* [AUTOTITLE](/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/creating-managing-security-campaigns)
