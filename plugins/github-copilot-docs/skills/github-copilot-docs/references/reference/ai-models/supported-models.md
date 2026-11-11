---
title: Supported AI models in GitHub Copilot
shortTitle: Supported models
allowTitleToDifferFromFilename: true
intro: 'Learn about the supported AI models in GitHub Copilot.'
versions:
  feature: copilot
category:
  - Learn about Copilot
redirect_from:
  - /copilot/using-github-copilot/using-claude-sonnet-in-github-copilot
  - /copilot/using-github-copilot/ai-models/using-claude-sonnet-in-github-copilot
  - /copilot/using-github-copilot/ai-models/using-claude-in-github-copilot
  - /copilot/using-github-copilot/ai-models/using-gemini-flash-in-github-copilot
  - /copilot/using-github-copilot/ai-models/using-gemini-in-github-copilot
  - /copilot/using-github-copilot/ai-models/using-openai-gpt-41-in-github-copilot
  - /copilot/using-github-copilot/ai-models/using-openai-o3-in-github-copilot
  - /copilot/using-github-copilot/ai-models/using-openai-o4-mini-in-github-copilot
  - /copilot/using-github-copilot/ai-models/supported-ai-models-in-copilot
  - /copilot/reference/ai-models/supported-ai-models-in-copilot
contentType: reference
---

GitHub Copilot supports multiple AI models, each with different strengths. Some prioritize speed and cost-efficiency, while others are optimized for accuracy, reasoning, or multimodal inputs. The right model depends on your task. For a side-by-side comparison to help you choose, see [AUTOTITLE](/copilot/reference/ai-models/model-comparison).

The models available to you depend on your Copilot plan and where you're using Copilot, such as GitHub.com or an IDE.

> [!NOTE]
> Model availability is subject to change. Some models may be replaced or updated over time.

For all of the default AI models, input prompts and output completions run through GitHub Copilot's content filters for harmful, offensive, or off-topic content, and for public code matching when enabled.

## Supported AI models in Copilot

This table lists the AI models available in Copilot, along with their release status.

{% rowheaders %}

| Model name                                             | Provider  | Release status             |
|--------------------------------------------------------|-----------|----------------------------|
| GPT-5.3-Codex| OpenAI | GA |
| GPT-5.4 nano[^gpt54nano]| OpenAI | GA |
| GPT-5.6 Luna| OpenAI | GA |
| GPT-5.6 Sol| OpenAI | GA |
| GPT-5.6 Terra| OpenAI | GA |
| GPT-6 Astra| OpenAI | GA |
| GPT-6 Luna| OpenAI | GA |
| GPT-6 Sol| OpenAI | GA |
| GPT-6.1 Sol| OpenAI | GA |
| GPT-6.1 Terra| OpenAI | GA |
| Claude Fable 5[^claude-fable-5]| Anthropic | GA |
| Claude Fable 5.1[^claude-fable-5]| Anthropic | GA |
| Claude Fable 5.2[^claude-fable-5]| Anthropic | GA |
| Claude Haiku 4.5| Anthropic | GA |
| Claude Haiku 5.5| Anthropic | GA |
| Claude Opus 4.8| Anthropic | GA |
| Claude Opus 4.8 (fast mode) (preview)| Anthropic | GA |
| Claude Opus 5| Anthropic | GA |
| Claude Opus 5.5| Anthropic | GA |
| Claude Sonnet 4.6| Anthropic | GA |
| Claude Sonnet 5| Anthropic | GA |
| Claude Sonnet 5.5| Anthropic | GA |
| Gemini 3.8 Flash| Google | GA |
| Gemini 4 Argon| Google | GA |
| Gemini 4 Carbon| Google | GA |
| MAI-Code-1.1-Flash[^mai-models]| Microsoft | GA |
| Kimi K3| Moonshot AI | GA |
| Grok 4.5| xAI | GA |
| Grok 4.6| xAI | GA |
| Grok 4.7| xAI | GA |

{% endrowheaders %}

