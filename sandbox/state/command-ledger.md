# Command Ledger

Muse-maintained record of inbound relay commands. This ledger — not the command file's
`status` field — is the source of truth for duplicate-execution protection. A command_id
listed here as `claimed` or `consumed` will never be executed again.

| command_id | status | claimed_at (UTC) | consumed_at (UTC) | notes |
|---|---|---|---|---|
| | | | | |

Statuses: `claimed` (execution started) · `consumed` (executed exactly once) · `rejected` (failed validation; never executed).
| CMD-2026-10-01-1852-001 | consumed | 2026-10-01T22:53:00Z | 2026-10-01T23:05:00Z | chat-authorized one-run relay test; created by Muse on Nagendra instruction; executed exactly once → S-2026-10-01-003 |
