---
title: Importing a repository with GitHub Importer
intro: 'If you have a project hosted on another Git-based hosting service, you can quickly import it to GitHub using the GitHub Importer tool.'
redirect_from:
  - /articles/importing-from-other-version-control-systems-to-github
  - /articles/importing-a-repository-with-github-importer
  - /github/importing-your-projects-to-github/importing-a-repository-with-github-importer
  - /github/importing-your-projects-to-github/importing-source-code-to-github/importing-a-repository-with-github-importer
  - /get-started/importing-your-projects-to-github/importing-source-code-to-github/importing-a-repository-with-github-importer
versions:
  fpt: '*'
  ghec: '*'
shortTitle: Import a repository
category:
  - Import source code
---

## About repository imports with GitHub Importer

GitHub Importer imports the source code and commit history of Git repositories hosted on external hosting services. For more information about the capabilities and limitations of GitHub Importer, see [AUTOTITLE](/migrations/importing-source-code/using-github-importer/about-github-importer#capabilities-and-limitations-of-github-importer).

GitHub uses the email address in the commit header to link a commit to a GitHub user. To correctly attribute commits in an imported repository, users will need to add the email address associated with their commits to their GitHub account. For more information, see [AUTOTITLE](/account-and-profile/how-tos/email-preferences/adding-an-email-address-to-your-github-account).

## Importing a repository with GitHub Importer

When you import a repository using the GitHub Importer, a new repository will be created. If you already have an existing repository you want to use, you can instead add your local repository to GitHub using Git. For more information, see [AUTOTITLE](/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github#importing-a-git-repository-with-the-command-line).

1. In the upper-right corner of any page on GitHub.com, click (icon: plus), and then click **Import repository**.

   ![Screenshot of the top-right corner of any page on GitHub. A plus icon is highlighted with an orange outline.](/assets/images/help/importer/import-repository.png)

1. On the "Import your project to GitHub" page, enter the URL for the remote repository hosted on another platform.
1. If the source repository is private, enter credentials for authentication. GitHub Importer will use the credentials to perform a `git clone` operation on the source repository.
1. Choose an owner and a name for the new repository on GitHub.
1. Choose the visibility of the new repository. For more information, see [AUTOTITLE](/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility).
1. Click **Begin import**.

You'll be redirected to a "Preparing your new repository" page, where you can track the status of your import. You'll receive an email when the repository has been completely imported.
