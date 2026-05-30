from messages.messages import (
    create_message
)

message = create_message(
    source="GateKeeper",
    destination="Heimdal",
    message_type="TELEMETRY",
    payload={
        "risk": "HIGH"
    }
)

print(message)