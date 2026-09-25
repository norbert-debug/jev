# JEV Control Plane architecture

## Objective

Create one reusable decision layer used by ChatGPT/Codex, Claude Code and project-specific applications.

## Core loop

```
1. COLLECT
2. NORMALIZE
3. PRECOMPUTE deterministic facts
4. JUDGE with Jev
5. COMBINE in policy code
6. ROUTE
7. REASON / WRITE / EXECUTE
8. VERIFY
9. LOG decision receipt
10. LEARN from human corrections
```

## Four planes

### 1. Data plane
Carries records, documents, messages, datasets, tasks and source metadata.

### 2. Judgment plane
Jev question sets grouped by domain. Every question set has:
- state schema
- question version
- allowed fields
- primitives
- expected uncertainty/escape options

### 3. Policy plane
Pure code:
- confidence thresholds
- composite scores
- risk policy
- model/tool routing
- stop conditions
- review queues

### 4. Reasoning/action plane
ChatGPT/Codex and Claude perform work that requires planning, synthesis, code generation or communication.

## Proposed routing contract

Every item can receive:

```json
{
  "project": "...",
  "artifact_type": "...",
  "topic": "...",
  "stage": "...",
  "actionability": 0,
  "commercial_relevance": 0,
  "source_quality": 0,
  "freshness_semantic": "...",
  "contains_conflict": 0,
  "looks_duplicate": 0,
  "needs_deep_reasoning": 0,
  "needs_human_review": 0
}
```

Numbers above are conceptual outputs; exact primitives/rubrics are defined per registry entry.

## LLM proposal review pattern

For agentic work, use a two-model contract:

1. Reasoning model proposes a candidate action.
2. Code packages the proposal plus local state.
3. Jev evaluates narrow questions, for example:
   - Is the action consistent with the stated goal?
   - Does the evidence support the claimed precondition?
   - Is required information missing?
   - Could the action have irreversible external impact?
4. Policy code chooses:
   - proceed
   - enrich/research
   - proposal-only
   - human review
   - reject/re-plan

Jev is evidence for routing, not an authority grant.

## Observability

Persist for each run:
- timestamp
- project
- input record ID/hash
- schema version
- question-set version
- Jev model version
- answers/probabilities/confidence
- policy rule that fired
- downstream model/tool
- human override
- eventual outcome

This creates an evaluation corpus for threshold tuning.
