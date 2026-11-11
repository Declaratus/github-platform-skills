---
title: Copilot feature matrix
intro: Identify which IDEs support which GitHub Copilot features.
versions:
  feature: copilot
category:
  - Learn about Copilot
contentType: reference
---

> [!NOTE]
> The GitHub Copilot feature matrix is currently in public preview and is subject to change.

GitHub recommends using the latest stable IDE and Copilot extension versions to get the best Copilot experience. 

**Key:**


* ✓ = supported
* ✗ = not supported
* P = under preview
* C = closing down

{% ides %}

## Features by IDE

The following table shows supported Copilot features in the latest version of each IDE.

| Feature | VS Code | Visual Studio | JetBrains | Eclipse | Xcode | NeoVim |
|:----|:----:|:----:|:----:|:----:|:----:|:----:|
| .NET Upgrade Agent |✗ |✓ |✗ |✗ |✗ |✗ |
| Agent skills |✓ |✓ |P |✗ |✗ |✗ |
| Agent mode |✓ |✓ |✓ |✓ |✓ |✗ |
| BYOK |P |✓ |P |P |P |✗ |
| Chat |✓ |✓ |✓ |✓ |✓ |✗ |
| Checkpoints |✓ |✓ |✓ |✗ |✓ |✗ |
| Code completion |✓ |✓ |✓ |✓ |✓ |✓ |
| Code referencing |✓ |✓ |✓ |✓ |✗ |✗ |
| Copilot code review |✓ |✓ |✓ |✗ |✓ |✗ |
| Custom agents |✓ |✓ |P |✓ |P |✗ |
| Custom instructions |✓ |✓ |P |P |P |✗ |
| Edit mode |✓ |✗ |✓ |✗ |✗ |✗ |
| Java Upgrade Agent |P |✗ |✗ |✗ |✗ |✗ |
| MCP |✓ |✓ |✓ |✓ |✓ |✗ |
| Next edit suggestions |✓ |✓ |P |P |P |✗ |
| Prompt files |✓ |✓ |P |✗ |P |✗ |
| Vision |P |✓ |P |✓ |P |✗ |
| Workspace indexing |✓ |✓ |✓ |✓ |✗ |✗ |

{% endides %}

{% vscode %}



## Features by VS Code version

The following table shows supported Copilot features across recent versions of the IDE.


## VS Code latest releases

| Feature | 1.108.0 | 1.107.0 | 1.106.0 | 1.105.0 | 1.104.0 |
|:----|:----:|:----:|:----:|:----:|:----:|
| .NET Upgrade Agent |✗ |✗ |✗ |✗ |✗ |
| Agent skills |✓ |✗ |✗ |✗ |✗ |
| Agent mode |✓ |✓ |✓ |✓ |✓ |
| BYOK |P |P |P |P |P |
| Chat |✓ |✓ |✓ |✓ |✓ |
| Checkpoints |✓ |✓ |✓ |✓ |✓ |
| Code completion |✓ |✓ |✓ |✓ |✓ |
| Code referencing |✓ |✓ |✓ |✓ |✓ |
| Copilot code review |✓ |✓ |✓ |✓ |✓ |
| Custom agents |✓ |✓ |P |P |P |
| Custom instructions |✓ |✓ |✓ |✓ |✓ |
| Edit mode |✓ |✓ |✓ |✓ |✓ |
| Java Upgrade Agent |P |P |P |P |P |
| MCP |✓ |✓ |✓ |✓ |✓ |
| Next edit suggestions |✓ |✓ |✓ |✓ |✓ |
| Prompt files |✓ |✓ |P |P |P |
| Vision |P |P |P |P |P |
| Workspace indexing |✓ |✓ |✓ |✓ |✓ |



## VS Code 2025 releases

