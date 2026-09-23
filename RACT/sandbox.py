
import json
import os
import time
import uuid


def receive_event():
    raw = os.environ.get("RACT_EVENT")

    if not raw:
        raise RuntimeError("No RACT_EVENT received")

    return json.loads(raw)


def iterate_state(state, iteration):
    return {
        "iteration": iteration,
        "previous_event_id": state["event_id"],
        "sandbox_event_id": str(uuid.uuid4()),
        "timestamp": time.time(),
        "payload": state["payload"],
        "state": f"state-{iteration}",
        "source": "sandbox",
    }


def run_iteration(initial_event, iterations=10):
    state = {
        "event_id": initial_event["event_id"],
        "payload": initial_event["payload"],
    }

    history = []

    for iteration in range(1, iterations + 1):
        state = iterate_state(state, iteration)
        history.append(state.copy())

        print(
            "SANDBOX_ITERATION:",
            json.dumps(state, sort_keys=True)
        )

    return history


if __name__ == "__main__":
    initial_event = receive_event()

    print(
        "SANDBOX_INITIAL_EVENT:",
        json.dumps(initial_event, sort_keys=True)
    )

    history = run_iteration(initial_event, iterations=10)

    print(
        "SANDBOX_ITERATIONS_COMPLETED:",
        len(history)
    )
