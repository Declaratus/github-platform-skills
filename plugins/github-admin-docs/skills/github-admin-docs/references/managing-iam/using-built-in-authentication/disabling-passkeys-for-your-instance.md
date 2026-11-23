---
title: Disabling passkeys for your instance
intro: Learn how to disable passkeys for all users on your instance.
permissions: Site administrators
versions:
  ghes: '*'
shortTitle: Disable passkeys
contentType: how-tos
category:
  - Configure authentication
---

Passkeys are enabled by default.

1. From an administrative account on GitHub Enterprise Server, in the upper-right corner of any page, click (icon: rocket).
1. If you're not already on the "Site admin" page, in the upper-left corner, click **Site admin**.
1. In the "(icon: rocket) Site admin" sidebar, click **Management Console**.
1. In the "Settings" sidebar, click **Authentication**.
1. In the "Passkeys" section, deselect **Enable passkeys**.
1. Under the "Settings" sidebar, click **Save settings**.

   > [!NOTE]
   > Saving settings in the Management Console restarts system services, which could result in user-visible downtime.

1. Wait for the configuration run to complete.

## Further reading

* [AUTOTITLE](/authentication/authenticating-with-a-passkey/about-passkeys)
