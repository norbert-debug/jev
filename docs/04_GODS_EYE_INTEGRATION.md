# God's Eye / lookalike integration

## Working definition

God's Eye is treated here as the lookalike/audience intelligence project: build commercially useful consumer/audience segments from first-party/context data and enrichment, inspired by the earlier Mastercard-style audience insight concept.

## Correct role for Jev

Jev should **not** calculate lookalikes.

The mathematical/data layer must create the candidate cohorts and features first. Jev then supplies fast semantic judgments over those features.

## Pipeline

```
raw customer/context data
 -> consent/privacy controls
 -> deterministic identity and feature engineering
 -> cohort / benchmark / lift calculations
 -> candidate segments
 -> Jev semantic labelling + quality judgments
 -> code-based portfolio ranking
 -> reasoning model creates commercial narrative
 -> human approval
 -> activation/export
```

## Candidate Jev dimensions

For a candidate segment:
- semantic_theme: household / mobility / digital / commerce / lifestyle / local-context / business / other
- advertiser_vertical_fit: Choice
- label_supported_by_features: Noul
- label_specificity: Score
- commercial_interpretability: Score
- likely_actionable_for_media_buying: Noul
- risk_of_overclaiming: Noul
- requires_manual_review: Noul

For enrichment records:
- feature semantically consistent with claimed segment
- likely noisy/ambiguous context
- mapping belongs to a given high-level taxonomy

## Deterministic calculations

Code owns:
- overrepresentation vs baseline
- lift/index
- reach
- minimum cohort size
- frequency
- freshness
- geographic aggregates
- identity matching
- suppression
- privacy eligibility
- activation IDs

## Deliverable structure

Each sellable segment should have:
- stable segment ID
- deterministic definition
- supporting features
- reach
- lift/index
- freshness
- Jev semantic label
- Jev confidence/ambiguity
- allowed/forbidden claims
- target advertiser categories
- activation route
- provenance

## Pilot

Select 30-50 candidate segments from existing data. Have a human label semantic quality and commercial usefulness. Calibrate Jev on these before applying the system to the full candidate universe.
