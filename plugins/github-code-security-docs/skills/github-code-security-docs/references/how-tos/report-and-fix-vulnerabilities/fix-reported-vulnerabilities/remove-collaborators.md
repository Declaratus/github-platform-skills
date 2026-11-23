---
title: Removing a collaborator from a repository security advisory
intro: When you remove a collaborator from a repository security advisory, they lose read and write access to the security advisory's discussion and metadata.
permissions: 'Repository owners, organization owners, security managers, and users with the **admin** role'
redirect_from:
  - /github/managing-security-vulnerabilities/removing-a-collaborator-from-a-security-advisory
  - /code-security/security-advisories/removing-a-collaborator-from-a-security-advisory
  - /code-security/repository-security-advisories/removing-a-collaborator-from-a-repository-security-advisory
  - /code-security/security-advisories/repository-security-advisories/removing-a-collaborator-from-a-repository-security-advisory
  - /code-security/security-advisories/working-with-repository-security-advisories/removing-a-collaborator-from-a-repository-security-advisory
  - /code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/removing-a-collaborator-from-a-repository-security-advisory
versions:
  fpt: '*'
  ghec: '*'
contentType: how-tos
shortTitle: Remove collaborators
category:
  - Report and disclose vulnerabilities
---

> [!NOTE]
> This article applies to repository-level security advisories in a public repository.
> To edit a global advisory in the GitHub Advisory Database, see [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/edit-advisory-database).

## Removing a collaborator from a security advisory

If you remove a user from a repository or organization, and the user is also a collaborator on a security advisory, GitHub will automatically remove the user as a collaborator for the security advisory. This prevents any unauthorized access from ex-collaborators.

1. On GitHub, navigate to the main page of the repository.
1. Under the repository name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab. If you cannot see the "(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" tab, select the **(icon: kebab-horizontal)** dropdown menu, and then click **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}**.
1. In the left sidebar, under "Reporting", click **(icon: shield) Advisories**.
1. In the "Security Advisories" list, click the name of the security advisory you'd like to remove a collaborator from.
1. On the right side of the page, under "Collaborators", find the name of the user or team you'd like to remove from the security advisory.
1. Next to the collaborator you want to remove, click **Remove**.

   ![Screenshot of the "Collaborators" area in the right sidebar of a draft security advisory. The "Remove username" button is outlined in dark orange.](/assets/images/help/security/security-advisory-remove-collaborator.png)

## Further reading

* [AUTOTITLE](/code-security/reference/permissions/repository-security-advisory)
* [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/add-collaborators)
