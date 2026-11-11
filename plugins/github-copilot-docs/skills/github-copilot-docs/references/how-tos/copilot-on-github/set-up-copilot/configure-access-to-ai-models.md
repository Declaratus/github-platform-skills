---
title: Configuring access to AI models in GitHub Copilot
shortTitle: Configure access to AI models
intro: 'Control which AI models your organization or enterprise can use with Copilot.'
versions:
  feature: copilot
redirect_from:
  - /copilot/using-github-copilot/ai-models/configuring-access-to-ai-models-in-copilot
  - /copilot/how-tos/ai-models/configuring-access-to-ai-models-in-copilot
  - /copilot/how-tos/ai-models/configure-access-to-ai-models
  - /github-models/use-github-models/integrating-ai-models-into-your-development-workflow
  - /copilot/how-tos/use-ai-models/configure-access-to-ai-models
contentType: how-tos
category:
  - Configure Copilot
---

Your access to GitHub Copilot models depends on:

* Your Copilot plan.
* The client you use (for example, GitHub.com, Visual Studio Code, or JetBrains IDEs).
* Whether your organization or enterprise restricts access to specific models.

For a list of available AI models, see [AUTOTITLE](/copilot/reference/ai-models/supported-models). For information on how Copilot Chat serves different AI models, see [AUTOTITLE](/copilot/reference/ai-models/model-hosting).

## Setup for individual plans

For individual Copilot plans, you can use AI models directly within Copilot without configuring access or managing policies. Copilot Free and Copilot Student only have access to auto model selection.

> [!NOTE]
> Models available depend on your plan. See [AUTOTITLE](/copilot/reference/ai-models/supported-models#supported-ai-models-per-copilot-plan).

## Setup for organization and enterprise plans

As an enterprise or organization owner, you can enable or disable access to AI models for members with a Copilot Enterprise or Copilot Business seat. See [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-availability-of-default-models) or [AUTOTITLE](/copilot/how-tos/administer-copilot/manage-for-organization/manage-default-models).

Image generation uses a dedicated image generation model, which you manage in the same model policy. To turn off image generation for members, disable this model. See [AUTOTITLE](/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/image-generation).

## Custom models

Bring your own key (BYOK) allows you to use Copilot with compatible models that you or your organization configure.

There are two ways to configure access to additional models:

* Users can configure additional models for themselves in a supported Copilot client.
* Enterprise owners, and organization owners with the necessary permissions, can make additional models available to eligible users in their enterprise or organization through GitHub's Copilot API.

Your ability to access additional locally hosted or cloud-hosted models depends on the surface in which you're using Copilot and the configuration method used to add models. For example, user-configured BYOK in Copilot CLI can connect to a compatible cloud-hosted service or a model server running on your computer or network.

For more information, see [AUTOTITLE](/copilot/concepts/models/bring-your-own-key).

Windows users can also add the MAI Code 1.1 Flash model to their local machine, directly from Copilot CLI, the Copilot app, or Visual Studio Code, provided their computer meets the required system resources. See [AUTOTITLE](/copilot/how-tos/github-copilot-app/add-llm-models#installing-a-local-model-from-the-model-picker), [AUTOTITLE](/copilot/how-tos/copilot-cli/customize-copilot/add-llm-models#installing-a-local-model-from-the-model-picker), and [AI language models in VS Code](https://code.visualstudio.com/docs/agent-customization/language-models#_use-on-device-models).
