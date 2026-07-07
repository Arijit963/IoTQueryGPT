import random
from generators.helper import add_sample
from generators.sql_templates import where_string
from generators.config import (
    STATUS,
    ROOMS,
    LOCATIONS
)

from generators.templates import (
    VERBS,
    STATUS_PATTERNS,
    ROOM_PATTERNS,
    LOCATION_PATTERNS
)

from generators.helper import make_instruction


def generate_categorical_queries():
    """
    Generate instruction tuning samples for
    categorical IoT fields.

    Supports:
        - Device Status
        - Rooms
        - Locations
    """

    dataset = []

    # =====================================================
    # Device Status
    # =====================================================

    for status in STATUS:

        for pattern in STATUS_PATTERNS:

            query = pattern.format(
                verb=random.choice(VERBS),
                status=status
            )

            sql = where_string("devices", "status", status)
                

            add_sample(
                dataset,
                query,
                sql
            )

    # =====================================================
    # Room Queries
    # =====================================================

    for room in ROOMS:

        for pattern in ROOM_PATTERNS:

            query = pattern.format(
                verb=random.choice(VERBS),
                room=room
            )

            sql =  where_string("sensors", "room", room)
                

            add_sample(
                dataset,
                query,
                sql
            )

    # =====================================================
    # Location Queries
    # =====================================================

    for location in LOCATIONS:

        for pattern in LOCATION_PATTERNS:

            query = pattern.format(
                verb=random.choice(VERBS),
                location=location
            )

            sql = where_string("devices", "location", location)

            add_sample(
                dataset,
                query,
                sql
            )

    random.shuffle(dataset)

    return dataset