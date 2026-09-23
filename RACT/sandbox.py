import json
import os
import uuid


def receive_event():
    raw = os.environ.get("RACT_EVENT")

    if raw is None:
        raise RuntimeError("RACT_EVENT environment variable is missing")

    return json.loads(raw)


def run_iteration(state, iteration):
    previous_event_id = state["event_id"]

    new_event_id = str(uuid.uuid4())

    return {
        "event_id": new_event_id,
        "previous_event_id": previous_event_id,
        "iteration": iteration,
        "payload": state["payload"],
        "state": "state-" + str(iteration),
        "source": "sandbox",
    }


if __name__ == "__main__":

    initial_event = receive_event()

    print("SANDBOX_INITIAL_EVENT:")
    print(json.dumps(initial_event, sort_keys=True))

    # Normalize the external GitHub event into the
    # sandbox's internal event schema.
    state = {
        "event_id": initial_event["event_id"],
        "payload": initial_event["payload"],
    }

    for iteration in range(1, 11):

        state = run_iteration(state, iteration)

        print("SANDBOX_ITERATION:")
        print(json.dumps(state, sort_keys=True))

    print("SANDBOX_ITERATIONS_COMPLETED: 10")

