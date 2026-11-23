---
title: About GitHub Importer
intro: "If your source code is stored on another Git-based hosting service, you can move the code to GitHub.com using GitHub Importer."
redirect_from:
  - /articles/about-github-importer
  - /github/importing-your-projects-to-github/about-github-importer
  - /github/importing-your-projects-to-github/importing-source-code-to-github/about-github-importer
  - /get-started/importing-your-projects-to-github/importing-source-code-to-github/about-github-importer
  - /articles/updating-commit-author-attribution-with-github-importer
  - /github/importing-your-projects-to-github/updating-commit-author-attribution-with-github-importer
  - /github/importing-your-projects-to-github/importing-source-code-to-github/updating-commit-author-attribution-with-github-importer
  - /get-started/importing-your-projects-to-github/importing-source-code-to-github/updating-commit-author-attribution-with-github-importer
  - /migrations/importing-source-code/using-github-importer/updating-commit-author-attribution-with-github-importer
versions:
  fpt: '*'
  ghec: '*'
category:
  - Import source code
---

## About GitHub Importer

GitHub Importer is a tool that quickly imports Git repositories from other hosting services to GitHub.com.

To get started with GitHub Importer, see [AUTOTITLE](/migrations/importing-source-code/using-github-importer/importing-a-repository-with-github-importer#importing-a-repository-with-github-importer).

## Capabilities and limitations of GitHub Importer

* GitHub Importer imports the source code and commit history of a repository. It does not import other associated data from the hosting service, such as issues and pull requests.
* GitHub Importer is only available on GitHub.com.
* During an import, you can authenticate with your remote repository. The repository must be accessible from the public internet. If the repository is hosted on a private network, GitHub Importer won't be able to access it.
* GitHub Importer does not support repositories that use version control systems other than Git, such as Mercurial, Subversion, or Team Foundation Version Control (TFVC). For more information about alternatives to GitHub Importer, see [AUTOTITLE](/migrations/importing-source-code/using-the-command-line-to-import-source-code/about-source-code-imports-using-the-command-line).
* Repositories and individual files on GitHub are subject to size limits. For more information, see [AUTOTITLE](/repositories/working-with-files/managing-large-files/about-large-files-on-github).
* GitHub Importer does not move Git Large File Storage (LFS) objects from the source repository to the target repository. If you use Git LFS, you will need to either convert the Git LFS objects to regular files tracked by Git before running the migration, or move the Git LFS objects to the new repository separately after running the migration.

## Further reading

* [AUTOTITLE](/migrations/importing-source-code/using-the-command-line-to-import-source-code/importing-an-external-git-repository-using-the-command-line)