| Feature | 1.108.0 | 1.107.0 | 1.106.0 | 1.105.0 | 1.104.0 | 1.103.0 | 1.102.0 | 1.101.0 | 1.100.0 | 1.99.0 | 1.98.0 | 1.97.0 |
|:----|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| .NET Upgrade Agent |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Agent skills |✓ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Agent mode |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |P |P |
| BYOK |P |P |P |P |P |P |P |P |P |P |P |P |
| Chat |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |
| Checkpoints |✓ |✓ |✓ |✓ |✓ |✓ |✗ |✗ |✗ |✗ |✗ |✗ |
| Code completion |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |
| Code referencing |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |
| Copilot code review |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |P |P |
| Custom agents |✓ |✓ |P |P |P |P |P |P |✗ |✗ |✗ |✗ |
| Custom instructions |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |P |
| Edit mode |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |
| Java Upgrade Agent |P |P |P |P |P |P |P |P |P |P |P |P |
| MCP |✓ |✓ |✓ |✓ |✓ |✓ |✓ |P |P |P |✗ |✗ |
| Next edit suggestions |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |P |P |
| Prompt files |✓ |✓ |P |P |P |P |P |P |P |P |P |P |
| Vision |P |P |P |P |P |P |P |P |P |P |P |P |
| Workspace indexing |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |



## VS Code 2024 releases

| Feature | 1.96.0 | 1.95.0 | 1.94.0 |
|:----|:----:|:----:|:----:|
| .NET Upgrade Agent |✗ |✗ |✗ |
| Agent skills |✗ |✗ |✗ |
| Agent mode |✗ |✗ |✗ |
| BYOK |P |P |P |
| Chat |✓ |✓ |✓ |
| Checkpoints |✗ |✗ |✗ |
| Code completion |✓ |✓ |✓ |
| Code referencing |✓ |✓ |✓ |
| Copilot code review |P |P |✗ |
| Custom agents |✗ |✗ |✗ |
| Custom instructions |P |P |✗ |
| Edit mode |P |P |✗ |
| Java Upgrade Agent |P |P |P |
| MCP |✗ |✗ |✗ |
| Next edit suggestions |✗ |✗ |✗ |
| Prompt files |✗ |✗ |✗ |
| Vision |✗ |✗ |✗ |
| Workspace indexing |✓ |✓ |✗ |



## VS Code 2023 releases

| Feature | 1.80.0 |
|:----|:----:|
| .NET Upgrade Agent |✗ |
| Agent skills |✗ |
| Agent mode |✗ |
| BYOK |P |
| Chat |✓ |
| Checkpoints |✗ |
| Code completion |✓ |
| Code referencing |✗ |
| Copilot code review |✗ |
| Custom agents |✗ |
| Custom instructions |✗ |
| Edit mode |✗ |
| Java Upgrade Agent |P |
| MCP |✗ |
| Next edit suggestions |✗ |
| Prompt files |✗ |
| Vision |✗ |
| Workspace indexing |✗ |



## VS Code 2022 releases

| Feature | 1.70.0 |
|:----|:----:|
| .NET Upgrade Agent |✗ |
| Agent skills |✗ |
| Agent mode |✗ |
| BYOK |P |
| Chat |✓ |
| Checkpoints |✗ |
| Code completion |✓ |
| Code referencing |✗ |
| Copilot code review |✗ |
| Custom agents |✗ |
| Custom instructions |✗ |
| Edit mode |✗ |
| Java Upgrade Agent |P |
| MCP |✗ |
| Next edit suggestions |✗ |
| Prompt files |✗ |
| Vision |✗ |
| Workspace indexing |✗ |



## VS Code 2021 releases

| Feature | 1.60.0 | 1.57.0 |
|:----|:----:|:----:|
| .NET Upgrade Agent |✗ |✗ |
| Agent skills |✗ |✗ |
| Agent mode |✗ |✗ |
| BYOK |P |P |
| Chat |✗ |✗ |
| Checkpoints |✗ |✗ |
| Code completion |✓ |P |
| Code referencing |✗ |✗ |
| Copilot code review |✗ |✗ |
| Custom agents |✗ |✗ |
| Custom instructions |✗ |✗ |
| Edit mode |✗ |✗ |
| Java Upgrade Agent |P |P |
| MCP |✗ |✗ |
| Next edit suggestions |✗ |✗ |
| Prompt files |✗ |✗ |
| Vision |✗ |✗ |
| Workspace indexing |✗ |✗ |



