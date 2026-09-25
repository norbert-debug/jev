# Source research

Updated: 2026-09-25

## Official TypeSafe findings

TypeSafe describes Jev as its flagship **System One** model: provide state plus typed questions and receive structured answers and probabilities directly.

Core primitives:
- Choice
- Score
- Noul

Important architectural points from the official documentation:

1. Questions should be atomic and independently answerable.
2. Multiple questions can be evaluated against the same state in one call.
3. Complex decisions should be decomposed into dimensions and recombined in code.
4. Choice and Score return probability distributions plus confidence.
5. Confidence should gate system behaviour; thresholds should reflect consequence/risk.
6. Low confidence is useful information and should route to review, clarification or a different system.
7. Jev currently accepts text/JSON/arrays of text, not images/audio/video.
8. Jev is not a prose, code or explanation generator.

Official patterns:
- speculative fan-out
- confidence-gated routing
- composite scoring
- intent routing

## Official integrations

Official TypeSafe GitHub repositories include:
- `typesafe-ai/skills`
- `typesafe-ai/typesafe-sdk-js`
- `typesafe-ai/typesafe-sdk-python`
- `typesafe-ai/system-one-adapter-python`

Claude Code plugin installation is supported through the official skill repository. Other coding agents can install the same skill through skills.sh.

## Ruben Hassid case studies

Source: https://ruben.substack.com/p/jev

The article demonstrates four useful patterns:

### LinkedIn
Export Connections and Invitations, perform deterministic parsing/matching in code, then use Jev to classify roles, company type, disqualifiers and invitation intent. Optionally enrich selected profiles and run a second pass.

### Gmail / Google contacts
Precompute email/domain/string facts in code and let Jev judge semantic contact type and professional relevance. Keep questions and thresholds centralised and validate against labelled rows.

### Research
Harvest a large corpus, use Jev for a cheap first-stage semantic filter, then a second-stage rubric, and send only the best subset to a generative model for human-readable synthesis.

### General lesson
Jev is most valuable when it shrinks or routes a large search space before an LLM does expensive reasoning.

## Provenance note

The Substack article is not mirrored verbatim here. This repository stores derived implementation notes and links to the original source.

## Community material

Community repositories such as `TypeSafeAI/jev-harness` are useful for architectural inspiration, particularly the "LLM proposes -> Jev judges narrow dimensions -> code decides" pattern, but `TypeSafeAI` is an unofficial community organisation. Official product authority remains `typesafe-ai`, typesafe.ai and docs.typesafe.ai.