[^claude-fable-5]: When Claude Fable 5, Claude Fable 5.1, or Claude Fable 5.2 is used, Anthropic retains data, including prompts and outputs, by default to operate safety classifiers that detect harmful use. Customers can request to use Claude Fable 5, Claude Fable 5.1, or Claude Fable 5.2 with zero data retention (ZDR) through the end of 2026 under a time-bound exemption while Anthropic rolls out Enterprise Frontier Safeguards (EFS). After that point, continued use of these models would require EFS, which will enable eligible customers to keep their data under their own control while also enabling automated safety monitoring. For an enterprise that has been approved and configured for this type of access, Claude Fable 5, Claude Fable 5.1, and Claude Fable 5.2 requests will use the ZDR endpoint through the end of 2026 when the models are enabled. To learn whether your enterprise is eligible and request access, contact your GitHub account team. Approval for access does not automatically enable Claude Fable 5, Claude Fable 5.1, or Claude Fable 5.2. An enterprise or organization administrator must still enable each model before users can access it. Other Claude models, except for Claude Fable 5, Claude Fable 5.1, and Claude Fable 5.2, continue to operate under ZDR. Customers who enable a Fable model with ZDR agree to use this model only for internal operations, including to develop and evaluate products for their own customers. They may not make the model endpoints or outputs available externally. To enable these models, see [AUTOTITLE](/copilot/how-tos/copilot-on-github/set-up-copilot/configure-access-to-ai-models).

## Supported AI models in Auto model selection

This table lists the supported AI models for Auto model selection. Available models may be limited by model policies. For example, as the long term support model, GPT-5.3-Codex will be used in the event no other models are available. See [AUTOTITLE](/copilot/concepts/models/fallback-and-lts-models) and [AUTOTITLE](/copilot/concepts/models/auto-model-selection).

{% rowheaders %}

| Model | Copilot cloud agent | Copilot Chat | Copilot CLI | GitHub Copilot app |
| --- | --- | --- | --- | --- |
| GPT-5.6 Luna | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-5.6 Sol | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-5.6 Terra | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-6 Astra | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-6 Luna | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-6 Sol | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-6.1 Sol | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Haiku 4.5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Opus 4.8 | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Opus 5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Opus 5.5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Sonnet 5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Sonnet 5.5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Gemini 3.8 Flash | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| MAI-Code-1.1-Flash | (icon: check) | (icon: check) | (icon: check) | (icon: check) |

{% endrowheaders %}

## Models with extended capabilities

The latest Copilot models support the following extended capabilities.

* **1 million token context window**: Allows the model to process significantly more content in a single session. This is useful when working across large codebases, long documents, or complex multi-file projects. When you select a supported model, you can choose between the default context size or the extended (1 million token) context.
* **Configurable reasoning levels**: Controls the depth of the model's reasoning process before it generates a response. When you select a supported model, you can choose which reasoning level you want to use. Higher reasoning levels can improve the quality of responses to complex problems.

Choosing a larger context window or higher reasoning will impact AI credits consumption; more tokens will be consumed, so more credits will be used. For this reason, we recommend that you use the regular context window and regular reasoning by default, selecting the larger context window and higher reasoning for more complex tasks only.