{% endvscode %}

{% visualstudio %}



## Features by Visual Studio version

The following table shows supported Copilot features across recent versions of the IDE.


## Visual Studio latest releases

| Feature | 18.6.0 | 17.14.0 |
|:----|:----:|:----:|
| .NET Upgrade Agent |✓ |✓ |
| Agent skills |✓ |✗ |
| Agent mode |✓ |✓ |
| BYOK |✓ |✓ |
| Chat |✓ |✓ |
| Checkpoints |✓ |✓ |
| Code completion |✓ |✓ |
| Code referencing |✓ |✓ |
| Copilot code review |✓ |✓ |
| Custom agents |✓ |✗ |
| Custom instructions |✓ |✓ |
| Edit mode |✗ |✗ |
| MCP |✓ |✓ |
| Next edit suggestions |✓ |✓ |
| Prompt files |✓ |✓ |
| Vision |✓ |✓ |
| Workspace indexing |✓ |✗ |



{% endvisualstudio %}

{% jetbrains %}



## Features by JetBrains version

The following table shows supported Copilot features across recent versions of the GitHub Copilot Extension for the IDE.


## JetBrains latest releases

| Feature | 1.5.66 | 1.5.65 | 1.5.64 | 1.5.63 | 1.5.62 |
|:----|:----:|:----:|:----:|:----:|:----:|
| Agent skills |P |P |P |✗ |✗ |
| Agent mode |✓ |✓ |✓ |✓ |✓ |
| BYOK |P |P |P |P |P |
| Chat |✓ |✓ |✓ |✓ |✓ |
| Checkpoints |✓ |✓ |✓ |✓ |✓ |
| Code completion |✓ |✓ |✓ |✓ |✓ |
| Code referencing |✓ |✓ |✓ |✓ |✓ |
| Copilot code review |✓ |✓ |✓ |✓ |✓ |
| Custom instructions |P |P |P |P |P |
| Custom agents |P |P |P |P |P |
| Edit mode |✓ |✓ |✓ |✓ |✓ |
| MCP |✓ |✓ |✓ |✓ |✓ |
| Next edit suggestions |P |P |P |P |P |
| Prompt files |P |P |P |P |P |
| Vision |P |P |P |P |P |
| Workspace indexing |✓ |✓ |✓ |✓ |✓ |



## JetBrains 2026 releases

| Feature | 1.5.66 | 1.5.65 | 1.5.64 | 1.5.63 |
|:----|:----:|:----:|:----:|:----:|
| Agent skills |P |P |P |✗ |
| Agent mode |✓ |✓ |✓ |✓ |
| BYOK |P |P |P |P |
| Chat |✓ |✓ |✓ |✓ |
| Checkpoints |✓ |✓ |✓ |✓ |
| Code completion |✓ |✓ |✓ |✓ |
| Code referencing |✓ |✓ |✓ |✓ |
| Copilot code review |✓ |✓ |✓ |✓ |
| Custom instructions |P |P |P |P |
| Custom agents |P |P |P |P |
| Edit mode |✓ |✓ |✓ |✓ |
| MCP |✓ |✓ |✓ |✓ |
| Next edit suggestions |P |P |P |P |
| Prompt files |P |P |P |P |
| Vision |P |P |P |P |
| Workspace indexing |✓ |✓ |✓ |✓ |



## JetBrains 2025 releases

| Feature | 1.5.62 | 1.5.54 | 1.5.53 | 1.5.49 | 1.5.45 | 1.5.43 | 1.5.41 | 1.5.0 | 1.0.1 |
|:----|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| Agent skills |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Agent mode |✓ |✓ |✓ |✓ |P |✗ |✗ |✗ |✗ |
| BYOK |P |P |P |P |P |P |P |P |P |
| Chat |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✗ |
| Checkpoints |✓ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Code completion |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |
| Code referencing |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |
| Copilot code review |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |
| Custom instructions |P |P |P |P |P |P |P |✗ |✗ |
| Custom agents |P |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Edit mode |✓ |✓ |✓ |✓ |✓ |✓ |P |✗ |✗ |
| MCP |✓ |✓ |✓ |P |P |✗ |✗ |✗ |✗ |
| Next edit suggestions |P |P |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Prompt files |P |P |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Vision |P |P |P |P |P |P |P |✗ |✗ |
| Workspace indexing |✓ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |



