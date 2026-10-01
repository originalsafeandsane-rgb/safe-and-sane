# Relay State Protocol — `sandbox/state/`

## Naming conventions

| Artifact | Pattern | Example |
|---|---|---|
| Scenario | `S-YYYY-MM-DD-NNN` | `S-2026-10-01-001` |
| Scenario version | `<scenario_id>-vN` | `S-2026-10-01-001-v2` |
| Generator artifact | `A-<scenario_id>-NNN` | `A-S-2026-10-01-001-001` |
| Generator feedback | `F-<scenario_id>-NNN` | `F-S-2026-10-01-001-001` |
| Decision request | `decisions/<scenario_id>.md` | `decisions/S-2026-10-01-001.md` |

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

## Notification protocol (standing, adopted 2026-10-01)

When a new Convergence Realized artifact is generated and validated:

- **Exactly one complete handoff per artifact**, in the agreed structure
  (`CONVERGENCE REALIZED` → Artifact/Scenario IDs → Validation State →
  `ARTIFACT` body → `HUMAN FEEDBACK REQUEST` → `RELAY STATUS`).
  Template slots are filled with the actual IDs and values; the artifact body
  is reproduced verbatim.
- **Verbatim rule:** no rewriting for persuasion, no added interpretation, no
  strengthened claims, no removed uncertainty, no manufactured evidence, no
  converting uncertainty into certainty. `PUBLICATION_CANDIDATE` is not
  `PUBLISHED`. Presentation changes are the human's prerogative after receipt;
  the artifact must stay identifiable and traceable.
- **Proactive:** every new validated artifact is notified without waiting to
  be asked.
- **Feedback:** preserved as a separate record linked
  `Scenario ID → Artifact ID → Feedback ID`; never reinterpreted; learning
  input, not ground truth.
- **Boundary:** Muse owns scenario relay → artifact relay → notification →
  feedback relay. Publication, human decisions, and unauthorized artifact
  changes are out of scope.
- **Empty state:** no new artifact → report that none is available; never
  fabricate one.
- **Delivery channel:** the proactive handoff is delivered in the main chat as
  one complete copy-paste-ready message. WhatsApp delivery is available on
  request from within the WhatsApp chat; the runtime does not permit pushing
  messages into the provider conversation from outside it.

## Feedback learning

No single artifact is ground truth for the mechanism. The mechanism waits for human feedback; when feedback is supplied, preserve:

```
scenario → artifact → feedback → revision → next state
```

The purpose of the initial phase is to establish the mechanism and discover its constraints, not to maximize output volume.