> [!NOTE]
> * The 1 million token context window is available in Visual Studio Code and Copilot CLI only.
> * Configurable reasoning levels are available in Visual Studio Code, Copilot CLI, and Copilot cloud agent.
> * Some models have extended capability pricing see [AUTOTITLE](/copilot/reference/copilot-billing/models-and-pricing#pricing-tables)

{% rowheaders %}

| Model | 1 million token context window | Configurable reasoning |
| --- | --- | --- |
| Claude Sonnet 4.6 | (icon: check) | (icon: check) |
| Claude Opus 4.8 | (icon: check) | (icon: check) |
| Claude Opus 5 | (icon: check) | (icon: check) |
| Claude Opus 5.5 | (icon: check) | (icon: check) |
| Claude Sonnet 5 | (icon: check) | (icon: check) |
| Claude Sonnet 5.5 | (icon: check) | (icon: check) |
| Claude Haiku 5.5 | (icon: check) | (icon: check) |
| Claude Opus 4.8 (fast mode) (preview) | (icon: x) | (icon: check) |
| Claude Fable 5 | (icon: check) | (icon: check) |
| Claude Fable 5.1 | (icon: check) | (icon: check) |
| Claude Fable 5.2 | (icon: check) | (icon: check) |
| GPT-5.3-Codex | (icon: check) | (icon: check) |
| GPT-5.6 Luna | (icon: check) | (icon: check) |
| GPT-5.6 Sol | (icon: check) | (icon: check) |
| GPT-5.6 Terra | (icon: check) | (icon: check) |
| GPT-6 Astra | (icon: check) | (icon: check) |
| GPT-6 Luna | (icon: check) | (icon: check) |
| GPT-6 Sol | (icon: check) | (icon: check) |
| GPT-6.1 Sol | (icon: check) | (icon: check) |
| GPT-6.1 Terra | (icon: check)  | (icon: check)  |
| Kimi K3 | (icon: check) | (icon: check) |

{% endrowheaders %}

## Supported AI models per client

The following table shows which models are available in each client.

{% rowheaders %}

| Model | GitHub.com | Copilot CLI | Visual Studio Code | Visual Studio | Eclipse | Xcode | JetBrains IDEs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Haiku 4.5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Haiku 5.5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Opus 4.8 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Opus 4.8 (fast mode) (preview) | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Opus 5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Opus 5.5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Fable 5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Fable 5.1 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Fable 5.2 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Sonnet 4.6 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: x) | (icon: x) | (icon: x) |
| Claude Sonnet 5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Sonnet 5.5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Gemini 3.8 Flash | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Gemini 4 Argon | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Gemini 4 Carbon | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| MAI-Code-1.1-Flash | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-5.3-Codex | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-5.4 nano[^gpt54nano] | (icon: x) | (icon: x) | (icon: x) | (icon: x) | (icon: x) | (icon: x) | (icon: x) |
| GPT-5.6 Luna | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: x) | (icon: x) | (icon: x) |
| GPT-5.6 Sol | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: x) | (icon: x) | (icon: x) |
| GPT-5.6 Terra | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: x) | (icon: x) | (icon: x) |
| GPT-6 Astra | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-6 Luna | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-6 Sol | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-6.1 Terra | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Grok 4.5 | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Grok 4.6 | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Grok 4.7 | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Kimi K3 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |

{% endrowheaders %}

