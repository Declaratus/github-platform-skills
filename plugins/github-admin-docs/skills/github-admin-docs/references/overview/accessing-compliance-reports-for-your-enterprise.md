---
title: Accessing compliance reports for your enterprise
intro: You can access GitHub's compliance reports, such as our SOC reports and Cloud Security Alliance CAIQ self-assessment (CSA CAIQ), for your enterprise.
versions:
  ghec: '*'
permissions: Enterprise owners can access compliance reports for the enterprise.
shortTitle: Access compliance reports
contentType: how-tos
category:
  - Secure and govern your enterprise
---

## About GitHub's compliance reports

You can access GitHub's compliance reports in your enterprise settings.

{%- ifversion ghec %}
* SOC 1, Type 2
* SOC 2, Type 2
{%- elsif fpt %}
* SOC 3
{%- endif %}
* Cloud Security Alliance CAIQ self-assessment (CSA CAIQ - Level 1)
* ISO/IEC 27001:2022 certification
{%- ifversion ghec %}
* Cloud Security Alliance STAR certification (CSA STAR - Level 2)
* GitHub Bug Bounty Quarterly reports
* GitHub.com Services Continuity and Incident Management Plan
* GitHub PCI DSS Attestation of Compliance
{%- endif %}

## Accessing compliance reports for your enterprise

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: checklist) Compliance**.
1. Under "Resources", to the right of the report you want to access, click **(icon: download) Download** or **(icon: link-external) View**.

   ![Screenshot of the "Resources" section of the "Compliance" page. Next to a report, a button, labeled "Download," is outlined in orange.](/assets/images/help/settings/compliance-report-download.png)

## Further reading

* [AUTOTITLE](/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/accessing-compliance-reports-for-your-organization){% ifversion enterprise-member-csv %}
* [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/exporting-membership-information-for-your-enterprise){% endif %}
