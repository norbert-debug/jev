# Prioritised use cases

## P0 - implement first

### 1. LinkedIn Relationship Radar
Goal: turn a very large network into a small reviewable list.

Jev:
- role family
- seniority
- target-role fit
- company-type fit from available text
- invitation intent
- disqualifiers
- semantic ambiguity

Code:
- parsing
- accepted/pending matching
- age buckets
- joins
- tier rules
- ranking math

Reasoning model:
- profile research for selected people
- outreach strategy
- personalised message drafts

### 2. Atlas Source and Opportunity Router
Goal: stop reasoning models from repeatedly reading the full Atlas corpus.

Jev:
- source category
- dataset usefulness
- commercial signal type
- likely customer/problem class
- evidence quality
- whether a new artifact contradicts current project knowledge
- whether an item warrants deeper analysis

Code:
- freshness dates
- URLs/checksums
- duplicate detection
- dataset joins
- numeric calculations

Reasoning model:
- synthesize opportunity hypotheses
- design data products
- produce implementation plans

### 3. God's Eye / lookalike Segment Judge
Goal: add a semantic decision layer over precomputed audience/customer features.

Jev:
- segment interpretation
- likely behavioural/contextual theme
- advertiser/category fit
- semantic consistency of candidate segments
- weak/ambiguous segment flags

Code:
- over-index/lift
- cohort construction
- frequency
- population thresholds
- joins/identity matching
- privacy rules

Reasoning model:
- commercial naming
- proposition
- client narrative
- segment portfolio design

## P1

### Gmail / relationship intelligence
- contact type
- thread intent
- relationship category
- commercial relevance
- reply-needed signal
- evidence of promised follow-up

Use Gmail connector/exports to retrieve permitted data; do not let Jev perform date arithmetic.

### Research radar
- bulk source classification
- relevance-to-current-project
- evidence type
- novelty vs current knowledge
- actionability
- audience fit

Only shortlisted sources go to full-text reasoning.

### Project knowledge hygiene
On every new artifact:
- which project does it belong to?
- is it a decision, fact, hypothesis, task, source, result or obsolete note?
- does it update an existing fact?
- does it conflict with current knowledge?
- should it become source of truth?
- is human review required?

## P2

- job/recruitment opportunity triage
- affiliate-program and partner classification
- client/lead scoring
- CRM notes routing
- support inbox routing
- data-quality issue triage
- document QA gates
- change-log prioritisation
