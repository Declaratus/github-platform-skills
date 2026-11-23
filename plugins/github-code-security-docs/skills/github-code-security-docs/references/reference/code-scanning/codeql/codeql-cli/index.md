---
title: Using the advanced functionality of the CodeQL CLI
intro: You can use the CodeQL CLI to locally develop, test and run CodeQL queries on software projects.
product: "CodeQL is available for the following repository types:\n\n{%- ifversion fpt %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghec %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{% endif %}"
shortTitle: CodeQL CLI
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
children:
  - /sarif-output
  - /csv-output
  - /codeql-query-packs
  - /extractor-options
  - /exit-codes
redirect_from:
  - /code-security/codeql-cli/codeql-cli-reference
  - /code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli
contentType: reference
---
