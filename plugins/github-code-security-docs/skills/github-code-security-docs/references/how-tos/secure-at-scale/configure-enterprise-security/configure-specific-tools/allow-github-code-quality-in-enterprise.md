---
title: Allowing use of GitHub Code Quality in your enterprise
shortTitle: Allow Code Quality
intro: Set enterprise policies for Code Quality to give organizations access while keeping repository enablement under your control.
versions:
  feature: code-quality
product: "{% ifversion fpt or ghec %}\nGitHub Team or GitHub Enterprise Cloud\n{% endif %}"
permissions: Enterprise owners
audience:
  - driver
contentType: how-tos
allowTitleToDifferFromFilename: true
redirect_from:
  - /code-security/code-quality/how-tos/allow-in-enterprise
category:
  - Secure at scale
---

> [!NOTE]
> Code Quality has its own standalone enterprise policies. Access was previously controlled by your Advanced Security policies, and those existing settings are automatically applied to the new Code Quality policies.

When you allow Code Quality for an organization and set the repository admin policy to **Allowed**, repository administrators can enable Code Quality scans and all associated capabilities, including bulk agentic remediation with Copilot. There is no separate policy for agentic remediation.

If you restrict Code Quality, repository administrators cannot enable scans or use Copilot-powered autofixes for code quality findings.

1. Navigate to your enterprise. For example, from [https://github.com/settings/enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text).
1. At the top of the page, click **(icon: law) Policies**.
1. In the sidebar, click (icon: code-square) **Code Quality**.
1. Select the "Organization access" dropdown menu, then click **Allow for all organizations** or **Allow for selected organizations**.
1. If you choose "Allow for selected organizations", select the dropdown menu for each organization where you want to enable Code Quality, then click **Available**.
1. To allow repository administrators to enable Code Quality on their repositories, select the "Repository admin policy" dropdown menu, then click **Allowed**.

## Next steps

To see Code Quality in action, turn the feature on for one or more repositories. See [AUTOTITLE](/code-security/how-tos/maintain-quality-code/enable-code-quality).
