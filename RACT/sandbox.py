import json
import os
import uuid


def receive_event():
    raw = os.environ.get("RACT_EVENT")

    if raw is None:
        raise RuntimeError("RACT_EVENT environment variable is missing")

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


if __name__ == "__main__":
    iteration = int(os.environ.get("RACT_ITERATION", "1"))

    event = receive_event()

    print("SANDBOX_RECEIVED:")
    print(json.dumps(event, sort_keys=True))

    new_state = process_event(event, iteration)

    print("SANDBOX_GENERATED:")
    print(json.dumps(new_state, sort_keys=True))

    # Return the new state to GitHub Actions.
    github_output = os.environ.get("GITHUB_OUTPUT")

    if github_output:
        with open(github_output, "a") as output:
            output.write(
                "next_event="
                + json.dumps(new_state)
                + "\n"
            )

