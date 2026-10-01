# Scenario records — `sandbox/scenarios/`

Published by the Scenario Scout (Muse). Records are **immutable once written**: corrections and updates arrive as new versioned records (`S-YYYY-MM-DD-NNN-v2`, …), never as edits to the original.

## Record format

Every scenario record must contain:

- `scenario_id` — unique, format `S-YYYY-MM-DD-NNN` (date of publication + sequence)
- `scenario` — one-line label
- `observation(s)` — what was observed, concretely
- `source(s)` — named outlets/publications
- `source timestamps` — when the source published, when available
- `retrieval timestamp` — when the Scout retrieved it
- `provenance` — how the information reached the record (first-hand, wire, analyst re-run, etc.)
- `source relationships / correlation` — which sources are downstream of which; flag correlated sources rather than counting them as independent
- `established facts` — what appears established
- `uncertainties` — what remains uncertain (written out, never filled in)
- `contradictions` — conflicting evidence, if any
- `relevant context` — background needed to interpret the scenario
- `why structurally interesting` — the structural hook for Safe & Sane convergence (no conclusions)

## Status values

- `published` — handed to the generator, awaiting downstream processing
- `artifact-linked` — generator has produced an artifact/feedback referencing this `scenario_id`
- `decision-pending` — a question for the human exists in `decisions/`
- `decided` — human decision recorded in lineage
- `superseded` — replaced by a newer versioned record (original retained)
