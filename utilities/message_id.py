# =========================================================
# Ratatoskr Message ID Generator
#
# Purpose:
# Generate unique message identifiers
# for transported intelligence.
#
# Philosophy:
# Every package deserves a tracking number.
# =========================================================

message_counter = 0


def generate_message_id():
    """
    Generate sequential message IDs.
    """

    global message_counter

    message_counter += 1

    return (
        f"MSG-{message_counter:06d}"
    )