## JetBrains 2024 releases

| Feature | 1.5.39 | 1.4.0 |
|:----|:----:|:----:|
| Agent skills |✗ |✗ |
| Agent mode |✗ |✗ |
| BYOK |P |P |
| Chat |✓ |P |
| Checkpoints |✗ |✗ |
| Code completion |✓ |✓ |
| Code referencing |✓ |✓ |
| Copilot code review |✓ |✓ |
| Custom instructions |✗ |✗ |
| Custom agents |✗ |✗ |
| Edit mode |P |✗ |
| MCP |✗ |✗ |
| Next edit suggestions |✗ |✗ |
| Prompt files |✗ |✗ |
| Vision |✗ |✗ |
| Workspace indexing |✗ |✗ |



{% endjetbrains %}

{% eclipse %}



## Features by Eclipse version

The following table shows supported Copilot features across recent versions of the GitHub Copilot Extension for the IDE.


## Eclipse latest releases

| Feature | 0.14.0 | 0.13.0 | 0.12.0 | 0.11.0 | 0.10.0 |
|:----|:----:|:----:|:----:|:----:|:----:|
| Agent skills |✗ |✗ |✗ |✗ |✗ |
| Agent mode |✓ |✓ |✓ |✓ |✓ |
| BYOK |P |P |P |✗ |✗ |
| Chat |✓ |✓ |✓ |✓ |✓ |
| Checkpoints |✗ |✗ |✗ |✗ |✗ |
| Code completion |✓ |✓ |✓ |✓ |✓ |
| Code referencing |✓ |✓ |✓ |✓ |✓ |
| Copilot code review |✗ |✗ |✗ |✗ |✗ |
| Custom agents |✓ |✓ |✗ |✗ |✗ |
| Custom instructions |P |P |P |P |P |
| Java Upgrade Agent |✗ |✗ |✗ |✗ |✗ |
| MCP |✓ |✓ |✓ |✓ |✓ |
| Next edit suggestions |P |P |✗ |✗ |✗ |
| Prompt files |✗ |✗ |✗ |✗ |✗ |
| Vision |✓ |✓ |✓ |✓ |✓ |
| Workspace indexing |✓ |✓ |✓ |✓ |✓ |



## Eclipse 2025 releases

| Feature | 0.14.0 | 0.13.0 | 0.12.0 | 0.11.0 | 0.10.0 | 0.9.0 | 0.8.0 | 0.7.0 | 0.6.0 | 0.5.0 | 0.4.0 | 0.3.0 | 0.2.0 | 0.1.0 |
|:----|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| Agent skills |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Agent mode |✓ |✓ |✓ |✓ |✓ |✓ |P |P |P |✗ |✗ |✗ |✗ |✗ |
| BYOK |P |P |P |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Chat |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |P |P |✗ |✗ |
| Checkpoints |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Code completion |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |P |P |
| Code referencing |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |
| Copilot code review |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Custom agents |✓ |✓ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Custom instructions |P |P |P |P |P |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Java Upgrade Agent |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| MCP |✓ |✓ |✓ |✓ |✓ |P |P |P |P |✗ |✗ |✗ |✗ |✗ |
| Next edit suggestions |P |P |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Prompt files |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Vision |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Workspace indexing |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✗ |✗ |✗ |✗ |✗ |✗ |



{% endeclipse %}

{% xcode %}



## Features by Xcode version

The following table shows supported Copilot features across recent versions of the GitHub Copilot Extension for the IDE.


## Xcode latest releases

