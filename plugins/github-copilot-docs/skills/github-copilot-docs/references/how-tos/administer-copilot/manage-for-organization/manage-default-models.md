---
title: Managing the availability of models in an organization
shortTitle: Manage default models
intro: 'Configure which default Copilot models are available to members of your organization.'
permissions: Organization owners
product: 'GitHub Copilot Business or GitHub Copilot Enterprise.'
versions:
  feature: copilot
contentType: how-tos
category:
  - Manage Copilot for a team
allowTitleToDifferFromFilename: true
---

> [!IMPORTANT] If your enterprise has opted in to the **enterprise teams model access** preview, your organization will not be able to access model settings. See [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-availability-of-default-models).

## Which models can I configure?

If your organization is part of an enterprise, the enterprise owner controls which Copilot models are available and how they can be configured at the organization level.

> [!TIP]
> For guidance on coordinating model access with broader governance and rollout decisions, see [AUTOTITLE](/copilot/get-started/enterprise-ai-governance).

When viewing the model settings for your organization, you may see the following statuses:

* **Enabled** or **Disabled** with a (icon: shield) icon: The enterprise owner has enforced this setting. You cannot change the availability of this model.
* **Enabled** or **Disabled** in a dropdown menu: The enterprise owner has made this model optional. You can configure the availability for your organization.
* **Delegate to Default Policy**: This model is available for you to configure, but no one has configured it in the organization. The model inherits the default set in the "Default availability" policy for your organization. See [AUTOTITLE](/copilot/concepts/enterprise/default-model-availability).

## Configuring model availability for your organization

If the enterprise owner has delegated a model to organizations, you can enable or disable it for your organization.

1. In the upper-right corner of GitHub, click your profile picture, then click **(icon: organization) Organizations**.
1. Select an organization by clicking it.
1. Under your organization name, click **(icon: gear) Settings**. If you cannot see the "Settings" tab, select the **(icon: kebab-horizontal)** dropdown menu, then click **Settings**.

   ![Screenshot of the tabs in an organization's profile. The "Settings" tab is outlined in dark orange.](/assets/images/help/discussions/org-settings-global-nav-update.png)
1. In the sidebar, under "Code, planning, and automation", click **(icon: copilot) Copilot**.
1. Click **Models**.
1. Next to a model in the list, click the dropdown menu and select an option:
   * **Enabled**: The model is available to members of your organization.
   * **Disabled**: The model is not available to members of your organization.

On this page, you can also configure the **Default availability for released models** policy to choose the default setting for unconfigured models.

## Further reading

* [AUTOTITLE](/copilot/reference/supported-surfaces-for-policies)
