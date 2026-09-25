# Atlas integration

## Purpose

Atlas scans public/institutional internet data, combines sources and turns them into business-usable data products and opportunity hypotheses. Its working model already separates machine source-of-truth work in GitHub from human-facing reporting.

The JEV layer should reduce corpus size before deep reasoning.

## Atlas JEV pipeline

```
source discovered
 -> deterministic metadata extraction
 -> Jev source classifier
 -> policy gate
 -> fetch/parse selected source
 -> deterministic data-quality checks
 -> Jev semantic usefulness / opportunity judgments
 -> cluster and rank in code
 -> ChatGPT/Claude deep-dive on top candidates
 -> update Atlas knowledge base
```

## Source-level questions

Candidate dimensions:
- source_kind: registry / statistics / geospatial / legal / procurement / company / infrastructure / environmental / other
- access_type: bulk_download / api / webpage / document / unknown
- likely_data_product_value: rubric
- likely_b2b_problem_signal: Noul
- target_customer_family: Choice
- evidence_directness: Score
- likely_overlap_with_existing_source: Noul
- deep_research_warranted: Noul

Do not ask Jev:
- whether a URL is duplicated
- how old a source is
- row counts
- schema equality
- coordinate math
- exact entity resolution

## Record/opportunity-level questions

For normalized records, possible semantic judgments:
- what business problem does this signal indicate?
- how actionable is the signal?
- who is likely to pay for this information?
- is the interpretation supported directly by the fields or speculative?
- does this belong to an existing Atlas hypothesis/product?
- does it justify enrichment from another source?

## Knowledge compiler

Every incoming Atlas note/commit/document should be tagged into:
- FACT
- DECISION
- HYPOTHESIS
- SOURCE
- DATASET
- EXPERIMENT
- RESULT
- TASK
- RISK
- SUPERSEDED

A reasoning model can then compile a current project brief from only:
1. current decisions,
2. non-superseded facts,
3. active hypotheses,
4. open tasks,
5. evidence with sufficient source quality.

## Immediate Atlas pilot

Use 100-300 existing source cards/items from Atlas. Label 40 manually. Test:
- commercial relevance
- source quality
- deep-research warranted
- overlap with existing Atlas themes

Only after this calibration should Jev gate automated Atlas research.
