---
title: Setting up a trial of GitHub Enterprise Server
intro: 'You can try GitHub Enterprise Server for free.'
redirect_from:
  - /articles/requesting-a-trial-of-github-enterprise
  - /articles/setting-up-a-trial-of-github-enterprise-server
  - /github/getting-started-with-github/setting-up-a-trial-of-github-enterprise-server
  - /github/getting-started-with-github/signing-up-for-github/setting-up-a-trial-of-github-enterprise-server
  - /get-started/signing-up-for-github/setting-up-a-trial-of-github-enterprise-server
versions:
  ghec: '*'
  ghes: '*'
shortTitle: Enterprise Server trial
category:
  - Get started with GitHub Enterprise
---

## About trials of GitHub Enterprise Server

You can request a 45-day trial to evaluate GitHub Enterprise Server. Your trial will be installed as a virtual appliance, with options for on-premises or cloud deployment. For more information about GitHub Enterprise Server, and for a list of supported virtualization platforms, see [AUTOTITLE](/enterprise-server@latest/admin/overview/about-github-enterprise-server).

{% ifversion ghes %}Dependabot{% else %}Security{% endif %} alerts and GitHub Connect are not currently available in trials of GitHub Enterprise Server. For a demonstration of these features, contact [GitHub's Sales team](https://github.com/enterprise/contact). For more information about these features, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-alerts) and [AUTOTITLE](/enterprise-server@latest/admin/configuring-settings/configuring-github-connect/enabling-github-connect-for-githubcom).

Trials are also available for GitHub Enterprise Cloud. For more information, see [AUTOTITLE](/enterprise-cloud@latest/admin/overview/setting-up-a-trial-of-github-enterprise-cloud).

If you're not sure whether GitHub Enterprise Cloud, GitHub Enterprise Server, or both are best for your organization, contact [GitHub's Sales team](https://github.com/enterprise/contact). If your organization has 11 or fewer developers, consider GitHub Team; organizations with 12 or more developers typically benefit the most from GitHub Enterprise. For more information, see [AUTOTITLE](/get-started/learning-about-github/githubs-plans).

## Setting up your trial of GitHub Enterprise Server

GitHub Enterprise Server is installed as a virtual appliance. Determine the best person in your organization to set up a virtual machine, and ask that person to submit a [trial request](https://enterprise.github.com/trial). You can begin your trial immediately after submitting a request.

To set up an account for the GitHub Enterprise Web portal, click the link in the email you received after submitting your trial request, and follow the prompts. Then, download your license file. For more information, see [AUTOTITLE](/enterprise-server@latest/billing/how-tos/manage-server-licenses/download-your-license).

To install GitHub Enterprise Server, download the necessary components and upload your license file. For more information, see the instructions for your chosen virtualization platform in [AUTOTITLE](/enterprise-server@latest/admin/installing-your-enterprise-server/setting-up-a-github-enterprise-server-instance).

## Next steps

To get the most out of your trial, follow these steps:

1. [Create an organization](/enterprise-server@latest/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch).
1. To learn the basics of using GitHub, see:
   * [Intro to GitHub](https://resources.github.com/devops/methodology/maximizing-devops-roi/) webcast
   * [Understanding the GitHub flow](https://guides.github.com/introduction/flow/) in GitHub Guides
   * [Hello World](https://guides.github.com/activities/hello-world/) in GitHub Guides
   * [AUTOTITLE](/get-started/using-github-docs/about-versions-of-github-docs)
1. To configure your instance to meet your organization's needs, see [AUTOTITLE](/enterprise-server@latest/admin/configuring-settings).
1. To integrate GitHub Enterprise Server with your identity provider, see [AUTOTITLE](/enterprise-server@latest/admin/managing-iam/using-saml-for-enterprise-iam) and [AUTOTITLE](/enterprise-server@latest/admin/managing-iam/using-ldap-for-enterprise-iam/using-ldap).
1. Invite people to join your trial.
   * Add users to your GitHub Enterprise Server instance using built-in authentication or your configured identity provider. For more information, see [AUTOTITLE](/enterprise-server@latest/admin/managing-iam/using-built-in-authentication/configuring-built-in-authentication).
   * To invite people to become account administrators, visit the [GitHub Enterprise Web portal](https://enterprise.github.com/login).

     > [!NOTE]
     > People you invite to become account administrators will receive an email with a link to accept your invitation.

To learn how your enterprise can use GitHub most effectively, see [AUTOTITLE](/admin/concepts/enterprise-best-practices/organize-work).

For information on planned features and products, see the [GitHub public roadmap](https://github.com/github/roadmap#github-public-roadmap).

## Finishing your trial

You can upgrade to full licenses in the [GitHub Enterprise Web portal](https://enterprise.github.com/login) at any time during the trial period.

If you haven't upgraded by the last day of your trial, you'll receive an email notifying you that your trial had ended. If you need more time to evaluate GitHub Enterprise, contact [GitHub's Sales team](https://github.com/enterprise/contact) to request an extension.

## Further reading

* [AUTOTITLE](/enterprise-cloud@latest/admin/overview/setting-up-a-trial-of-github-enterprise-cloud)
