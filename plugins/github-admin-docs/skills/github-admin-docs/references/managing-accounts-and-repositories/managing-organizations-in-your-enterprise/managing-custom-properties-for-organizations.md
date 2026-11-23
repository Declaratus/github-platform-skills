---
title: Managing custom properties for organizations
intro: 'With custom properties, you can add metadata to organizations in your enterprise and use that metadata to target repositories with rulesets.'
permissions: 'Enterprise owners {% ifversion custom-org-roles %}and users with the "Manage the Enterprise''s custom properties definitions" permission {% endif %}can add and set a custom property schema at the enterprise level.'
versions:
  ghec: '*'
  ghes: '>= 3.21'
shortTitle: Organization custom properties
contentType: how-tos
category:
  - Manage accounts and repositories
---

> [!NOTE]
> For GitHub Enterprise Server, this feature will only be available from version 3.21.

## About custom properties

Custom properties are structured metadata fields that you can add to repositories and organizations in GitHub to enable better organization, governance, and automation across your environment. See [AUTOTITLE](/admin/managing-accounts-and-repositories/managing-organizations-in-your-enterprise/custom-properties).

This article relates to **organization custom properties.**

## Allowed characters

Custom property names and values may only contain certain characters:

* Names: `a-z`, `A-Z`, `0-9`, `_`, `-`, `$`, `#`
* Values: All printable ASCII characters except `"`

## Adding custom properties

You can add custom properties to your enterprise and set values for those properties for organizations in your enterprise.

{% ifversion ghec %}You can also use the REST API to create and manage custom properties for an organization. See [AUTOTITLE](/rest/enterprise-admin/custom-properties).{% endif %}

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. Under the enterprise name, click the (icon: organization) **Organizations** tab.

     ![Screenshot of an enterprise. The "Organizations" tab is highlighted with an orange outline.](/assets/images/help/enterprises/organizations-tab.png)
1. In the left sidebar, click **Custom properties**.
1. To add a new custom property, click **New property** in the upper right corner.
1. In the "Name" field, type the name you'd like to use for your custom property. The name can't contain spaces, and cannot exceed 75 characters in length.
1. Optionally, in the "Description" field, add a description for the custom property.
1. Under "Type", select the type of property you'd like to add.
1. Optionally, select **Allow organization actors to set this property** to allow organization users and apps with the organization-level "custom properties" fine-grained permission to set and update the property value for their organization.
1. Optionally, select **Require this property for all organizations** and add a default value. Enabling this option indicates that you require that **all organizations in your enterprise** have a value for this property. Organizations that don't have an explicit value for this property will inherit the default value.
1. Click **Save property**.

## Setting values for organizations in your enterprise

You, and any users with the "Edit custom properties values at the organization level" permission, can set values for custom properties for organizations in your enterprise.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. Under the enterprise name, click the (icon: organization) **Organizations** tab.

     ![Screenshot of an enterprise. The "Organizations" tab is highlighted with an orange outline.](/assets/images/help/enterprises/organizations-tab.png)
1. In the left sidebar, click **Custom properties**.
1. Click the "Set values" tab.
1. Select one or more organizations from the list and click **(icon: pencil) Edit properties**.

1. In the modal dialog that appears, select a value for each property you'd like to set for the selected organizations.
1. Click **Save changes**.
