---
title: Enforcing policies for GitHub Sponsors in your enterprise
intro: Enterprise owners can control whether to allow the enterprise's organizations to sponsor open source projects.
permissions: Enterprise owners can enforce policies for GitHub Sponsors in an enterprise.
versions:
  feature: enterprise-orgs-sponsors-with-cc
shortTitle: 'GitHub Sponsors policies'
redirect_from:
  - /admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-sponsors-in-your-enterprise
contentType: how-tos
category:
  - Secure and govern your enterprise
---

## About enterprise policies for GitHub Sponsors

GitHub Sponsors allows your organizations to financially support developers who build the open source projects you depend on. For more information, see [AUTOTITLE](/sponsors/getting-started-with-github-sponsors/about-github-sponsors) and [AUTOTITLE](/sponsors/sponsoring-open-source-contributors/sponsoring-an-open-source-contributor-through-github).

By default, organizations that belong to an enterprise that pays by credit card cannot sponsor open source contributors. You can set a policy to enable GitHub Sponsors for individual organizations in your enterprise.

Organizations that belong to an enterprise that pays by invoice can either pay for sponsorship by invoice or attribute sponsorships using a linked account. For more information, see [AUTOTITLE](/sponsors/sponsoring-open-source-contributors/paying-for-github-sponsors-by-invoice) or [AUTOTITLE](/sponsors/sponsoring-open-source-contributors/attributing-sponsorships-to-your-organization).

## Enforcing a policy to allow the use of GitHub Sponsors in your enterprise

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under (icon: law) "Policies", click **Sponsors**.
1. Under "Sponsors", click **Add organization**.
1. Begin typing the name of the organization you'd like to enable sponsorships for, then click the name of the organization in the list.
1. Click **Enable sponsorships**.

## Enforcing a policy to disallow the use of GitHub Sponsors in your enterprise

You can disallow the use of GitHub Sponsors for an organization that you previously allowed to use the feature.

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under (icon: law) "Policies", click **Sponsors**.
1. Under "Sponsors", to the right of the organization's name, click **Disable**.
