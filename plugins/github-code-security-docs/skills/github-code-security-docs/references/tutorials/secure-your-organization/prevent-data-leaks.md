---
title: Best practices for preventing data leaks in your organization
intro: Learn guidance and recommendations to help you avoid private or sensitive data present in your organization from being exposed.
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
shortTitle: Prevent data leaks
redirect_from:
  - /code-security/getting-started/best-practices-for-preventing-data-leaks-in-your-organization
  - /code-security/tutorials/secure-your-organization/best-practices-for-preventing-data-leaks-in-your-organization
contentType: tutorials
category:
  - Plan your security strategy
---

## About this guide

As an organization owner, preventing exposure of private or sensitive data should be a top priority. Whether intentional or accidental, data leaks can cause substantial risk to the parties involved. While GitHub takes measures to help protect you against data leaks, you are also responsible for administering your organization to harden security.

There are several key components when it comes to defending against data leaks:

* Taking a proactive approach towards prevention
* Early detection of possible leaks
* Maintaining a mitigation plan when an incident occurs

The best approach will depend on the type of organization you're managing. For example, an organization that focuses on open source development might require looser controls than a fully commercial organization, to allow for external collaboration. This article provide high level guidance on the GitHub features and settings to consider, which you should implement according to your needs.

## Secure accounts

Protect your organization's repositories and settings by implementing security best practices, including enabling 2FA and requiring it for all members, and establishing strong password guidelines.

{% ifversion ghec %}- Enabling secure authentication processes by using SAML and SCIM integrations, as well as 2FA authentication whenever possible. For more information, see [AUTOTITLE](/organizations/managing-saml-single-sign-on-for-your-organization/about-identity-and-access-management-with-saml-single-sign-on), [AUTOTITLE](/organizations/managing-saml-single-sign-on-for-your-organization/about-scim-for-organizations), and [AUTOTITLE](/authentication/securing-your-account-with-two-factor-authentication-2fa). {% endif %}

* Requiring organization members, outside collaborators, and billing managers to enable 2FA for their personal accounts, making it harder for malicious actors to access an organization's repositories and settings.{% ifversion ghec %} This is one step further from enabling secure authentication.{% endif %} For more information, see [AUTOTITLE](/organizations/keeping-your-organization-secure/managing-two-factor-authentication-for-your-organization/requiring-two-factor-authentication-in-your-organization).

* Encouraging your users to create strong passwords and secure them appropriately, by following GitHub’s recommended password guidelines. For more information, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/creating-a-strong-password).{% ifversion secret-scanning-push-protection-for-users %}

* Encouraging your users to keep push protection for users enabled in their personal account settings, so that no matter which public repository they push to, they are protected. For more information, see [AUTOTITLE](/code-security/how-tos/secure-your-secrets/prevent-future-leaks/manage-user-push-protection).{% endif %}

* Establishing an internal security policy in GitHub, so users know the appropriate steps to take and who to contact if an incident is suspected. For more information, see [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/add-security-policy).

For more detailed information about securing accounts, see [AUTOTITLE](/code-security/tutorials/implement-supply-chain-best-practices/securing-accounts).

## Prevent data leaks

As an organization owner, you should limit and review access as appropriate for the type of your organization. Consider the following settings for tighter control:

