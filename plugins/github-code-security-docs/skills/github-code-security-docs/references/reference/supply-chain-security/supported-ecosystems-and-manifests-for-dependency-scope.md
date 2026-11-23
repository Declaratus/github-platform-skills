---
title: Supported ecosystems and manifests for dependency scope
intro: 'Dependabot alerts supports a variety of ecosystems and manifests for dependency scope.'
allowTitleToDifferFromFilename: true
versions:
  fpt: '*'
  ghec: '*'
  ghes: '*'
shortTitle: Dependency scope
contentType: reference
category:
  - Secure your dependencies
---

The table below summarizes whether dependency scope is supported for various ecosystems and manifests, that is, whether Dependabot can identify if a dependency is used for development or production.

| **Language** | **Ecosystem** | **Manifest file** | **Dependency scope supported** |
|:---|:---:|:---:|:---|
| Dart | pub | pubspec.yaml |  (icon: check) |
| Dart | pub | pubspec.lock |  (icon: check) |
| Go | Go modules | go.mod | No, defaults to runtime |
| Java | Maven | pom.xml | (icon: check) `test` maps to development, else scope defaults to runtime |
| JavaScript | npm | package.json | (icon: check) |
| JavaScript | npm | package-lock.json | (icon: check) |
| JavaScript | npm | pnpm-lock.yaml | (icon: check) |
| JavaScript |	yarn v1 | yarn.lock | No, defaults to runtime |
| PHP | Composer | composer.json | (icon: check) |
| PHP | Composer | composer.lock | (icon: check) |
| Python | Poetry | poetry.lock | (icon: check) |
| Python | Poetry | pyproject.toml | (icon: check) |
| Python | pip | requirements.txt | (icon: check) Scope is development if the filename contains `test` or `dev`, else it is runtime |
| Python | pip | pipfile.lock | (icon: check) |
| Python | pip | pipfile | (icon: check) |
| Ruby | RubyGems | Gemfile |	(icon: check) |
| Ruby | RubyGems | Gemfile.lock	| No, defaults to runtime |
| Rust | Cargo | Cargo.toml | (icon: check) |
| Rust | Cargo | Cargo.lock | No, defaults to runtime |
| YAML | GitHub Actions | - | No, defaults to runtime |
| .NET (C#, F#, VB, etc.) | NuGet | .csproj / .vbproj .vcxproj / .fsproj | No, defaults to runtime |
| .NET | NuGet | packages.config | No, defaults to runtime |
| .NET | NuGet | .nuspec | (icon: check) When the tag != runtime |
