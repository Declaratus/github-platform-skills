---
title: Creating CodeQL CLI database bundles
shortTitle: Create database bundles
intro: Create a database bundle with CodeQL troubleshooting information.
allowTitleToDifferFromFilename: true
product: "CodeQL is available for the following repository types:\n\n{%- ifversion fpt %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghec %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{% endif %}"
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/how-tos/find-and-fix-code-vulnerabilities/scan-from-the-command-line/creating-database-bundle-for-troubleshooting
  - /code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/creating-database-bundle-for-troubleshooting
  - /code-security/how-tos/scan-code-for-vulnerabilities/scan-from-the-command-line/creating-database-bundle-for-troubleshooting
contentType: how-tos
category:
  - Customize vulnerability detection with CodeQL
---

> [!WARNING]
> CodeQL CLI database bundles contain a copy of the source code being analyzed by CodeQL, therefore we suggest sharing these bundles only with people who are authorized to access that source code.

{% ifversion ghes %}

> [!NOTE]
> This article describes the features available with the CodeQL CLI {% ifversion ghes < 3.20 %}2.22.4{% elsif ghes < 3.21 %}2.23.9{% elsif ghes < 3.22 %}2.24.3{% elsif ghes < 3.23 %}2.25.6{% endif %} bundle included in the initial release of GitHub Enterprise Server {{ allVersions[currentVersion].currentRelease }}.
>
> If your site administrator has updated your CodeQL CLI version to a newer release, please see the [GitHub Enterprise Cloud version](/enterprise-cloud@latest/{{ currentArticle }}) of this article for information on the latest features.

{% endif %}

The following CodeQL CLI command syntax is suggested when creating a database bundle for troubleshooting purposes. This sample `database bundle` command requires CodeQL CLI version 2.17.6 or higher.

```shell
codeql database bundle --output=codeql-debug-artifacts.zip --include-diagnostics --include-logs --include-results -- <dir>
```

For this command, `<dir>` must be the path to the directory where the CodeQL database was created.

The successful command execution creates a zip file called `codeql-debug-artifacts.zip` which contains CodeQL troubleshooting information. That file is the database bundle.

This command assumes that the `--log-dir` command line argument was not used for the `database create` and `database analyze` commands. When that command line argument is used, the log files created by those commands will not be included with the database bundle.

## Increasing the verbosity for `database create` and `database analyze`

If the `database create` and `database analyze` commands are not detailed enough for troubleshooting purposes, you can increase their verbosity.

Both commands support the `--verbosity` command line argument which can be set to `progress++` prior to creating a database bundle.
