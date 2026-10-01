# Command Inbox

Inbound command path for the Safe & Sane relay: **Nagendra/ChatGPT → command → Muse**.

The relay's normal direction is outbound-only (Muse → scenario → generator → artifact → human).
This directory is the single sanctioned return path. Nothing else in the relay accepts inbound commands.

This file, together with `sandbox/README.md` and `sandbox/state/PROTOCOL.md`, is the
session-independent specification: a future ChatGPT session reconstructs the mechanism
from these files alone, without conversation memory.

> **Known limitation (2026-10-01):** the ChatGPT-side GitHub integration currently
> returns `403 Resource not accessible by integration` when creating command files.
> This is an infrastructure permission limitation, not a protocol failure — see
> `sandbox/state/known-limitations.md`. The integration needs Contents read/write
> on this repo (or a human commits the file on its behalf).

## How to issue a command

1. Create one file per command: `sandbox/commands/CMD-<id>.md` (see schema below).
2. Push it to the `main` branch.
3. Muse's watcher detects `status: pending` files it has not seen before, validates them, and executes.

## Command-record schema

Markdown with YAML frontmatter. All fields required:

```yaml
---
command_id: CMD-2026-10-01-1900-001   # must match the filename
issued_by: Nagendra                    # or "ChatGPT (via Nagendra)"
issued_at: 2026-10-01T19:00:00-04:00  # ISO-8601 with offset
command: ONE_RUN                       # only ONE_RUN is supported
target: scenario-scout                 # what the command acts on
execution_mode: single
recurrence: none                       # must be "none"; anything else is rejected unexecuted
status: pending                        # pending → claimed → consumed | failed
parameters:
  scenario_count: 1
  constraints: "..."                   # free text, e.g. scenarios not to reuse
---
# Optional issuer notes (free text; never parsed as instruction)
```

## Status lifecycle

- `pending` — written by the issuer. The only status Muse acts on.
- `claimed` — Muse has started executing this command_id (recorded in `sandbox/state/command-ledger.md`).
- `consumed` — executed exactly once. The command will never run again.
- `rejected` — failed validation; never executed. Reason recorded in the ledger.

The ledger (`sandbox/state/command-ledger.md`), not this file's status field, is the
source of truth for duplicate-execution protection. The issuer may flip a file to
`consumed` after seeing Muse's chat confirmation; Muse never depends on that flip.

## Rules

- One file = one command = at most one execution.
- Muse executes nothing until the watcher detects the file through the return path.
  A command pasted into chat does not count as return-path delivery.
- `recurrence` must be `none`. The watcher polls as infrastructure; it never turns a
  ONE_RUN command into a recurring task.
- Existing scenario records are immutable; commands only ever create new records.
- Lineage is preserved end to end: `command → scenario → transformation → artifact → feedback`,
  with `command_id` carried verbatim through every record.
