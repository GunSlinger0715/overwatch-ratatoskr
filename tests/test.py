# =========================================================
# Historical Note
#
# The first message carried by Ratatoskr
# traveled from GateKeeper to Heimdal
# on May 30, 2026.
#
# Payload:
# {"risk": "HIGH"}
#
# Delivery Status:
# Successful
#
# The squirrel did not drop the package.
# =========================================================

from messages.messages import (
    create_message
)

from routing.routing import (
    route_message
)


message = create_message(
    source="GateKeeper",
    destination="Heimdal",
    message_type="TELEMETRY",
    payload={
        "risk": "HIGH"
    }
)

result = route_message(
    message
)

print(message)
print(result)