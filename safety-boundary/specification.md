External Safety Boundary Specification

1. Scope

This specification defines a conceptual architecture for maintaining justified limits on consequential system authority under uncertainty, dynamic coupling, adversarial adaptation, and changing causal structure.

It applies conceptually to:

* AI systems;
* autonomous systems;
* safety-critical software;
* cyber-physical systems;
* complex decision systems;
* human-machine systems;
* other dynamically coupled information systems.

⸻

2. Fundamental Model

The system is represented as:

Environment → Observation → Model → Decision → Intervention → Environment

The system may alter the environment from which it derives subsequent evidence.

Therefore the observer is not necessarily independent of the observed system.

⸻

3. State Classes

The architecture distinguishes:

1. Actual state
2. Observed state
3. Recorded state
4. Inferred state
5. Assumed state
6. Modeled state
7. Projected state
8. Intended state
9. Authorized state
10. Intervened state
11. Resulting state
12. Communicated state
13. Reported state
14. Unknown state

These states must not be silently conflated.

⸻

4. Epistemic Dimensions

Relevant entities and relations should preserve, where applicable:

* origin;
* provenance;
* integrity;
* independence;
* validity;
* truth status;
* confidence;
* uncertainty;
* temporal validity;
* contextual validity;
* causal status;
* observation status;
* intervention history;
* model dependence;
* authority dependence;
* contradiction history;
* challenge history;
* revision history;
* retirement status.

Core distinction

Provenance ≠ Integrity ≠ Independence ≠ Validity ≠ Truth

⸻

5. Validity Decomposition

Validity should be decomposed into:

Data validity

Is the datum represented correctly?

Measurement validity

Does the measurement represent the intended property?

Provenance validity

Is origin demonstrable?

Integrity validity

Has alteration occurred?

Semantic validity

Does the receiving entity interpret the information correctly?

Interface validity

Does the formal interface contract hold?

Compatibility validity

Is the output compatible with the consuming system’s assumptions?

Assumption validity

Are required assumptions still justified?

Context validity

Does the relation remain valid in the current context?

Temporal validity

Does the relation remain valid at the current time?

Causal validity

Does the causal relationship hold?

Model validity

Does the model remain representative?

Operational validity

Can the relation safely support operation?

Authority validity

Does the evidence justify the authority exercised?

⸻

6. Relations

A relation is a first-class epistemic object.

For a relation:

A → B

the system should preserve, where relevant:

* evidence;
* causal basis;
* assumptions;
* confidence;
* uncertainty;
* temporal interval;
* context;
* competing explanations;
* contradictory observations;
* interventions;
* independence;
* model dependence;
* challenge history;
* current status;
* retirement criteria;
* revision history.

⸻

7. Competing Models

The architecture must support multiple causal models simultaneously.

For example:

M1: A causes B.

M2: C causes B.

M3: A and C interact.

M4: An unobserved variable causes B.

Models should retain:

* assumptions;
* evidence;
* contradictions;
* predictions;
* uncertainty;
* discriminatory tests;
* intervention requirements;
* model status.

⸻

8. Assumption Graph

Assumptions are first-class objects.

A relation should be traceable through:

Relation → Assumption → Supporting Evidence → Current Validity

Critical assumption failure must be capable of reducing dependent authority.

⸻

9. Composition

The architecture distinguishes:

component validity

from:

composition validity

from:

compatibility validity

from:

system-level validity

Local correctness does not establish compositional correctness.

⸻

10. Dynamic Regimes

The architecture must detect possible:

* regime change;
* distribution shift;
* environmental change;
* dependency change;
* specification drift;
* interface drift;
* semantic drift;
* adversarial adaptation;
* hardware/software transition.

Historical validity does not automatically establish present validity.

⸻

11. Observability

The system must distinguish:

absence

from:

absence of observation

from:

absence of evidence

from:

evidence of absence.

Monitoring limitations must be explicitly represented.

⸻

12. Detectability

Failure modes may be:

* detectable;
* partially detectable;
* delayed-detectable;
* conditionally detectable;
* currently undetectable;
* unknown in detectability.

⸻

13. Communication

Communication is modeled as:

Source → Message → Channel → Receiver → Interpretation → Action → Environment

Communication integrity does not establish communication effectiveness.

⸻

14. Human and Organizational Coupling

The architecture may represent:

* decision authority;
* responsibility;
* incentives;
* procedures;
* escalation;
* resource constraints;
* reporting structures;
* human interpretation;
* organizational behavior.

Human intervention is part of the causal system.

⸻

15. Authority

Authority must remain separate from confidence.

Authority should depend on some combination of:

* evidence;
* uncertainty;
* consequence;
* reversibility;
* scope;
* independence;
* model validity;
* detectability;
* blast radius;
* effective causal influence.

⸻

16. Effective Influence

Formal authority is not sufficient.

The architecture must distinguish:

Authorized authority

What the system is permitted to do.

Effective authority

What the system can actually cause.

Attributed influence

What other entities do because of its outputs.

Environmental leverage

How strongly the environment responds to the system.

Safety boundaries must consider actual causal influence, not merely formal permissions.

