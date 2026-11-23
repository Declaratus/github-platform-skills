---
title: About GitHub Enterprise Cloud
intro: Learn about GitHub Enterprise Cloud, its features, and management options for large businesses and teams.
versions:
  ghec: '*'
contentType: concepts
category:
  - Get started with GitHub Enterprise
---

GitHub Enterprise Cloud is a deployment option for GitHub Enterprise, adding advanced features to GitHub, including:

* SAML authentication
* Additional GitHub Actions minutes
* Restriction of email notifications to verified domains
* Privately published GitHub Pages sites
* Managed user accounts
* Repository rulesets
* GitHub's compliance reports

For a full list of features included with GitHub Enterprise Cloud, see our [Pricing](https://github.com/pricing) page.

## What are the differences between GitHub Enterprise Cloud and other plans?

A key difference between GitHub Enterprise Cloud and other GitHub plans is access to an enterprise account, which gives administrators a central point for managing multiple organizations. See [AUTOTITLE](/admin/concepts/enterprise-fundamentals/enterprise-accounts).

When you purchase GitHub Enterprise, you get access to both GitHub Enterprise Cloud and GitHub Enterprise Server. For more information about GitHub Enterprise Server and how it differs from GitHub Enterprise Cloud, see [AUTOTITLE](/admin/overview/about-github-for-enterprises#about-deployment-options).

## About enterprise types

While setting up your trial of GitHub Enterprise Cloud, you'll choose an enterprise type.

* Enterprise with personal accounts
* Enterprise with managed users

To help you decide which choice is best for your enterprise, see [AUTOTITLE]({% ifversion not ghec %}/enterprise-cloud@latest{% endif %}/admin/identity-and-access-management/understanding-iam-for-enterprises/choosing-an-enterprise-type-for-github-enterprise-cloud){% ifversion not ghec %} in the GitHub Enterprise Cloud documentation.{% else %}.{% endif %}

## Copilot access

Eligible enterprises can provide Copilot access to licensed users at no additional per-user access charge. Administrators must assign access separately, and metered usage is billed from the first use without an included allowance. For eligibility and details, see [AUTOTITLE](/copilot/get-started/whats-changing-with-github-enterprise-and-copilot).

## About data residency

If you choose an enterprise with managed users, you can also choose where your company's data is stored.

By default, GitHub stores data for GitHub.com in the USA. When you adopt GitHub Enterprise Cloud with data residency, you can choose where your company's code and data are stored. Your enterprise will be hosted on a dedicated subdomain of GHE.com.
                                                                                                                                            
                                                                                                                                            Data residency makes it easy to separate open source and enterprise work, and helps you meet specific data residency compliance requirements.
                                                                                                                                            
                                                                                                                                            The available regions are:
                                                                                                                                            
                                                                                                                                            * EU (includes Azure regions in EFTA countries, currently Norway and Switzerland)
                                                                                                                                            * Australia
                                                                                                                                            * US
                                                                                                                                            * Japan
                                                                                                                                            
                                                                                                                                            In the future, GitHub plans to offer data residency in more regions.

## About documentation

Documentation for both administrators and users of GitHub Enterprise Cloud is available on this site, GitHub Docs.

* [Enterprise administrator documentation](/admin)
* [User documentation](/)

You can read documentation that reflects the features available with GitHub Enterprise Cloud. For more information, see [AUTOTITLE](/get-started/using-github-docs/about-versions-of-github-docs).

## Can I try GitHub Enterprise Cloud?

You can sign up for a free, 30-day trial of GitHub Enterprise Cloud. See [AUTOTITLE](/admin/overview/setting-up-a-trial-of-github-enterprise-cloud).

## Further reading

* [AUTOTITLE](/get-started/onboarding/getting-started-with-github-enterprise-cloud)
* [AUTOTITLE](/admin/data-residency/about-github-enterprise-cloud-with-data-residency)
* [ GitHub public roadmap ]( https://github.com/github/roadmap#github-public-roadmap ) in the `github/roadmap` repository
