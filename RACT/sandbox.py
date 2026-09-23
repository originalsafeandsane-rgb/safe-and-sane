import json
import os
import uuid


def receive_event():
    raw = os.environ.get("RACT_EVENT")

    if raw is None:
        raise RuntimeError("RACT_EVENT environment variable is missing")

    return json.loads(raw)


def run_iteration(state, iteration):
    return {
        "iteration": iteration,
        "previous_event_id": state["event_id"],
        "sandbox_event_id": str(uuid.uuid4()),
        "payload": state["payload"],
        "state": "state-" + str(iteration),
        "source": "sandbox",
    }


if __name__ == "__main__":

    event = receive_event()

    print("SANDBOX_INITIAL_EVENT:")
    print(json.dumps(event, sort_keys=True))

    state = {
        "event_id": event["event_id"],
        "payload": event["payload"],
    }

    for iteration in range(1, 11):

        state = run_iteration(state, iteration)

        print("SANDBOX_ITERATION:")
        print(json.dumps(state, sort_keys=True))

    print("SANDBOX_ITERATIONS_COMPLETED: 10")

