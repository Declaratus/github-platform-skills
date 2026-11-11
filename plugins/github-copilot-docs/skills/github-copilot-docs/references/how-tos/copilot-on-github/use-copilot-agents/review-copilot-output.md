---
title: Review output from Copilot
shortTitle: Review Copilot output
allowTitleToDifferFromFilename: true
intro: 'Copilot pull requests deserve the same thorough review as any contribution.'
product: "Copilot cloud agent is available for all paid Copilot plans.\n\nThe agent is available in all repositories stored on GitHub, except repositories owned by managed user accounts and where it has been explicitly disabled.<br><a href=\"https://github.com/features/copilot/plans?ref_product=copilot&ref_type=engagement&ref_style=button\" target=\"_blank\" class=\"btn btn-primary mt-3 mr-3 no-underline\"><span>Sign up for Copilot</span> (icon: link-external)</a>"
versions:
  feature: copilot
redirect_from:
  - /copilot/how-tos/use-copilot-agents/coding-agent/review-copilot-prs
  - /copilot/how-tos/use-copilot-agents/cloud-agent/review-copilot-prs
  - /copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/reviewing-a-pull-request-created-by-copilot
  - /copilot/using-github-copilot/coding-agent/reviewing-a-pull-request-created-by-copilot
  - /copilot/how-tos/agents/copilot-coding-agent/reviewing-a-pull-request-created-by-copilot
  - /copilot/how-tos/agents/copilot-coding-agent/review-copilot-prs
  - /copilot/how-tos/agents/coding-agent/review-copilot-prs
contentType: how-tos
category: 
  - Author and optimize with Copilot
---

## Review Copilot's changes

When Copilot finishes a coding task and requests your review, check the pull request thoroughly before merging.

> [!IMPORTANT]
> If your repository requires pull request approvals, **your approval of a Copilot pull request won't count** toward the required number. Another reviewer must approve the pull request before it can be merged.

To request changes from Copilot on its pull request, mention `@copilot` in a comment, or push commits directly to the branch. For more information, see [AUTOTITLE](/copilot/how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-on-github).

## Manage GitHub Actions workflow runs

By default, GitHub Actions workflows will not run automatically when Copilot pushes changes to a pull request.

GitHub Actions workflows can be privileged and have access to sensitive secrets. Inspect the proposed changes in the pull request and ensure that you are comfortable running your workflows on the pull request branch. You should be especially alert to any proposed changes in the `.github/workflows/` directory that affect workflow files.

To allow GitHub Actions workflows to run, click the **Approve and run workflows** button in the pull request's merge box.

![Screenshot of the merge box on a pull request from Copilot with the "Approve and run workflows" button.](/assets/images/help/copilot/cloud-agent/approve-and-run-workflows.png)

Optionally, you can configure Copilot cloud agent to allow GitHub Actions workflows to run without human intervention. For more information, see [AUTOTITLE](/copilot/how-tos/use-copilot-agents/cloud-agent/configuring-agent-settings).

To have Copilot watch a pull request and fix failed GitHub Actions workflows or merge conflicts automatically, enable Agent Merge with **Watch and fix** in the merge box. See [AUTOTITLE](/copilot/how-tos/copilot-on-github/use-copilot-agents/get-pull-requests-ready-to-merge).

## Give feedback on Copilot's work

Use the feedback buttons on Copilot's pull requests and comments to rate the output. Your feedback helps improve Copilot's quality.

1. On a pull request or comment from Copilot, click the thumbs up (:+1:) or thumbs down (:-1:) button.
1. If you click the thumbs down button, optionally select a reason and leave a comment, then click **Submit feedback**.

## Further reading

* [AUTOTITLE](/copilot/tutorials/cloud-agent/get-the-best-results)
* [AUTOTITLE](/copilot/how-tos/use-copilot-agents/cloud-agent/troubleshoot-cloud-agent)
