# Safe & Sane Collaboration Relay — `/sandbox/`

Shared state and communication layer between two participants:

- **Muse (Hana)** — Scenario Scout + Relay Participant. Discovers real-world scenarios, publishes scenario records, relays generator feedback and decision requests to the human.
- **External convergence generator** (operated through ChatGPT) — consumes scenario records, produces convergence artifacts and feedback, raises questions that need human judgment.
- **Nagendra** — final human authority. All public-facing publication decisions are his alone.

## Directory map

| Directory | Purpose |
|---|---|
| `scenarios/` | Scenario records published by the Scout. Immutable once written. |
| `artifacts/` | Convergence artifacts produced by the generator from scenarios. |
| `feedback/` | Feedback records from the generator on scenarios or artifacts. |
| `decisions/` | Questions requiring human judgment, raised by the generator. |
| `state/` | Relay protocol and current relay state. |

## Lifecycle

Every relay item preserves the lineage chain:

```
source → transformation → artifact → feedback → decision
```

1. Scout publishes a scenario record in `scenarios/` (never manufactured; uncertainties written out, never resolved for cleanliness).
2. Generator reads the scenario and writes artifacts to `artifacts/` and/or feedback to `feedback/`, preserving `scenario_id` and lineage.
3. If the generator hits uncertainty, consequential ambiguity, or insufficient provenance, it writes a decision request to `decisions/<scenario_id>.md`. The Scout does not decide; it relays the question to the human.
4. The human's decision is preserved as part of the scenario lineage and informs subsequent processing.

## Hard rules

- **Never overwrite an original scenario record.** Prefer new versioned records (`<id>-v2`, `<id>-v3`) over destructive modification.
- **Never publish directly to X or any public channel.** Material may be *prepared* for publication; publication itself is outside the relay and requires the human's explicit decision.
- **Do not modify unrelated Safe & Sane material.** The relay lives entirely under `/sandbox/`.
- **Optimize for** reality → evidence → provenance → useful scenario → safe convergence → human control. Not for volume, virality, or engagement.

## Current status

See `state/relay-state.md`. Protocol: `state/PROTOCOL.md`.
