---
title: Managing access to the Management Console
shortTitle: Manage Management Console access
intro: You can increase the security of {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} by creating or deleting Management Console users. As the root site administrator, you can access the Management Console as well as configure Management Console authentication rate limits.
redirect_from:
  - /admin/configuration/administering-your-instance-from-the-management-console/managing-access-to-the-management-console
versions:
  ghes: '*'
contentType: how-tos
category:
  - Install and configure your instance
---

## About access to the Management Console

From the Management Console, you can initialize, configure, and monitor {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. For more information, see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-web-ui/about-the-management-console).

You can access the Management Console as the root site administrator or a Management Console user. An administrator created the root site administrator password during the initial setup process for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. For more information about Management Console access, see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-web-ui).

You can also use the `gh es` GitHub CLI extension to manage the root site administrator password, which controls access to the Management Console. For more information, see the [GH ES CLI usage documentation](https://github.com/github/gh-es/blob/main/USAGE.md#gh-es-access-set-password) and [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-command-line/administering-your-instance-using-the-github-cli).


## Root site administrator

The root site administrator account authenticates with a password established during the initial setup of {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.
The root site administrator password should be used for initial setup and recovery only, along with creating the first Management Console user account. Day-to-day administration should be performed with named Management Console accounts for proper attribution.

## Management Console user

Management Console users can perform all administrative tasks for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} including the creation or deletion of Management Console user accounts.

These users, sometimes called operators, can also add SSH keys to the Management Console to grant administrative access to the instance via SSH.

## Creating or deleting a user account for the Management Console

While signed into the Management Console, you can create new Management Console user accounts.

1. In the top navigation bar, click **User Management**.
1. Click **Create user**.
1. Fill in the user's name, username, and email address.
1. To finish creating the user account, click **Create**. If email notifications are configured for the instance, the user will automatically receive an invitation email with access instructions for the Management Console. For more information, see [Inviting new Management Console users](#inviting-new-management-console-users).
1. Optionally, to delete a Management Console user account, click (icon: trash) to the right of any user account you wish to delete. Then confirm deletion.

## Inviting new Management Console users

If you have configured email for notifications for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, new Management Console users will automatically receive an invitation to complete creation of the Management Console user account. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-user-applications-for-your-enterprise/configuring-email-for-notifications).

If you have not configured email notifications for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, you must manually copy the Management Console invitation link and send it to the user. The user must set a password using the link before the user can access the Management Console.

1. In the top navigation bar, click **User Management**.
1. To copy the invitation link, click (icon: link) on any Management Console user account.
1. Send the invitation link to the Management Console user. The invitation link will lead the user through the final account setup steps.

## Configuring rate limits for authentication to the Management Console

You can configure the lockout time and login attempt limits for the Management Console.

After you configure rate limits and a Management Console user exceeds the limit, the Management Console will remain locked for the duration set by the lockout time. If the root site administrator's Management Console login is locked, someone with administrative SSH access must unlock the login. To immediately unlock access to the Management Console by the root site administrator, use the `ghe-reactivate-admin-login` command via the administrative shell. For more information, see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-command-line/command-line-utilities#ghe-reactivate-admin-login) and [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-command-line/accessing-the-administrative-shell-ssh).
                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                     If you forgot the root site administrator's password to access the Management Console, you can set a new password with the `ghe-set-password` command via the administrative shell. For more information, see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-command-line/command-line-utilities#ghe-set-password) and [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-command-line/accessing-the-administrative-shell-ssh).

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. Optionally, under "Lockout time for Management Console users", type a number of minutes to lock the Management Console after too many failed login attempts. When locked out, the root site administrator must be manually unlocked.
1. Optionally, under "Login attempt limit for all users", type a maximum number of failed login attempts to allow before the Management Console is locked.
1. Under the "Settings" sidebar, click **Save settings**.

   > [!NOTE]
   > Saving settings in the Management Console restarts system services, which could result in user-visible downtime.

1. Wait for the configuration run to complete.
