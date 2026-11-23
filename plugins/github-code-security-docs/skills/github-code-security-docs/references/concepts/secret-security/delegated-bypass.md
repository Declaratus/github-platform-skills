---
title: Delegated bypass for push protection
intro: Maintain your secret security while unblocking trusted actors with delegated bypass for push protection.
product: "Delegated bypass for push protection is available for the following repository types:\n\n{% ifversion fpt %}\n* Organization-owned repositories on GitHub Team with [GitHub Secret Protection](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{% ifversion ghec %}\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Secret Protection](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}\n\n{% ifversion ghes %}\n* Organization-owned repositories with [GitHub Secret Protection](/get-started/learning-about-github/about-github-advanced-security) enabled{% endif %}"
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
shortTitle: Delegated bypass
redirect_from:
  - /code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection
  - /code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection
  - /code-security/concepts/secret-security/about-delegated-bypass-for-push-protection
contentType: concepts
category:
  - Protect your secrets
---

## About delegated bypass for push protection

With delegated bypass for push protection, you can:

* **Grant bypass permissions** to select individuals, roles, and teams, allowing them to push commits that are initially blocked by push protection.{% ifversion push-protection-org-enterprise-exemptions %}
* **Grant exemptions** to select actors, skipping push protection entirely for all of their commits. Exemptions should be granted to trusted automation like migration bots or service accounts that need to push frequent commits with minimal friction.{% endif %}
* **Introduce a review cycle** for bypass requests from all other contributors. Requests expire after 7 days.

Delegated bypass applies to files created, edited, and uploaded on GitHub.

## Users with bypass privileges

The following types of users can always bypass push protection:
* Organization owners
* Security managers
* Users in teams, default roles, or custom roles that have been added to the bypass list
* Users who are assigned (either directly or via a team) a custom role with the "review and manage secret scanning bypass requests" fine-grained permission

## Next steps

To start managing bypass privileges, see [AUTOTITLE](/code-security/how-tos/secure-your-secrets/manage-bypass-requests/enable-delegated-bypass).
