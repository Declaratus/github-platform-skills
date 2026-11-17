# Copilot Trust Center: data retention, training and IP indemnity

Hand-maintained notes from GitHub's [Copilot Trust Center FAQ](https://copilot.github.trust.page/faq). The FAQ is not part of `github/docs`, so the build does not refresh this file.

- Captured: 2026-11-17, from the rendered FAQ page.
- Wording is paraphrased. Each line links the FAQ entry it comes from; quote that entry, not this file, when exact wording matters.
- Scope: Copilot Business and Copilot Enterprise unless a line says otherwise. The FAQ entries captured here do not mention the Copilot access plan, so whether they apply to it is unverified.
- Recheck the live FAQ before relying on these notes for a current answer. It is a rendered trust.page, not a docs.github.com page, so the `.md` trick does not apply. If you cannot load it, say the FAQ was not checked live and give the capture date.

## Retention (Business and Enterprise defaults)

Source: [How long does GitHub retain Copilot data for Business and Enterprise customers?](https://copilot.github.trust.page/faq?s=b9buqrq7o9ssfk3ta50x6)

| How Copilot is used | Inputs and outputs | User engagement data | Feedback data |
| --- | --- | --- | --- |
| Chat and code completions in the IDE, the Copilot app, Copilot CLI | Not retained by default | Two years | As long as needed for its purpose |
| All other Copilot access and use | Retained for the life of the account | Two years | As long as needed for its purpose |

- In both cases GitHub may retain inputs and outputs for a limited time to investigate confirmed Acceptable Use Policy or Terms of Service violations, or to protect the security and integrity of the service. The FAQ calls this targeted and time-limited, under the Data Protection Agreement (DPA).
- Some Copilot CLI commands can write inputs or outputs to repositories, where normal repository retention applies.
- Copilot Vision (listed under other Copilot use): images are deleted from active processing within 48 hours unless flagged, and flagged images within 30 days. They are not used to train or fine-tune models.
- Definitions, from [What personal data does GitHub Copilot process?](https://copilot.github.trust.page/faq?s=vjh8wz7ajqbq0256cpk5kj):
  - Inputs: prompts, attachments, workspace code and conversation history.
  - Outputs: responses and suggestions.
  - User engagement data: pseudonymous interaction data such as accepted or dismissed suggestions, errors, system logs and usage metrics.
  - Feedback data: reactions, optional comments and support-ticket feedback.
- Agentic features, from [How do Copilot's agentic features handle data governance and user privacy?](https://copilot.github.trust.page/faq?s=lvd1dmc8qq4z6bvsuz3cxx):
  - Data the agent reads for a task is processed in the GitHub Actions runner and retained for the duration of the task.
  - On GHE.com with data residency, that data stays in region. On GitHub.com it may be processed anywhere.
  - The FAQ describes Actions-runner sessions only. Cloud sandbox sessions differ; see `copilot-on-github.md` below.

### Related pages in the bundled docs

These add detail by surface. Where they differ from the FAQ, give both and cite each.

- `references/concepts/copilot-surfaces/copilot-on-github.md`: chat data in GitHub Actions-based sessions is retained for 28 days, and in cloud sandbox sessions for the life of the account. The FAQ gives "life of the account" for all non-IDE use and does not mention the 28-day case.
- `references/how-tos/copilot-on-github/chat-with-copilot/chat-in-github.md`: Copilot Chat on GitHub keeps up to 100 recent conversations, and deletes messages after 28 days. This is also shorter than the FAQ's "life of the account".
- `references/concepts/security-governance-and-network-settings/session-data.md`: for Business and Enterprise, local CLI and app sessions stay local unless the "Store local sessions in the Cloud" policy is set to at least "View from cloud".
- `references/concepts/prompting-and-context/copilot-memory.md`: Copilot Memory repository facts expire after 90 days by default, configurable from 7 to 180 days. User-level preferences always use the default, and if an organization and its enterprise both set a period, the shorter one applies.
- `references/reference/ai-models/model-hosting.md`: per-provider retention: zero data retention (ZDR) agreements with OpenAI, Anthropic (generally available features), xAI and Fireworks, and Google Durable Caching for Gemini models (encrypted, up to 24 hours, not used for training).

## Training

- Business and Enterprise data is not used to train AI models. The DPA prohibits it without customer authorization. [FAQ](https://copilot.github.trust.page/faq?s=v2qe7voltpwtv2usl4ikhs); also `references/how-tos/manage-your-account/manage-policies.md`.
- GitHub does not retain Business or Enterprise code or queries for training, even for preview features and models used under the pre-release terms. [FAQ](https://copilot.github.trust.page/faq?s=0hs16u5png8o7w27rwux) DPA coverage itself is generally available features plus the listed DPA-covered previews (`references/tutorials/roll-out-at-scale/govern-at-scale/resources-for-approval.md`).
- GitHub does not train on the contents of any paid organization's repositories, even when a user works there with a personal Free, Pro, Pro+ or Max plan. It also excludes the interaction data of anyone who is a member or outside collaborator of a paid organization. [FAQ](https://copilot.github.trust.page/faq?s=jx7wyz2ck24557t3vjq38v)
- Individual plans (Free, Pro, Pro+, Max) may be used for training unless the user opts out. [FAQ](https://copilot.github.trust.page/faq?s=i0rqxc8ormqky35nbk9l34)
- Third-party model providers do not train on customer data or retain customer code. The exception is Claude Fable 5: Anthropic retains prompts and outputs to run safety classifiers. [FAQ](https://copilot.github.trust.page/faq?s=qoerjag9v36a9muz82voo). `references/reference/ai-models/model-hosting.md` extends this to Fable 5.1 and 5.2, says retention is the default (ZDR by request through the end of 2026 under a time-bound exemption), and says some Anthropic beta or preview features are outside ZDR.
- Third-party models use the customer's existing GitHub or Microsoft contract. Providers are GitHub subprocessors, and their own terms do not flow down to customers. [FAQ](https://copilot.github.trust.page/faq?s=b1xo2pn45zwpqavomhe8)

## IP indemnity and the public-code filter

- Business and Enterprise customers are entitled to IP indemnification for Copilot responses. [FAQ](https://copilot.github.trust.page/faq?s=mp8vvy1z1ym1knw9id4ri)
- Indemnity is uncapped for unmodified outputs when the customer follows Microsoft's required mitigations for GitHub offerings. For most features, either: [FAQ](https://copilot.github.trust.page/faq?s=lvwf3vcwslo6dvac56p1n8)
  - set "Suggestions matching public code" to Block; or
  - set it to Allow, use code referencing, and comply with the licenses it cites.
- The public-code filter does not apply to Copilot coding agent, but unmodified code the agent generates is still covered. (Same FAQ entry.)
- Third-party models are covered by the contractual indemnity. [FAQ](https://copilot.github.trust.page/faq?s=roivyyje3cb0mu16z82x8)
- The optional filter checks code outputs for matches or near-matches against public GitHub code of 65 lexemes or more (about 150 characters on average), and does not show matching output. An enterprise admin can set it for all organizations or defer control to each organization. [FAQ](https://copilot.github.trust.page/faq?s=5kqpw9aqvigdth1jvnrrme)
- The bundled docs show the filter policy applies to IDEs and, in annotate mode only, to GitHub Actions-based cloud sessions. Copilot CLI, the GitHub Copilot app, cloud sandbox sessions and code review can return matching code even when the policy is Block (`references/reference/supported-surfaces-for-policies.md`, `references/responsible-use/agents.md`). The FAQ names only the coding agent as an exception, so whether the indemnity mitigation is met on those other surfaces is unverified; confirm with GitHub.
- Where an output is capable of being owned, GitHub does not claim ownership. [FAQ](https://copilot.github.trust.page/faq?s=lk4105tkl6mqx73u6f8d9h)

## Contract documents

- Bought from GitHub: the GitHub Customer Agreement. Its Generative AI Services Terms cover code ownership, indemnity and data use, and the agreement also includes the GitHub DPA. [FAQ](https://copilot.github.trust.page/faq?s=og9w8tc0i9aagny4fhnmz)
- Bought through Microsoft: substantively the same terms. The Microsoft Privacy and Security Terms incorporate the GitHub DPA, and the Microsoft DPA does not apply to GitHub's online services. [FAQ](https://copilot.github.trust.page/faq?s=wz10uxnrfk656duvtkzwi)
