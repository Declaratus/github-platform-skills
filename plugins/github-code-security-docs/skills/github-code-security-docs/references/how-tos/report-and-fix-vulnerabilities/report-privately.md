---
title: Privately reporting a security vulnerability
intro: Some public repositories configure security advisories so that anyone can report security vulnerabilities directly and privately to the maintainers.
versions:
  fpt: '*'
  ghec: '*'
contentType: how-tos
permissions: '**Anyone** can privately report a security vulnerability to repository maintainers.'
shortTitle: Report privately
redirect_from:
  - /code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability
  - /code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability
  - /code-security/security-advisories/repository-security-advisories/evaluating-the-security-settings-of-a-repository
  - /code-security/security-advisories/working-with-repository-security-advisories/evaluating-the-security-settings-of-a-repository
  - /code-security/how-tos/report-and-fix-vulnerabilities/report-a-vulnerability/evaluating-the-security-settings-of-a-repository
  - /code-security/how-tos/report-and-fix-vulnerabilities/report-a-vulnerability
  - /code-security/how-tos/report-and-fix-vulnerabilities/report-a-vulnerability/privately-reporting-a-security-vulnerability
  - /code-security/how-tos/report-and-fix-vulnerabilities/privately-reporting-a-security-vulnerability
category:
  - Report and disclose vulnerabilities
---

Owners and administrators of public repositories can enable private vulnerability reporting on their repositories. See [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).

> [!NOTE]
> * If you have admin or security permissions for a public repository, you don’t need to submit a vulnerability report. Instead, create a draft security advisory directly. See [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/create-repository-advisory).
> * Private vulnerability reporting is separate from a repository’s `SECURITY.md` file. You can only report vulnerabilities privately for repositories where this feature is enabled. If the repository has a security policy, the policy is displayed above the reporting form so you can review the maintainer's guidance before submitting.

If a public repository has private vulnerability reporting enabled, anyone can submit a private vulnerability report to the repository maintainers.

If the repository doesn't have private vulnerability reporting enabled, you need to initiate the reporting process by following the instructions in the security policy for the repository, or by creating an issue asking the maintainers for a preferred security contact. See [AUTOTITLE](/code-security/concepts/vulnerability-reporting-and-management/coordinated-disclosure#about-reporting-and-disclosing-vulnerabilities-in-projects-on-github).

1. On GitHub, navigate to the main page of the repository.
1. Under the repository name, click the **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}** tab. If you cannot see the "(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" tab, select the **(icon: kebab-horizontal)** dropdown menu, and then click **(icon: shield) {% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}**.
1. Click **Report a vulnerability** to open the advisory form.
1. If the repository has a security policy, review the policy displayed above the form.
1. Fill in the vulnerability reporting form.

   > [!TIP]
   > By default, you must provide a summary, details, proof of concept, and impact statement. Maintainers can customize the form and require other information. Provide enough detail for the maintainers to reproduce and assess the vulnerability.

1. Optionally, select **I used AI assistance to find or write up this report**.
1. At the bottom of the form, click **Submit report**. GitHub will display a message letting you know that maintainers have been notified and that you have a pending credit for this security advisory.

   > [!TIP]
   > When the report is submitted, GitHub automatically adds the reporter of the vulnerability as a collaborator and as a credited user on the proposed advisory.

1. Optionally, click **Start a temporary private fork** if you want to start to fix the issue. Note that only the repository maintainer can merge changes from that private fork into the parent repository.

   ![Screenshot of the bottom of a security advisory. A button, labeled "Start a temporary fork" is outlined in dark orange.](/assets/images/help/security/advisory-start-a-temporary-private-fork-button.png)

The next steps depend on the action taken by the repository maintainer. See [AUTOTITLE](/code-security/how-tos/report-and-fix-vulnerabilities/fix-reported-vulnerabilities/manage-vulnerability-reports).

## Rate limits for private vulnerability reports

To protect maintainers from spam and abuse, GitHub limits the number of private vulnerability reports that you can submit:

* You can submit a maximum of 25 reports per 24-hour period across repositories where you are not a trusted reporter.
* You can submit a maximum of 5 reports to a single repository per 24-hour period.
* By default, a repository accepts a maximum of 10 reports per 24-hour period from all reporters combined.

Repository maintainers can set a lower or higher total limit for their repository and exempt trusted reporters. Reports to a repository where you are a trusted reporter are exempt from that repository's limits and do not count toward your global 25-report limit. Reports to other repositories still count toward both the global limit and each repository's limits.

If you reach a rate limit, you will see a message when you try to submit a new report on GitHub. Each 24-hour period starts with the first report that counts toward that limit, and the limit resets in full when the period ends.
