---
title: Adding a sales tax certificate
intro: 'If you''re a customer in the United States with a GitHub Customer Agreement and you''re exempt from sales tax, you can upload a certificate to ensure the correct sales tax amount is calculated.'
redirect_from:
  - /billing/managing-your-github-billing-settings/adding-a-sales-tax-certificate
  - /billing/using-the-billing-platform/adding-a-sales-tax-certificate
  - /billing/managing-your-billing/adding-a-sales-tax-certificate
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
product: 'US-based organization and enterprise accounts that use the GitHub Customer Agreement, see {% ifversion fpt or ghec %}[AUTOTITLE](/organizations/managing-organization-settings/upgrading-to-the-github-customer-agreement){% elsif ghes %}[AUTOTITLE](/enterprise-cloud@latest/organizations/managing-organization-settings/upgrading-to-the-github-customer-agreement) in the GitHub Enterprise Cloud documentation{% endif %}'
shortTitle: Add sales tax certificate
contentType: how-tos
category:
  - Set up payment
---

If you're a GitHub customer in the United States, you need to ensure that your account is set up to calculate sales tax correctly. If you're exempt from sales tax, you can upload a certificate to your account in JPEG (`.jpg`, `.jpeg`), PNG (`.png`), or PDF (`.pdf`) format.

## Adding a sales tax exemption certificate to your account

Enterprise owners, organization owners, and billing managers can upload a sales tax exemption certificate to an enterprise account if the account uses the GitHub Customer Agreement.

1. Navigate to your organization or enterprise. For example, from the [Organizations](https://github.com/settings/organizations?ref_product=github&ref_type=engagement&ref_style=text) or [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) pages on GitHub.com.
1. From the list of "Billing & licensing" pages, click **Payment information**.
1. Review your "Billing information" and update any incorrect data. You must ensure that the address fields are correct and that the "City" and "Postal/Zip code" fields are accepted. If there is any missing information or any errors are reported, the option to upload a sales tax certificate is hidden.
1. At the bottom of the page in the "Sales Tax" section, click **Upload certificate**, and select the certificate file you want to upload. If "Sales Tax" is missing, check that your billing information defines your country as "United States of America."

Your account is marked as tax exempt while your certificate is reviewed. If your certificate is not approved, you will need to upload a new one.
