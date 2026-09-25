# Implementation roadmap

## Phase 0 - foundation

- [x] Create JEV repository
- [x] Add ChatGPT/Codex instructions
- [x] Add Claude instructions
- [x] Document Atlas, God's Eye and LinkedIn architecture
- [x] Add initial question registry
- [ ] Create TypeSafe account/API key
- [ ] Install official TypeSafe skill in Claude Code
- [ ] Install skill in the coding environment used with ChatGPT/Codex where supported
- [ ] Add secret locally as TYPESAFE_API_KEY

## Phase 1 - prove Jev with a tiny evaluation

- [ ] Build one CLI/script calling `jev-latest`
- [ ] Run 20 synthetic records
- [ ] Record model/version/latency/usage
- [ ] Verify probabilities/confidence and error handling

## Phase 2 - LinkedIn pilot

- [ ] Export Connections.csv and Invitations.csv from LinkedIn
- [ ] Keep exports outside Git
- [ ] Create labelled sample of 50-100 rows
- [ ] Implement first-pass questions
- [ ] Evaluate false positives/negatives
- [ ] Tune thresholds
- [ ] Run full export
- [ ] Enrich only selected rows
- [ ] Produce reviewable priority list

## Phase 3 - Atlas JEV Control Plane

- [ ] inventory current Atlas source cards/artifacts
- [ ] sample 100-300 items
- [ ] label 40-60
- [ ] implement source/usefulness/actionability questions
- [ ] generate project-state compiler
- [ ] compare "full LLM read" vs "Jev prefilter + LLM" on cost/time/quality

## Phase 4 - God's Eye

- [ ] freeze segment feature schema
- [ ] select 30-50 candidate segments
- [ ] label semantic quality/commercial usefulness
- [ ] implement segment judge
- [ ] add overclaim/manual-review gates
- [ ] integrate with deterministic lift/reach calculations

## Phase 5 - Gmail and research

- [ ] relationship/contact triage
- [ ] thread intent + follow-up queue
- [ ] research corpus first-stage filter
- [ ] knowledge novelty/contradiction routing

## Definition of done for any Jev automation

A workflow is not production-ready until:
- state fields are explicit
- deterministic work is separated
- questions are versioned
- thresholds are tested on labelled data
- low-confidence path exists
- privacy is minimised
- decision receipts are logged
- human override is possible
