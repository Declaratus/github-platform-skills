---
title: Dependency graph supported package ecosystems
shortTitle: Dependency graph ecosystems
intro: Dependency graph supports a variety of ecosystems.
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
redirect_from:
  - /code-security/supply-chain-security/understanding-your-software-supply-chain/dependency-graph-supported-package-ecosystems
contentType: reference
category:
  - Secure your dependencies
---

## Understanding the table

The dependency graph supports different methods of submitting data for direct and indirect (transitive) dependencies. See [AUTOTITLE](/code-security/concepts/supply-chain-security/dependency-graph-data).

In the table below:

* The **Static transitive dependencies**, **Dependabot graph jobs** (currently not available for GitHub Enterprise Server), and **Automatic dependency submission** columns show you supported methods for submitting data.
* The **Static transitive dependencies** column also indicates whether static analysis will add `direct` and `transitive` labels for dependent packages in that ecosystem.
* The **Dependabot graph jobs** column indicates whether Dependabot can generate dependency graphs using its own job infrastructure. Where supported, this method takes precedence over automatic dependency submission. See [AUTOTITLE](/code-security/concepts/supply-chain-security/dependency-graph-data#dependabot-graph-jobs).
* The **Recommended files** column suggests formats that explicitly define which versions are used for all direct and all indirect dependencies. These files lock the package versions to those included in the build and enable Dependabot to find vulnerable versions in both direct and indirect dependencies.

## Supported package ecosystems

| Package manager | Languages | Static transitive dependencies | Dependabot graph jobs | Automatic dependency submission | Recommended files | Additional files |
| --- | --- | --- | --- | --- | --- | --- |
| {% ifversion dependabot-bazel-support %} |
| Bazel | Starlark | (icon: x) | (icon: x) | (icon: x) | `MODULE.bazel`, `WORKSPACE` | `MODULE.bazel.lock`, `maven_install.json`, `*.MODULE.bazel` |
| {% endif %} |
| Cargo | Rust | (icon: x) | (icon: x) | (icon: x) | `Cargo.lock` | `Cargo.toml` |
| Composer             | PHP           | (icon: x) | (icon: x) | (icon: x) | `composer.lock` | `composer.json` |
| {% ifversion dependabot-deno-support %} |
| Deno | TypeScript, JavaScript | (icon: x) | (icon: x) | (icon: x) | `deno.lock` | `deno.json`, `deno.jsonc` |
| {% endif %} |
| NuGet | .NET languages (C#, F#, VB), C++  | (icon: x) | (icon: x) | (icon: check) | `.csproj`, `.vbproj`, `.nuspec`, `.vcxproj`, `.fsproj` | `packages.config` |
| GitHub Actions workflows | YAML | (icon: x) | (icon: x) | (icon: x) | `.yml`, `.yaml` | (icon: x) |
| Go modules | Go | (icon: x) | (icon: check) | (icon: x) |  `go.mod`| (icon: x) |
| Gradle | Java  | (icon: x) | (icon: x) | (icon: check) |  (icon: x) | (icon: x) |
| {% ifversion dependabot-julia-support %} |
| Julia | Julia | (icon: x) | (icon: x) | (icon: x) | `Manifest.toml` | `Project.toml` |
| {% endif %} |
| Maven | Java, Scala | (icon: check) | (icon: x) | (icon: check) | `pom.xml`  | (icon: x)  |
| npm | JavaScript | (icon: check) | (icon: x) | (icon: x) | `package-lock.json` | `package.json`|
| {% ifversion dependabot-opentofu-support %} |
| OpenTofu | HCL | (icon: x) | (icon: x) | (icon: x) | `.terraform.lock.hcl` | `.tf`, `.tofu` |
| {% endif %} |
| pip             | Python                    | (icon: x) | (icon: check) | (icon: check) | `requirements.txt`, `pipfile.lock` | `pipfile`, `setup.py` |
| pnpm             | JavaScript                    | (icon: check) | (icon: x) | (icon: x) | `pnpm-lock.yaml` | `package.json` |
| pub             | Dart                    | (icon: x) | (icon: x) | (icon: x) | `pubspec.lock` | `pubspec.yaml` |
| Poetry | Python                    | (icon: x) | (icon: check) | (icon: check) | `poetry.lock` | `pyproject.toml` |
| RubyGems             | Ruby           | (icon: x) | (icon: x) | (icon: x) | `Gemfile.lock` | `Gemfile`, `*.gemspec` |
| Swift Package Manager | Swift | (icon: x) | (icon: x) | (icon: x) | `Package.resolved` | (icon: x) |
| Yarn | JavaScript | (icon: check) | (icon: x) | (icon: x) | `yarn.lock` | `package.json` |

> [!NOTE]
> * If you list your Python dependencies within a `setup.py` file, we may not be able to parse and list every dependency in your project.
> * GitHub Actions workflows must be located in the `.github/workflows/` directory of a repository to be recognized as manifests. Any actions or workflows referenced using the syntax `jobs[*].steps[*].uses` or `jobs.<job_id>.uses` will be parsed as dependencies. For more information, see [AUTOTITLE](/actions/reference/workflows-and-actions/workflow-syntax).
> * For GitHub Actions, alerts are only generated for actions that use semantic versioning, not SHA versioning. For more information, see [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-alerts) and [AUTOTITLE](/code-security/concepts/supply-chain-security/dependabot-version-updates).
{% ifversion dependabot-npm12-pnpm11-pnpm12-bun14 %}> * When pnpm writes `pnpm-lock.yaml` as two YAML documents, the dependency graph does not detect the dependencies in that file. This is the default format for pnpm 12 projects that pin a pnpm version. For more information, see [AUTOTITLE](/code-security/reference/supply-chain-security/supported-ecosystems-and-repositories#pnpm).{% endif %}

{% ifversion dependabot-community-ecosystems %}

### Community-maintained ecosystems

The following ecosystems are maintained by their upstream community maintainers. GitHub integrates Dependabot with these ecosystems but does not maintain them directly.

| Ecosystem | Maintained by |
| --- | --- |
| {% ifversion dependabot-julia-support %} |
| Julia | Julia community |
| {% endif %} |
| {% ifversion dependabot-opentofu-support %} |
| OpenTofu | OpenTofu community |
| {% endif %} |
| pub | Dart community |

{% endif %}

