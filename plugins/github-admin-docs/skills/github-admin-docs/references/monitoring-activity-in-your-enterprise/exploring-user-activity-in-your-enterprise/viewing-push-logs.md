---
title: Viewing push logs
intro: Site administrators can view a list of Git push operations for any repository on the enterprise.
redirect_from:
  - /enterprise/admin/articles/viewing-push-logs
  - /enterprise/admin/installation/viewing-push-logs
  - /enterprise/admin/user-management/viewing-push-logs
  - /admin/user-management/viewing-push-logs
  - /admin/user-management/monitoring-activity-in-your-enterprise/viewing-push-logs
  - /admin/monitoring-activity-in-your-enterprise/exploring-user-activity/viewing-push-logs
versions:
  ghes: '*'
contentType: how-tos
category:
  - Monitor and audit your enterprise
---
Push log entries show:

* Who initiated the push
* Whether it was a force push or not
* The branch someone pushed to
* The protocol used to push
* The originating IP address
* The Git client used to push
* The SHA hashes from before and after the operation

If you want to see a detailed history of changes to a repository, you can use the activity view. The activity view displays all pushes, merges, force pushes, and branch changes, and associates these changes with commits and authenticated users.
For more information, see [AUTOTITLE](/repositories/viewing-activity-and-data-for-your-repository/using-the-activity-view-to-see-changes-to-a-repository).

## Viewing a repository's push logs

1. Sign into GitHub Enterprise Server as a site administrator.
1. Navigate to a repository.
1. In the upper-right corner of the repository's page, click (icon: rocket).
1. In the upper-right corner of the page, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. In the left sidebar, click **Push Log**.

## Viewing a repository's push logs on the command-line

1. SSH into {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. If your instance comprises multiple nodes, for example if high availability or geo-replication are configured, SSH into the primary node. If you use a cluster, you can SSH into any node. Replace HOSTNAME with the hostname for your instance, or the hostname or IP address of a node. For more information, see [AUTOTITLE]({% ifversion not ghes %}/enterprise-server@latest{% endif %}/admin/administering-your-instance/administering-your-instance-from-the-command-line/accessing-the-administrative-shell-ssh).

   ```shell copy
   ssh -p 122 admin@HOSTNAME
   ```
1. In the appropriate Git repository, open the audit log file:

   ```shell
   ghe-spokesctl ssh --primary OWNER/REPOSITORY -- cat audit_log
   ```
