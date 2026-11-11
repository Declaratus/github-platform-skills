---
title: Setting up GitHub Copilot for your organization
shortTitle: Set up for organization
intro: 'Enable GitHub Copilot for your organization so members can write code faster.'
permissions: Organization owners
product: 'Organizations with a Copilot Enterprise or Copilot Business plan'
versions:
  feature: copilot
redirect_from:
  - /copilot/copilot-business/enabling-and-setting-up-github-copilot-business
  - /copilot/overview-of-github-copilot/enabling-and-setting-up-github-copilot-for-business
  - /copilot/managing-copilot-business/enabling-and-setting-up-github-copilot-for-business
  - /copilot/managing-copilot-business/enabling-and-setting-up-github-copilot-business
  - /copilot/setting-up-github-copilot/setting-up-github-copilot-for-your-organization
  - /copilot/get-started/setting-up-github-copilot/setting-up-github-copilot-for-your-organization
  - /copilot/how-tos/set-up/setting-up-github-copilot-for-your-organization
  - /copilot/how-tos/set-up/set-up-for-organization
contentType: how-tos
category: 
  - Configure Copilot
---

## Enable GitHub Copilot

Owners of **organizations on GitHub Free or GitHub Team** can purchase Copilot Business for their organization. [Subscribe to Copilot Business](https://github.com/github-copilot/purchase?ref_product=copilot&ref_type=purchase&ref_style=button&ref_plan=business).

If your organization is owned by an enterprise that has a Copilot subscription, you can ask your enterprise owner to enable Copilot for your organization. Go to [https://github.com/settings/copilot](https://github.com/settings/copilot) and request access under "Get Copilot from an organization."

## Set policies

Control which Copilot features are available in your organization. See [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-organization/manage-policies).

## Configure networking

If your organization members connect through an HTTP proxy server or firewall, add the required URLs to the allowlist. See [AUTOTITLE](/copilot/reference/copilot-allowlist-reference).

If your environment uses custom SSL certificates, install them on your members' machines. See [AUTOTITLE](/copilot/how-tos/copilot-in-your-ide/set-up-copilot/configure-network-settings#installing-custom-certificates).

## Grant access to members

Enable Copilot for some or all members of your organization. Consider starting with teams most likely to benefit, to discover potential blockers and demonstrate early success. See [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-organization/manage-access/grant-access).

> [!TIP] If your organization belongs to an enterprise on GHE.com, users need additional setup to authenticate from their development environment. See [AUTOTITLE](/copilot/how-tos/copilot-in-your-ide/set-up-copilot/authenticate-to-ghecom).

## Next steps

* **Set a governance posture that supports adoption**. Avoid over-restricting Copilot by delegating administration, enabling vetted features promptly, and aligning spend controls with your goals. See [AUTOTITLE](/copilot/tutorials/roll-out-at-scale/govern-at-scale/govern-for-adoption).
* **Explore self-service license management options**. Many successful rollouts use a self-service model where developers can claim a license without approval. See [AUTOTITLE](/copilot/tutorials/roll-out-at-scale/assign-licenses/set-up-self-serve-licenses).
* **Learn how to plan and implement an effective enablement process to drive Copilot adoption**. See [AUTOTITLE](/copilot/tutorials/roll-out-at-scale/enable-developers/drive-adoption).
* **Enhance the development experience by enabling and training developers on the latest features**. For example, share context with Copilot Spaces and enable Copilot code review on pull requests. For an example showing how these features fit together, see [AUTOTITLE](/copilot/tutorials/roll-out-at-scale/enable-developers/integrate-ai-agents).
