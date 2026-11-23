---
title: About GitHub Enterprise Importer
intro: 'With GitHub Enterprise Importer, you can migrate your enterprise to GitHub Enterprise Cloud from various sources.'
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /early-access/github/migrating-with-github-enterprise-importer/about-github-enterprise-importer
  - /early-access/github/migrating-with-github-enterprise-importer/understanding-github-enterprise-importer/about-github-enterprise-importer
  - /early-access/enterprise-importer/understanding-github-enterprise-importer/about-github-enterprise-importer
  - /migrations/using-github-enterprise-importer/migrating-repositories-with-github-enterprise-importer
  - /early-access/github/migrating-with-github-enterprise-importer/understanding-github-enterprise-importer/migration-support-for-github-enterprise-importer
  - /early-access/enterprise-importer/understanding-github-enterprise-importer/migration-support-for-github-enterprise-importer
  - /migrations/using-github-enterprise-importer/understanding-github-enterprise-importer/migration-support-for-github-enterprise-importer
  - /early-access/github/migrating-with-github-enterprise-importer/preparing-to-migrate-with-github-enterprise-importer
  - /early-access/github/migrating-with-github-enterprise-importer/running-a-migration-with-github-enterprise-importer/preparing-to-run-a-migration-with-github-enterprise-importer
  - /early-access/enterprise-importer/preparing-to-migrate-with-github-enterprise-importer/preparing-to-run-a-migration-with-github-enterprise-importer
  - /migrations/using-github-enterprise-importer/preparing-to-migrate-with-github-enterprise-importer/preparing-to-run-a-migration-with-github-enterprise-importer
  - /migrations/using-github-enterprise-importer/preparing-to-migrate-with-github-enterprise-importer
category:
  - Understand enterprise migration tools
---

## About GitHub Enterprise Importer

GitHub Enterprise Importer is a highly customizable migration tool designed to help you move your enterprise to GitHub Enterprise Cloud.

You can migrate on a repository-by-repository basis or, if your migration source is GitHub.com, on an organization-by-organization basis.

GitHub Enterprise Importer allows you to customize your migration to meet your enterprise's unique needs with:
* **A distinct migration permissions role** for repository migrations, which allows you to designate teams and/or individual users to run a migration and removes the need for organization owners to complete the migration.
* **High fidelity migration**, which allows you to migrate a single repository, a series of repositories, or an entire organization.
* **Support for custom trial run migrations**, which allow you to run a migration as many times as you desire before running the production migration.
* **Clear and unblocking error logging**, so that migrations are allowed to continue with non-critical migration errors, such as not being able to move a single pull request comment. After the migration, you can review a log file that opens automatically.
* **Users retain ownership of their history**, to ensure that their Git history or GitHub metadata is maintained across the migration.

You can run your migration with either the GitHub CLI or the API.

The GitHub CLI simplifies the migration process and is recommended for most customers. Advanced customers with heavy customization needs can use the API to build their own integrations with GitHub Enterprise Importer.

## Supported migration paths

GitHub Enterprise Importer supports migrations **to** GitHub Enterprise Cloud (GitHub.com or GHE.com) **from** the following sources.

* Azure DevOps (ADO) Cloud
* Bitbucket Server and Bitbucket Data Center 5.14+
* GitHub.com
* GitHub Enterprise Server (GHES) 3.4.1+
* GHE.com (only when the destination is a different enterprise on GHE.com)
* GitLab (GitLab.com or [maintained self-hosted versions](https://docs.gitlab.com/policy/maintenance/#maintained-versions))

### Alternative tooling for GitHub Enterprise Server to GHE.com

In supported patch releases in version 3.17 and later, Enterprise Live Migrations is available as an alternative tool for migrations from GitHub Enterprise Server to GHE.com. Enterprise Live Migrations reduces downtime for developers during the migration and offers better support for large monorepos. See [AUTOTITLE](/migrations/elm/about-live-migrations).

## Getting started

To learn more about the migration path you require, and the data that GitHub Enterprise Importer migrates, see the following articles.

{% ifversion fpt or ghec %}
* [AUTOTITLE](/migrations/using-github-enterprise-importer/ado/understand-migrations-from-azure-devops-to-github)
{% endif %}
* [AUTOTITLE](/migrations/using-github-enterprise-importer/migrating-from-bitbucket-server-to-github-enterprise-cloud/about-migrations-from-bitbucket-server-to-github-enterprise-cloud)
* [AUTOTITLE](/migrations/using-github-enterprise-importer/migrating-between-github-products/about-migrations-between-github-products)
