---
title: Viewing metrics for custom patterns
shortTitle: View custom pattern metrics
intro: Find out how many alerts are being raised and addressed for a custom pattern.
permissions: 'Repository owners, organization owners, security managers, enterprise administrators, and users with the **admin** role'
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
contentType: how-tos
redirect_from:
  - /code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/metrics-for-custom-patterns
  - /code-security/how-tos/view-and-interpret-data/metrics-for-custom-patterns
category:
  - Protect your secrets
---

> [!NOTE] Metrics for custom patterns are in public preview and subject to change.

Activity overviews for custom patterns are available at the repository, organization, and enterprise levels. Each overview displays alerts generated and push protection blocks over the last 30 days.

1. Navigate to where the custom pattern was created. A custom pattern can be created in a repository, organization, or enterprise account.
   * For a repository or organization, display the "Advanced Security" settings for the repository or organization where the custom pattern was created. For more information, see [Defining a custom pattern for a repository](/code-security/how-tos/secure-your-secrets/customize-leak-detection/define-custom-patterns#defining-a-custom-pattern-for-a-repository) or [Defining a custom pattern for an organization](/code-security/how-tos/secure-your-secrets/customize-leak-detection/define-custom-patterns#defining-a-custom-pattern-for-an-organization).
   * For an enterprise, under "Policies" display the "Advanced Security" area, and then click **Security features**. For more information, see [Defining a custom pattern for an enterprise account](/code-security/how-tos/secure-your-secrets/customize-leak-detection/define-custom-patterns#defining-a-custom-pattern-for-an-enterprise-account).
1. Under "Custom patterns", click the custom pattern you want to view.

The metrics are displayed under the custom pattern's name.
