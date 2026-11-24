---
title: Repository security advisories
shortTitle: Repository security advisory
intro: The actions you can take in a repository security advisory depend on whether you have admin or write permissions to the security advisory.
allowTitleToDifferFromFilename: true
redirect_from:
  - /code-security/reference/permissions/permission-levels-for-repository-security-advisories
  - /articles/permission-levels-for-maintainer-security-advisories
  - /github/managing-security-vulnerabilities/permission-levels-for-maintainer-security-advisories
  - /github/managing-security-vulnerabilities/permission-levels-for-security-advisories
  - /code-security/security-advisories/permission-levels-for-security-advisories
  - /code-security/repository-security-advisories/permission-levels-for-repository-security-advisories
  - /code-security/security-advisories/repository-security-advisories/permission-levels-for-repository-security-advisories
  - /code-security/security-advisories/working-with-repository-security-advisories/permission-levels-for-repository-security-advisories
  - /code-security/reference/permission-levels-for-repository-security-advisories
  - /code-security/reference/permissions/security-advisory-permissions
versions:
  fpt: '*'
  ghec: '*'
contentType: reference
category:
  - Report and disclose vulnerabilities
---

## Permissions overview

Repository owners, organization owners, security managers, and users with the **admin** role can:
   * Create a security advisory for the repository.
   * Access all security advisories for the repository.
   * Add collaborators to the security advisory.

Collaborators have **write** permissions to the security advisory.

Action | Write permissions | Admin permissions |
------ | ----------------- | ----------------- |
See a draft security advisory | (icon: check)  | (icon: check)  |
Add collaborators to the security advisory (see [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/add-collaborators)) | (icon: x) | (icon: check)  |
Edit and delete any comments in the security advisory | (icon: check)  | (icon: check)  |
Create a temporary private fork in the security advisory (see [AUTOTITLE](/code-security/tutorials/fix-reported-vulnerabilities/collaborate-in-a-fork)) | (icon: x) | (icon: check)  |
Add changes to a temporary private fork in the security advisory (see [AUTOTITLE](/code-security/tutorials/fix-reported-vulnerabilities/collaborate-in-a-fork)) | (icon: check)  | (icon: check)  |
Create pull requests in a temporary private fork (see [AUTOTITLE](/code-security/tutorials/fix-reported-vulnerabilities/collaborate-in-a-fork)) | (icon: check)  | (icon: check)  |
Merge changes in the security advisory (see [AUTOTITLE](/code-security/tutorials/fix-reported-vulnerabilities/collaborate-in-a-fork)) | (icon: x) | (icon: check)  |
Add and edit metadata in the security advisory (see [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/publish-repository-advisory)) | (icon: check)  | (icon: check)  |
Add and remove credits for a security advisory (see [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/edit-repository-advisories)) | (icon: check)  | (icon: check)  |
Close the draft security advisory | (icon: x) | (icon: check)  |
Publish the security advisory (see [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/publish-repository-advisory)) | (icon: x) | (icon: check)  |

Collaborators with write permissions can't create a temporary private fork, with one exception: the reporter of a privately reported vulnerability can create one while they remain a collaborator on the security advisory. See [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/report-privately).

Repository security advisory collaborators without write access to the repository cannot create or view confidential comments. This restriction includes the reporter of a privately reported vulnerability unless they also have write access. See [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/manage-vulnerability-reports#discussing-a-report-with-people-who-have-write-access).

{% ifversion ghec %}

### Permissions from custom repository roles

Organizations that use custom repository roles can let people work on repository security advisories without making them repository administrators or security managers. Add one or more of these permissions to a custom repository role. See [AUTOTITLE](/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/about-custom-repository-roles).

* **View security advisories**: view draft security advisories, their status, and comments, but not confidential comments or the advisory's event history.
* **Create, edit, and manage security advisories**: everything in "View security advisories", plus create and edit security advisories, comment, manage collaborators, and create a temporary private fork.
* **Accept private vulnerability reports and close or reopen security advisories**: requires one of the permissions above.
* **Publish security advisories and request CVEs**: requires one of the permissions above.

Action | View | Create, edit, and manage | Accept, close, or reopen | Publish and request CVEs |
------ | ---- | ------------------------ | ------------------------ | ------------------------ |
See draft security advisories | (icon: check) | (icon: check) | (icon: x) | (icon: x) |
Create and edit security advisories, comment, and manage collaborators | (icon: x) | (icon: check) | (icon: x) | (icon: x) |
Create a temporary private fork | (icon: x) | (icon: check) | (icon: x) | (icon: x) |
Accept a private vulnerability report, or close or reopen a security advisory | (icon: x) | (icon: x) | (icon: check)¹ | (icon: x) |
Publish a security advisory or request a CVE | (icon: x) | (icon: x) | (icon: x) | (icon: check)¹ |
Merge changes from a temporary private fork | (icon: x) | (icon: x) | (icon: x) | (icon: x)² |

¹ Only together with "View security advisories" or "Create, edit, and manage security advisories". Without one of them, these permissions grant no access.

² Merging changes from a temporary private fork still requires a repository administrator or security manager, even if a custom role includes all of these permissions.

When someone with "Create, edit, and manage security advisories" creates a temporary private fork, they are added as a collaborator on the security advisory so they can work in the fork. They remain a collaborator until they are removed, even if the custom role changes. Other people need to be added as collaborators to create pull requests in the fork.

People with these permissions can't delete a temporary private fork. Confidential comments are only available to people with "Create, edit, and manage security advisories" who also have write access to the repository.

People with "View security advisories" or "Create, edit, and manage security advisories" who watch the repository are notified about new draft security advisories and private vulnerability reports.

{% endif %}

### Permission differences for global security advisories

Unlike repository security advisories, anyone can contribute to **global security advisories** in the GitHub Advisory Database at [github.com/advisories](https://github.com/advisories). Edits to global advisories will not change or affect how the advisory appears on the repository. See [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/edit-advisory-database).

## Further reading

* [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/add-collaborators)
* [AUTOTITLE](/code-security/tutorials/fix-reported-vulnerabilities/collaborate-in-a-fork)
* [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/remove-collaborators)
* [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/delete-repository-advisories)
