# ChatGPT + Claude + Jev operating model

## Shared rule

Both agents should use the same JEV question registry and policy concepts. The goal is reproducibility: a classification should not depend on which generative model happened to run the workflow.

## ChatGPT / Codex

Best role:
- business/research orchestration
- connected-app retrieval
- synthesis across sources
- user-facing analysis
- document/report creation
- code/repository work when the environment supports it

Instruction:
> Before using a reasoning model on a large collection, check whether an atomic Jev classification/routing pass can reduce the set. Keep deterministic operations in code. Use Jev uncertainty to decide which items need deeper analysis or human review.

## Claude Code

Best role:
- codebase execution
- data pipelines
- CLI/scripts
- evaluation harnesses
- local file processing
- repository-wide refactors

Instruction:
> Use /typesafe:typesafe-ai when designing Jev workflows. Show the state contract, questions, thresholds and evaluation plan before implementing an automation.

## Cross-agent handoff artifact

Every large workflow should write/update a machine-readable run manifest:

```json
{
  "run_id": "...",
  "project": "...",
  "source_snapshot": "...",
  "state_schema_version": "...",
  "question_set_version": "...",
  "model_version": "...",
  "policy_version": "...",
  "items_processed": 0,
  "items_auto_routed": 0,
  "items_sent_to_reasoning": 0,
  "items_for_human_review": 0
}
```

## What Jev should never be asked to do

- write the final report
- make multi-step plans
- perform arithmetic
- compare exact identifiers
- execute tools
- decide permissions
- invent missing facts
- silently take external action
