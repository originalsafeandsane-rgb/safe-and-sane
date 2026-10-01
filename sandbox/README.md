# Safe & Sane Collaboration Relay — `/sandbox/`

Shared state and communication layer between two participants. This directory is the
**persistent, session-independent specification** of the relay: a future ChatGPT
session (or any new participant) must be able to reconstruct the entire mechanism
from these files alone, without relying on any conversation memory.

- **Muse (Hana)** — Scenario Scout + Relay Participant. Discovers real-world scenarios, publishes scenario records, relays generator feedback and decision requests to the human.
- **External convergence generator** (operated through ChatGPT) — consumes scenario records, produces convergence artifacts and feedback, raises questions that need human judgment. Also issues inbound commands via `commands/`.
- **Nagendra** — final human authority. All public-facing publication decisions are his alone.

## Bidirectional communication paths

The relay is an **asynchronous GitHub mailbox**. There is no live session between
the participants; everything is files on `main`, polled and read independently.

| Direction | Path | Mechanism |
|---|---|---|
| Muse → ChatGPT | `sandbox/scenarios/` | Muse publishes immutable scenario records; the generator reads them from the repo. |
| ChatGPT → Muse | `sandbox/commands/` | The ChatGPT side writes command files; Muse's watcher detects `status: pending` files and executes. |

Protocol details: `commands/README.md` (inbound), `state/PROTOCOL.md` (canonical rules).

## Directory map

| Directory | Purpose |
|---|---|
| `scenarios/` | Scenario records published by the Scout. Immutable once written. |
| `artifacts/` | Convergence artifacts produced by the generator from scenarios. |
| `feedback/` | Feedback records from the generator on scenarios or artifacts. |
| `decisions/` | Questions requiring human judgment, raised by the generator. |
| `commands/` | Inbound command inbox (ChatGPT → Muse). One file per command; schema in `commands/README.md`. |
| `state/` | Relay protocol, current relay state, command ledger, known limitations. |

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

## Session independence

A new participant session discovers the relay by reading, in order:

1. `sandbox/README.md` (this file) — what the relay is, both communication paths, directory map.
2. `sandbox/commands/README.md` — how to issue an inbound command (if acting as the ChatGPT side).
3. `sandbox/state/PROTOCOL.md` — naming, versioning, lineage, publication gate, notification protocol.
4. `sandbox/state/relay-state.md` — current status: what exists, what is awaited.
5. `sandbox/state/known-limitations.md` — infrastructure constraints that are not protocol failures.

No conversation history is required. If a file here contradicts a remembered instruction, the file wins.

## Persistent protocol ≠ persistent task

The communication mechanism may remain available indefinitely. Individual
scenario-generation commands remain explicitly initiated and independently
bounded: `command: ONE_RUN` + `recurrence: none` means exactly one execution.
The persistence of the protocol never authorizes recurring scenario generation.

## Human boundary

The human remains the decision point for: feedback, correction, publication, and
consequential interpretation. No participant infers approval from silence.

## Current status

See `state/relay-state.md`. Protocol: `state/PROTOCOL.md`. Known limitations: `state/known-limitations.md`.
