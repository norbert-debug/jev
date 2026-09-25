# JEV Control Plane

This repository is the working knowledge base and implementation blueprint for using TypeSafe AI's Jev together with ChatGPT/Codex and Claude Code.

## What Jev is

Jev is TypeSafe AI's System One model. It does not generate prose. It receives a **state** plus typed questions and returns structured decisions and probabilities. The supported primitives are:

- **Choice**: choose one option from a fixed set.
- **Score**: place an item on an ordered rubric.
- **Noul**: estimate whether a proposition is true.

The design rule for this repository is simple:

> **Jev judges. Code combines. ChatGPT/Claude reason and write. Humans approve consequential actions.**

## Why we are using it

Jev should become the low-cost decision layer in front of expensive reasoning models. It is best used for large-volume work such as:

- LinkedIn contact and invitation classification
- Gmail/contact triage
- research corpus filtering
- lead and account prioritisation
- source/data quality classification
- project artifact routing
- detecting stale, duplicate, conflicting or incomplete information
- deciding what deserves deeper analysis by ChatGPT or Claude
- quality gates before an agent acts

## Target architecture

```
Sources
  GitHub / Drive / Gmail / LinkedIn exports / public data / APIs
      |
      v
Deterministic preprocessing
  parsing / joins / dates / dedupe / math / identifiers
      |
      v
Jev
  atomic semantic judgments + probabilities
      |
      v
Policy engine
  thresholds / composite scores / confidence gates / routing
      |
      +--> auto-handle low-risk work
      +--> ChatGPT/Codex for research, synthesis, writing
      +--> Claude Code for repository/code work
      +--> human review for consequential or uncertain cases
```

## Repository map

- `AGENTS.md` - instructions for ChatGPT/Codex
- `CLAUDE.md` - instructions for Claude Code
- `docs/00_SOURCE_RESEARCH.md` - source inventory and findings
- `docs/01_ARCHITECTURE.md` - JEV Control Plane architecture
- `docs/02_USE_CASES.md` - prioritised use-case map
- `docs/03_ATLAS_INTEGRATION.md` - Atlas integration design
- `docs/04_GODS_EYE_INTEGRATION.md` - God's Eye/lookalike integration design
- `docs/05_LINKEDIN_RADAR.md` - LinkedIn implementation blueprint
- `docs/06_CHATGPT_CLAUDE_OPERATING_MODEL.md` - cross-agent operating rules
- `docs/07_ROADMAP.md` - implementation roadmap
- `config/question-registry.yaml` - first question registry
- `.env.example` - secret names only

## Official sources

- https://typesafe.ai/
- https://docs.typesafe.ai/introduction
- https://github.com/typesafe-ai
- https://github.com/typesafe-ai/skills
- https://github.com/typesafe-ai/typesafe-sdk-js
- https://github.com/typesafe-ai/typesafe-sdk-python

## Case-study source

- https://ruben.substack.com/p/jev
- https://jev.rubenhassid.ai/

The Substack material is referenced and summarized, not mirrored verbatim.

## Installation

### Claude Code

```bash
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai
```

Invoke explicitly with:

```
/typesafe:typesafe-ai
```

### Other coding agents / Codex-compatible environments

```bash
npx skills add typesafe-ai/skills --skill typesafe-ai
```

### API

Use `TYPESAFE_API_KEY` as an environment secret. Never commit the key.

Python:
```bash
pip install typesafe-sdk
```

JavaScript/TypeScript:
```bash
npm install @typesafe-ai/sdk
```

## Current implementation priority

1. Build the shared JEV Control Plane contract.
2. Run a LinkedIn pilot on exported Connections/Invitations.
3. Add project artifact classification for Atlas.
4. Add God's Eye/lookalike scoring.
5. Add Gmail and research pipelines.
6. Calibrate thresholds on labelled examples before automating higher-impact actions.

See `docs/07_ROADMAP.md`.
