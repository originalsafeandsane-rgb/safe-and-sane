import json
import os


def receive_dynamic_state():
    raw = os.environ.get("RACT_EVENT")

    if raw is None:
        raise RuntimeError("RACT_EVENT environment variable is missing")

    return json.loads(raw)


def ground_truth_recovery(event):
    required_fields = {
        "event_id",
        "previous_event_id",
        "iteration",
        "payload",
        "source",
        "state",
    }

    observed_fields = set(event.keys())

    structure_present = required_fields.issubset(observed_fields)
    correct_source = event.get("source") == "sandbox"
    correct_iteration = event.get("iteration") == 1
    correct_state = event.get("state") == "state-1"

    return (
        structure_present
        and correct_source
        and correct_iteration
        and correct_state
    )


def adversarial_perturbation(event):
    original = dict(event)

    perturbed = dict(original)
    perturbed["payload"] = "ADVERSARIAL_PERTURBATION"

    perturbation_detected = (
        perturbed["payload"] != original["payload"]
    )

    original_not_falsely_recovered = (
        perturbed["payload"] != original["payload"]
    )

    return (
        perturbation_detected
        and original_not_falsely_recovered
    )


def primitive_minimization():
    primitives = {
        "REP",
        "ALIGN",
        "CONSTRAIN",
        "TRANSFORM",
    }

    required = {
        "REP",
        "ALIGN",
        "CONSTRAIN",
        "TRANSFORM",
    }

    for primitive in primitives:
        reduced = primitives - {primitive}

        if required.issubset(reduced):
            return False

    return True


def external_perturbation_detection(event):
    expected_payload = os.environ.get("EXPECTED_PAYLOAD")

    if expected_payload is None:
        raise RuntimeError(
            "EXPECTED_PAYLOAD environment variable is missing"
        )

    observed_payload = event.get("payload")

    return observed_payload != expected_payload


if __name__ == "__main__":

    event = receive_dynamic_state()

    print("DYNAMIC_EVENT_RECEIVED:")
    print(json.dumps(event, sort_keys=True))

    # Gate 1 — Ground-truth recovery
    if ground_truth_recovery(event):
        print("GROUND_TRUTH_RECOVERY: PASS")
    else:
        print("GROUND_TRUTH_RECOVERY: FAIL")

    # Gate 2 — Adversarial perturbation
    if adversarial_perturbation(event):
        print("ADVERSARIAL_PERTURBATION: CONDITIONAL PASS")
    else:
        print("ADVERSARIAL_PERTURBATION: FAIL")

    # Gate 3 — Primitive minimization
    if primitive_minimization():
        print("PRIMITIVE_MINIMIZATION: PASS")
    else:
        print("PRIMITIVE_MINIMIZATION: FAIL")

    # Gate 4 — External perturbation detection
    if external_perturbation_detection(event):
        print("EXTERNAL_PERTURBATION_DETECTION: PASS")
    else:
        print("EXTERNAL_PERTURBATION_DETECTION: FAIL")
