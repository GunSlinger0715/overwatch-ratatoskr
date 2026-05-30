from delivery.delivery_tracker import (
    track_delivery
)

from delivery.delivery_log import (
    log_delivery,
    get_delivery_history
)


delivery = track_delivery(
    message_id="MSG-000001",
    source="GateKeeper",
    destination="Heimdal"
)

log_delivery(
    delivery
)

print(
    get_delivery_history()
)