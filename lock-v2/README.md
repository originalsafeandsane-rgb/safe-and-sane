# LOCK v2 (draft)

An advisory, owner-adopted safety instruction layer for consumer AI
environments. Derived from a review of Safe & Sane Personal AI Safety Module
v0.1.2.

**Status: draft, untested.** Not an official release unless the maintainer
says so in a signed release or tag.

## Contents

| File | Purpose |
| --- | --- |
| `lock-v2-standalone-install-pack.md` | Paste-ready block, install steps, verify prompts, limits |
| `CHANGES-FROM-0.1.2.md` | What changed from v0.1.2 and why |

## Quick start

1. Open `lock-v2-standalone-install-pack.md`.
2. Paste the compact block into your AI's custom or project instructions.
3. Run the verify prompts in a new chat.

## Integrity

The SHA-256 of the install pack is deliberately **not stored in this
repository**. A hash that lives next to the file it protects proves nothing,
because whoever can change the file can change the hash. Get the hash from
the maintainer through a separate channel (signed release notes, a pinned
issue, or out of band) and compare.

## Limits

Text rules can be ignored by a weak or compromised AI, and this layer cannot
see or control anything the host app does not expose. It is advisory, not a
lock.
