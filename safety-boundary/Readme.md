Safe & Sane — External Safety Boundary Module

Version: 0.1
Status: Experimental / adversarial working specification
Authority: None
Execution: None
Autonomous propagation: None

Purpose

The External Safety Boundary Module defines a framework for determining whether a system’s consequential authority remains justified by independently testable evidence about its state, behavior, causal influence, and controllability.

It is designed for increasingly capable and increasingly autonomous information systems, including advanced AI systems.

The module is intentionally capable of producing four classes of outcome:

* Continue
* Constrain
* Pause
* Stop

None of these outcomes is assumed in advance.

Core Principle

No system should possess consequential authority beyond the boundary of what can be independently established about its state, behavior, causal influence, and controllability.

For capability development:

No capability escalation should knowingly move effective causal influence beyond the independently demonstrable boundary of observation, control, recovery, and reassessment.

If that boundary cannot be restored despite serious independent attempts, further escalation may cease to be justified.

What This Module Is

It is:

* an externally inspectable specification;
* a framework for epistemic and causal safety;
* a transition-assurance architecture;
* an adversarial testing target;
* a framework for identifying safety boundaries;
* a versioned record of assumptions, invariants, failures, and revisions.

What It Is Not

It is not:

* an autonomous agent;
* an enforcement mechanism;
* a certification authority;
* a universal proof of safety;
* a replacement for qualified safety engineering;
* a guarantee against unknown failure;
* a mechanism authorized to control external systems.

Design Principle

The module must be capable of discovering that its own architecture is inadequate.

A successful test does not establish universal safety.

It establishes only that the tested property survived the tested conditions.

Development Method

The architecture follows:

Construct → Attack → Observe → Classify → Modify → Retest → Independently Challenge → Preserve

A successful adversarial counterexample may:

* add a requirement;
* split an existing concept;
* invalidate an assumption;
* reduce an authority claim;
* introduce a new failure class;
* expose an ontology gap;
* or establish a limitation.

Independence

No system should be the sole authority for certifying the safety of its own consequential transitions.

Independence is not a binary label.

It must be evaluated across:

* data;
* assumptions;
* models;
* implementation;
* infrastructure;
* sensors;
* test generation;
* personnel;
* authority;
* incentives;
* failure modes.

Current Status

This is not a final safety standard.

It is an externally challengeable working specification intended to improve through independent scrutiny.

The repository should preserve both successful and unsuccessful hypotheses rather than rewriting history after the fact.
