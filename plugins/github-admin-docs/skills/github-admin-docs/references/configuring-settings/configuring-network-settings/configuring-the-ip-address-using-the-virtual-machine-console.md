---
title: Configuring the IP address using the virtual machine console
intro: By default, GitHub Enterprise Server retrieves network settings via the dynamic host configuration protocol (DHCP). If your platform supports it, or if DHCP is unavailable, you can also configure the network settings using the virtual machine console.
redirect_from:
  - /enterprise/admin/installation/configuring-the-ip-address-using-the-virtual-machine-console
  - /enterprise/admin/configuration/configuring-the-ip-address-using-the-virtual-machine-console
  - /admin/configuration/configuring-the-ip-address-using-the-virtual-machine-console
  - /admin/configuration/configuring-network-settings/configuring-the-ip-address-using-the-virtual-machine-console
versions:
  ghes: '*'
shortTitle: Set the IP using the console
contentType: how-tos
category:
  - Install and configure your instance
---

> [!NOTE]
> We do not support adding additional network adapters to GitHub Enterprise Server.

1. Using your virtualization platform tools, open the virtual machine console.
1. To start your network setup, press **S**.
1. Choose to configure the `IPv4` or `IPv6` protocol.
1. Configure options for the protocol you chose.
1. To finish configuring your settings, press **D**.
