import json
import os
import uuid


VALID_PERTURBATIONS = {
    "none",
    "payload",
    "lineage",
    "state",
    "coherence",
}


def receive_event():
    raw = os.environ.get("RACT_EVENT")

    if raw is None:
        raise RuntimeError(
            "RACT_EVENT environment variable is missing"
        )

    return json.loads(raw)


def receive_perturbations():
    raw = os.environ.get(
        "RACT_PERTURBATIONS",
        '["none"]',
    )

    try:
        perturbations = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "RACT_PERTURBATIONS must be valid JSON"
        ) from exc

    if not isinstance(perturbations, list):
        raise RuntimeError(
            "RACT_PERTURBATIONS must be a JSON list"
        )

    if not perturbations:
        perturbations = ["none"]

    normalized = []

    for perturbation in perturbations:
        if not isinstance(perturbation, str):
            raise RuntimeError(
                "Every perturbation must be a string"
            )

        perturbation = perturbation.lower()

        if perturbation not in VALID_PERTURBATIONS:
            raise RuntimeError(
                f"Invalid perturbation: {perturbation}. "
                f"Valid values: {sorted(VALID_PERTURBATIONS)}"
            )

        if perturbation not in normalized:
            normalized.append(perturbation)

    if "none" in normalized and len(normalized) > 1:
        raise RuntimeError(
            "'none' cannot be combined with other perturbations"
        )

    return normalized


def process_event(event, iteration):
    return {
        "event_id": str(uuid.uuid4()),
        "previous_event_id": event["event_id"],
        "iteration": iteration,
        "payload": event["payload"],
        "state": f"state-{iteration}",
        "source": "sandbox",
    }


def apply_perturbation(event, perturbation):
    if perturbation == "none":
        return

    if perturbation == "payload":
        event["payload"] = "adversarial-test"

    elif perturbation == "lineage":
        event["previous_event_id"] = (
            "FAKE-PREVIOUS-EVENT"
        )

    elif perturbation == "state":
        event["state"] = "INVALID-STATE"

    elif perturbation == "coherence":
        iteration = event.get("iteration")

        if iteration is None:
            raise RuntimeError(
                "Cannot create coherence perturbation "
                "without iteration"
            )

        event["state"] = (
            f"state-{iteration + 1}"
        )

    else:
        raise RuntimeError(
            f"Unknown perturbation: {perturbation}"
        )


def perturb_event(event, perturbations):
    """
    Create an experimental copy of the canonical event.

    All perturbations are applied to the experimental copy.
    The canonical event is never modified.
    """

    experimental_event = dict(event)

    for perturbation in perturbations:
        apply_perturbation(
            experimental_event,
            perturbation,
        )

    return experimental_event


def write_json_output(name, value):
    github_output = os.environ.get("GITHUB_OUTPUT")

    if github_output:
        with open(github_output, "a") as output:
            output.write(
                f"{name}={json.dumps(value)}\n"
            )


if __name__ == "__main__":

    iteration = int(
        os.environ.get("RACT_ITERATION", "1")
    )

    perturbations = receive_perturbations()

    event = receive_event()

    print("SANDBOX_RECEIVED:")
    print(
        json.dumps(
            event,
            sort_keys=True,
        )
    )

    canonical_event = process_event(
        event,
        iteration,
    )

    print()
    print("SANDBOX_CANONICAL:")
    print(
        json.dumps(
            canonical_event,
            sort_keys=True,
        )
    )

    experimental_event = perturb_event(
        canonical_event,
        perturbations,
    )

    print()
    print("SANDBOX_EXPERIMENTAL:")
    print(
        json.dumps(
            experimental_event,
            sort_keys=True,
        )
    )

    canonical_preserved = (
        canonical_event
        != experimental_event
        or perturbations == ["none"]
    )

    print()
    print("SANDBOX_MODE:")
    print(
        json.dumps(
            {
                "canonical_preserved":
                    canonical_preserved,
                "perturbations":
                    perturbations,
            },
            sort_keys=True,
        )
    )

    # Canonical continuation of the coupled system.
    write_json_output(
        "next_event",
        canonical_event,
    )

    # Experimental shadow branch.
    write_json_output(
        "experiment_event",
        experimental_event,
    )

    # Preserve the perturbation set as structured JSON.
    write_json_output(
        "perturbations",
        perturbations,
    )
