---
title: Viewing and filtering alerts from secret scanning
intro: Learn how to find and filter {% ifversion fpt or ghec %}{% ifversion fpt or ghec %}secret scanning alerts for users{% else %}secret scanning{% endif %}{% else %}{% ifversion fpt or ghec %}secret scanning alerts for users{% else %}secret scanning{% endif %} alerts{% endif %} for your repository.
permissions: 'Repository owners, organization owners, security managers, and users with the **admin** role'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
contentType: how-tos
shortTitle: View alerts
allowTitleToDifferFromFilename: true
redirect_from:
  - /code-security/secret-scanning/managing-alerts-from-secret-scanning/viewing-alerts
category:
  - Protect your secrets
---

You can find and filter {% ifversion fpt or ghec %}secret scanning alerts for users{% else %}secret scanning{% endif %} through your repository's **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab. To learn more about alerts and the different types you may encounter, see [AUTOTITLE](/code-security/concepts/secret-security/about-alerts).

## Viewing alerts

Alerts for secret scanning are displayed under the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab of the repository.

1. On GitHub, navigate to the main page of the repository.
1. Under the repository name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab. If you cannot see the "(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" tab, select the **(icon: kebab-horizontal)** dropdown menu, and then click **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}**.
1. In the left sidebar, under "Vulnerability alerts", click **Secret scanning**.
1. Optionally, toggle to "Generic" to see alerts for generic patterns{% ifversion secret-scanning-ai-generic-secret-detection %} or secrets detected with AI{% endif %}.
1. Under "Secret scanning", click the alert you want to view.
   {% ifversion secret-scanning-user-owned-repos %}

   > [!NOTE]
   > Only people with admin permissions to the repository containing a leaked secret can view security alert details and token metadata for an alert. Enterprise owners can request temporary access to the repository for this purpose.

   {% endif %}
{% ifversion code-secret-alert-assignees %}

1. Optionally, assign the alert to someone to fix using the **Assignees** control shown on the right. See [Assigning alerts](/code-security/concepts/security-at-scale/about-security-campaigns#about-assigning-alerts).

{% endif %}

## Filtering alerts

You can apply various filters to the alerts list to help you find the alerts you're interested in. You can use the dropdown menus above the alerts list, or input the qualifiers listed in the table into the search bar.

|Qualifier|Description|
|---------|-----------|
|`bypassed`|Display alerts for secrets where push protection has been bypassed (`true`). For more information, see [AUTOTITLE](/code-security/concepts/secret-security/push-protection).|
|`is`|Display alerts that are open (`open`), closed (`closed`), found in a public repository (`publicly-leaked`), or found in more than one repository within the same organization or enterprise (`multi-repository`). |
|`props`|Display alerts for repositories with a specific custom property (`CUSTOM_PROPERTY_NAME`) set. For example, `props:data_sensitivity:high` display results for repositories with the `data_sensitivity` property set to the value `high`. |
|`provider`|Display alerts for a specific provider (`PROVIDER-NAME`), for example, `provider:github`. For a list of supported partners, see [AUTOTITLE](/code-security/reference/secret-security/supported-secret-scanning-patterns#supported-provider-patterns).|
|`repo`|Display alerts detected in a specified repository (`REPOSITORY-NAME`), for example: `repo:octo-repository`.|
|`resolution`|Display alerts closed as "false positive" (`false-positive`), "hidden by config" (`hidden-by-config`), "pattern deleted" (`pattern-deleted`), "pattern edited" (`pattern-edited`), "revoked" (`revoked`), "used in tests" (`used-in-tests`), or "won't fix" (`wont-fix`).|
|{% ifversion fpt or ghec %}|
|`results`|Display alerts for supported secrets and custom patterns (`default`), or for generic patterns (`generic`) such as private keys, and AI-detected generic secrets such as passwords. See [AUTOTITLE](/code-security/reference/secret-security/supported-secret-scanning-patterns#supported-provider-patterns), and for more information about AI-detected generic secrets, see [AUTOTITLE](/code-security/responsible-use/security-and-quality-ai-features).|
|{% elsif ghes %}|
|`results`|Display alerts for supported secrets and custom patterns (`default`), or generic patterns such as private keys (`generic`){% ifversion secret-scanning-ai-generic-secret-detection %}, and AI-detected generic secrets such as passwords{% endif %}. See [AUTOTITLE](/code-security/reference/secret-security/supported-secret-scanning-patterns#supported-provider-patterns).|
|{% endif %}|
|`secret-type`|Display alerts for a specific secret type (`SECRET-NAME`), for example, `secret-type:github_personal_access_token`. For a list of supported secret types, see [AUTOTITLE](/code-security/reference/secret-security/supported-secret-scanning-patterns#supported-provider-patterns).|
|`sort`|Display alerts from newest to oldest (`created-desc`), oldest to newest (`created-asc`), most recently updated (`updated-desc`), or least recently updated (`updated-asc`).|
|`team`|Display alerts owned by members of the specified team, for example: `team:octocat-dependabot-team`.|
|`topic`|Display alerts with the matching repository topic, for example: `topic:asdf`.|
|`validity`|Display alerts for secrets with a specific validity (`active`, `inactive`, or `unknown`). {% ifversion fpt or ghec %}Applies only to GitHub tokens unless you enable validity checks.{% endif %} For more information about validity statuses, see [AUTOTITLE](/code-security/tutorials/remediate-leaked-secrets/evaluating-alerts#checking-a-secrets-validity).|

## Next steps

* [AUTOTITLE](/code-security/tutorials/remediate-leaked-secrets/evaluating-alerts)
