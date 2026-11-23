---
title: Adding a collaborator to a repository security advisory
intro: Add other users or teams to collaborate on a security advisory with you.
permissions: 'Repository owners, organization owners, security managers, and users with the **admin** role'
redirect_from:
  - /articles/adding-a-collaborator-to-a-maintainer-security-advisory
  - /github/managing-security-vulnerabilities/adding-a-collaborator-to-a-maintainer-security-advisory
  - /github/managing-security-vulnerabilities/adding-a-collaborator-to-a-security-advisory
  - /code-security/security-advisories/adding-a-collaborator-to-a-security-advisory
  - /code-security/repository-security-advisories/adding-a-collaborator-to-a-repository-security-advisory
  - /code-security/security-advisories/repository-security-advisories/adding-a-collaborator-to-a-repository-security-advisory
  - /code-security/security-advisories/working-with-repository-security-advisories/adding-a-collaborator-to-a-repository-security-advisory
  - /code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/adding-a-collaborator-to-a-repository-security-advisory
versions:
  fpt: '*'
  ghec: '*'
contentType: how-tos
shortTitle: Add collaborators
category:
  - Report and disclose vulnerabilities
---

This article applies to repository-level security advisories in a public repository. To edit a global advisory in the GitHub Advisory Database, see [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/edit-advisory-database).

Collaborators have write permissions to the security advisory. For more information, see [AUTOTITLE](/code-security/reference/permissions/repository-security-advisory).

> [!NOTE]
> If you remove a user from a repository or organization, and the user is also a collaborator on a security advisory, GitHub will automatically remove the user as a collaborator for the security advisory. This prevents any unauthorized access from ex-collaborators. For more information about removing a collaborator on a security advisory, see [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/remove-collaborators).

1. On GitHub, navigate to the main page of the repository.
1. Under the repository name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab. If you cannot see the "(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" tab, select the **(icon: kebab-horizontal)** dropdown menu, and then click **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}**.
1. In the left sidebar, under "Reporting", click **(icon: shield) Advisories**.
1. In the "Security Advisories" list, click the security advisory you'd like to add a collaborator to.
1. On the right side of the page, under "Collaborators", type the name of the user or team you'd like to add to the security advisory.
1. Click **(icon: plus)** to add the selected user or team as a collaborator.
   ![Screenshot of the "Collaborators" area in the sidebar of a draft security advisory. The "Add collaborator" button, a plus icon, is outlined in orange.](/assets/images/help/security/security-advisory-add-collaborator-button.png)

## Further reading

* [AUTOTITLE](/code-security/tutorials/fix-reported-vulnerabilities/collaborate-in-a-fork)
