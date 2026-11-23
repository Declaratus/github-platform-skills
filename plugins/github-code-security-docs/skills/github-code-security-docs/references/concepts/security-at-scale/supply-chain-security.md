---
title: Supply chain security for your enterprise
intro: You can enable enterprise-level features that help your developers understand and update the dependencies their code relies on.
shortTitle: Supply chain security
permissions: ''
versions:
  ghes: '*'
redirect_from:
  - /admin/code-security/managing-supply-chain-security-for-your-enterprise/about-supply-chain-security-for-your-enterprise
  - /admin/managing-code-security/managing-supply-chain-security-for-your-enterprise/about-supply-chain-security-for-your-enterprise
  - /code-security/concepts/security-at-scale/about-supply-chain-security-for-your-enterprise
contentType: concepts
category:
  - Secure your dependencies
---

You can allow users to identify their projects' dependencies by enabling the dependency graph for GitHub Enterprise Server. For more information, see [Enabling the dependency graph for your enterprise](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/enable-dependency-graph).

{% ifversion ghes %}
After you enable the dependency graph, users will have access to the dependency review feature. Dependency review helps you understand dependency changes and the security impact of these changes at every pull request. For more information, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependency-review).
{% endif %}

You can also allow users to find and fix vulnerabilities in their code dependencies by enabling Dependabot alerts and Dependabot updates. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-github-connect/enabling-dependabot-for-your-enterprise).

After you enable Dependabot alerts, you can view vulnerability data from the GitHub Advisory Database on GitHub Enterprise Server and manually sync the data. For more information, see [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/configure-specific-tools/view-vulnerability-data).
