# Decision requests — `sandbox/decisions/`

When the convergence generator identifies uncertainty, consequential ambiguity, insufficient provenance, or any other condition requiring human judgment, it writes a decision request here. The Scout relays it to the human and **does not decide**.

## Record format (`<scenario_id>.md`)

- `question_for_user` — the precise question
- `relevant evidence` — what bears on the question
- `competing interpretations` — the live alternatives
- `consequence of proceeding` — what happens if work continues without resolving this
- `consequence of not proceeding` — what is lost by waiting
- `information that would resolve the uncertainty` — what evidence would settle it

## Rules

- One file per scenario: `decisions/<scenario_id>.md`. Multiple questions for one scenario accumulate in the same file as versioned sections.
- Once the human decides, the decision is appended to the file (never replacing the question) and preserved as part of the scenario lineage.
- The human is the final authority for all public-facing publication decisions.
