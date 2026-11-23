---
title: CodeQL for VS Code
shortTitle: CodeQL for VS Code
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
product: "CodeQL is available for the following repository types:\n\n{%- ifversion fpt %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghec %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{% endif %}"
intro: You can write, run, and test CodeQL queries inside Visual Studio Code with the CodeQL extension.
redirect_from:
  - /code-security/codeql-for-vs-code/about-codeql-for-visual-studio-code
  - /code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/about-codeql-for-vs-code
  - /code-security/concepts/code-scanning/codeql/about-codeql-for-vs-code
contentType: concepts
category:
  - Customize vulnerability detection with CodeQL
---

## About CodeQL for Visual Studio Code

You can run CodeQL queries on databases generated from source code, in order to find errors and security vulnerabilities in a codebase. For more information about CodeQL code scanning, see [AUTOTITLE](/code-security/concepts/code-scanning/codeql/codeql-code-scanning).

With the CodeQL for Visual Studio Code extension, you can:

* Write custom CodeQL queries and supporting libraries.
* Directly view and use the CodeQL security queries from the large, open-source [`github/codeql`](https://github.com/github/codeql) repository.
* Run queries over one or more CodeQL databases.
* Track the flow of data through a program, highlighting areas that are potential security vulnerabilities.
* View, create, and edit all types of CodeQL packs of queries or libraries that you can use or publish to share with others.
* Run unit tests for CodeQL queries.
* Use a dedicated editor for viewing, creating, and editing CodeQL model packs, which are used to extend standard CodeQL analysis.

The CodeQL for Visual Studio Code extension also adds a CodeQL sidebar view to VS Code. This contains a list of local CodeQL databases, an overview of the queries that you have run in the current session, and a variant analysis view for large-scale analysis.

### IntelliSense

The extension provides standard IntelliSense features for query files (extension `.ql`) and library files (extension `.qll`) that you open in the VS Code editor. These include:

* Syntax highlighting
* Right-click options (such as **Go To Definition**)
* Autocomplete suggestions
* Hover information

For more information about Intellisense in VS Code, see [IntelliSense](https://code.visualstudio.com/docs/editor/intellisense) in the Visual Studio Code documentation.

You can also use the VS Code **Format Document** command to format your code according to the [CodeQL style guide](https://github.com/github/codeql/blob/main/docs/ql-style-guide.md).

### The VS Code Command Palette

You can run commands for the CodeQL for Visual Studio Code extension from the VS Code Command Palette. For more information about the VS Code Command Palette, see [User Interface](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) in the VS Code documentation.

## Data and telemetry

If you specifically opt in to permit GitHub to do so, GitHub will collect usage data and metrics for the purposes of helping the core developers to improve the CodeQL for Visual Studio Code extension. For more information, see [AUTOTITLE](/code-security/reference/code-scanning/codeql/codeql-for-vs-code/telemetry-in-codeql-for-visual-studio-code).

## About the GitHub CodeQL license

**License notice:** If you don’t have a license for GitHub Code Security then, by installing this product, you are agreeing to the [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md).

{% ifversion ghec %}For information about how you can try GitHub Advanced Security for free, see [AUTOTITLE](/code-security/tutorials/trialing-github-advanced-security/trial-advanced-security).
{% elsif fpt %}For information about how you can try GitHub Enterprise with GitHub Advanced Security for free, see [AUTOTITLE](/enterprise-cloud@latest/admin/overview/setting-up-a-trial-of-github-enterprise-cloud) and [AUTOTITLE](/enterprise-cloud@latest/code-security/tutorials/trialing-github-advanced-security/trial-advanced-security#setting-up-your-trial-of-github-advanced-security) in the GitHub Enterprise Cloud documentation.{% endif %}

## Next steps

To learn about how to install the CodeQL for Visual Studio Code extension, see [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/scan-from-vs-code/install-codeql-for-vs-code).
