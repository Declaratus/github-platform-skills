---
title: Secret scanning for partners
intro: When secret scanning detects authentication details for a service provider in a public repository on GitHub, an alert is sent directly to the provider. This allows service providers who are GitHub partners to promptly take action to secure their systems.
product: "{%- ifversion fpt or ghec %}\n\nSecret scanning alerts for partners runs by default on the following repositories:\n\n* Public repositories and public npm packages on GitHub\n\n{% endif %}"
versions:
  fpt: '*'
  ghec: '*'
shortTitle: Secret scanning for partners
redirect_from:
  - /code-security/secret-scanning/introduction/about-secret-scanning-for-partners
  - /code-security/concepts/secret-security/about-secret-scanning-for-partners
contentType: concepts
category:
  - Protect your secrets
---

## About secret scanning alerts for partners

GitHub scans public repositories and public npm packages for secrets issued by specific service providers who joined our partnership program, and alerts the relevant service provider whenever a secret is detected in a supported location. The service provider validates the string and then decides whether they should revoke the secret, issue a new secret, or contact you directly. Their action will depend on the associated risks to you or them. {% ifversion fpt or ghec %}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           To find out about our partner program, see [AUTOTITLE](/code-security/tutorials/secret-scanning-partner-program).
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {% else %}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           To find out about our partner program, see [AUTOTITLE](/enterprise-cloud@latest/code-security/tutorials/secret-scanning-partner-program) in the GitHub Enterprise Cloud documentation.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {% endif %}

> [!NOTE]You cannot change the configuration of secret scanning for partner patterns on public repositories.

Secret scanning alerts for partners scans:

* Descriptions and comments in issues
* Titles, descriptions, and comments, in open and closed _historical_ issues
* Titles, descriptions, and comments in pull requests
* Titles, descriptions, and comments in GitHub Discussions
* Wikis
* Secret gists

The reason partner alerts are directly sent to the secret providers whenever a leak is detected for one of their secrets is that this enables the provider to take immediate action to protect you and protect their resources. The notification process for regular alerts is different. Regular alerts are displayed on the repository's **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab on GitHub for you to resolve.

If access to a resource requires paired credentials, then secret scanning will create an alert only when both parts of the pair are detected in the same file. This ensures that the most critical leaks are not hidden behind information about partial leaks. Pair matching also helps reduce false positives since both elements of a pair must be used together to access the provider's resource.

## What are the supported secrets

For information about the secrets and service providers supported by push protection, see [AUTOTITLE](/code-security/reference/secret-security/supported-secret-scanning-patterns).

## Further reading

* [AUTOTITLE](/code-security/concepts/secret-security/secret-scanning)
* [AUTOTITLE](/code-security/reference/secret-security/supported-secret-scanning-patterns)
* [AUTOTITLE](/code-security/tutorials/secret-scanning-partner-program)
