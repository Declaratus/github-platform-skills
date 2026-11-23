---
title: Secret scanning pattern configuration data
shortTitle: Secret pattern data
intro: Understand the data displayed in the secret scanning pattern configuration page to make informed decisions about push protection settings.
permissions: 'Organization owners and security managers'
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
contentType: reference
category:
  - Protect your secrets
redirect_from:
  - /code-security/reference/secret-security/secret-scanning-pattern-configuration-data
---

When configuring push protection, you can view performance data for each secret pattern to make informed enablement decisions. Use metrics like alert volume and false positive rates to balance security with developer experience. See [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/configure-global-settings#specifying-patterns-to-include-in-push-protection){% ifversion security-configuration-enterprise-level %} or [AUTOTITLE](/code-security/how-tos/secure-at-scale/configure-enterprise-security/establish-complete-coverage/configure-additional-settings#specifying-patterns-to-include-in-push-protection-for-your-enterprise){% endif %}.

| Column                                      | Description            |
   |---------------------------------------------|----------------------------------------------|
   | Name | Name of the pattern or secret |
   | Alert total | Total number of alerts for the pattern (percentage and absolute numbers) |
   | False positives | Percentage of false positives for the pattern |
   | Bypass rate | Percentage of bypasses for the pattern |
   | GitHub default | Default behavior for push protection, as recommended by GitHub |
   | Enterprise setting | **Uneditable at organization level**</br>Current enablement status for push protection</br>Can be `Enabled`, `Disabled`, and `Default`.</br>At enterprise level, `Default` is the default value. |
   | Organization setting | **Only valid at organization level**</br>Current enablement status for push protection</br>Can be `Enabled`, `Disabled`, and `Enterprise` (inherited from the enterprise).</br>`Enterprise` is the default value. |
 
