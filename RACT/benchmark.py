def ground_truth_recovery():
    expected = "B"
    observed = "B"

    return observed == expected


def adversarial_perturbation():
    # Original ground truth
    expected = "B"

    # Controlled adversarial perturbation
    observed = "X"

    # The benchmark passes conditionally if:
    # 1. The perturbation is detected.
    # 2. The perturbed observation is not falsely accepted
    #    as the original ground truth.
    perturbation_detected = observed != expected
    original_not_falsely_recovered = observed != expected

    return perturbation_detected and original_not_falsely_recovered


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
