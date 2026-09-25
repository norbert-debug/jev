# CLAUDE.md - Claude Code instructions for JEV

## First-time setup

Install the official TypeSafe skill:

```bash
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai
```

Use `/typesafe:typesafe-ai` whenever designing or reviewing Jev questions.

Store the API key only as `TYPESAFE_API_KEY` in an environment/secret store. Never write it to this repository.

## Working model

Jev is the fast judge. Claude is the planner/builder.

For every workflow:

1. normalize and compute deterministic facts in code;
2. define a compact state contract;
3. ask atomic Jev questions;
4. combine outputs with explicit thresholds/rules in code;
5. send only selected/ambiguous cases to Claude for deeper reasoning;
6. preserve a decision receipt: input reference, question version, model version, answer, probability/confidence, route.

## Before adding a Jev workflow

Produce:
- the state schema;
- the complete question set;
- thresholds and routing rules;
- labelled evaluation sample;
- false-positive and false-negative risks;
- what is deterministic vs semantic;
- privacy minimisation;
- expected fallback behavior.

Do not build UI or automation until the questions and thresholds are inspectable.

## Confidence policy

Default architecture:
- high confidence + low-risk action -> automatic route may be allowed;
- medium confidence -> review/enrichment/reasoning model;
- low confidence -> do not infer; route to review or collect more data.

Exact thresholds must be calibrated per use case.

## Atlas

Use Jev primarily to classify and route sources, datasets, extracted opportunities, contradictions, missing fields, freshness, actionability and likely commercial relevance. Do not use Jev for joins, geospatial calculations, numeric market sizing or exact entity resolution.

## God's Eye / lookalike

Use Jev for semantic segment labeling, propensity/fit dimensions and explainable bounded judgments over precomputed customer/context features. Code owns lift calculations, over-indexing, segment construction, joins and audience math.

## LinkedIn

Follow `docs/05_LINKEDIN_RADAR.md`.
