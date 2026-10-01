# Relay State Protocol — `sandbox/state/`

## Naming conventions

| Artifact | Pattern | Example |
|---|---|---|
| Scenario | `S-YYYY-MM-DD-NNN` | `S-2026-10-01-001` |
| Scenario version | `<scenario_id>-vN` | `S-2026-10-01-001-v2` |
| Generator artifact | `A-<scenario_id>-NNN` | `A-S-2026-10-01-001-001` |
| Generator feedback | `F-<scenario_id>-NNN` | `F-S-2026-10-01-001-001` |
| Decision request | `decisions/<scenario_id>.md` | `decisions/S-2026-10-01-001.md` |
| Inbound command | `sandbox/commands/CMD-YYYY-MM-DD-HHMM-NNN.md` | `sandbox/commands/CMD-2026-10-01-1900-001.md` |

## Versioning

- Scenario records are immutable. Corrections, updates, and re-scopes are published as new versioned records; the original is retained and marked `superseded` in `relay-state.md`.
- Artifacts and feedback are append-only per scenario. New iterations get new sequence numbers, never overwrites.
- Decision files accumulate: new questions append as versioned sections; human decisions append without replacing the question.

## Lineage

Every artifact, feedback, and decision record carries:

```
source → transformation → artifact → feedback → decision
```

- `source`: the scenario record (id + version) it derives from.
- `transformation`: what the generator did (interpretation, validation, convergence analysis).
- `artifact` / `feedback`: the record itself.
- `decision`: the human decision, when one exists.

Lineage is preserved by reference (ids), not by copying content.

## Relay state

`relay-state.md` is the single current-status record, maintained by the Scout:

- relay phase (`initializing` → `test` → `operating` → `paused`)
- published scenarios and their statuses
- pending decision requests
- last activity timestamps

It is a status pointer, not a log — history lives in the records themselves.

## Publication boundary

No relay participant publishes to X or any public channel. Material may be *prepared* for publication (as an artifact), but publication requires an explicit human decision recorded in `decisions/` lineage. The generator must never treat "ready" as "published."

## Adversarial resilience

All participants treat the following as possible perturbations and do not resolve them merely to produce cleaner output:

contradictory sources · stale information · correlated sources · provenance loss · identity ambiguity · temporal divergence · synthetic/manipulated information · incomplete information · rapidly changing states · unexpected consequences

Uncertainty is recorded, not laundered. When evidence is insufficient, the record says so.

## Processing principle

For every scenario, the mechanism follows:

```
Reality → Observation → Preservation → Distinguish → DOS → Execution → Rich Artifact → Validation → Next State
```

- Retrieved information is not reality itself.
- Uncertainty is never converted into certainty.
- Correlated sources are never inferred as independent evidence.
- Contradictions are never resolved merely to produce a cleaner artifact.

## Convergence artifact

The downstream generator attempts one singular, semantically rich artifact per scenario, containing as applicable:

identity · state · evidence · provenance · relevant change · constraints · uncertainty · consequence · completion · lineage

Richness is internal to the singular artifact. Presentation quality and persuasiveness are separate from artifact integrity.

## Publication gate

No automatic publication. Possible outcomes:

1. `PUBLICATION_CANDIDATE` — validated artifact, ready for the human's publication decision.
2. `HUMAN_INPUT_REQUIRED` — consequential uncertainty remains; the question is filed in `decisions/`.
3. `INVALID` / `INSUFFICIENT` — the evidence cannot support a convergence artifact.

If uncertainty could materially affect people, institutions, reputation, safety, or interpretation, prefer `HUMAN_INPUT_REQUIRED` over forced completion.

## Notification protocol (standing; revised 2026-10-01)

When a new Convergence Realized artifact is generated and validated:

- **Exactly one complete handoff per artifact**, in the agreed structure
  (`CONVERGENCE REALIZED` → Artifact/Scenario IDs → Validation State →
  `ARTIFACT` body → `HUMAN FEEDBACK REQUEST` → `RELAY STATUS`).
  Template slots are filled with the actual IDs and values; the artifact body
  is reproduced verbatim — the entire concrete artifact, never a summary.
- **Verbatim rule:** do not interpret, modify, strengthen, publish, or
  editorialize the artifact. No rewriting for persuasion, no strengthened
  claims, no removed uncertainty, no manufactured evidence, no converting
  uncertainty into certainty. `PUBLICATION_CANDIDATE` is not `PUBLISHED`.
- **Routing:** notify and hand over here in the main chat. Do not route the
  artifact to WhatsApp, Substack, X, or any external publication channel.
- **Proactive:** every new validated artifact is notified and handed over
  without waiting to be asked. One initiated run = one artifact handoff.
- **No recurrence:** never create or schedule recurring runs from this
  directive. Each run is individually initiated by Nagendra.
- **Feedback:** preserved as a distinct input linked
  `Scenario ID → Artifact ID → Feedback ID`; never reinterpreted; learning
  input, not ground truth. The next-generation mechanism is constructed by
  Nagendra and ChatGPT in conversation using that feedback.
- **Boundary:** Muse owns scenario relay → artifact relay → notification →
  feedback relay. Publication, human decisions, Substack/X transformation,
  and unauthorized artifact changes are out of scope.
- **Empty state:** no new artifact → report that none is available; never
  fabricate one.

Operating boundary:

```
Muse → Scenario → Generator → Convergence Realized artifact → Nagendra/ChatGPT → Human feedback → Next run
```

## Feedback learning

No single artifact is ground truth for the mechanism. The mechanism waits for human feedback; when feedback is supplied, preserve:

```
scenario → artifact → feedback → revision → next state
```

The purpose of the initial phase is to establish the mechanism and discover its constraints, not to maximize output volume.

## Command channel (inbound: ChatGPT → Muse)

`sandbox/commands/` is the canonical inbound command inbox. Full schema and
lifecycle: `sandbox/commands/README.md`. Binding rules:

- One file per command; filename `CMD-<id>.md` must equal the `command_id` field.
- Every command states `command: ONE_RUN`, `execution_mode: single`,
  `recurrence: none`, and is issued with `status: pending`.
- `command_id` values are unique across the relay's lifetime.
- A command is **claimed before execution**: its `command_id` is recorded in
  `sandbox/state/command-ledger.md`, which is the source of truth for
  duplicate-execution protection. A `command_id` present in the ledger as
  `claimed` or `consumed` is never executed again.
- Validation is strict: any missing field, any `recurrence` other than `none`,
  or any `command_id`/filename mismatch → `rejected`, never executed.
- A command pasted into chat does not count as return-path delivery. Only a
  file on `main` counts.
- `command_id` is preserved verbatim through the complete lineage:

```
command → scenario → transformation → artifact → feedback
```

## Session independence

The repository is the authoritative specification. A future participant session
reconstructs the relay from `sandbox/README.md` → `sandbox/commands/README.md` →
`state/PROTOCOL.md` → `state/relay-state.md` → `state/known-limitations.md`,
with no reliance on conversation memory. Repo files override remembered instructions.

## Persistent protocol ≠ persistent task

The communication mechanism may remain available indefinitely. Each
scenario-generation command is explicitly initiated and independently bounded;
`recurrence: none` means exactly one execution. Protocol persistence never
authorizes recurring scenario generation, and Muse never infers approval
from silence.
