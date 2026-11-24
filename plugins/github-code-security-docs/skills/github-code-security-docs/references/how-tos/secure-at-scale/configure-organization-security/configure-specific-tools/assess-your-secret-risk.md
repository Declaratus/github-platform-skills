---
title: Running the secret risk assessment for your organization
shortTitle: Assess your secret risk
intro: Determine your organization's exposure to leaked secrets by generating a secret risk assessment report.
product: 'Free for organizations on GitHub Team and GitHub Enterprise <br><a href="https://github.com/get_started?with=risk-assessment&ref_product=code-scanning&ref_type=engagement&ref_style=button" target="_blank" class="btn btn-primary mt-3 mr-3 no-underline"><span>Get started with security risk assessments</span> (icon: link-external)</a>'
permissions: 'Organization owners and security managers'
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets/assess-your-secret-risk
  - /code-security/securing-your-organization/understanding-your-organizations-exposure-to-leaked-secrets
contentType: how-tos
docsTeamMetrics:
  - secret-protection
category:
  - Secure at scale
---

## Generating an initial secret risk assessment

1. On GitHub, navigate to the main page of the organization.
1. Under your organization name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. In the sidebar, under "Security", click **(icon: key) Assessments**.
1. To generate the secret risk assessment, click **Scan your organization**.

   > [!NOTE]
   > If you haven't previously run a security risk assessment, this will also initiate a **code security risk assessment**.

    If you're an organization owner and you've opted in for email notifications, GitHub will send you an email to let you know when the report is ready to view.

## Rerunning the secret risk assessment

> [!NOTE]
> You can only generate a secret risk assessment report once every 90 days.
1. On GitHub, navigate to the main page of the organization.
1. Under your organization name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab.
1. In the sidebar, under "Security", click **(icon: key) Assessments**.
1. Towards the top right side of the existing report, click **Rerun scan**.

If you're an organization owner and you've opted in for email notifications, GitHub will send you an email to let you know when the report is ready to view.

