---
title: Managing requests to bypass push protection
intro: As a member of the bypass list for an organization or repository, you can review bypass requests from other members of the organization or repository.
permissions: "* Organization owners\n* Security managers\n* Users in teams, default roles, or custom roles that have been added to the bypass list.\n* Users who are assigned a custom role with the \"review and manage secret scanning bypass requests\" fine-grained permission."
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
contentType: how-tos
shortTitle: Manage bypass requests
redirect_from:
  - /code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/managing-requests-to-bypass-push-protection
  - /code-security/how-tos/secure-your-secrets/manage-bypass-requests/managing-requests-to-bypass-push-protection
category:
  - Protect your secrets
---

When delegated bypass for push protection is enabled, designated reviewers can approve or deny requests from contributors who want to push commits containing secrets.

This article explains how to review and manage bypass requests for repositories and organizations.

For more information about how bypass requests work, see [AUTOTITLE](/code-security/concepts/secret-security/bypass-requests).

## Managing requests for a repository

1. On GitHub, navigate to the main page of the repository.
1. Under the repository name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab. If you cannot see the "(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" tab, select the **(icon: kebab-horizontal)** dropdown menu, and then click **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}**.
1. In the left sidebar, under "Requests," click **Push protection bypass**.
1. Select the **All statuses** dropdown menu, then click **Open** to view requests that are awaiting review, and those that have been approved but for which the commits haven't been pushed to the repository yet.
1. Click the request that you want to review.
1. Review the details of the request.
1. Optionally, add a review comment. The comment will be added to the review request timeline and the secret scanning alert timeline. For example, you may wish to explain the reason for the approval or denial of the request for auditing and reporting reasons, and suggest next steps for the contributor to take.

1. To allow the contributor to push the commit containing the secret, click **Approve bypass request**. Or, to require the contributor to remove the secret from the commit, click **Deny bypass request**.

## Managing requests for an organization

Organization owners, security managers and organization members with the relevant fine-grained permission (via a custom role) can review and manage bypass requests for all repositories in the organization using security overview. See [AUTOTITLE](/code-security/how-tos/secure-your-secrets/manage-bypass-requests/review-bypass-requests).

## Filtering requests

You can filter requests by:

* Approver (member of the bypass list)
* Requester (contributor making the request)
* Timeframe
* Status

### Filtering by status

The following statuses are assigned to a request:

|Status|Description|
|---------|-----------|
|`Cancelled`| The request has been canceled by the contributor.|
|`Completed`|The request has been approved and the commit(s) have been pushed to the repository.|
|`Denied`|The request has been reviewed and denied.|
|`Expired`| The request has expired. Requests are valid for 7 days. |
|`Open`| The request has either not yet been reviewed, or has been approved but the commit(s) have not been pushed to the repository.  |

## Further reading

* [AUTOTITLE](/code-security/concepts/secret-security/delegated-bypass)
* [AUTOTITLE](/code-security/how-tos/secure-your-secrets/manage-bypass-requests/enable-delegated-bypass)
* [AUTOTITLE](/code-security/how-tos/secure-your-secrets/manage-bypass-requests/review-bypass-requests)
