---
title: Configuring runners for GitHub Copilot cloud agent in your organization
shortTitle: Configure agent runners
allowTitleToDifferFromFilename: true
intro: 'Configure the GitHub Actions runners used by Copilot cloud agent and control whether repositories can customize the runner type.'
permissions: Organization owners
product: "Copilot cloud agent is available for all paid Copilot plans.\n\nThe agent is available in all repositories stored on GitHub, except repositories owned by managed user accounts and where it has been explicitly disabled.<br><a href=\"https://github.com/github-copilot/purchase?ref_product=copilot&ref_type=trial&ref_style=button&utm_source=configuring-runners-cca-your-org-doc-signup-cta&utm_medium=docs&utm_campaign=universe-2026\" target=\"_blank\" class=\"btn btn-primary mt-3 mr-3 no-underline\"><span>Sign up for Copilot</span>(icon: link-external)</a>"
versions:
  feature: copilot
contentType: how-tos
category:
  - Manage Copilot for a team
---

## About organization-level runner controls

This customization applies only when Copilot runs on GitHub Actions. It doesn't apply to sessions that run in a cloud sandbox.

By default, Copilot cloud agent sessions that run on GitHub Actions use a standard GitHub-hosted runner (`ubuntu-latest`). As an organization owner, you can change the default runner type for all repositories in your organization, and choose whether individual repositories are allowed to override this default.

This is useful if your organization requires all Copilot cloud agent sessions that run on GitHub Actions to use specific runners—for example, to use larger runners for better performance, or to use self-hosted runners that have access to internal resources.

You can configure:

* **Runner type**: Choose between a standard GitHub-hosted runner or a labeled runner from a specific runner group.
* **Allow repositories to customize the runner type**: Control whether repositories can override the organization default using a Copilot setup steps workflow defined at `.github/workflows/copilot-setup-steps.yml`.

## Configuring the default runner type

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the sidebar, under "Code, planning, and automation", click **(icon: copilot) Copilot**, and then click **Cloud**.
1. Next to "Runner type," click the pencil icon ((icon: pencil)).
1. Select the runner type to use by default for Copilot cloud agent across your organization.
   * **Standard GitHub runner**: Copilot cloud agent will use `ubuntu-latest`.
   * **Labeled runner**: Copilot cloud agent will use a runner matching the group name and/or label you specify. Enter values in the **Runner group name** and/or **Runner label** fields.
1. Click **Save runner selection**.

## Preventing repositories from customizing the runner type

By default, repositories can override the organization-level runner configuration using a Copilot setup steps workflow located at `.github/workflows/copilot-setup-steps.yml`. If you want to enforce a consistent runner type across all repositories, you can disable this option.

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the sidebar, under "Code, planning, and automation", click **(icon: copilot) Copilot**, and then click **Cloud**.
1. Under "Allow repositories to customize the runner type," toggle the setting to enable or disable repository-level customization.
   * When enabled, repositories can override the default runner by setting the `runs-on` field in the `copilot-setup-steps` job of `copilot-setup-steps.yml`. See [AUTOTITLE](/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment).
   * When disabled, all repositories in your organization will use the organization-level runner type.
1. Click **Save**.

## Further reading

* [AUTOTITLE](/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment)
* [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-organization/add-copilot-cloud-agent)
