---
title: Follow-up tasks
shortTitle: 6. Follow-up tasks
intro: After each migration has finished, you'll need to complete some additional tasks before the repository is ready for work.
versions:
  fpt: '*'
  ghec: '*'
contentType: other
docsTeamMetrics:
  - ado-migration
category:
  - Migrate from Azure DevOps
redirect_from:
  - /migrations/ado/phase-6-follow-up-tasks
  - /migrations/ado/follow-up-tasks
---

## Checking the migration status

First, check whether your migration succeeded or failed.

The way you check the status of your migration depends on how you ran the migration.

* If you ran the migration using the GitHub CLI, by default, the process will display whether the migration succeeded or failed once the migration is complete. If the migration failed, you will see the reason for failure.

  ```text
  Migration completed (ID: RM_123)! State: SUCCEEDED
  ```

* If you ran the migration using the GitHub CLI with the optional `--queue-only` argument, the process will exit immediately after queueing the migration, and will not tell you if the migration succeeded or failed. You can check a migration's status using the `wait-for-migration` command, or by reviewing the migration log.

## Reviewing the migration log

You should review the migration log for each migrated repository. People with read access to a repository can access the migration log for the repository on GitHub.

1. Navigate to the migrated repository in your destination organization.
1. Under your repository name, click **(icon: issue-opened) Issues**.

   ![Screenshot of the main page of a repository. In the horizontal navigation bar, a tab, labeled "Issues," is outlined in dark orange.](/assets/images/help/repository/repo-tabs-issues-global-nav-update.png)
1. Click the issue with the title "Migration Log."

For more information, see [AUTOTITLE](/migrations/using-github-enterprise-importer/completing-your-migration-with-github-enterprise-importer/accessing-your-migration-logs-for-github-enterprise-importer).

## Setting repository visibility

All repositories are migrated as private by default, and only the user that ran the migration and organization owners will have access to the repository. If you don't want the repository to be private, change the visibility.

* You can change a repository's visibility in the browser. For more information, see [AUTOTITLE](/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility).
* Alternatively, you can use GitHub CLI to change repository visibility from the command line. For more information, see [`gh repo edit`](https://cli.github.com/manual/gh_repo_edit) in the GitHub CLI documentation.

   For example, replace YOUR_ORG with your organization name, and the command below will set all of the organization's repositories to internal visibility.

   ```bash copy
   export ORG=YOUR_ORG
   gh repo list "$ORG" --limit 100000 --json name -q '.[].name' | xargs -I{} gh repo edit "$ORG/{}" --visibility internal
   ```

## Reclaiming mannequins

After you run a migration with GitHub Enterprise Importer or Enterprise Live Migrations, all user activity in the migrated repository (except Git commits) is attributed to placeholder identities called mannequins.

> [!NOTE]
> Only organization owners can reclaim mannequins. If you've been granted the migrator role, contact an organization owner to perform this step.

1. Decide if you want to reclaim mannequins.
1. Plan when you'll complete reclaims.
1. Reclaim mannequins. You can reattribute the history for each mannequin to an organization member with the GitHub CLI or in your browser. If you use the GitHub CLI, you can reclaim mannequins in bulk. For more information, see [AUTOTITLE](/migrations/using-github-enterprise-importer/completing-your-migration-with-github-enterprise-importer/reclaiming-mannequins-for-github-enterprise-importer).
1. If any of the members do not already have appropriate access to the repository via team membership, give the members access to the repository. For more information, see [AUTOTITLE](/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/managing-an-individuals-access-to-an-organization-repository).

## Configuring IP allow lists

If you added the IP ranges for GitHub Enterprise Importer to the IP allow list for your destination organization, you can remove those entries. If you disabled your identity provider's IP allow list restrictions for your destination enterprise, you can re-enable them now.

## Configure Azure Pipelines and Azure Boards

If you used Azure Pipelines or Azure Boards previously and want to continue using them with your repositories now they are hosted on GitHub, you can follow these guides on Microsoft Learn to configure the relevant extension.

* [Connect Azure Pipelines to GitHub](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/github)
* [Configure the Azure Boards app for GitHub](https://learn.microsoft.com/en-us/azure/devops/boards/github/install-github-app)

## Supporting your developers in their new environment

There are some difference between Azure DevOps and GitHub that would be helpful for you and your developers to know. Share [AUTOTITLE](/migrations/using-github-enterprise-importer/ado/key-differences-between-azure-devops-and-github) with them.