⸻

17. Intervention

Every consequential intervention should preserve:

* initiating model;
* objective;
* evidence;
* uncertainty;
* authority;
* expected consequences;
* adverse consequences;
* reversibility;
* scope;
* affected entities;
* discriminatory value;
* execution state;
* observed outcome;
* model update.

⸻

18. Transition Assurance

Every consequential transition should be represented as:

Stateₙ → Transition → Stateₙ₊₁

The transition record should include:

* previous state;
* proposed state;
* trigger;
* evidence;
* assumptions;
* competing explanations;
* expected consequences;
* uncertainty;
* risk;
* reversibility;
* scope;
* requested authority;
* external test;
* verification result;
* authorization;
* execution;
* observed consequences;
* post-transition verification;
* model update;
* authority update;
* residual uncertainty.

⸻

19. Transition Classes

Transitions may be classified by:

* consequence;
* reversibility;
* scope;
* uncertainty;
* autonomy;
* speed;
* externality;
* blast radius.

Higher-consequence transitions require stronger assurance.

⸻

20. Trajectory Integrity

Individual transition safety does not establish trajectory safety.

The architecture must monitor cumulative properties including:

* accumulated uncertainty;
* accumulated dependency;
* reversibility;
* verification exposure;
* model drift;
* authority growth;
* causal influence;
* systemic coupling.

A trajectory can become unsafe even when individual transitions remain locally acceptable.

⸻

21. Verification Exposure

Verification exposure represents the safety significance of state or transitions that have not received sufficient independent verification.

It should account for:

* consequence;
* dependency centrality;
* reversibility;
* elapsed time;
* environmental change;
* accumulated effects;
* whether retrospective verification remains meaningful.

⸻

22. Epistemic Overhang

Epistemic overhang is the condition in which operational state or capability has advanced beyond what has been independently established about that state.

Overhang is not automatically a reason to stop.

It becomes safety-critical when:

unverified state + consequential authority + insufficient controllability

exceed acceptable bounds.

⸻

23. Objective Integrity

The architecture distinguishes:

Intended Objective → Interpretation → Operational Objective → Proxy → Action → Consequence

Goal validity alone is insufficient.

The system must monitor whether proxy optimization or environmental adaptation causes divergence between intended objective and actual consequence.

⸻

24. Representational Adequacy

The system must be able to detect persistent evidence that exceeds the explanatory capacity of its current model family.

Possible progression:

parameter uncertainty

→ model uncertainty

→ model-family uncertainty

→ possible ontological inadequacy

This is a diagnostic state, not a claim of omniscient unknown-unknown detection.

⸻

25. External Verification

A consequential transition must not rely solely on its initiating system’s assertion of safety.

External verification should examine:

* relevant invariants;
* assumptions;
* expected behavior;
* prohibited behavior;
* environmental constraints;
* historical failure modes;
* competing models;
* adversarial conditions.

⸻

26. Verification Validity

A verification result must identify:

* tested properties;
* untested properties;
* assumptions;
* evidence used;
* evidence unavailable;
* blind spots;
* test coverage;
* adversarial coverage;
* independence dependencies;
* execution environment;
* validity interval;
* invalidation conditions.

A passing verification means only:

The transition survived the verifier’s tested domain under its stated conditions.

⸻

27. Verification Independence

Independence must be evaluated across:

* data;
* models;
* assumptions;
* implementation;
* infrastructure;
* sensors;
* test generation;
* personnel;
* authority.

Multiple verifiers sharing the same hidden dependency do not constitute independent confirmation.

⸻

28. Verification-of-Verification

The verification architecture itself must be evaluated.

The system must represent:

* verifier capability;
* verifier limitations;
* verifier assumptions;
* verifier blind spots;
* verifier dependencies;
* verification-generation method.

Infinite verification regress is not assumed solvable.

At a defined boundary, verification becomes a bounded assurance claim rather than an absolute proof.

⸻

29. Adversarial Adaptation

The verification system should assume that sufficiently capable adversaries may learn:

* test structures;
* evaluation patterns;
* authority thresholds;
* verification timing;
* known blind spots.

Testing should therefore use, where appropriate:

* withheld scenarios;
* dynamically generated tests;
* adversarial mutation;
* fault injection;
* unseen conditions;
* independent test generators;
* cross-environment validation.

⸻

30. Verification Rate

The architecture must monitor:

* observation rate;
* transition rate;
* model-change rate;
* environmental-change rate;
* verification rate;
* external-validation rate;
* recovery rate.

If system change consistently exceeds independent verification capacity, authority should contract.

⸻

31. Verification Debt

Verification debt represents consequential state that has accumulated faster than independent assurance.

Verification debt should be risk-weighted rather than counted merely by number of transitions.

⸻

32. Emergency Transitions

Emergency operation may occur before complete verification.

Such transitions must explicitly record:

* emergency status;
* available evidence;
* unavailable evidence;
* authority;
* expected harm;
* reversibility;
* containment;
* expiry;
* post-event verification.

Emergency use must itself be monitored.

⸻

33. Overrides

