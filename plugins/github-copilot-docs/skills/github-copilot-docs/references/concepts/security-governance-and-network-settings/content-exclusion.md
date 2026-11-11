---
title: Content exclusion for GitHub Copilot
shortTitle: Content exclusion
intro: You can prevent Copilot from accessing certain files.
product: 'Organizations{% ifversion ghec %} and enterprises{% endif %} with a Copilot Business or Copilot Enterprise plan.'
versions:
  feature: copilot
redirect_from:
  - /copilot/concepts/content-exclusion-for-github-copilot
  - /copilot/concepts/content-exclusion
  - /copilot/concepts/context/content-exclusion
contentType: concepts
category:
  - Manage Copilot for a team
---

## About content exclusion for Copilot

You can configure content exclusion to make Copilot ignore certain files. When you exclude content from Copilot:

* Inline suggestions will not be available in the affected files.
* The content in affected files will not inform inline suggestions in other files.
* The content in affected files will not inform Copilot's responses.
* Affected files will not be reviewed in a Copilot code review.

### Who can configure content exclusion

Repository administrators, organization owners, and enterprise owners can configure content exclusion.

* **Repository administrators** can exclude content for their own repositories. This affects any Copilot users in the enterprise working within those specific repositories.
* **Organization owners** can exclude content for users assigned a Copilot seat through their organization.

{% ifversion ghec %}

* **Enterprise owners** can apply exclusion rules to all Copilot users in the enterprise.

{% endif %}

### Availability of content exclusion

The Copilot Business and Copilot Enterprise plans provide the following level of support for content exclusion.

| Tool                                            | Inline suggestions support                    | Chat and agent support                         |
|-------------------------------------------------|:---------------------------------------------:|:----------------------------------------------:|
| Visual Studio        | (icon: check)  | (icon: check)   |
| Visual Studio Code    | (icon: check)  | (icon: check)   |
| JetBrains IDEs                                  | (icon: check)  | (icon: check)   |
| Vim/Neovim                                      | (icon: check)  | Not applicable                                 |
| Xcode                                           | (icon: check)  | (icon: x)   |
| Eclipse                                         | (icon: check)  | (icon: x)   |
| Azure Data Studio                               | (icon: x)  | Not applicable                                 |
| The GitHub Copilot app | Not applicable                                | (icon: check)   |
| GitHub Copilot CLI        | Not applicable                                | (icon: check)   |
| Copilot in the cloud | Not applicable | (icon: check) |
| Copilot code review | Not applicable | (icon: check) |

Copilot in the cloud includes chat and agent sessions started on the GitHub website, GitHub Mobile, or cloud sandboxes.

### Limitations of content exclusion

Content exclusion is not a filesystem security boundary and cannot guarantee prevention of every form of file access. It is a guardrail for the tools that GitHub controls, and is not guaranteed to be respected by third-party MCP servers or clients.

It's also possible that Copilot may use semantic information from an excluded file if the information is provided by the IDE indirectly. Examples of such content include type information and hover-over definitions for symbols used in code, as well as general project properties such as build configuration information.

> [!NOTE]
> When you use a Copilot agent in an IDE, GitHub Copilot CLI, or the GitHub Copilot app, content exclusion prevents the agent from accessing excluded files through Copilot tools and checks identifiable file paths in commands and scripts before running them, but might not detect indirect file access. Content exclusion is not a substitute for operating-system permissions or other access controls.

Currently, content exclusions do not apply to symbolic links (symlinks) and repositories located on remote filesystems.

### Data sent to GitHub

After you configure content exclusion, the client (for example, the Copilot extension for VS Code) sends the current repository URL to the GitHub server so that the server can return the correct policy to the client. These URLs are not logged anywhere.

## Further reading

* [AUTOTITLE](/copilot/how-tos/configure-content-exclusion/exclude-content-from-copilot)
* [AUTOTITLE](/copilot/how-tos/configure-content-exclusion/review-changes)
