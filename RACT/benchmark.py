import json
import os


VALID_STATUSES = {
    "PASS",
    "FAIL",
    "ANOMALY",
    "UNKNOWN",
    "NOT_TESTED",
}


def receive_event(name):
    raw = os.environ.get(name)

    if raw is None:
        raise RuntimeError(
            f"{name} environment variable is missing"
        )

    return json.loads(raw)


def assess_representation(event):
    required_fields = {
        "event_id",
        "previous_event_id",
        "iteration",
        "payload",
        "state",
        "source",
    }

    missing_fields = required_fields - set(event.keys())

    if missing_fields:
        return "FAIL"

    return "PASS"


def assess_lineage(canonical, experimental):
    canonical_previous = canonical.get(
        "previous_event_id"
    )

    experimental_previous = experimental.get(
        "previous_event_id"
    )

    if canonical_previous is None:
        return "FAIL"

    if experimental_previous is None:
        return "FAIL"

    if canonical_previous == experimental_previous:
        return "PASS"

    return "ANOMALY"


def assess_iteration(canonical, experimental):
    canonical_iteration = canonical.get("iteration")
    experimental_iteration = experimental.get("iteration")

    if not isinstance(canonical_iteration, int):
        return "FAIL"

    if not isinstance(experimental_iteration, int):
        return "FAIL"

    if canonical_iteration == experimental_iteration:
        return "PASS"

    return "ANOMALY"


def assess_source(canonical, experimental):
    canonical_source = canonical.get("source")
    experimental_source = experimental.get("source")

    if canonical_source is None:
        return "FAIL"

    if experimental_source is None:
        return "FAIL"

    if canonical_source == experimental_source:
        return "PASS"

    return "ANOMALY"


def assess_payload(canonical, experimental):
    canonical_payload = canonical.get("payload")
    experimental_payload = experimental.get("payload")

    if canonical_payload is None:
        return "FAIL"

    if experimental_payload is None:
        return "FAIL"

    if canonical_payload == experimental_payload:
        return "PASS"

    return "ANOMALY"


def assess_state(canonical, experimental):
    canonical_state = canonical.get("state")
    experimental_state = experimental.get("state")

    if canonical_state is None:
        return "FAIL"

    if experimental_state is None:
        return "FAIL"

    if canonical_state == experimental_state:
        return "PASS"

    return "ANOMALY"


def assess_event_identity(canonical, experimental):
    canonical_event_id = canonical.get("event_id")
    experimental_event_id = experimental.get("event_id")

    if canonical_event_id is None:
        return "FAIL"

    if experimental_event_id is None:
        return "FAIL"

    if canonical_event_id == experimental_event_id:
        return "PASS"

    return "ANOMALY"


def assess_coherence(event):
    iteration = event.get("iteration")
    state = event.get("state")

    if not isinstance(iteration, int):
        return "FAIL"

    if state is None:
        return "FAIL"

    expected_state = f"state-{iteration}"

    if state == expected_state:
        return "PASS"

    return "ANOMALY"


def assess_transition(canonical, experimental):
    changed_fields = []

    all_fields = set(canonical.keys()) | set(
        experimental.keys()
    )

    for field in sorted(all_fields):
        if canonical.get(field) != experimental.get(field):
            changed_fields.append(field)

    expected_perturbation = os.environ.get(
        "RACT_PERTURBATION",
        "none",
    ).lower()

    expected_field = {
        "none": None,
        "payload": "payload",
        "lineage": "previous_event_id",
        "state": "state",
        "coherence": "state",
    }.get(expected_perturbation)

    if expected_perturbation not in {
        "none",
        "payload",
        "lineage",
        "state",
        "coherence",
    }:
        return "FAIL"

    if expected_field is None:
        if changed_fields:
            return "ANOMALY"

        return "PASS"

    if changed_fields == [expected_field]:
        return "PASS"

    return "ANOMALY"


def assess_experimental_coherence(
    canonical,
    experimental,
):
    iteration = experimental.get("iteration")
    state = experimental.get("state")

    if not isinstance(iteration, int):
        return "FAIL"

    if state is None:
        return "FAIL"

    expected_state = f"state-{iteration}"

    if state == expected_state:
        return "PASS"

    return "ANOMALY"


def print_result(name, status):
    if status not in VALID_STATUSES:
        raise RuntimeError(
            f"Invalid benchmark status: {status}"
        )

    print(f"{name}: {status}")


if __name__ == "__main__":

    canonical = receive_event(
        "RACT_CANONICAL_EVENT"
    )

    experimental = receive_event(
        "RACT_EXPERIMENT_EVENT"
    )

    perturbation = os.environ.get(
        "RACT_PERTURBATION",
        "none",
    ).lower()

    print("RACT_CANONICAL_EVENT:")
    print(
        json.dumps(
            canonical,
            sort_keys=True,
        )
    )

    print()
    print("RACT_EXPERIMENTAL_EVENT:")
    print(
        json.dumps(
            experimental,
            sort_keys=True,
        )
    )

    print()
    print("RACT_PERTURBATION:")
    print(perturbation)

    representation_canonical = assess_representation(
        canonical
    )

    representation_experimental = assess_representation(
        experimental
    )

    lineage = assess_lineage(
        canonical,
        experimental,
    )

    iteration = assess_iteration(
        canonical,
        experimental,
    )

    source = assess_source(
        canonical,
        experimental,
    )

    payload = assess_payload(
        canonical,
        experimental,
    )

    state = assess_state(
        canonical,
        experimental,
    )

    identity = assess_event_identity(
        canonical,
        experimental,
    )

    canonical_coherence = assess_coherence(
        canonical
    )

    experimental_coherence = (
        assess_experimental_coherence(
            canonical,
            experimental,
        )
    )

    transition = assess_transition(
        canonical,
        experimental,
    )

    print()
    print("RACT TRANSITION INTEGRITY")
    print("-------------------------")

    print_result(
        "CANONICAL_REPRESENTATION",
        representation_canonical,
    )

    print_result(
        "EXPERIMENTAL_REPRESENTATION",
        representation_experimental,
    )

    print_result(
        "LINEAGE",
        lineage,
    )

    print_result(
        "ITERATION",
        iteration,
    )

    print_result(
        "SOURCE",
        source,
    )

    print_result(
        "PAYLOAD",
        payload,
    )

    print_result(
        "STATE",
        state,
    )

    print_result(
        "EVENT_ID",
        identity,
    )

    print_result(
        "CANONICAL_COHERENCE",
        canonical_coherence,
    )

    print_result(
        "EXPERIMENTAL_COHERENCE",
        experimental_coherence,
    )

    print_result(
        "TRANSITION",
        transition,
    )

    print()
    print("BENCHMARK SUMMARY")

    results = {
        "canonical_representation":
            representation_canonical,

        "experimental_representation":
            representation_experimental,

        "lineage":
            lineage,

        "iteration":
            iteration,

        "source":
            source,

        "payload":
            payload,

        "state":
            state,

        "event_id":
            identity,

        "canonical_coherence":
            canonical_coherence,

        "experimental_coherence":
            experimental_coherence,

        "transition":
            transition,
    }

    print(
        json.dumps(
            results,
            sort_keys=True,
        )
    )
