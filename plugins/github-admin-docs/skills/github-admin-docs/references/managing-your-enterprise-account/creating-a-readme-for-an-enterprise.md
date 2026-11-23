---
title: Creating a README for an enterprise
intro: You can create a README to tell your members what is happening in your enterprise.
versions:
  feature: enterprise-readme
permissions: Enterprise owners can create and edit an enterprise README.
shortTitle: Create a README
redirect_from:
  - /enterprise-onboarding/feature-enhancements/create-a-readme-for-your-enterprise
contentType: how-tos
category:
  - Get started with GitHub Enterprise
---

## About READMEs for enterprises

To help people understand what is happening in your enterprise, you should create a README. For example, you can use a README to help members learn about different organizations in the enterprise, to share links to important resources, or to communicate information about the settings and policies of your enterprise.

The README is displayed on the enterprise's "Overview" page, which is the landing page you see when you navigate to the enterprise. This page is only visible to members of the enterprise.

You can also create READMEs for organizations in your enterprise, visible either publicly or only to members. For more information, see [AUTOTITLE](/organizations/collaborating-with-groups-in-organizations/customizing-your-organizations-profile).

## Creating a README for an enterprise

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. On the "Overview" page, click **Create README**. If a README is already present on the page, click **Edit**.
1. Write the content for your README. You can use Markdown to format the content, such as adding headings, images, and lists. For more information, see [AUTOTITLE](/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

   >[!NOTE] You can only link to publicly hosted images in your README. You cannot upload an image to your README, or link to an image from a private repository.

1. Click **Save**.

## Further reading

* [AUTOTITLE](/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
* [AUTOTITLE](/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)
