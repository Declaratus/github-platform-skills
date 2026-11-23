---
title: Reviewing requests to bypass push protection
shortTitle: Review bypass requests
intro: Approve or deny requests from contributors who need to push commits containing secrets to your organization's repositories.
permissions: "Access requires:\n* Organization views: **write** access to repositories in the organization\n* Enterprise views: organization owners and security managers"
product: "{% ifversion fpt %}\nOrganizations owned by a GitHub Team account with GitHub Secret Protection, or owned by a GitHub Enterprise account\n{% endif %}"
contentType: how-tos
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /code-security/security-overview/reviewing-requests-to-bypass-push-protection
  - /code-security/how-tos/secure-your-secrets/manage-bypass-requests/reviewing-requests-to-bypass-push-protection
category:
  - Secure at scale
---

## Prerequisites

Before you can review bypass requests, delegated bypass must be enabled for your organization or repositories. See [AUTOTITLE](/code-security/how-tos/secure-your-secrets/manage-bypass-requests/enable-delegated-bypass).

You can review and manage these requests in security overview.

## Reviewing bypass requests for an organization

1. On GitHub, navigate to the main page of the organization.
1. Under your organization name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. In the sidebar, under "Requests", click **(icon: key) Push protection bypass**.
1. Select the **All statuses** dropdown menu, then click **Open** to view requests that are awaiting review, or that have been approved but for which the commits haven't been pushed to the repository yet.
1. Click the request that you want to review.
1. Review the details of the request.
1. Optionally, add a review comment. The comment will be added to the review request timeline and the secret scanning alert timeline. For example, you may wish to explain the reason for the approval or denial of the request for auditing and reporting reasons, and suggest next steps for the contributor to take.

1. To allow the contributor to push the commit containing the secret, click **Approve bypass request**. Or, to require the contributor to remove the secret from the commit, click **Deny bypass request**.

## Filtering requests

You can filter requests by repository, approver (member who has reviewed the request), requester (contributor making the request), timeframe, and status.

### Filtering by status

The following statuses are assigned to a request:

|Status|Description|
|---------|-----------|
|`Approved`|The request has been approved, but the commit(s) have not yet been pushed to the repository.|
|`Cancelled`|The request has been cancelled by the contributor.|
|`Completed`|The request has been approved and the commit(s) have been pushed to the repository, or the request was rejected.|
|`Denied`|The request has been reviewed and denied.|
|`Expired`|The request has expired. Requests are valid for 7 days.|
|`Open`|The request has not yet been reviewed.|

## Further reading

* [AUTOTITLE](/code-security/concepts/secret-security/delegated-bypass)
* [AUTOTITLE](/code-security/how-tos/secure-your-secrets/manage-bypass-requests/enable-delegated-bypass)
