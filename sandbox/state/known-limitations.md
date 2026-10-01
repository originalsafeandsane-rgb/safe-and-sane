# Known Infrastructure Limitations

Constraints of the surrounding infrastructure. These are **not protocol failures**:
the relay mechanism is sound; the capability below it is missing or misconfigured.

## 2026-10-01 — ChatGPT-side GitHub write access (command inbox)

- **Symptom:** the ChatGPT side's GitHub integration returned
  `403 Resource not accessible by integration` when attempting to create a
  command file under `sandbox/commands/`.
- **Classification:** infrastructure permission limitation, not a protocol failure.
  No workaround is applied; a command is not treated as created unless its file
  exists on `main`.
- **Required permission:** the ChatGPT-side integration needs write access
  (Contents: read and write) to the `safe-and-sane` repository, `main` branch,
  scoped at minimum to `sandbox/commands/` — or a human commits the command
  file on its behalf.
- **Status:** open. The inbound path is fully specified (`sandbox/commands/README.md`)
  and Muse's detection side is implemented and live; it activates on the first
  successfully pushed command file.

## 2026-10-01 — No push channel from GitHub to Muse (detection requires polling)

- **Symptom:** GitHub cannot notify Muse of new files; Muse has no inbound
  webhook endpoint.
- **Classification:** architectural constraint, not a protocol failure.
- **Standing answer:** detection uses polling (a lightweight hook script, ~60s
  interval). The poll is infrastructure, not task recurrence: it takes no action
  unless a valid pending command exists. Recorded here so future sessions do not
  re-litigate it.
- **Status:** accepted; mechanism in place.