| Feature | 0.46.0 | 0.45.0 | 0.44.0 | 0.43.0 | 0.42.0 |
|:----|:----:|:----:|:----:|:----:|:----:|
| Agent skills |✗ |✗ |✗ |✗ |✗ |
| Agent mode |✓ |✓ |✓ |✓ |✓ |
| BYOK |P |P |P |P |P |
| Chat |✓ |✓ |✓ |✓ |✓ |
| Checkpoints |✓ |✓ |✓ |✗ |✗ |
| Code completion |✓ |✓ |✓ |✓ |✓ |
| Code referencing |✗ |✗ |✗ |✗ |✗ |
| Copilot code review |✓ |✓ |✓ |✓ |✓ |
| Custom agents |P |P |✗ |✗ |✗ |
| Custom instructions |P |P |P |P |P |
| MCP |✓ |✓ |✓ |✓ |✓ |
| Next edit suggestions |P |P |✗ |✗ |✗ |
| Prompt files |P |P |P |P |P |
| Vision |P |P |P |P |P |
| Workspace indexing |✗ |✗ |✗ |✗ |✗ |



## Xcode 2025 releases

| Feature | 0.46.0 | 0.45.0 | 0.44.0 | 0.43.0 | 0.42.0 | 0.41.0 | 0.40.0 | 0.39.0 | 0.38.0 | 0.37.0 | 0.36.0 | 0.35.0 | 0.34.0 | 0.33.0 | 0.32.0 | 0.31.0 | 0.30.0 |
|:----|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| Agent skills |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Agent mode |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |P |P |P |✗ |✗ |✗ |✗ |✗ |
| BYOK |P |P |P |P |P |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Chat |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |P |✗ |
| Checkpoints |✓ |✓ |✓ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Code completion |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |P |
| Code referencing |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Copilot code review |✓ |✓ |✓ |✓ |✓ |✓ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Custom agents |P |P |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Custom instructions |P |P |P |P |P |P |P |P |P |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| MCP |✓ |✓ |✓ |✓ |✓ |✓ |P |P |P |P |P |P |✗ |✗ |✗ |✗ |✗ |
| Next edit suggestions |P |P |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Prompt files |P |P |P |P |P |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Vision |P |P |P |P |P |P |P |P |P |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Workspace indexing |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |



## Xcode 2024 releases

| Feature | 0.29.0 | 0.28.0 | 0.27.0 | 0.26.0 | 0.25.0 | 0.24.0 | 0.23.0 | 0.0.0 |
|:----|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| Agent skills |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Agent mode |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| BYOK |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Chat |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Checkpoints |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Code completion |P |P |✗ |✗ |✗ |✗ |✗ |✗ |
| Code referencing |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Copilot code review |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Custom agents |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Custom instructions |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| MCP |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Next edit suggestions |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Prompt files |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Vision |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Workspace indexing |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |



{% endxcode %}

{% vimneovim %}



## Features by NeoVim version

The following table shows supported Copilot features across recent versions of the GitHub Copilot Extension for the IDE.


## NeoVim latest releases

| Feature | 1.18.0 | 1.17.0 | 1.16.0 | 1.15.0 | 1.14.0 |
|:----|:----:|:----:|:----:|:----:|:----:|
| Agent skills |✗ |✗ |✗ |✗ |✗ |
| Agent mode |✗ |✗ |✗ |✗ |✗ |
| BYOK |✗ |✗ |✗ |✗ |✗ |
| Chat |✗ |✗ |✗ |✗ |✗ |
| Checkpoints |✗ |✗ |✗ |✗ |✗ |
| Code completion |✓ |✓ |✓ |✓ |✓ |
| Code referencing |✗ |✗ |✗ |✗ |✗ |
| Copilot code review |✗ |✗ |✗ |✗ |✗ |
| Custom agents |✗ |✗ |✗ |✗ |✗ |
| Custom instructions |✗ |✗ |✗ |✗ |✗ |
| MCP |✗ |✗ |✗ |✗ |✗ |
| Next edit suggestions |✗ |✗ |✗ |✗ |✗ |
| Prompt files |✗ |✗ |✗ |✗ |✗ |
| Vision |✗ |✗ |✗ |✗ |✗ |
| Workspace indexing |✗ |✗ |✗ |✗ |✗ |



