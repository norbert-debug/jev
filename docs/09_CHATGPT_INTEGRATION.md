# ChatGPT integration

Updated: 2026-09-25

## Current status

A search of the current ChatGPT plugin directory did not surface a direct TypeSafe/Jev plugin.

Therefore there are two distinct integration modes:

### A. Codex / coding-agent mode

Use:
- this repository's `AGENTS.md`;
- the official TypeSafe agent skill through skills.sh where the agent environment supports it;
- the official TypeSafe SDK in repository code.

This is the preferred immediate path for code and project automation.

### B. Hosted ChatGPT mode

To make Jev a callable tool inside a hosted ChatGPT workflow, expose a small private connector/tool wrapper around the official TypeSafe API.

The wrapper should have one primary tool:

`jev_evaluate(state, questions, model?)`

The API key stays server-side. The model sees only the tool schema and returned typed judgments.

## Tool contract

Input:
- `state`: string, JSON object or array of text accepted by the Jev integration
- `questions`: versioned Choice / Score / Noul question map
- `model`: optional, default `jev-latest`

Output:
- resolved model version
- answers
- probabilities
- confidence where applicable
- usage
- request/decision metadata needed for receipts

## Required ChatGPT behavior

Before deep reasoning over a large set:
1. perform deterministic preprocessing;
2. use Jev for semantic filtering/routing where appropriate;
3. use confidence to choose auto-route vs reasoning vs review;
4. send only selected/ambiguous cases to the full reasoning model;
5. preserve raw Jev outputs for audit/evaluation.

## Security

- never place `TYPESAFE_API_KEY` in the conversation state;
- never expose the key as a tool argument;
- keep raw LinkedIn/Gmail/private project exports out of the public repository;
- minimise the state sent to Jev;
- require a separate authorization gate for consequential external actions.

## Why the wrapper is deliberately small

The semantic contract belongs in `config/question-registry.yaml` and policy code, not inside the connector. This keeps ChatGPT and Claude using the same questions and thresholds.
