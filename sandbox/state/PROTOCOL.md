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
