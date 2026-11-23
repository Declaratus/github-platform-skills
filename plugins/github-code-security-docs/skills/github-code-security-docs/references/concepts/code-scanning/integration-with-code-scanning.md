---
title: Integration with code scanning
shortTitle: Integration with code scanning
intro: You can perform code scanning externally and then display the results in GitHub, or configure webhooks that listen to code scanning activity in your repository.
product: "Code scanning is available for the following repository types:\n\n* Public repositories on GitHub.com\n* Organization-owned repositories on GitHub Team, GitHub Enterprise Cloud, or GitHub Enterprise Server, with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled."
redirect_from:
  - /github/finding-security-vulnerabilities-and-errors-in-your-code/about-integration-with-code-scanning
  - /code-security/secure-coding/about-integration-with-code-scanning
  - /code-security/secure-coding/integrating-with-code-scanning/about-integration-with-code-scanning
  - /github/finding-security-vulnerabilities-and-errors-in-your-code/integrating-with-code-scanning/about-integration-with-code-scanning
  - /code-security/code-scanning/integrating-with-code-scanning/about-integration-with-code-scanning
  - /code-security/concepts/code-scanning/about-integration-with-code-scanning
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
contentType: concepts
category:
  - Find and fix code vulnerabilities
---

## About integration with code scanning

{% ifversion ghes %}

> [!NOTE]
> Your site administrator must enable code scanning before you can use this feature. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/configuring-code-scanning-for-your-appliance).
>
> You may not be able to enable or disable code scanning if an enterprise owner has set a GitHub Code Security policy at the enterprise level. For more information, see [AUTOTITLE](/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise).

{% endif %}

As an alternative to running code scanning within GitHub, you can perform analysis elsewhere, using the CodeQL CLI or another static analysis tool, and then upload the results. For more information, see [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/integrate-with-existing-tools/use-with-existing-ci-system).

If you run code scanning using multiple configurations, an alert will sometimes have multiple analysis origins. If an alert has multiple analysis origins, you can view the status of the alert for each analysis origin on the alert page. For more information, see [AUTOTITLE](/code-security/concepts/code-scanning/code-scanning-alerts#about-alerts-from-multiple-configurations).

## Integrations with webhooks

You can use code scanning webhooks to build or configure integrations, such as [GitHub Apps](/apps/creating-github-apps/registering-a-github-app) or [OAuth apps](/apps/oauth-apps/building-oauth-apps), that subscribe to code scanning events in your repository. For example, you could build an integration that creates an issue on GitHub or sends you a Slack notification when a new code scanning alert is added in your repository. For more information, see [AUTOTITLE](/webhooks) and [AUTOTITLE](/webhooks/webhook-events-and-payloads#code_scanning_alert).

## Further reading

* [AUTOTITLE](/code-security/concepts/code-scanning/code-scanning)
* [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/integrate-with-existing-tools/use-with-existing-ci-system)
* [AUTOTITLE](/code-security/reference/code-scanning/sarif-files/sarif-support)
