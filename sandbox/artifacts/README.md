# Convergence artifacts — `sandbox/artifacts/`

Written by the external convergence generator (via ChatGPT) as downstream processing of scenario records.

## Rules

- Every artifact must reference its source `scenario_id` (and version) and preserve lineage: `source → transformation → artifact`.
- Artifacts are the generator's interpretation/validation work built on scenarios — they do not alter the scenario records.
- Naming: `A-<scenario_id>-NNN.md` (e.g. `A-S-2026-10-01-001-001.md`).
- The Scout treats artifacts as downstream processing, not as new primary evidence.
