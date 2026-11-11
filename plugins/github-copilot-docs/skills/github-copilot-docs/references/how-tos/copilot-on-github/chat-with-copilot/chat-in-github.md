---
title: Asking GitHub Copilot questions in GitHub
shortTitle: Chat in GitHub
intro: 'Get instant answers about your code, repositories, and development questions — right from GitHub.'
versions:
  feature: copilot
redirect_from:
  - /copilot/github-copilot-enterprise/copilot-chat-in-github/using-github-copilot-chat-in-githubcom
  - /copilot/github-copilot-enterprise/copilot-chat-in-github/about-github-copilot-chat-in-githubcom
  - /copilot/github-copilot-chat/copilot-chat-in-github/using-github-copilot-chat-in-githubcom
  - /copilot/github-copilot-chat/copilot-chat-in-github/about-github-copilot-chat-in-githubcom
  - /copilot/github-copilot-chat/copilot-chat-in-github
  - /copilot/using-github-copilot/asking-github-copilot-questions-in-githubcom
  - /copilot/using-github-copilot/asking-github-copilot-questions-in-github
  - /copilot/using-github-copilot/copilot-chat/asking-github-copilot-questions-in-github
  - /copilot/how-tos/chat/asking-github-copilot-questions-in-github
  - /copilot/how-tos/chat/use-chat-in-github
  - /copilot/how-tos/use-chat/use-chat-in-github
  - /copilot/how-tos/chat-with-copilot/use-chat-in-github
  - /copilot/how-tos/chat-with-copilot/chat-in-github
contentType: how-tos
category:
  - Author and optimize with Copilot
---

## Submitting a question to Copilot Chat

Copilot Chat is available from any page on GitHub. Some questions work best in a specific context, such as a repository, issue, or pull request.

1. Navigate to [https://github.com/copilot](https://github.com/copilot?ref_product=copilot&ref_type=engagement&ref_style=text).
1. In the prompt box, type a question and press <kbd>Enter</kbd>.

   Some examples of general questions you could ask are:

   * {% prompt %}What are the advantages of the Go programming language?{% endprompt %}
   * {% prompt %}What is Agile software development?{% endprompt %}
   * {% prompt %}What is the most popular JavaScript framework?{% endprompt %}
   * {% prompt %}Give me some examples of regular expressions.{% endprompt %}
   * {% prompt %}Write a bash script to output today's date.{% endprompt %}

1. Optionally, after submitting a question, you can click (icon: square-fill) in the text box to stop the response.
1. Within a conversation thread, you can ask follow-up questions. Copilot will answer within the context of the conversation.

### Viewing and editing generated files

> [!NOTE]
> This feature is currently in public preview and subject to change.

Copilot may generate files as part of its response, which you can view, edit, and download from the side panel.

### Changing and comparing AI models

You can choose from a selection of AI models, each with different strengths. Different models consume AI credits at different rates based on their token pricing. For details, see [AUTOTITLE](/copilot/reference/copilot-billing/models-and-pricing).

If you access Copilot Chat through a Copilot Business{% ifversion ghec %} or Copilot Enterprise{% endif %} subscription, your organization{% ifversion ghec %} or enterprise{% endif %} must grant members the ability to switch to a different model. See [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-organization/manage-policies){% ifversion ghec %} or [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-enterprise-policies){% endif %}.

1. At the bottom of Copilot Chat, select the **CURRENT-MODEL** (icon: chevron-down) dropdown menu, then click the AI model of your choice.

After submitting a prompt, you can also regenerate a response using a different model by clicking the retry icon ((icon: sync)) below the response. You can switch between responses to compare results.

### Using subthreads in a conversation

Subthreads are branches of a conversation that let you explore aspects of a topic, or new topics, all within the same thread.

To create a subthread, hover over one of your previous questions and click the (icon: pencil) button. Edit the question, then click **Send**. You cannot edit any attachments.

The response to your edited question is displayed in a new subthread. An edit counter appears below the question. Hover over the counter, then click (icon: chevron-left) or (icon: chevron-right) to navigate between subthreads.

### Using images in Copilot Chat

You can attach images and PDFs to your prompts when using a model that supports image input.

Copilot supports the following file types:

* JPEG (`.jpg`, `.jpeg`)
* PNG (`.png`)
* GIF (`.gif`)
* WEBP (`.webp`)
* PDF (`.pdf`)
* HEIC (`.heic`)
* HEIF (`.heif`)

For example, you can attach:

* A screenshot of a code snippet and ask Copilot to explain the code.
* A mockup of the user interface for an application and ask Copilot to generate the code.
* A flowchart and ask Copilot to describe the processes shown in the image.
* A screenshot of a web page and ask Copilot to generate HTML for a similar page.

Image and PDF attachments are available on all Copilot plans and are enabled by default, with no policy required to turn the feature on or off.

To attach a file, drag and drop it into the prompt box, or click (icon: plus) and select **(icon: file-code) Upload from computer**. Select a model that supports image input from the model picker.

### Continuing a conversation alongside an agent session

When you start a Copilot cloud agent task from Copilot Chat—for example, by asking Copilot to create a pull request or research a repository—you can keep chatting while the cloud agent session runs. Copilot Chat reflects the status of the in-progress session and draws on its context, so you can ask follow-up questions about what the agent is doing. When the session is complete, you can ask further questions about the work or start another session from Copilot Chat. For more information, see [AUTOTITLE](/copilot/how-tos/copilot-on-github/use-copilot-agents/manage-and-track-agents).

### Conversation history and retention

Copilot Chat stores up to 100 of your most recent conversations. Messages within each conversation are kept for 28 days before being permanently deleted. Once a conversation has no messages left, it's automatically removed from your history.

## Further reading

* [AUTOTITLE](/copilot/tutorials/explore-a-codebase)
