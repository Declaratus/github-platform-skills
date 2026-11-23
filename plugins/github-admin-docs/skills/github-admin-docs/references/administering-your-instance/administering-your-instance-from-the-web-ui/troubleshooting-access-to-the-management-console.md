---
title: Troubleshooting access to the Management Console
shortTitle: Troubleshoot Management Console
intro: You can troubleshoot access problems for the Management Console.
redirect_from:
  - /admin/configuration/administering-your-instance-from-the-management-console/troubleshooting-access-to-the-management-console
versions:
  ghes: '*'
contentType: how-tos
category:
  - Install and configure your instance
---

## About problems with Management Console access

If you experience problems accessing the Management Console, you can try the following troubleshooting steps.

## Unlocking the Management Console after failed login attempts

The Management Console locks after the number of failed login attempts configured by your authentication policies. For more information, see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-web-ui/managing-access-to-the-management-console#configuring-rate-limits-for-authentication-to-the-management-console).

### Unlocking the root site administrator account

If the root site administrator's Management Console login is locked, someone with administrative SSH access must unlock the login. To immediately unlock access to the Management Console by the root site administrator, use the `ghe-reactivate-admin-login` command via the administrative shell. For more information, see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-command-line/command-line-utilities#ghe-reactivate-admin-login) and [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-command-line/accessing-the-administrative-shell-ssh).

If you forgot the root site administrator's password to access the Management Console, you can set a new password with the `ghe-set-password` command via the administrative shell. For more information, see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-command-line/command-line-utilities#ghe-set-password) and [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-command-line/accessing-the-administrative-shell-ssh).

### Unlocking a Management Console user account

The root site administrator can unlock access to the Management Console for other user accounts.

1. Sign into the Management Console as the root site administrator. For more information, see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-web-ui/accessing-the-management-console).
1. In the top navigation bar, click **User Management**.
1. Locked user accounts will appear as "State: blocked". To unblock the user and allow authentication, to the right of the user's details, click (icon: law).

## Troubleshooting failed connections to the Management Console

If you cannot connect to the Management Console on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, you can review the following information to troubleshoot the problem.

### Error: "Your session has expired" for connections through a load balancer

If you access {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} through a load balancer and connections to the Management Console fail with a message that your session has expired, you may need to reconfigure your load balancer. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-network-settings/using-github-enterprise-server-with-a-load-balancer#error-your-session-has-expired-for-connections-to-the-management-console).
