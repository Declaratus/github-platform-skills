---
title: Enabling public monitoring for your enterprise
shortTitle: Enable public monitoring
intro: 'Start detecting secrets your enterprise members leak in public repositories outside your enterprise''s boundaries.'
versions:
  feature: secret-scanning-public-monitoring
permissions: Enterprise owners and enterprise security managers can enable public monitoring for their enterprise.
contentType: how-tos
docsTeamMetrics:
  - secret-protection
category:
  - Secure at scale
---

## Prerequisites

Before enabling public monitoring, ensure your enterprise has:

* GitHub Advanced Security or GitHub Secret Protection enabled
* For GitHub Enterprise Cloud with data residency enterprises, we strongly recommend at least one verified domain configured, since it's the only method available to receive attributed alerts. See [AUTOTITLE](/admin/configuring-settings/configuring-user-applications-for-your-enterprise/verifying-or-approving-a-domain-for-your-enterprise).

> [!NOTE]
> A verified domain isn't required to enable public monitoring. For enterprises not using GitHub Enterprise Cloud with data residency, configuring one is optional, but it provides full attribution coverage. See [AUTOTITLE](/code-security/concepts/secret-security/public-monitoring#attribution-methods).

## Enabling public monitoring

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click (icon: gear) **Settings**.
1. In the left sidebar, click **(icon: codescan) Advanced Security**.
1. Under "Additional Settings," toggle **Public monitoring**.
