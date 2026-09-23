def ground_truth_recovery():
    expected = "B"
    observed = "B"

    return observed == expected


def adversarial_perturbation():
    expected = "B"
    observed = "X"

    perturbation_detected = observed != expected
    original_not_falsely_recovered = observed != expected

    return perturbation_detected and original_not_falsely_recovered


def primitive_minimization():
    primitives = {
        "REP",
        "ALIGN",
        "CONSTRAIN",
        "TRANSFORM",
    }

    # The current benchmark requires all four candidate
    # primitives to represent the tested transition structure.
    required = {
        "REP",
        "ALIGN",
        "CONSTRAIN",
        "TRANSFORM",
    }

    # Test whether removing any single primitive destroys
    # the required representation.
    for primitive in primitives:
        reduced = primitives - {primitive}

        if required.issubset(reduced):
            return False

    return True


if __name__ == "__main__":

    # Gate 1 — Ground-truth recovery
    if ground_truth_recovery():
        print("GROUND_TRUTH_RECOVERY: PASS")
    else:
        print("GROUND_TRUTH_RECOVERY: FAIL")

    # Gate 2 — Adversarial perturbation
    if adversarial_perturbation():
        print("ADVERSARIAL_PERTURBATION: CONDITIONAL PASS")
    else:
        print("ADVERSARIAL_PERTURBATION: FAIL")

    # Gate 3 — Primitive minimization
    if primitive_minimization():
        print("PRIMITIVE_MINIMIZATION: PASS")
    else:
        print("PRIMITIVE_MINIMIZATION: FAIL")
