---
title: GitHub secret types
shortTitle: Secret types
intro: Learn about the different types of secrets used by GitHub.
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
contentType: concepts
category:
  - Protect your secrets
redirect_from:
  - /code-security/concepts/secret-security/github-secret-types
---

GitHub secrets are used to securely store sensitive information like API keys, tokens, and passwords in repositories.

When you store the sensitive information as a GitHub secret, you remove the need to hardcode the credential or key, and prevent exposure of it in your code or logs. The secret can then be used to authenticate services, manage credentials, and securely pass sensitive data in workflows.

There are {% ifversion fpt or ghec %}three {% else %}two {% endif %}types of secrets used by GitHub:

* Dependabot secrets
* Actions secrets{% ifversion fpt or ghec %}
* Codespaces secrets{% endif %}

Depending on the GitHub secret type, you can create and manage secrets under your repository, organization, or personal account security settings page.

For information on the usage, scope, permissions, and limitations of each secret type, see [AUTOTITLE](/code-security/reference/secret-security/secret-types).