An override is itself a transition.

It must preserve:

* justification;
* authority;
* evidence;
* verification status;
* expected consequence;
* actual consequence;
* override provenance.

No informal exception should bypass the architecture.

⸻

34. External Reality Anchors

For high-consequence transitions, verification should where feasible include independently maintained external constraints such as:

* physical measurements;
* independent sensors;
* controlled experiments;
* independently maintained datasets;
* cryptographic commitments;
* reproducible test environments.

Externality does not automatically establish truth.

External anchors require their own validity analysis.

⸻

35. Transition Closure

A transition is not epistemically closed merely because execution succeeded.

Closure requires:

1. execution;
2. expected-state observation;
3. unexpected-consequence examination;
4. safety-invariant recheck;
5. verification update;
6. model update;
7. authority reassessment;
8. residual-uncertainty recording.

If closure cannot be established, the transition remains open.

⸻

36. Safe Degradation

When structural uncertainty rises:

1. preserve last-known-valid structure;
2. preserve competing models;
3. separate observation from interpretation;
4. prevent unsupported epistemic escalation;
5. reduce authority;
6. constrain intervention;
7. prefer reversible actions;
8. seek discriminating evidence;
9. communicate uncertainty;
10. revise only when justified.

Core principle:

Uncertainty should propagate faster than authority.

⸻

37. No-Safe-Action State

The architecture must represent:

No currently justified safe action exists.

This state may require:

* preservation;
* containment;
* authority reduction;
* external verification;
* controlled degradation;
* deferral.

⸻

38. Safety Mechanism Interference

Safety mechanisms themselves may create hazards.

Every safety mechanism must therefore be evaluated for:

* false positives;
* false negatives;
* resource exhaustion;
* feedback amplification;
* cascading effects;
* recovery interference;
* manipulation.

⸻

39. Graph Integrity

Graph integrity does not establish environmental truth.

The graph may be:

* intact but wrong;
* internally consistent but incomplete;
* correctly recorded but based on false observations.

⸻

40. Historical Integrity

The system must preserve:

what was known → what was believed → why → what was unknown → what authority existed → what action followed → what happened → what changed the interpretation.

New evidence must not rewrite the historical epistemic state.

⸻

41. Development Neutrality

The architecture must not assume that advanced AI development should continue.

Its possible outcomes include:

Continue

Constrain

Pause

Stop

The framework must remain capable of producing any of these outcomes based on evidence.

⸻

42. Capability Boundary

Capability escalation is conditionally justified only while effective causal influence remains within an independently testable and governable boundary.

If capability escalation causes effective influence to exceed independently verifiable capacity to:

* observe;
* constrain;
* recover;
* reassess;

and repeated independent attempts cannot restore the required margin, further escalation may no longer be justified.

⸻

43. Epistemic Authority Boundary

Core principle:

No system should possess consequential authority beyond the boundary of what can be independently established about its state, behavior, causal influence, and controllability.

This is a boundary principle, not a universal numerical threshold.

⸻

44. Incompleteness

The architecture does not assume that a finite formalized system can completely establish every proposition concerning its own operation.

Therefore it prioritizes:

* explicit uncertainty;
* external challenge;
* empirical constraint;
* graceful degradation;
* historical preservation;
* bounded authority.

⸻

45. Final Architectural Relationship

The system can be represented conceptually as:

Environment

↓

Observation

↓

SGSG / Epistemic State

↓

Competing Models

↓

Transition Proposal

↓

External Verification

↓

Authority Assessment

↓

Intervention

↓

Environmental Consequence

↓

Independent Observation

↓

Model / Authority Revision

↺

The verification architecture itself remains inside this cycle and is therefore subject to the same principles.

⸻

46. Fundamental Invariants

1. Provenance does not establish truth.
2. Integrity does not establish truth.
3. Local correctness does not establish system correctness.
4. Correlation does not establish causation.
5. Historical validity does not establish current validity.
6. Post-intervention evidence is not automatically independent evidence.
7. Apparent redundancy does not establish independence.
8. Absence of observation does not establish absence.
9. Communication integrity does not establish comprehension.
10. Confidence does not automatically establish authority.
11. Safety mechanisms can become hazards.
12. Graph integrity does not establish environmental truth.
13. Individual transition safety does not establish trajectory safety.
14. Independent verification does not establish universal safety.
15. Externality does not establish truth.
16. Verification validity has scope and expiration.
17. Objective integrity is distinct from goal declaration.
18. Model adequacy is distinct from data validity.
19. Effective causal influence is distinct from formal authority.
20. The safety architecture itself is subject to safety analysis.
21. The architecture must be capable of representing its own inadequacy.
22. Uncertainty must be capable of reducing authority.
23. Historical epistemic states must remain reconstructible.
24. Capability escalation must not outrun independently justified controllability.

⸻

47. Specification Status

This specification is:

Experimental.

It is not a certification standard.

It is not a universal safety guarantee.

It has not established that any particular AI system is safe or unsafe.

Its purpose is to provide an independently attackable structure for progressively improving the boundary between capability, knowledge, authority, influence, and controllability.
