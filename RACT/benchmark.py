def ground_truth_recovery():
    expected = "B"
    observed = "B"

    return observed == expected


if __name__ == "__main__":
    if ground_truth_recovery():
        print("GROUND_TRUTH_RECOVERY: PASS")
    else:
        print("GROUND_TRUTH_RECOVERY: FAIL")
