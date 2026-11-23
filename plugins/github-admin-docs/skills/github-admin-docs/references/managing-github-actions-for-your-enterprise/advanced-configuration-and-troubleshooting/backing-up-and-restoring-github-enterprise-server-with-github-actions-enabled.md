---
title: Backing up and restoring GitHub Enterprise Server with GitHub Actions enabled
shortTitle: Backing up and restoring
intro: To restore a backup of {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} when GitHub Actions is enabled, you must configure GitHub Actions before restoring the backup with GitHub Enterprise Server Backup Utilities.
versions:
  ghes: '*'
redirect_from:
  - /admin/github-actions/backing-up-and-restoring-github-enterprise-server-with-github-actions-enabled
  - /admin/github-actions/advanced-configuration-and-troubleshooting/backing-up-and-restoring-github-enterprise-server-with-github-actions-enabled
contentType: how-tos
category:
  - Enable GitHub features for your enterprise
---

## About backups of GitHub Enterprise Server when using GitHub Actions

You can use GitHub Enterprise Server Backup Utilities to back up and restore the data and configuration for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to a new instance. For more information, see [AUTOTITLE](/admin/backing-up-and-restoring-your-instance/configuring-backups-on-your-instance).

However, not all the data for GitHub Actions is included in these backups. GitHub Actions uses external storage to store workflow artifacts and logs. This data is stored on your external provider, such as Azure blob storage, Amazon S3, Google Cloud Storage, or MinIO. As a result, GitHub Enterprise Server backups and GitHub Enterprise Server high availability configurations do not provide protection for the data stored on this external storage, and instead rely on the data protection and replication provided by the external storage provider, such as Azure, Google Cloud, or AWS.

## Restoring a backup of GitHub Enterprise Server when GitHub Actions is enabled

To restore a backup of {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} with GitHub Actions, you must manually configure network settings and external storage on the destination instance before you restore your backup from GitHub Enterprise Server Backup Utilities.

1. Create a new instance with the "New Install" option. For installation instructions for the virtualization platform of your choice, see [AUTOTITLE](/admin/installing-your-enterprise-server/setting-up-a-github-enterprise-server-instance).
1. In the Management Console, configure network settings and external storage for GitHub Actions on the destination instance. See [AUTOTITLE](/admin/configuring-settings).
1. After GitHub Actions is configured and enabled, to restore the rest of the data from the backup, use the `ghe-restore` command. For more information, see [AUTOTITLE](/admin/backing-up-and-restoring-your-instance/configuring-backups-on-your-instance#restoring-a-backup).
1. Re-register your self-hosted runners on the destination instance. For more information, see [AUTOTITLE](/actions/how-tos/manage-runners/self-hosted-runners/add-runners).
1. To ensure that the bundled actions that are pre-installed on your new instance are up to date, enter the following command.

   ```shell copy
   ghe-config --unset 'app.actions.actions-repos-sha1sum'
   ```

   1. To apply the configuration, run the following command.
   
      > [!NOTE]
      > During a configuration run, services on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} may restart, which can cause brief downtime for users.
   
       ```shell copy
       ghe-config-apply
       ```
   
   1. Wait for the configuration run to complete.
