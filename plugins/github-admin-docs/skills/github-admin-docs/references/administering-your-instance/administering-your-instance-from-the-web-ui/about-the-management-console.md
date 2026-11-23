---
title: About the Management Console
intro: 'From the Management Console, you can initialize, configure, and monitor {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.'
redirect_from:
  - /admin/configuration/administering-your-instance-from-the-management-console/about-the-management-console
versions:
  ghes: '*'
contentType: concepts
category:
  - Install and configure your instance
---

## About the Management Console

The Management Console allows you to manage the low-level configuration of {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. For example, you can complete initial setup, manage licensing and low-level settings, configure authentication, schedule maintenance windows, and monitor your instance.

You can always reach the Management Console using {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}'s IP address, even when the instance is in maintenance mode, or there is a critical application failure or hostname or SSL misconfiguration.

To access the Management Console, you can use the root site administrator password established during initial setup of {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} or log in as a Management Console user. For more information, see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-web-ui/accessing-the-management-console). You must also be able to connect to the virtual machine host on port 8443. If you're having trouble reaching the Management Console, please check intermediate firewall and security group configurations.

The Management Console password hash is stored in `/data/user/common/secrets.conf`. If high availability or clustering is configured, the file is automatically synced from the primary node to any additional nodes. Any change to the primary's password will automatically be replicated to all of the instance's nodes. For more information about high availability, see [AUTOTITLE](/admin/monitoring-and-managing-your-instance/configuring-high-availability/about-high-availability-configuration).

When someone performs an action in the Management Console via the web interface or REST API, an event appears in the audit log. For more information, see [AUTOTITLE](/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/audit-log-events-for-your-enterprise).

## Examples of activities in the Management Console

In the Management Console, you can perform administrative tasks for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, including:

* **Initial setup:** Walk through the initial setup process when first launching {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} by visiting {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}'s IP address in your browser.

* **Identity and access management:** Improve the security of {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} by creating dedicated user accounts for the Management Console. For more information, see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-web-ui/managing-access-to-the-management-console).

* **Configuring authentication policies for the Management Console:** Set rate limits for login attempts, and the lockout duration if someone exceeds the rate limit. For more information, see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-web-ui/managing-access-to-the-management-console#configuring-rate-limits-for-authentication-to-the-management-console).
* **Configuring basic settings for your instance:** Configure DNS, hostname, SSL, user authentication, email, monitoring services, and log forwarding on the Settings page.
* **Scheduling maintenance windows:** Take {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} offline while performing maintenance using the Management Console or administrative shell.
* **Troubleshooting:** Generate a support bundle or view high level diagnostic information.
* **License management:** View or update your GitHub Enterprise license.
