---
title: Debugging invalid JSON
shortTitle: Debug invalid JSON
intro: 'Copilot Chat can identify and resolve syntax errors or structural issues in JSON data.'
redirect_from:
  - /copilot/example-prompts-for-github-copilot-chat/debugging-errors/debugging-invalid-json
  - /copilot/copilot-chat-cookbook/debugging-errors/debugging-invalid-json
  - /copilot/tutorials/copilot-chat-cookbook/debugging-errors/debugging-invalid-json
  - /copilot/tutorials/copilot-chat-cookbook/debugging-errors/debug-invalid-json
  - /copilot/copilot-chat-cookbook/debugging-errors/debugging-invalid-json
  - /copilot/tutorials/copilot-chat-cookbook/debug-errors/debug-invalid-json
versions:
  feature: copilot
category:
  - Debugging code
  - Author and optimize with Copilot
  - Improve quality and maintainability
surface:
  - Chat
octicon: bug
contentType: tutorials
---

When working with JSON data, you may encounter issues such as trailing commas, mismatched braces, or incorrect data types that make the JSON invalid. GitHub Copilot Chat can help you debug and fix these errors by suggesting corrections to fix invalid JSON.

## Example scenario

Consider a scenario where an application consumes JSON data from an API, but the response fails to parse due to invalid formatting. You receive the error message:

```bash
Error: Parse error
----------------------^
Expecting 'STRING', 'NUMBER', 'NULL', 'TRUE', 'FALSE', '{', '[', got 'undefined'
```

Below is the JSON data that caused the error:

```json id=json-error
{
  "location": "San Francisco",
  "current_weather": {
    "temperature": 18,
    "unit": "Celsius",
    "conditions": "Cloudy
  },
  "forecast": {
    "day": "Monday",
    "high": 22,
    "low": 15,
    "precipitation": 10
  }
}
```

## Example prompt

```copilot copy prompt ref=json-error
Why is my JSON object invalid and how can I fix it?
```

## Example response

> [!NOTE] The following response is an example. Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.

Copilot might suggest that your JSON is invalid because it's missing a closing quote for the `conditions` value. Here is the corrected JSON:

```json
{
  "location": "San Francisco",
  "current_weather": {
    "temperature": 18,
    "unit": "Celsius",
    "conditions": "Cloudy"
  },
  "forecast": {
    "day": "Monday",
    "high": 22,
    "low": 15,
    "precipitation": 10
  }
}
```

In this example response, Copilot's suggestions include fixing the closing quote for the `conditions` value, which resolves the JSON parsing error.

## Further reading

* [AUTOTITLE](/copilot/concepts/prompting-and-context/prompt-engineering)
* [AUTOTITLE](/copilot/get-started/best-practices)
