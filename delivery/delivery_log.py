# =========================================================
# Ratatoskr Delivery Log
#
# Purpose:
# Maintain a history of completed
# message deliveries.
#
# Philosophy:
# Every package leaves a trail.
# =========================================================

delivery_history = []


def log_delivery(delivery_record):
    """
    Store completed delivery.
    """

    delivery_history.append(
        delivery_record
    )

    return delivery_record


def get_delivery_history():
    """
    Return delivery history.
    """

    return delivery_history