---
title: Enabling automatic update checks
intro: You can enable automatic update checks so that {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} checks for and downloads the latest GitHub Enterprise Server release.
redirect_from:
  - /enterprise/admin/installation/enabling-automatic-update-checks
  - /enterprise/admin/enterprise-management/enabling-automatic-update-checks
  - /admin/enterprise-management/enabling-automatic-update-checks
  - /admin/enterprise-management/updating-the-virtual-machine-and-physical-resources/enabling-automatic-update-checks
  - /admin/monitoring-managing-and-updating-your-instance/updating-the-virtual-machine-and-physical-resources/enabling-automatic-update-checks
  - /admin/monitoring-and-managing-your-instance/updating-the-virtual-machine-and-physical-resources/enabling-automatic-update-checks
versions:
  ghes: '*'
shortTitle: Enable automatic update checks
contentType: how-tos
category:
  - Back up and upgrade your instance
---

## About automatic update checks

When an upgrade package is automatically downloaded for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, you'll receive a message letting you know you can upgrade GitHub Enterprise Server. Packages download to the `/var/lib/ghe-updates` directory on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. For more information about the recommendations and requirements for upgrades, see [AUTOTITLE](/admin/upgrading-your-instance/preparing-to-upgrade/overview-of-the-upgrade-process).

If a hotpatch is available for an upgrade, the `.hpkg` will download automatically. In the management console you can choose to install the hotpatch immediately or schedule installation for a later time. For more information, see [AUTOTITLE](/admin/upgrading-your-instance/performing-an-upgrade/upgrading-with-a-hotpatch).

## Enabling automatic update checks

> [!TIP]
> To enable automatic update checks, {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} must be able to connect to `https://github-enterprise.s3.amazonaws.com`.

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. In the top navigation bar, click **Updates**.

   ![Screenshot of the header of the Management Console. A tab, labeled "Updates", is highlighted with an orange outline.](/assets/images/enterprise/management-console/updates-tab.png)
1. Click **Yes, automatically check for updates**.
1. Under the "Settings" sidebar, click **Save settings**.

   > [!NOTE]
   > Saving settings in the Management Console restarts system services, which could result in user-visible downtime.

1. Wait for the configuration run to complete.

## Viewing whether an update is available

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. In the top navigation bar, click **Updates**.

   ![Screenshot of the header of the Management Console. A tab, labeled "Updates", is highlighted with an orange outline.](/assets/images/enterprise/management-console/updates-tab.png)
1. At the top of the page, view whether your instance is up-to-date, or whether an update is available.

## Viewing the status of the most recent update check

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. In the top navigation bar, click **Updates**.

   ![Screenshot of the header of the Management Console. A tab, labeled "Updates", is highlighted with an orange outline.](/assets/images/enterprise/management-console/updates-tab.png)
1. Under "Logs," view status of the most recent update check.