Recommendation | More information
------------------ | -----------------
Disable the ability to fork repositories. | [AUTOTITLE](/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-forking-policy-for-your-repository)
Disable changing repository visibility. | [AUTOTITLE](/organizations/managing-organization-settings/restricting-repository-visibility-changes-in-your-organization)
Restrict repository creation to private or internal. |  [AUTOTITLE](/organizations/managing-organization-settings/restricting-repository-creation-in-your-organization)
Disable repository deletion and transfer. | [AUTOTITLE](/organizations/managing-organization-settings/setting-permissions-for-deleting-or-transferring-repositories)
| {% ifversion deploy-keys-enterprise-org-policy %} |
Disable the ability to use deploy keys. | [AUTOTITLE](/organizations/managing-organization-settings/restricting-deploy-keys-in-your-organization)
| {% endif %} |
Scope personal access tokens to the minimum permissions necessary. | None
Secure your code by converting public repositories to private whenever appropriate. You can alert the repository owners of this change automatically using a GitHub App. | [Prevent-Public-Repos](https://github.com/apps/prevent-public-repos) in GitHub Marketplace
Confirm your organization’s identity by verifying your domain and restricting email notifications to only verified email domains. | [AUTOTITLE](/organizations/managing-organization-settings/verifying-or-approving-a-domain-for-your-organization){% ifversion ghec or ghes %} and [AUTOTITLE](/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/restricting-email-notifications-for-your-organization){% endif %}{% ifversion fpt or ghec %}
Ensure your organization has upgraded to the GitHub Customer Agreement instead of using the Standard Terms of Service. | [AUTOTITLE](/organizations/managing-organization-settings/upgrading-to-the-github-customer-agreement){% endif %}
Prevent contributors from making accidental commits. | [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository#avoiding-accidental-commits-in-the-future)

## Detect data leaks

No matter how well you tighten your organization to prevent data leaks, some may still occur, and you can respond by using secret scanning, the audit log, and branch protection rules.

### Use secret scanning

Secret scanning helps secure code and keep secrets safe across organizations and repositories by scanning and detecting secrets that were accidentally committed over the full Git history of every branch in GitHub repositories. Any strings that match patterns {% ifversion fpt or ghec %}provided by secret scanning partners, by other service providers, or {% endif %}defined by you or your organization, are reported as alerts in the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab of repositories.

{% ifversion fpt or ghec %}
There are two forms of secret scanning available: **Secret scanning alerts for partners** and **{% ifversion fpt or ghec %}Secret scanning alerts for users{% else %}Secret scanning{% endif %}**.

* Secret scanning alerts for partners: These are enabled by default and automatically run on all public repositories and public npm packages.
* {% ifversion fpt or ghec %}Secret scanning alerts for users{% else %}Secret scanning{% endif %}: To get additional scanning capabilities for your organization, you need to enable {% ifversion fpt or ghec %}secret scanning alerts for users{% else %}secret scanning{% endif %}.

  When enabled, {% ifversion fpt or ghec %}secret scanning alerts for users{% else %}secret scanning{% endif %} can be detected on the following types of repository:{% ifversion fpt %}
  * Public repositories owned by personal accounts on GitHub.com
  * Public repositories owned by organizations
  * Private and internal repositories owned by organizations using GitHub Team or GitHub Enterprise Cloud, with a license for GitHub Code Security{% elsif ghec %}
  * Public repositories owned by organizations that use GitHub Enterprise Cloud
  * Private and internal repositories when you have a license for GitHub Code Security{% endif %}
{% endif %}

> [!TIP]
> Regardless of the enablement status of secret scanning and push protection, organizations on GitHub Team and GitHub Enterprise can run a free report to scan the code in the organization for leaked secrets. See [AUTOTITLE](/code-security/concepts/secret-security/secret-security-with-github).

{% ifversion ghes %}Your site administrator must enable secret scanning for your instance before you can use this feature. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configure-secret-scanning).{% endif %}

For more information about secret scanning, see [AUTOTITLE](/code-security/concepts/secret-security/secret-scanning).

You can also enable secret scanning as a push protection for a repository or an organization. When you enable this feature, secret scanning prevents contributors from pushing code with a detected secret. For more information, see [AUTOTITLE](/code-security/concepts/secret-security/push-protection). Finally, you can also extend the detection to include custom secret string structures. For more information, see [AUTOTITLE](/code-security/how-tos/secure-your-secrets/customize-leak-detection/define-custom-patterns).

### Review the audit log for your organization

You can also proactively secure IP and maintain compliance for your organization by leveraging your organization's audit log, along with the GraphQL Audit Log API. For more information, see [AUTOTITLE](/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization) and [AUTOTITLE](/graphql/reference/enterprise-admin#interface-auditentry).

### Set up branch protection rules

To ensure that all code is properly reviewed prior to being merged into the default branch, you can enable branch protection. By setting branch protection rules, you can enforce certain workflows or requirements before a contributor can push changes. For more information, see [AUTOTITLE](/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

As an alternative to branch protection rules, you can create rulesets. Rulesets have a few advantages over branch protection rules, such as statuses, and better discoverability without requiring admin access. You can also apply multiple rulesets at the same time. For more information, see [AUTOTITLE](/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).

## Mitigate data leaks

If a user pushes sensitive data, ask them to remove it by using the `git filter-repo` tool. For more information, see [AUTOTITLE](/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository). Also, if the sensitive data has not been pushed yet, you can just undo those changes locally; for more information, see [the GitHub Blog](https://github.blog/2015-06-08-how-to-undo-almost-anything-with-git/) (but note that `git revert` is not a valid way to undo the addition of sensitive data as it leaves the original sensitive commit in Git history).

If you're unable to coordinate directly with the repository owner to remove data that you're confident you own, you can fill out a DMCA takedown notice form and tell GitHub Support.  Make sure to include the problematic commit hashes.  For more information, see [DMCA takedown notice](https://support.github.com/contact/dmca-takedown).

> [!NOTE]
> If one of your repositories has been taken down due to a false claim, you should fill out a DMCA
counter notice form and alert GitHub Support. For more information, see [DMCA counter notice](https://support.github.com/contact/dmca-counter-notice).

{% ifversion ghec or fpt %}

### Revoke exposed tokens

If credentials have been exposed in a GitHub repository, GitHub secret scanning can be used to report and revoke the credentials. For more information, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-secret-scanning-alerts/resolving-alerts#reporting-a-leaked-secret-in-a-private-repository).

You can also revoke exposed credentials that you do not own and have been exposed outside of GitHub repositories. By doing this, you are contributing to the overall security of the GitHub community and can quickly limit the impact of these credentials. The API supports revoking:

* Personal access tokens (classic) with the `ghp_` prefix
* Fine-grained personal access tokens with the `github_pat_` prefix
* OAuth app tokens with the `gho_` prefix
* GitHub App user-to-server tokens with the `ghu_` prefix
* GitHub App refresh tokens with the `ghr_` prefix

If you find any exposed tokens either on GitHub or elsewhere, you can submit a revocation request using the REST API. See [AUTOTITLE](/rest/credentials/revoke#revoke-a-list-of-credentials) for the complete and authoritative list of supported credential types.

{% endif %}

## Next steps

* [AUTOTITLE](/code-security/tutorials/implement-supply-chain-best-practices/securing-code)
* [AUTOTITLE](/code-security/tutorials/implement-supply-chain-best-practices/securing-builds)
