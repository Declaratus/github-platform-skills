---
title: Publishing and using CodeQL packs
shortTitle: Publish and use packs
intro: Share or download a CodeQL pack, then analyze your CodeQL database.
product: "CodeQL is available for the following repository types:\n\n{%- ifversion fpt %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghec %}\n* Public repositories on GitHub.com, see [GitHub CodeQL Terms and Conditions](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md)\n* Organization-owned repositories on GitHub Team or GitHub Enterprise Cloud with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{%- elsif ghes %}\n* Organization-owned repositories with [GitHub Code Security](/get-started/learning-about-github/about-github-advanced-security) enabled\n\n{% endif %}"
versions:
  fpt: '*'
  ghes: '*'
  ghec: '*'
redirect_from:
  - /code-security/codeql-cli/publishing-and-using-codeql-packs
  - /code-security/codeql-cli/using-the-codeql-cli/publishing-and-using-codeql-packs
  - /code-security/codeql-cli/using-the-advanced-functionality-of-the-codeql-cli/publishing-and-using-codeql-packs
  - /code-security/tutorials/customize-code-scanning/publishing-and-using-codeql-packs
  - /code-security/how-tos/scan-code-for-vulnerabilities/scan-from-the-command-line/publish-and-use-packs
contentType: how-tos
category:
  - Customize vulnerability detection with CodeQL
---

{% ifversion ghec or ghes %}

## Working with CodeQL packs on {% ifversion ghec %}GitHub Enterprise Cloud with data residency{% elsif ghes %}GitHub Enterprise Server{% endif %}

By default, the CodeQL CLI expects to download CodeQL packs from and publish packs to the Container registry on GitHub.com. However, you can also work with CodeQL packs in a Container registry on {% ifversion ghec %}GitHub Enterprise Cloud with data residency{% elsif ghes %}GitHub Enterprise Server{% endif %} by creating a `qlconfig.yml` file to tell the CLI which Container registry to use for each pack.

Create a `~/.codeql/qlconfig.yml` file on Linux/MacOS or `%HOMEPATH%\.codeql\qlconfig.yml` on Windows using your preferred text editor, and add entries to specify which registry to use for one or more package name patterns.
For example, the following `qlconfig.yml` file associates all packs with the Container registry at `{% ifversion ghec %}SUBDOMAIN.ghe.com{% elsif ghes %}https://GHE_HOSTNAME{% endif %}`, except packs matching `codeql/\*` or the `other-org/*` organization, which are associated with the Container registry on GitHub.com:

```yaml
registries:
- packages:
  - 'codeql/*'
  - 'other-org/*'
  # Container registry on GitHub.com
  url: https://ghcr.io/v2/
- packages: '*'
  # Container registry hosted at `{% ifversion ghec %}SUBDOMAIN.ghe.com{% elsif ghes %}https://GHE_HOSTNAME{% endif %}`
  url: {% ifversion ghes %}https://containers.GHE_HOSTNAME/v2/{% elsif ghec %}https://containers.SUBDOMAIN.ghe.com{% endif %}
```

The CodeQL CLI will determine which registry to use for a given package name by finding the first item in the `registries` list with a `packages` property that matches that package name.
This means that you’ll generally want to define the most specific package name patterns first. The `packages` property may be a single package name, a glob pattern, or a YAML list of package names and glob patterns.

The `registries` list can also be placed inside a `codeql-workspace.yml` file. Doing so will allow you to define the registries to be used within a specific workspace, so that it can be shared amongst other CodeQL users of the workspace. The `registries` list in `codeql-workspace.yml` will be merged with and take precedence over the list in the global `qlconfig.yml`. For more information about `codeql-workspace.yml`, see [AUTOTITLE](/code-security/concepts/code-scanning/codeql/codeql-workspaces#about-codeql-workspaces).

You can now use `codeql pack publish`, `codeql pack download`, and `codeql database analyze` to manage packs on {% ifversion ghec %}GitHub Enterprise Cloud with data residency{% elsif ghes %}GitHub Enterprise Server{% endif %}.

{% endif %}

## Authenticating to GitHub Container registries

You can publish packs and download private packs by authenticating to the appropriate GitHub Container registry.

{% ifversion ghec or ghes %}

### Authenticating to Container registries on GitHub.com

{% endif %}

You can authenticate to the Container registry in two ways:

1. Pass the `--github-auth-stdin` option to the CodeQL CLI, then supply a GitHub Apps token or personal access token via standard input.
1. Set the `GITHUB_TOKEN` environment variable to a GitHub Apps token or personal access token.

{% ifversion ghec or ghes %}

### Authenticating to Container registries on {% ifversion ghec %}GitHub Enterprise Cloud with data residency{% elsif ghes %}GitHub Enterprise Server{% endif %}

Similarly, you can authenticate to a Container registry on {% ifversion ghec %}GitHub Enterprise Cloud with data residency{% elsif ghes %}GitHub Enterprise Server{% endif %}, or authenticate to multiple registries simultaneously (for example, to download or run private packs from multiple registries) in two ways:

1. Pass the `--registries-auth-stdin` option to the CodeQL CLI, then supply a registry authentication string via standard input.
1. Set the `CODEQL_REGISTRIES_AUTH` environment variable to a registry authentication string.

A registry authentication string is a comma-separated list of `<registry-url>=<token>` pairs, where `registry-url` is a Container registry URL, such as `{% ifversion ghes %}https://containers.GHE_HOSTNAME/v2/{% elsif ghec %}https://containers.SUBDOMAIN.ghe.com{% endif %}`, and `token` is a GitHub Apps token or personal access token for that Container registry.
This ensures that each token is only passed to the Container registry you specify.

