---
title: About secret scanning alerts
intro: Learn about the different types of secret scanning alerts.
permissions: 'Repository owners, organization owners, security managers, and users with the **admin** role'
product: "Secret scanning is available for the following repository types:\n\n* **Public repositories**: Secret scanning runs automatically for free.\n* **Organization-owned private and internal repositories**: Available with [GitHub Secret Protection](/get-started/learning-about-github/about-github-advanced-security) enabled on GitHub Team or GitHub Enterprise Cloud.\n* **User-owned repositories**: Available on GitHub Enterprise Cloud with Enterprise Managed Users. Available on GitHub Enterprise Server when the enterprise has [GitHub Secret Protection](/get-started/learning-about-github/about-github-advanced-security) enabled."
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
shortTitle: Secret scanning alerts
allowTitleToDifferFromFilename: true
redirect_from:
  - /code-security/secret-scanning/managing-alerts-from-secret-scanning/about-alerts
contentType: concepts
---

## About types of alerts

There are {% ifversion fpt or ghec %}three{% else %}two{% endif %} types of secret scanning alerts:

* **{% ifversion fpt or ghec %}User alerts{% else %}Secret scanning alerts{% endif %}:** Reported to users in the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab of the repository, when a supported secret is detected in the repository.
* **Push protection alerts:** Reported to users in the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab of the repository, when a contributor bypasses push protection. {% ifversion fpt or ghec %}
* **Partner alerts:** Reported directly to secret providers that are part of secret scanning's partner program. These alerts are not reported in the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab of the repository.{% endif %}

## About {% ifversion fpt or ghec %}user alerts {% else %}secret scanning alerts{% endif %}

When you enable secret scanning for a repository or push commits to a repository with secret scanning enabled, GitHub scans the contents for secrets that match patterns defined by service providers{% ifversion ghes or ghec %} and any custom patterns defined in your enterprise, organization, or repository{% endif %}.

When secret scanning detects a secret, GitHub generates an alert. GitHub displays an alert in the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab of the repository. If the same secret appears multiple times within a single file, only one alert is created.

To help you triage alerts more effectively, GitHub separates alerts into two lists:

* **Default** alerts
* **Generic** alerts

### Default alerts list

The default alerts list displays alerts that relate to supported patterns and specified custom patterns. This is the main view for alerts.

### Generic alerts list

The generic alerts list displays alerts that relate to generic secrets detected with patterns and deterministic methods (such as private keys){% ifversion secret-scanning-ai-generic-secret-detection %}, as well as secrets detected with AI (such as passwords){% endif %}. These types of alerts can have a higher rate of false positives or secrets used in tests. You can toggle to the generic alerts list from the default alerts list.

GitHub will continue to release new patterns and secret types to the generic alerts list.

In addition, alerts that fall into this category:
* Are limited in quantity to 5000 alerts per repository (this includes open and closed alerts).
* Are not shown in the summary views for security overview, only in the "Secret scanning" view.
* Only have the first five detected locations shown on GitHub for generic patterns{% ifversion secret-scanning-ai-generic-secret-detection %}, and only the first detected location shown for AI-detected secrets{% endif %}.{% ifversion secret-scanning-ai-generic-secret-detection %}
* Can appear after a delay for existing secrets, because enabling AI-detected secrets for a repository queues a historical scan of existing code.{% endif %}

For GitHub to scan for generic patterns{% ifversion secret-scanning-ai-generic-secret-detection %} and AI-detected secrets{% endif %}, you must first enable the feature{% ifversion secret-scanning-ai-generic-secret-detection %}s{% endif %} for your repository or organization. For more information, see [AUTOTITLE](/code-security/how-tos/secure-your-secrets/detect-secret-leaks/enabling-secret-scanning-for-generic-patterns){% ifversion secret-scanning-ai-generic-secret-detection %} and [AUTOTITLE](/code-security/how-tos/secure-your-secrets/detect-secret-leaks/enabling-secret-scanning-for-ai-detected-secrets){% endif %}.

If access to a resource requires paired credentials, then secret scanning will create an alert only when both parts of the pair are detected in the same file. This ensures that the most critical leaks are not hidden behind information about partial leaks. Pair matching also helps reduce false positives since both elements of a pair must be used together to access the provider's resource.

## About push protection alerts

Push protection scans pushes for supported secrets. If push protection detects a supported secret, it will block the push. When a contributor bypasses push protection to push a secret to the repository, a push protection alert is generated and displayed in the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab of the repository. To see all push protection alerts for a repository, you must filter by `bypassed: true` on the alerts page. For more information, see [AUTOTITLE](/code-security/how-tos/manage-security-alerts/manage-secret-scanning-alerts/viewing-alerts#filtering-alerts).

If access to a resource requires paired credentials, then secret scanning will create an alert only when both parts of the pair are detected in the same file. This ensures that the most critical leaks are not hidden behind information about partial leaks. Pair matching also helps reduce false positives since both elements of a pair must be used together to access the provider's resource.

> [!NOTE]
> {% ifversion secret-scanning-push-protection-for-users %}You can also enable push protection for your personal account, called "push protection for users", which prevents you from accidentally pushing supported secrets to _any_ public repository. Alerts are _not_ created if you choose to bypass your user-based push protection only. Alerts are only created if the repository itself has push protection enabled. For more information, see [AUTOTITLE](/code-security/how-tos/secure-your-secrets/prevent-future-leaks/manage-user-push-protection).{% endif %}
>
> Older versions of certain tokens may not be supported by push protection as these tokens may generate a higher number of false positives than their most recent version. Push protection may also not apply to legacy tokens. For tokens such as Azure Storage Keys, GitHub only supports _recently created_ tokens, not tokens that match the legacy patterns. For more information about push protection limitations, see [AUTOTITLE](/code-security/reference/secret-security/secret-scanning-scope).

{% ifversion fpt or ghec %}

## About partner alerts

When GitHub detects a leaked secret in a public repository or npm package, an alert is sent directly to the secret provider, if they are part of GitHub's secret scanning partner program. For more information about secret scanning alerts for partners, see [AUTOTITLE](/code-security/tutorials/secret-scanning-partner-program) and [AUTOTITLE](/code-security/reference/secret-security/supported-secret-scanning-patterns).

Partner alerts are not sent to repository administrators, so you do not need to take any action for this type of alert.

{% endif %}

## Further reading

* [AUTOTITLE](/code-security/reference/secret-security/supported-secret-scanning-patterns)
* [AUTOTITLE](/code-security/how-tos/secure-your-secrets/detect-secret-leaks/enabling-secret-scanning-for-generic-patterns)
