---
title: Accessing the Management Console
shortTitle: Access Management Console
intro: You can access the Management Console as the root site administrator or a Management Console user.
redirect_from:
  - /admin/configuration/administering-your-instance-from-the-management-console/accessing-the-management-console
versions:
  ghes: '*'
contentType: how-tos
category:
  - Install and configure your instance
---

## About access to the Management Console

From the Management Console, you can initialize, configure, and monitor {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. For more information, see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-web-ui/about-the-management-console).

You can access the Management Console as the root site administrator or a Management Console user. An administrator created the root site administrator password during the initial setup process for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.

## Accessing the Management Console

The first time that you access the Management Console for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, you must upload your license file. For more information, see [AUTOTITLE](/billing/how-tos/manage-server-licenses/download-your-license).

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. If you have created multiple Management Console user accounts, select **Root site admin** or **Management Console user**. For more information about Management Console user accounts see, [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-web-ui/managing-access-to-the-management-console).
1. Type your Management Console credentials. Then click **Continue**.
1. Click **Continue**.

## Accessing the Management Console as an unauthenticated user

1. Visit this URL in your browser, replacing `hostname` with your actual GitHub Enterprise Server hostname or IP address:

   ```shell
   http(s)://HOSTNAME/setup
   ```

1. If you have created multiple Management Console user accounts, select **Root site admin** or **Management Console user**. For more information about Management Console user accounts see, [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-web-ui/managing-access-to-the-management-console).
1. Type your Management Console credentials. Then click **Continue**.
1. Click **Continue**.
