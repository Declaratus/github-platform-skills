---
title: Configuring applications
intro: You can configure internal application settings for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.
redirect_from:
  - /enterprise/admin/installation/configuring-applications
  - /enterprise/admin/configuration/configuring-applications
  - /admin/configuration/configuring-applications
  - /admin/configuration/configuring-your-enterprise/configuring-applications
  - /admin/configuration/configuring-user-applications-for-your-enterprise/configuring-applications
versions:
  ghes: '*'
contentType: how-tos
category:
  - Enable GitHub features for your enterprise
---
## Adjusting image caching

You can choose the amount of time that {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} caches avatars. When you increase the cache time, you increase the amount of time a user's avatar will take to load. Configuring the cache time with too low a value can overload {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} work processes.

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. In the "Settings" sidebar, click **Applications**.
1. Under "Avatar image cache time (seconds)", type the number of seconds that you would like {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to cache avatar images.
1. Under the "Settings" sidebar, click **Save settings**.

   > [!NOTE]
   > Saving settings in the Management Console restarts system services, which could result in user-visible downtime.

1. Wait for the configuration run to complete.

## Enabling retention policy for checks

You can enable a retention policy for checks, actions, and associated data by setting thresholds for archival and deletion. For more information about configuring actions, see [AUTOTITLE](/admin/managing-github-actions-for-your-enterprise/getting-started-with-github-actions-for-your-enterprise/about-github-actions-for-enterprises).

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. In the "Settings" sidebar, click **Checks**.
1. Select **Enable archiving of Checks-related data**.
1. Under "Archive threshold (days)", type the number of days for the archival threshold. Checks older than this number of days will be archived before being permanently deleted.
1. Under "Delete threshold (days)", type the number of days for the deletion threshold. An archived check exists in an archived state for the number of days specified here. After this threshold, the check will be permanently deleted.
1. Under the "Settings" sidebar, click **Save settings**.

   > [!NOTE]
   > Saving settings in the Management Console restarts system services, which could result in user-visible downtime.

1. Wait for the configuration run to complete.
