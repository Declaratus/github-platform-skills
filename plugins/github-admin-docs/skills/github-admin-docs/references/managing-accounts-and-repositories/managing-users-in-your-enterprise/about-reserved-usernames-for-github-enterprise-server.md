---
title: About reserved usernames for GitHub Enterprise Server
shortTitle: Reserved usernames
intro: Certain words are reserved for internal use and cannot be used as usernames.
permissions: Enterprise owners
versions:
  ghes: '*'
contentType: reference
category:
  - Manage accounts and repositories
---

## About reserved usernames

GitHub Enterprise Server reserves certain usernames for internal use. You cannot assign reserved usernames to users or organizations on your instance. For example, the following words are reserved:

* `admin`
* `enterprise`
* `login`
* `staff`
* `support`

## Viewing reserved username

You can view a full list of reserved usernames for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}.

1. In the upper-right corner of any page, click (icon: rocket).
1. In the left sidebar, click **Reserved logins**.
