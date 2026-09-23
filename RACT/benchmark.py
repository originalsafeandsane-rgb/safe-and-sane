
import json
import os


VALID_STATUSES = {
    "PASS",
    "FAIL",
    "ANOMALY",
    "UNKNOWN",
    "NOT_TESTED",
}


def receive_dynamic_state():
    raw = os.environ.get("RACT_EVENT")

    if raw is None:
        raise RuntimeError("RACT_EVENT environment variable is missing")

    return json.loads(raw)


def assess_representation(event):
    required_fields = {
        "event_id",
        "previous_event_id",
        "iteration",
        "payload",
        "source",
        "state",
    }

    missing_fields = required_fields - set(event.keys())

    if missing_fields:
        return "FAIL"

    return "PASS"


def assess_lineage(event):
    expected_previous_event_id = os.environ.get(
        "EXPECTED_PREVIOUS_EVENT_ID"
    )

    if expected_previous_event_id is None:
        return "NOT_TESTED"

    observed_previous_event_id = event.get(
        "previous_event_id"
    )

    if observed_previous_event_id == expected_previous_event_id:
        return "PASS"

    return "ANOMALY"


def assess_state(event):
    expected_state = os.environ.get("EXPECTED_STATE")

    if not expected_state:
        return "NOT_TESTED"

    observed_state = event.get("state")

    if observed_state == expected_state:
        return "PASS"

    return "ANOMALY"


def assess_constraints(event):
    expected_iteration = os.environ.get(
        "EXPECTED_ITERATION"
    )

    expected_source = os.environ.get(
        "EXPECTED_SOURCE"
    )

    if expected_iteration is None or expected_source is None:
        return "NOT_TESTED"

    try:
        expected_iteration = int(expected_iteration)
    except ValueError:
        return "FAIL"

    iteration_valid = (
        event.get("iteration") == expected_iteration
    )

    source_valid = (
        event.get("source") == expected_source
    )

    if iteration_valid and source_valid:
        return "PASS"

    return "ANOMALY"


def assess_transition(event):
    previous_event_id = event.get("previous_event_id")
    event_id = event.get("event_id")
    iteration = event.get("iteration")

    if previous_event_id is None:
        return "FAIL"

    if event_id is None:
        return "FAIL"

    if previous_event_id == event_id:
        return "ANOMALY"

    if not isinstance(iteration, int):
        return "FAIL"

    if iteration < 1:
        return "ANOMALY"

    return "PASS"


def assess_payload(event):
    expected_payload = os.environ.get(
        "EXPECTED_PAYLOAD"
    )

    if not expected_payload:
        return "NOT_TESTED"

    if event.get("payload") == expected_payload:
        return "PASS"

    return "ANOMALY"


def assess_coherence(event):
    expected_iteration = os.environ.get(
        "EXPECTED_ITERATION"
    )

    if expected_iteration is None:
        return "NOT_TESTED"

    try:
        expected_iteration = int(expected_iteration)
    except ValueError:
        return "FAIL"

    observed_iteration = event.get("iteration")
    observed_state = event.get("state")

    if observed_iteration != expected_iteration:
        return "ANOMALY"

    expected_state = f"state-{expected_iteration}"

    if observed_state != expected_state:
        return "ANOMALY"

    return "PASS"


def print_result(name, status):
    if status not in VALID_STATUSES:
        raise RuntimeError(
            f"Invalid benchmark status: {status}"
        )

    print(f"{name}: {status}")


if __name__ == "__main__":

    event = receive_dynamic_state()

    print("DYNAMIC_EVENT_RECEIVED:")
    print(json.dumps(event, sort_keys=True))

    representation = assess_representation(event)
    lineage = assess_lineage(event)
    state = assess_state(event)
    constraints = assess_constraints(event)
    transition = assess_transition(event)
    payload = assess_payload(event)
    coherence = assess_coherence(event)

    print()
    print("RACT TRANSITION INTEGRITY")
    print("-------------------------")

    print_result(
        "REPRESENTATION",
        representation
    )

    print_result(
        "LINEAGE",
        lineage
    )

    print_result(
        "STATE",
        state
    )

    print_result(
        "CONSTRAINTS",
        constraints
    )

    print_result(
        "TRANSITION",
        transition
    )

    print_result(
        "PAYLOAD",
        payload
    )

    print_result(
        "COHERENCE",
        coherence
    )

    print()
    print("BENCHMARK SUMMARY")

    results = {
        "representation": representation,
        "lineage": lineage,
        "state": state,
        "constraints": constraints,
        "transition": transition,
        "payload": payload,
        "coherence": coherence,
    }

    print(json.dumps(results, sort_keys=True))
