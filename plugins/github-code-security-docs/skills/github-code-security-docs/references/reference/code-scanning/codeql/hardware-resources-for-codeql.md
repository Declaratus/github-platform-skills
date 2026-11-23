---
title: Recommended hardware resources for running CodeQL
shortTitle: Hardware resources for CodeQL
intro: Recommended specifications (RAM, CPU cores, and disk) for running CodeQL analysis on self-hosted machines, based on the size of your codebase.
product: "CodeQL is available for the following repository types:\n\n{%- ifversion fpt %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghec %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{% endif %}"
redirect_from:
  - /code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/recommended-hardware-resources-for-running-codeql
  - /code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/recommended-hardware-resources-for-running-codeql
  - /code-security/reference/code-scanning/codeql/recommended-hardware-resources-for-running-codeql
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
contentType: reference
category:
  - Find CodeQL CLI commands
---
You can configure CodeQL on GitHub Actions or on an external CI system. CodeQL is fully compatible with GitHub-hosted runners on GitHub Actions.

If you're using an external CI system, or self-hosted runners on GitHub Actions for private repositories, you're responsible for configuring your own hardware. The optimal hardware configuration for running CodeQL may vary based on the size and complexity of your codebase, the programming languages and build systems being used, and your CI workflow configuration.

The table below provides recommended hardware specifications for running CodeQL analysis, based on the size of your codebase. Use these as a starting point for determining your choice of hardware or virtual machine. A machine with greater resources may improve analysis performance, but may also be more expensive to maintain.

| Codebase size | RAM | CPU |
|--------|--------|--------|
| Small (<100 K lines of code) | 8 GB or higher | 2 cores |
| Medium (100 K to 1 M lines of code) | 16 GB or higher | 4 or 8 cores |
| Large (>1 M lines of code) | 64 GB or higher | 8 cores |

For all codebase sizes, we recommend using an SSD with 14 GB or more of disk space. There must be enough disk space to check out and build your code, plus additional space for data produced by CodeQL.
