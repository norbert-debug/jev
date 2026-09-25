"""
First JEV live smoke test.

Prerequisites:
  pip install -r requirements.txt
  set TYPESAFE_API_KEY in the environment

This intentionally uses synthetic project artifacts only.
"""

import json
import os
import time

from typesafe_sdk import Choice, Noul, Score, TypeSafeClient


SYNTHETIC_ITEMS = [
    {"title": "New government registry export", "short_text": "Bulk CSV updated weekly with company identifiers and activity codes.", "source_type": "dataset"},
    {"title": "Old architecture note", "short_text": "We will store all production data in a local SQLite database. This was the initial idea before the cloud design.", "source_type": "note"},
    {"title": "Customer interview insight", "short_text": "Three logistics companies said identifying planned infrastructure work earlier would help them target sales.", "source_type": "research"},
    {"title": "Open task", "short_text": "Verify whether the API exposes historical snapshots and document rate limits.", "source_type": "task"},
    {"title": "Decision", "short_text": "GitHub remains the technical source of truth; Drive is for human-facing reports.", "source_type": "decision"},
    {"title": "Hypothesis", "short_text": "Planned fibre deployments may be a useful signal for B2B lead generation.", "source_type": "hypothesis"},
    {"title": "Result", "short_text": "The first parser processed 10,000 records without schema errors.", "source_type": "result"},
    {"title": "Risk", "short_text": "The current source can change field names without versioning.", "source_type": "risk"},
    {"title": "Source link", "short_text": "Official public portal containing downloadable geospatial datasets.", "source_type": "source"},
    {"title": "Duplicate-like note", "short_text": "GitHub should be our technical source of truth and Drive should only contain reports.", "source_type": "note"},
    {"title": "Pricing idea", "short_text": "Possible subscription model for a monthly B2B opportunity feed; no customer validation yet.", "source_type": "hypothesis"},
    {"title": "Enrichment idea", "short_text": "Add municipality demographics to already geocoded addresses.", "source_type": "idea"},
    {"title": "Completed research", "short_text": "The source provides API access, bulk downloads and a public data dictionary.", "source_type": "result"},
    {"title": "Question", "short_text": "Do we have legal permission to combine this first-party audience data with the external source?", "source_type": "risk"},
    {"title": "Deprecated plan", "short_text": "Deploy the prototype on the server selected in the March plan, although the project later moved to Cloudflare.", "source_type": "note"},
    {"title": "Commercial signal", "short_text": "A public tender announces 180 planned retail refurbishments across several regions.", "source_type": "source"},
    {"title": "Low-value source", "short_text": "Generic opinion article with no primary data or references.", "source_type": "article"},
    {"title": "Structured evidence", "short_text": "Official register lists permit status, coordinates, applicant and issue date.", "source_type": "registry"},
    {"title": "Next experiment", "short_text": "Compare Jev prefilter plus LLM against full-corpus LLM analysis on 200 items.", "source_type": "task"},
    {"title": "Potential conflict", "short_text": "This document says the MVP should use PostgreSQL, while the current architecture says DuckDB/Parquet first.", "source_type": "note"},
]


QUESTIONS = {
    "artifact_type": Choice(
        instructions="What role does this artifact primarily play in the project?",
        criteria={
            "fact": "A claim presented as established information.",
            "decision": "A choice that has been made and should guide future work.",
            "hypothesis": "A proposition that still needs evidence or testing.",
            "source": "A pointer to external evidence or a data source.",
            "task": "Work that still needs to be performed.",
            "result": "An observed outcome of completed work.",
            "risk": "A problem, uncertainty, conflict, or downside that may affect the project.",
            "other": "None of the listed categories clearly applies.",
        },
    ),
    "deep_reasoning_warranted": Noul(
        instructions="This item contains enough relevant novelty, ambiguity, conflict, or potential value that a deeper reasoning-model analysis is warranted."
    ),
    "commercial_value": Score(
        instructions="How much plausible commercial value or decision value does this item contain for a data-product project?",
        criteria=[
            "Little or no decision/commercial value.",
            "Some possible value but weak or indirect.",
            "Clear value that should influence research or product work.",
            "High value and likely worth prioritising for deeper analysis.",
        ],
    ),
}


def main():
    if not os.getenv("TYPESAFE_API_KEY"):
        raise SystemExit(
            "TYPESAFE_API_KEY is not set. Set it in this PowerShell session and run again."
        )

    client = TypeSafeClient()
    rows = []

    for i, item in enumerate(SYNTHETIC_ITEMS, start=1):
        started = time.perf_counter()
        response = client.system_one(state=item, questions=QUESTIONS)
        elapsed_ms = round((time.perf_counter() - started) * 1000, 1)

        answer = {
            "index": i,
            "title": item["title"],
            "model": getattr(response, "model", None),
            "latency_ms": elapsed_ms,
            "artifact_type": response.answers["artifact_type"].choice,
            "artifact_type_confidence": response.answers["artifact_type"].confidence,
            "deep_reasoning_warranted": response.answers["deep_reasoning_warranted"].noul,
            "commercial_value_score": response.answers["commercial_value"].score,
            "commercial_value_confidence": response.answers["commercial_value"].confidence,
        }
        rows.append(answer)
        print(json.dumps(answer, ensure_ascii=False))

    print("\n--- SUMMARY ---")
    print(f"Processed: {len(rows)}")
    print(
        "Deep-reasoning candidates:",
        sum(1 for r in rows if r["deep_reasoning_warranted"] >= 0.7),
    )
    print(
        "Low-confidence artifact classifications:",
        sum(1 for r in rows if r["artifact_type_confidence"] < 0.6),
    )


if __name__ == "__main__":
    main()
