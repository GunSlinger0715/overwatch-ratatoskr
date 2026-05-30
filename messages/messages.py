from utilities.message_id import (
    generate_message_id
)

# =========================================================
# Ratatoskr Message Model
#
# Purpose:
# Define standardized messages that
# move between OVERWATCH subsystems.
#
# Philosophy:
# Observe.
# Carry.
# Deliver.
# Connect.
# =========================================================

from datetime import datetime


def create_message(
    source,
    destination,
    message_type,
    payload
):
    """
    Create a standardized message.
    """

    return {
        "message_id": generate_message_id(),
        "source": source,
        "destination": destination,
        "message_type": message_type,
        "payload": payload,
        "timestamp": (
            datetime.utcnow().isoformat()
        )
    }