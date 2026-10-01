# Command Ledger

Muse-maintained record of inbound relay commands. This ledger — not the command file's
`status` field — is the source of truth for duplicate-execution protection. A command_id
listed here as `claimed` or `consumed` will never be executed again.

| command_id | status | claimed_at (UTC) | consumed_at (UTC) | notes |
|---|---|---|---|---|
| | | | | |

Statuses: `claimed` (execution started) · `consumed` (executed exactly once) · `rejected` (failed validation; never executed).
