import json
import os
import time
import uuid


def receive_event():
    raw = os.environ.get("RACT_EVENT")

    if not raw:
        raise RuntimeError("No RACT_EVENT received")

    event = json.loads(raw)

    return event


def process_event(event):
    return {
        "event_id": event["event_id"],
        "received_at": time.time(),
        "source": "sandbox",
        "payload": event["payload"],
    }


if __name__ == "__main__":
    event = receive_event()
    response = process_event(event)

    print(
        "SANDBOX_RESPONSE:",
        json.dumps(response, sort_keys=True)
    )