> [!NOTE]
> In Visual Studio Code you can add more models than those that are available by default with your Copilot subscription. See [AUTOTITLE](/copilot/how-tos/copilot-in-your-ide/chat-with-copilot/change-the-chat-model?tool=vscode#adding-more-models).

## Minimum IDE versions for recent models

Some Copilot models require minimum versions of supported IDEs or Copilot extensions or plugins. The table below lists the minimum versions known from changelog entries or provided release guidance. This information is tentative and subject to change as model support rolls out. For best results, keep your IDE and Copilot extension or plugin updated to the latest available version.

{% rowheaders %}

| Model                                                    | Visual Studio Code | Visual Studio | JetBrains IDEs | Xcode | Eclipse |
|----------------------------------------------------------|----------------------------------------------|------------------------------------------|----------------|-------|---------|
| Gemini 3.8 Flash     | TBD | `17.14.22` or `18.1.0`         | TBD | TBD | TBD |
| Gemini 4 Argon      | TBD | `17.14.22` or `18.1.0`         | TBD | TBD | TBD |
| Gemini 4 Carbon     | TBD | TBD                            | TBD | TBD | TBD |
| GPT-5.3-Codex        | `v1.104.1` | `17.14.19`                     | `1.5.61` | `0.45.0` | `0.13.0` |
| GPT-5.6 Luna         | `1.128.0` | TBD | TBD | TBD | TBD |
| GPT-5.6 Sol          | `1.128.0` | TBD | TBD | TBD | TBD |
| GPT-5.6 Terra        | `1.128.0` | TBD | TBD | TBD | TBD |
| GPT-6 Astra         | `1.136.1` | `17.14.19` | TBD | TBD | TBD |
| GPT-6 Luna          | TBD | `17.14.19` | TBD | TBD | TBD |
| GPT-6 Sol           | TBD | `17.14.19` | TBD | TBD | TBD |
| GPT-6.1 Sol          | TBD | `17.14.19` | TBD | TBD | TBD |
| GPT-6.1 Terra        | TBD | TBD | TBD | TBD | TBD |
| Claude Opus 4.8      | `v1.118` | `17.14.6`                     | TBD | TBD | TBD |
| Claude Opus 5       | `v1.128.0` | `17.14.22` | TBD | TBD | TBD |
| Claude Opus 5.5      | TBD | `17.14.6` | TBD | TBD | TBD |
| Claude Sonnet 5  | `v1.124` | `17.14.6` | TBD | TBD | TBD |
| Claude Sonnet 5.5 | TBD | `17.14.6` | TBD | TBD | TBD |
| Claude Haiku 5.5  | TBD | TBD | TBD | TBD | TBD |
| Claude Fable 5      | `v1.124` | `17.14.6`                    | TBD | TBD | TBD |
| Claude Fable 5.1    | TBD | TBD                    | TBD | TBD | TBD |
| Claude Fable 5.2    | TBD | TBD                    | TBD | TBD | TBD |
| Kimi K3     | `v1.131` | TBD            | TBD | TBD | TBD |
| MAI Code 1.1 Flash  | `v1.121` | TBD                            | TBD | TBD | TBD |
| Grok 4.5             | TBD | `17.14.19` | TBD | TBD | TBD |
| Grok 4.6             | TBD | TBD | TBD | TBD | TBD |
| Grok 4.7             | TBD | `17.14.19` | TBD | TBD | TBD |

{% endrowheaders %}

> [!NOTE]
>
> * For GPT-5.3-Codex in Visual Studio Code, `v1.108` and later provide improved prompting and response quality.
> * "No minimum listed" means the reviewed changelog or release guidance did not specify a minimum version, not that all older versions are supported.
> * Even when a model appears in the model picker on older supported versions, prompting and model behavior may work best with the latest IDE and Copilot extension or plugin versions.

## Supported AI models per Copilot plan

The following table shows which AI models are available in each Copilot plan. For more information about the plans, see [AUTOTITLE](/copilot/get-started/plans).

> [!NOTE] Copilot Student and Copilot Free users have access to models through auto model selection only.

{% rowheaders %}

| Available models                               | Copilot Pro  | Copilot Pro+ | Copilot Max | Copilot Business | Copilot Enterprise |
|---------------------------------------------------------|-------------------------------------------------|-----------------------------------------------------|------------------------------------------------|-----------------------------------------------------|-------------------------------------------------------|
| Claude Haiku 4.5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Haiku 5.5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Opus 4.8 | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Opus 4.8 (fast mode) (preview) | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Opus 5 | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Opus 5.5 | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Fable 5[^claude-fable-5] | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Fable 5.1[^claude-fable-5] | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Fable 5.2[^claude-fable-5] | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Sonnet 4.6[^claude-sonnet-46-plans] | (icon: check) | (icon: check) | (icon: x) | (icon: x) | (icon: x) |
| Claude Sonnet 5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Claude Sonnet 5.5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Gemini 3.8 Flash | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Gemini 4 Argon | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Gemini 4 Carbon | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-5.3-Codex | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-5.4 nano[^gpt54nano] | (icon: x) | (icon: check) | (icon: check) | (icon: x) | (icon: x) |
| GPT-5.6 Luna | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-5.6 Sol | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-5.6 Terra | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-6 Astra | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-6 Luna | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-6 Sol | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-6.1 Sol | (icon: x) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| GPT-6.1 Terra | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Grok 4.5 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Grok 4.6 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Grok 4.7 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| Kimi K3 | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |
| MAI-Code-1.1-Flash | (icon: check) | (icon: check) | (icon: check) | (icon: check) | (icon: check) |

{% endrowheaders %}

[^gpt54nano]: GPT-5.4 nano is currently only available in the Codex Visual Studio Code extension (Copilot Pro+ only) and is not available in Copilot Chat.

[^claude-sonnet-46-plans]: Claude Sonnet 4.6 was retired on September 1, 2026, but remains available to individual Copilot subscribers on annual Copilot Pro and Copilot Pro+ plans. It is not available to subscribers on monthly plans.

> [!NOTE]
> * If you're an organization or enterprise owner, you can enable or restrict access to specific models for your members. See [AUTOTITLE](/copilot/how-tos/copilot-on-github/set-up-copilot/configure-access-to-ai-models#setup-for-organization-and-enterprise-plans).

## Fallback and long-term support (LTS) models

For more information about fallback and LTS models, see [AUTOTITLE](/copilot/concepts/models/fallback-and-lts-models).

## Evaluation models

GitHub Copilot offers access to evaluation models.

> [!IMPORTANT]
> * Testing revealed evaluation models may perform worse than other models on security-related, or other categories of prompts.
> * Users should always carefully review and validate code, including code security, using a range of models and with a thorough human review before incorporating suggestions into production.

Evaluation models may appear in the product with codenames rather than official model or provider names. These models come from or are fine-tuned by one or more of the following providers: Microsoft, OpenAI, Anthropic, and Google. Data handling for each provider is limited to GitHub's existing agreement with that provider, and evaluation models undergo GitHub and Microsoft testing and verification before release.

Evaluation models may be added, updated, or removed without notice. Availability and rate limits may differ from generally available models.

Access to evaluation models in auto model selection  for users Copilot plans for individuals is governed by a policy. To disable evaluation models:

1. In the upper-right corner of any page on GitHub, click your profile picture, then click **(icon: gear) Settings**.
1. At the top of the page, click **(icon: copilot) AI controls**.
1. For the **Evaluation models in Copilot auto model selection** setting, select **Disabled** from the dropdown.

[^mai-models]: MAI models are continuously improving models. Performance and behavior may evolve over time as new checkpoints are released.

## Utility models

Utility models power background features across surfaces, and cannot be disabled or selected in the model picker. See [AUTOTITLE](/copilot/concepts/models/utility-models).

## Models eligible for default enablement

For enterprises on a Copilot Business or Copilot Enterprise plan, a policy controls whether unconfigured generally available (GA) models are enabled or disabled by default. See [AUTOTITLE](/copilot/concepts/enterprise/default-model-availability).

The default policy applies to models that you have not explicitly configured. These models are indicated in your enterprise or organization's model settings with the **Delegate to Default Policy** label. When a new model is released, it inherits the default until you explicitly configure it.

The following models are **not** in scope. They are disabled by default, regardless of your "Default availability" policy setting.

* Pre-GA models
* Open weight models (DeepSeek, Kimi K3)
* Models that are not covered by GitHub's data retention agreement (Claude Fable 5, Claude Fable 5.1, Claude Fable 5.2)
* For enterprises that have restricted models to data-resident or FedRAMP-compliant models, any models that do not respect these policies

## Model support

If a particular model seems unavailable, refer to the model vendor's support page for the latest information about its availability. If more than one model from different vendors is unavailable, contact [GitHub Support](https://support.github.com) or refer to the [GitHub status page](https://www.githubstatus.com/) for additional information.

## Model retirement history

The following table lists AI models that are retired or scheduled for retirement from Copilot, along with their retirement dates and suggested alternatives.

{% rowheaders %}

| Model name                                                  | Retirement date             | Suggested alternative             |
|-------------------------------------------------------------|-----------------------------|-----------------------------------|
| Gemini 3.7 Flash | 2026-10-19 | Latest Gemini Flash model |
| GPT-5 mini | 2026-10-19 | Latest GPT Luna model |
| GPT-5.4 | 2026-10-19 | Latest GPT Sol model |
| GPT-5.4 mini | 2026-10-19 | Latest GPT Luna model |
| GPT-5.5 | 2026-10-19 | Latest GPT Sol model |
| Claude Opus 4.7 | 2026-10-02 | Latest Claude Opus model |
| Gemini 3.5 Flash | 2026-10-02 | Latest Gemini Flash model |
| Gemini 3.6 Flash | 2026-10-02 | Latest Gemini Flash model |
| Kimi K2.7 Code | 2026-10-02 | Latest Kimi model |
| MAI-Code-1-Flash | 2026-09-10 | Latest MAI-Code model |
| Claude Opus 4.5 | 2026-09-01 | Latest Claude Opus model |
| Claude Opus 4.6 | 2026-09-01 | Latest Claude Opus model |
| Claude Sonnet 4.5 | 2026-09-01 | Latest Claude Sonnet model |
| Claude Sonnet 4.6[^claude-sonnet-46-annual] | 2026-09-01 | Latest Claude Sonnet model |
| Gemini 3.1 Pro | 2026-09-01 | Latest Gemini Flash model |
| Raptor mini | 2026-09-01 | Latest MAI-Code model |
| Gemini 2.5 Pro | 2026-07-31 | Latest Gemini Flash model |
| Gemini 3 Flash | 2026-07-31 | Latest Gemini Flash model |
| Claude Opus 4.6 (fast mode) (preview) | 2026-06-29 | Latest Claude Opus model in fast mode |
| GPT-5.2 | 2026-06-05 | Latest GPT model |
| GPT-5.2-Codex | 2026-06-05 | Latest GPT Codex model |
| GPT-4.1 | 2026-06-01 | Latest GPT model |
| Grok Code Fast 1 | 2026-05-15 | Latest GPT mini model |
| Claude Sonnet 4 | 2026-05-01 | Latest Claude Sonnet model |
| GPT-5.1 | 2026-04-15 | Latest GPT Codex model |
| GPT-5.1-Codex | 2026-04-01 | Latest GPT Codex model |
| GPT-5.1-Codex-Max | 2026-04-01 | Latest GPT Codex model |
| GPT-5.1-Codex-Mini | 2026-04-01 | Latest GPT Codex model |
| Gemini 3 Pro | 2026-03-26 | Latest Gemini Flash model |
| Claude Opus 4.1 | 2026-02-17 | Latest Claude Opus model |
| GPT-5 | 2026-02-17 | Latest GPT model |
| GPT-5-Codex | 2026-02-17 | Latest GPT Codex model |
| Claude Sonnet 3.5 | 2025-11-06 | Latest Claude Haiku model |
| Claude Opus 4 | 2025-10-23 | Latest Claude Opus model |
| Claude Sonnet 3.7 | 2025-10-23 | Latest Claude Sonnet model |
| Claude Sonnet 3.7 Thinking | 2025-10-23 | Latest Claude Sonnet model |
| Gemini 2.0 Flash | 2025-10-23 | Latest Gemini Flash model |
| o1-mini | 2025-10-23 | Latest GPT mini model |
| o3 | 2025-10-23 | Latest GPT model |
| o3-mini | 2025-10-23 | Latest GPT mini model |
| o4-mini | 2025-10-23 | Latest GPT mini model |

{% endrowheaders %}

[^claude-sonnet-46-annual]: Claude Sonnet 4.6 remains available to individual Copilot subscribers on annual plans. The retirement of Claude Sonnet 4.6 does not apply to these subscribers.

## Next steps

* To get up and running with Copilot, see [AUTOTITLE](/copilot/get-started/quickstart-for-using-github-copilot-on-github-com) and [AUTOTITLE](/copilot/get-started/quickstart-for-using-github-copilot-in-your-ide) .
* To configure which models are available to you, see [AUTOTITLE](/copilot/how-tos/copilot-on-github/set-up-copilot/configure-access-to-ai-models).
* To learn more about Responsible Use and Responsible AI, see [Copilot Trust Center](https://copilot.github.trust.page/) and [AUTOTITLE](/copilot/responsible-use).
