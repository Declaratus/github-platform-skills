---
title: Editing security advisories in the GitHub Advisory Database
intro: Improve advisories published in the GitHub Advisory Database by making community contributions.
permissions: '**Anyone** can suggest improvements to the GitHub Advisory Database.'
redirect_from:
  - /code-security/security-advisories/editing-security-advisories-in-the-github-advisory-database
  - /code-security/supply-chain-security/managing-vulnerabilities-in-your-projects-dependencies/editing-security-advisories-in-the-github-advisory-database
  - /code-security/dependabot/dependabot-alerts/editing-security-advisories-in-the-github-advisory-database
  - /code-security/security-advisories/global-security-advisories/editing-security-advisories-in-the-github-advisory-database
  - /code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/editing-security-advisories-in-the-github-advisory-database
  - /code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/editing-security-advisories-in-the-github-advisory-database
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
contentType: how-tos
shortTitle: Edit Advisory Database
category:
  - Report and disclose vulnerabilities
---

{% ifversion ghes %}

## Editing advisories in the GitHub Advisory Database

{% endif %}

1. Navigate to [https://github.com/advisories](https://github.com/advisories?ref_product=security-advisories&ref_type=engagement&ref_style=text).
1. Select the security advisory you would like to contribute to.
1. On the right-hand side of the page, click the **Suggest improvements for this vulnerability** link.
1. In the "Improve security advisory" form, make the desired improvements. You can edit or add any detail.{% ifversion fpt or ghec %} For information about correctly specifying information on the form, including affected versions, see [AUTOTITLE](/code-security/tutorials/fix-reported-vulnerabilities/write-security-advisories).{% endif %}
1. Under **Reason for change**, explain why you want to make this improvement. If you include links to supporting material this will help our reviewers.
1. When you finish editing the advisory, click **Submit improvements**.
1. Once you submit your community contribution, a pull request containing your changes will be created for review in [github/advisory-database](https://github.com/github/advisory-database) by the GitHub Security Lab curation team. If the advisory originated from a GitHub repository, we will also tag the original publisher for optional commentary. You can view the pull request and get notifications when it is updated or closed.

You can also open a pull request directly on an advisory file in the [github/advisory-database](https://github.com/github/advisory-database) repository. For more information, see the [contribution guidelines](https://github.com/github/advisory-database/blob/main/CONTRIBUTING.md).

{% ifversion ghes %}

## Editing advisories from GitHub Enterprise Server

If you have GitHub Connect enabled on your instance, you will be able to see advisories by adding `/advisories` to the instance url.

1. Navigate to `https://HOSTNAME/advisories`.
1. Select the security advisory you would like to contribute to.
1. On the right-hand side of the page, click the **Suggest improvements for this vulnerability on GitHub.** link. A new tab opens with the same security advisory on GitHub.
1. Edit the advisory, following steps four through six in [Editing advisories in the GitHub Advisory Database](#editing-advisories-in-the-github-advisory-database) above.
{% endif %}
