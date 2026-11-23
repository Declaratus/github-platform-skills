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

### Permission differences for global security advisories

Unlike repository security advisories, anyone can contribute to **global security advisories** in the GitHub Advisory Database at [github.com/advisories](https://github.com/advisories). Edits to global advisories will not change or affect how the advisory appears on the repository. See [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/edit-advisory-database).

## Further reading

* [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/add-collaborators)
* [AUTOTITLE](/code-security/tutorials/fix-reported-vulnerabilities/collaborate-in-a-fork)
* [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/remove-collaborators)
* [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/delete-repository-advisories)
