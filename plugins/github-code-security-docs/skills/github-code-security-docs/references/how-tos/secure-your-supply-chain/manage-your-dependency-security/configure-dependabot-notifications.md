---
title: Configuring notifications for Dependabot alerts
shortTitle: Configure Dependabot notifications
intro: Optimize how you receive notifications about Dependabot alerts.
redirect_from:
  - /github/managing-security-vulnerabilities/configuring-notifications-for-vulnerable-dependencies
  - /code-security/supply-chain-security/configuring-notifications-for-vulnerable-dependencies
  - /code-security/supply-chain-security/managing-vulnerabilities-in-your-projects-dependencies/configuring-notifications-for-vulnerable-dependencies
  - /code-security/dependabot/dependabot-alerts/configuring-notifications-for-dependabot-alerts
  - /code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/configuring-notifications-for-dependabot-alerts
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
contentType: how-tos
category:
  - Secure your dependencies
---

By default, GitHub sends notifications about new alerts by email to people with write, maintain, or admin permissions to a repository. See [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-alerts#how-alert-notifications-work).

## Configuring notifications for Dependabot alerts

You can configure notification settings for yourself or your organization from the Manage notifications drop-down (icon: bell) shown at the top of each page. For more information, see [AUTOTITLE](/subscriptions-and-notifications/get-started/configuring-notifications#choosing-your-notification-settings).

You can choose to receive notifications:

* In your inbox, as web notifications. A web notification is sent when Dependabot is enabled for a repository, when a new manifest file is committed to the repository, and when a new vulnerability with a critical or high severity is found (**On GitHub** option).
* By email. An email is sent when Dependabot is enabled for a repository, when a new manifest file is committed to the repository, and when a new vulnerability with a critical or high severity is found (**Email** option).
* On the command line. Warnings are displayed as callbacks when you push to repositories with any insecure dependencies (**CLI** option).
* On GitHub Mobile, as web notifications. For more information, see [AUTOTITLE](/subscriptions-and-notifications/get-started/configuring-notifications#managing-your-notification-settings-with-github-mobile).

> [!NOTE]
> The email and web/GitHub Mobile notifications are:
>
> * _Per repository_ when Dependabot is enabled on the repository, or when a new manifest file is committed to the repository.
> * _Per organization_ when a new vulnerability is discovered.
> * Sent when a new vulnerability is discovered. GitHub doesn't send notifications when vulnerabilities are updated.

{% ifversion update-notification-settings-22 %}
You can customize the way you are notified about Dependabot alerts. For example, you can receive a daily or weekly digest email summarizing alerts for up to 10 of your repositories using the **Email weekly digest** option.
{% else %}
You can customize the way you are notified about Dependabot alerts. For example, you can receive a weekly digest email summarizing alerts for up to 10 of your repositories using the **Email a digest summary of vulnerabilities** and **Weekly security email digest** options.{% endif %}

{% ifversion update-notification-settings-22 %}
![Screenshot of the notification options for Dependabot alerts. A dropdown menu with frequency options is outlined in orange.](/assets/images/help/dependabot/dependabot-notification-frequency.png){% endif %}{% ifversion ghes %}
![Screenshot of the notification options for Dependabot alerts.](/assets/images/help/enterprises/dependabot-alerts-options-no-ui.png){% endif %}

> [!NOTE]
> You can filter your notifications on GitHub to show Dependabot alerts. For more information, see [AUTOTITLE](/subscriptions-and-notifications/reference/inbox-filters#dependabot-custom-filters).

Email notifications for Dependabot alerts that affect one or more repositories include the `X-GitHub-Severity` header field. You can use the value of the `X-GitHub-Severity` header field to filter email notifications for Dependabot alerts. For more information, see [AUTOTITLE](/subscriptions-and-notifications/reference/email-notification-headers).

## Further reading

* [AUTOTITLE](/subscriptions-and-notifications/get-started/configuring-notifications)
* [AUTOTITLE](/subscriptions-and-notifications/reference/inbox-filters#supported-is-queries)
