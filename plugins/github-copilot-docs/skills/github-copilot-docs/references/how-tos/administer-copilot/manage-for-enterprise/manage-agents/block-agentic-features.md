---
title: Blocking agentic features in your enterprise
intro: Disable features for all users and repositories.
permissions: Enterprise owners and AI managers
versions:
  feature: copilot
shortTitle: Block agentic features
contentType: how-tos
category:
  - Manage Copilot for a team
allowTitleToDifferFromFilename: true
redirect_from:
  - /copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/block-copilot-cloud-agent
---

Most Copilot policies only affect users who receive a Copilot license from your enterprise or organizations. However, there are dedicated policies to completely disable features in your repositories, including for users who get access to Copilot from a personal plan or another enterprise.

## Blocking Copilot in the cloud

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: copilot) AI controls**.
1. In the sidebar, click **(icon: copilot) Copilot**.
1. Under "Features & clients", click **Configure features & clients**.
1. Next to **Block Copilot cloud agent in all repositories owned by ENTERPRISE-NAME**, click the toggle.

## Blocking Copilot code review

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: copilot) AI controls**.
1. In the sidebar, click **(icon: copilot) Copilot**.
1. Under "Features & clients", click **Configure features & clients**.
1. Find the **Copilot code review** policies.
1. Next to **Block Copilot code review in all enterprise repositories**, click the toggle.
