---
title: Managing GitHub Mobile for your enterprise
intro: You can decide whether people can use GitHub Mobile to connect to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.
permissions: Enterprise owners
versions:
  ghes: '*'
redirect_from:
  - /admin/configuration/configuring-your-enterprise/managing-github-for-mobile-for-your-enterprise
  - /admin/configuration/managing-github-for-mobile-for-your-enterprise
  - /admin/configuration/configuring-your-enterprise/managing-github-mobile-for-your-enterprise
  - /admin/configuration/configuring-user-applications-for-your-enterprise/managing-github-mobile-for-your-enterprise
shortTitle: Manage GitHub Mobile
contentType: how-tos
category:
  - Enable GitHub features for your enterprise
---

## About GitHub Mobile

GitHub Mobile allows people to triage, collaborate, and manage work on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} from a mobile device after successful authentication. GitHub Mobile is available as an Android and iOS app. For more information, see [AUTOTITLE](/get-started/using-github/github-mobile).

You can allow or disallow people from using GitHub Mobile to authenticate to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} and access your instance's data. By default, GitHub Mobile is enabled for people who use {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.

## Enabling or disabling GitHub Mobile

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. If you have created multiple Management Console user accounts, select **Root site admin** or **Management Console user**. For more information about Management Console user accounts see, [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-web-ui/managing-access-to-the-management-console).
1. Type your Management Console credentials. Then click **Continue**.
1. In the "Settings" sidebar, click **Mobile**.
1. Under "GitHub Mobile", select or deselect **Enable GitHub Mobile Apps**.
1. Under the "Settings" sidebar, click **Save settings**.

   > [!NOTE]
   > Saving settings in the Management Console restarts system services, which could result in user-visible downtime.

1. Wait for the configuration run to complete.