## NeoVim 2024 releases

| Feature | 1.18.0 | 1.17.0 | 1.16.0 | 1.15.0 | 1.14.0 |
|:----|:----:|:----:|:----:|:----:|:----:|
| Agent skills |✗ |✗ |✗ |✗ |✗ |
| Agent mode |✗ |✗ |✗ |✗ |✗ |
| BYOK |✗ |✗ |✗ |✗ |✗ |
| Chat |✗ |✗ |✗ |✗ |✗ |
| Checkpoints |✗ |✗ |✗ |✗ |✗ |
| Code completion |✓ |✓ |✓ |✓ |✓ |
| Code referencing |✗ |✗ |✗ |✗ |✗ |
| Copilot code review |✗ |✗ |✗ |✗ |✗ |
| Custom agents |✗ |✗ |✗ |✗ |✗ |
| Custom instructions |✗ |✗ |✗ |✗ |✗ |
| MCP |✗ |✗ |✗ |✗ |✗ |
| Next edit suggestions |✗ |✗ |✗ |✗ |✗ |
| Prompt files |✗ |✗ |✗ |✗ |✗ |
| Vision |✗ |✗ |✗ |✗ |✗ |
| Workspace indexing |✗ |✗ |✗ |✗ |✗ |



## NeoVim 2023 releases

| Feature | 1.13.0 | 1.12.0 | 1.11.0 | 1.10.0 | 1.9.0 |
|:----|:----:|:----:|:----:|:----:|:----:|
| Agent skills |✗ |✗ |✗ |✗ |✗ |
| Agent mode |✗ |✗ |✗ |✗ |✗ |
| BYOK |✗ |✗ |✗ |✗ |✗ |
| Chat |✗ |✗ |✗ |✗ |✗ |
| Checkpoints |✗ |✗ |✗ |✗ |✗ |
| Code completion |✓ |✓ |✓ |✓ |✓ |
| Code referencing |✗ |✗ |✗ |✗ |✗ |
| Copilot code review |✗ |✗ |✗ |✗ |✗ |
| Custom agents |✗ |✗ |✗ |✗ |✗ |
| Custom instructions |✗ |✗ |✗ |✗ |✗ |
| MCP |✗ |✗ |✗ |✗ |✗ |
| Next edit suggestions |✗ |✗ |✗ |✗ |✗ |
| Prompt files |✗ |✗ |✗ |✗ |✗ |
| Vision |✗ |✗ |✗ |✗ |✗ |
| Workspace indexing |✗ |✗ |✗ |✗ |✗ |



## NeoVim 2022 releases

| Feature | 1.8.0 | 1.7.0 | 1.6.0 | 1.5.0 | 1.4.0 | 1.3.0 | 1.2.0 | 1.1.0 |
|:----|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| Agent skills |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Agent mode |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| BYOK |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Chat |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Checkpoints |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Code completion |✓ |✓ |✓ |✓ |✓ |✓ |✓ |✓ |
| Code referencing |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Copilot code review |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Custom agents |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Custom instructions |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| MCP |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Next edit suggestions |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Prompt files |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Vision |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |
| Workspace indexing |✗ |✗ |✗ |✗ |✗ |✗ |✗ |✗ |



## NeoVim 2021 releases

| Feature | 1.0.0 | 0.0.1 |
|:----|:----:|:----:|
| Agent skills |✗ |✗ |
| Agent mode |✗ |✗ |
| BYOK |✗ |✗ |
| Chat |✗ |✗ |
| Checkpoints |✗ |✗ |
| Code completion |✓ |P |
| Code referencing |✗ |✗ |
| Copilot code review |✗ |✗ |
| Custom agents |✗ |✗ |
| Custom instructions |✗ |✗ |
| MCP |✗ |✗ |
| Next edit suggestions |✗ |✗ |
| Prompt files |✗ |✗ |
| Vision |✗ |✗ |
| Workspace indexing |✗ |✗ |



{% endvimneovim %}
