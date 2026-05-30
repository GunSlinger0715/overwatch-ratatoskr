# =========================================================
# Ratatoskr Routing Engine
#
# Purpose:
# Route messages between OVERWATCH
# subsystems.
#
# Philosophy:
# Every message has a destination.
# =========================================================


def route_message(message):
    """
    Route a message to its destination.
    """

    destination = message.get(
        "destination",
        "UNKNOWN"
    )

    return (
        f"Message delivered to "
        f"{destination}"
    )