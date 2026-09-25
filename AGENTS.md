# AGENTS.md - ChatGPT / Codex operating instructions

## Mission

Use Jev as a fast semantic decision layer, not as a replacement for a reasoning model.

Whenever a task contains a large set of records, documents, sources, contacts, leads, tasks, commits or candidate actions, first decide whether Jev can reduce the set or attach useful typed judgments before using a more expensive reasoning model.

## Mandatory division of labour

1. **Deterministic code owns**
   - counting
   - date arithmetic
   - joins and matching
   - deduplication
   - exact string/ID comparison
   - mathematical formulas
   - thresholds
   - weighted/composite ranking

2. **Jev owns**
   - semantic classification
   - bounded judgment
   - rubric scoring
   - intent/role/topic routing
   - uncertainty estimation

3. **ChatGPT/Codex owns**
   - planning
   - multi-step reasoning
   - research synthesis
   - writing
   - explaining results
   - proposing candidate actions
   - coding the surrounding workflow

4. **Human review owns**
   - destructive actions
   - external communication unless explicitly authorised
   - material business decisions when confidence/evidence is weak
   - changes with high financial, privacy, legal or reputational impact

## Jev question design rules

- One semantic idea per question.
- Prefer many independent questions in one request over one broad question.
- Every Choice should include an escape option such as `unknown`, `unclear` or `other`.
- Keep question text and thresholds centralised in the question registry.
- Give Jev only the fields necessary for the judgment.
- Do not ask Jev to count, do math or perform exact matching.
- Use confidence/probability as a routing input, never as proof.
- Calibrate thresholds using labelled examples from the real domain.
- Pin a model version after calibration if threshold stability matters.
- Log model version, question version, state schema version and decision outcome.

## Agent routing

When processing an incoming project item, classify at least:

- project
- artifact_type
- semantic_topic
- lifecycle_stage
- actionability
- urgency
- source_quality
- completeness
- contradiction_risk
- duplicate_or_stale
- requires_reasoning_model
- requires_human_review

Then route:
- low-risk + high-confidence + deterministic handler available -> handle automatically
- analysis/writing needed -> ChatGPT
- repository/code execution needed -> Codex/Claude Code
- low confidence or high consequence -> human review

## Project rule

For Atlas and God's Eye, never ask the reasoning model to reread the entire corpus if a Jev prefilter can narrow the relevant set first.
