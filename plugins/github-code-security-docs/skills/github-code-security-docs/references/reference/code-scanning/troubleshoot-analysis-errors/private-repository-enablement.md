---
title: Cannot enable CodeQL in a private repository
shortTitle: Private repository enablement
intro: 'GitHub Code Security must be enabled in order to use code scanning on private repositories.'
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/reference/code-scanning/troubleshoot-analysis-errors/cannot-enable-codeql-in-a-private-repository
  - /code-security/code-scanning/troubleshooting-code-scanning/cannot-enable-codeql-in-a-private-repository
  - /code-security/how-tos/scan-code-for-vulnerabilities/troubleshooting/troubleshooting-analysis-errors/cannot-enable-codeql-in-a-private-repository
contentType: reference
category:
  - Troubleshoot security tools
---

{% ifversion fpt %}
If you are on a **GitHub Free** or **GitHub Pro** plan, you can only use code scanning on repositories that are publicly available. To enable code scanning for private or internal repositories, you must upgrade to GitHub Team or GitHub Enterprise with GitHub Code Security and enable Code Security for the repository. For more information, see [AUTOTITLE](/get-started/learning-about-github/githubs-plans#github-team) and [AUTOTITLE](/get-started/learning-about-github/about-github-advanced-security).
{% endif %}

## Confirm whether GitHub Code Security is enabled

1. On GitHub, navigate to the main page of the repository.
1. Under your repository name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of a repository header showing the tabs. The "Settings" tab is highlighted by a dark orange outline.](/assets/images/help/repository/repo-actions-settings.png)
1. In the "{% ifversion security-and-quality-tab %}Security and quality{% else %}Security{% endif %}" section of the sidebar, click **(icon: codescan) Advanced Security**.
1. On the settings page, scroll down to "Code Security."
1. If there is an associated and active **Enable** button, Code Security is available for this repository but not yet enabled.

1. If use of GitHub Code Security is blocked by a policy, "(icon: shield) Disabled" is shown in place of the **Enable** button.

   !["Screenshot of the Advanced Security" setting. The disabled option is highlighted in dark orange.](/assets/images/help/repository/ghas-enterprise-policy-block.png)

### Requesting access to GitHub Code Security

1. In the "Code Security" settings, click the enterprise or organization name to display a list of users with access to edit the policy that controls access to GitHub Code Security. For more information, see [AUTOTITLE](/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise#enforcing-a-policy-for-the-availability-of-advanced-security-in-your-enterprises-organizations).
1. Follow your company's policy for requesting access to additional features.

### Enabling GitHub Code Security

1. Open the "Code security" settings page.
1. Next to the "Code Security" feature, click **Enable**.
1. Rerun code scanning.
