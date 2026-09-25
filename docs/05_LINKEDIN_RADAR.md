# LinkedIn Radar blueprint

## Goal

Classify a large LinkedIn network quickly, then spend expensive research/personalisation only on the best candidates.

## Input

Use LinkedIn's own data export for Connections and Invitations.

## Preprocessing

Code should:
- detect the real CSV header
- parse dates
- compute connection/invitation age buckets
- match outgoing invitations against connections
- count missing fields
- never infer unavailable location/revenue/company-size fields before enrichment

## First-pass Jev state

Connections:
- position
- company
- connected_for
- optional name suffix/credentials

Invitations with message:
- name
- message
- invitation_age

## First-pass questions

Connections:
- role_family: Choice
- seniority: Choice
- company_type_from_text: Choice
- target_role_fit: Noul
- obvious_disqualifier: Noul
- company_text_is_ambiguous: Noul

Invitations:
- message_intent: Choice
- self_described_seniority: Choice
- appears_personalized: Noul
- commercial_pitch: Noul

Rows with insufficient signal should go to an explicit review/no-signal bucket.

## Enrichment

Only enrich selected/review candidates. Then add:
- geography fit
- company scale rubric
- likely decision-maker
- company/industry fit
- recent activity class

## Tiering

Tiering is code, not Jev. Example:
- high fit + sufficient confidence -> priority
- partial fit or ambiguity -> review/enrich
- clear disqualifier -> reject
- missing evidence -> no-signal

Thresholds must be calibrated on a labelled sample.

## Safety/privacy

- keep raw exports out of Git
- minimise fields sent to Jev
- keep API keys in environment variables
- log IDs/hashes where possible rather than raw personal data
- no automatic messaging without a separate explicit authorisation step

## Output

CSV/Sheet with:
- profile URL
- deterministic metadata
- Jev answers
- probabilities/confidence
- tier
- enrichment status
- review flag
- outreach status

The reasoning model drafts outreach only for the final selected set.
