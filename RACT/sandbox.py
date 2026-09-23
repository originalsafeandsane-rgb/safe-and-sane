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


def process_event(event, iteration):
    return {
        "event_id": str(uuid.uuid4()),
        "previous_event_id": event["event_id"],
        "iteration": iteration,
        "payload": event["payload"],
        "state": f"state-{iteration}",
        "source": "sandbox",
    }


def perturb_event(event, perturbation):
    """
    Create an experimental copy of the canonical event.

    The canonical event is never modified.
    """

    experimental_event = dict(event)

    if perturbation == "none":
        return experimental_event

    if perturbation == "payload":
        experimental_event["payload"] = "adversarial-test"

    elif perturbation == "lineage":
        experimental_event["previous_event_id"] = (
            "FAKE-PREVIOUS-EVENT"
        )

    elif perturbation == "state":
        experimental_event["state"] = "INVALID-STATE"

    elif perturbation == "coherence":
        iteration = experimental_event.get("iteration")

        if iteration is None:
            raise RuntimeError(
                "Cannot create coherence perturbation "
                "without iteration"
            )

        experimental_event["state"] = (
            f"state-{iteration + 1}"
        )

    else:
        raise RuntimeError(
            f"Unknown perturbation: {perturbation}"
        )

    return experimental_event


def write_json_output(name, value):
    github_output = os.environ.get("GITHUB_OUTPUT")

    if github_output:
        with open(github_output, "a") as output:
            output.write(
                f"{name}={json.dumps(value)}\n"
            )


def write_string_output(name, value):
    github_output = os.environ.get("GITHUB_OUTPUT")

    if github_output:
        with open(github_output, "a") as output:
            output.write(
                f"{name}={value}\n"
            )


if __name__ == "__main__":

    iteration = int(
        os.environ.get("RACT_ITERATION", "1")
    )

    perturbation = os.environ.get(
        "RACT_PERTURBATION",
        "none",
    ).lower()

    if perturbation not in VALID_PERTURBATIONS:
        raise RuntimeError(
            f"Invalid perturbation: {perturbation}. "
            f"Valid values: {sorted(VALID_PERTURBATIONS)}"
        )

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
        perturbation,
    )

    print()
    print("SANDBOX_EXPERIMENTAL:")
    print(
        json.dumps(
            experimental_event,
            sort_keys=True,
        )
    )

    canonical_unchanged = (
        canonical_event
        == (
            experimental_event
            if perturbation == "none"
            else canonical_event
        )
    )

    print()
    print("SANDBOX_MODE:")
    print(
        json.dumps(
            {
                "canonical_preserved":
                    canonical_unchanged,
                "perturbation":
                    perturbation,
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

    # Plain string; do not JSON-encode it.
    write_string_output(
        "perturbation",
        perturbation,
    )
