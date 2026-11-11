---
title: GitHub Copilot policies for enterprises and organizations
shortTitle: Policies
allowTitleToDifferFromFilename: true
intro: 'Control the availability of GitHub Copilot features and models for your users.'
versions:
  feature: copilot
contentType: concepts
redirect_from:
  - /copilot/concepts/policies
category:
  - Manage Copilot for a team
docsTeamMetrics:
  - ai-governance
---

## How do policies work?

You will find policies for GitHub Copilot on your enterprise's **(icon: copilot) AI controls** tab or in your organization's settings. Policies control which GitHub Copilot features, agents, and models your users can access, and how they can use those features. For example, a policy controls whether users can use Copilot CLI.

In an enterprise, policies are set at the enterprise level first. For most policies, enterprise administrators can either explicitly enable or disable a policy, or let organizations decide.

Users who receive access to Copilot directly from the enterprise, rather than through an organization, are not covered by the "Let organizations decide" option. A separate **Policies for enterprise-assigned users** setting determines whether "Let organizations decide" policies default to enabled or disabled for these users.

## Who do policies apply to?

Generally, policies only apply to users on your Copilot plan. A user is governed by the policies of the enterprise or organization where they receive a Copilot Business or Copilot Enterprise license.

A small number of policies work differently and govern a setting for everyone. For example, you can block Copilot in the cloud for all users in your enterprise's repositories. If this is the case, you will see this highlighted in the policy description.

## What about users with multiple licenses?

A user can receive access to Copilot from multiple organizations in the same enterprise. If these organizations have configured the same policy differently, the **least restrictive** policy usually applies, but there are some exceptions.

More rarely, if a user receives a license from multiple different enterprises, the **most restrictive** policy across enterprises almost always applies. For example, if any enterprise disables Copilot Chat in GitHub, that feature is disabled for the user.

For model policies on a GitHub Team plan, a user's model access is determined by the organization paying for their usage. You can find this organization under "Usage billed to" on the [Copilot features page](https://github.com/settings/copilot/features).

A user's individual plan is cancelled when they are added to a Copilot Business or Copilot Enterprise plan, so a user's personal policies cannot conflict with an enterprise's or organization's.

To see details for each policy, see [AUTOTITLE](/copilot/reference/enterprise-administrators/policy-conflicts).

## What is the default status of policies?

For enterprises with Copilot Business or Copilot Enterprise plans, two separate policies control whether unconfigured generally available (GA) features and models default to enabled or disabled.

If these policies are enabled, users benefit from the latest features and models without the need for administrator intervention.

For more information, see [AUTOTITLE](/copilot/concepts/enterprise/default-availability).

## Where do policies apply?

Policies can apply to any surface where users authenticate to Copilot, including IDEs, the GitHub website, and Copilot CLI.

However, not all policies apply to every surface. See [AUTOTITLE](/copilot/reference/supported-surfaces-for-policies).

## How can I prevent policy drift?

If too many people have access to policy settings and your enterprise's governance posture isn't clearly communicated, policy settings can drift over time. This is a risk for enterprises with strict compliance requirements.

* Regularly review the people with access to policies:

   * In enterprises, enterprise owners or users with the "Manage enterprise AI controls" custom role permission
   * In organizations, organization owners or users with various granular custom permissions

* Use your audit log to monitor changes to policy settings or organization enablement.

## Setting policies

To set policies, see:

* [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies)
* [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-organization/manage-policies)