For example, the following registry authentication string specifies that the CodeQL CLI should authenticate as follows:

* Use the token `<token1>` to authenticate to Container registry on GitHub.com.
* Use the token `<token2>` to authenticate to the Container registry for the enterprise at `{% ifversion ghes %}https://containers.GHE_HOSTNAME/v2/{% elsif ghec %}https://containers.SUBDOMAIN.ghe.com{% endif %}`.

```shell
https://ghcr.io/v2/=<token1>,{% ifversion ghes %}https://containers.GHE_HOSTNAME/v2/{% elsif ghec %}https://containers.SUBDOMAIN.ghe.com{% endif %}=<token2>
```

{% endif %}

## Publishing your CodeQL pack

To share your CodeQL pack with other people, you can publish it to the Container registry.

### Configuring the `qlpack.yml` file before publishing

{% ifversion ghes %}

> [!NOTE]
> This article describes the features available with the CodeQL CLI {% ifversion ghes < 3.20 %}2.22.4{% elsif ghes < 3.21 %}2.23.9{% elsif ghes < 3.22 %}2.24.3{% elsif ghes < 3.23 %}2.25.6{% elsif ghes < 3.24 %}2.27.0{% endif %} bundle included in the initial release of GitHub Enterprise Server {{ allVersions[currentVersion].currentRelease }}.
>
> If your site administrator has updated your CodeQL CLI version to a newer release, please see the [GitHub Enterprise Cloud version](/enterprise-cloud@latest/{{ currentArticle }}) of this article for information on the latest features.

{% endif %}

You can check and modify the configuration details of your CodeQL pack prior to publishing. Open the `qlpack.yml` file in your preferred text editor.

```yaml
library: # set to true if the pack is a library. Set to false or omit for a query pack
name: <scope>/<pack>
version: <x.x.x>
description: <Description to publish with the package>
defaultSuite: # optional, one or more queries in the pack to run by default
    - query: <relative-path>/query-file>.ql
defaultSuiteFile: default-queries.qls # optional, a pointer to a query-suite in this pack
license: # optional, the license under which the pack is published
dependencies: # map from CodeQL pack name to version range
```

* `name:` must follow the `<scope>/<pack>` format, where `<scope>` is the GitHub organization that you will publish to and `<pack>` is the name for the pack.

* A maximum of one of `defaultSuite` or `defaultSuiteFile` is allowed. These are two different ways to define a default query suite to be run, the first by specifying queries directly in the qlpack.yml file and the second by specifying a query suite in the pack.

### Running `codeql pack publish`

When you are ready to publish a pack to the GitHub Container registry, you can run the following command in the root of the pack directory:

```shell
codeql pack publish
```

The published package will be displayed in the packages section of GitHub organization specified by the scope in the `qlpack.yml` file.

> [!NOTE]
> If you're publishing model packs to the GitHub Container registry in order to extend coverage to all repositories in an organization as part of a default setup configuration, then you need to ensure that repositories running code scanning can access those model packs. For more information, see [AUTOTITLE](/code-security/how-tos/find-and-fix-code-vulnerabilities/manage-your-configuration/edit-default-setup) and [AUTOTITLE](/packages/learn-github-packages/configuring-a-packages-access-control-and-visibility).

## Downloading an existing CodeQL pack

To run a pack that someone else has created, you must first download it by running the following command:

```shell
codeql pack download <scope>/<pack>@x.x.x
```

* `<scope>`: the name of the GitHub organization that you will download from.
* `<pack>`: the name for the pack that you want to download.
* `@x.x.x`: an optional version number. If omitted, the latest version will be downloaded.

This command accepts arguments for multiple packs.

If you write scripts that specify a particular version number of a
query pack to download, keep in mind that when you update your version of
CodeQL to a newer one, you may
also need to switch to a newer version of the query pack. Newer
versions of CodeQL _may_ provide
degraded performance when used with query packs that have been pinned
to a very old version. For more information, see [AUTOTITLE](/code-security/reference/code-scanning/codeql/codeql-cli/codeql-query-packs#codeql-pack-compatibility).

## Using a CodeQL pack to analyze a CodeQL database

To analyze a CodeQL database with a CodeQL pack, run the following command:

```shell
codeql database analyze <database> <scope>/<pack>@x.x.x:<path>
```

* `<database>`: the CodeQL database to be analyzed.
* `<scope>`: the name of the GitHub organization that the pack is published to.
* `<pack>`: the name for the pack that you are using.
* `@x.x.x`: an optional version number. If omitted, the latest version will be used.
* `:<path>`: an optional path to a query, directory, or query suite. If omitted, the pack’s default query suite will be used.

The `analyze` command will run the default suite of any specified CodeQL packs. You can specify multiple CodeQL packs to be used for analyzing a CodeQL database. For example:

```shell
codeql <database> analyze <scope>/<pack> <scope>/<other-pack>
```

> [!NOTE]
> The `codeql pack download` command stores the pack it downloads in an internal location that is not intended for local modification. Unexpected (and hard to troubleshoot) behavior may result if the pack is modified after downloading. For more information about customizing packs, see [AUTOTITLE](/code-security/tutorials/customize-code-scanning/create-and-work-with-codeql-packs).
