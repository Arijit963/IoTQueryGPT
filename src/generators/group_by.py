import random

from generators.helper import add_sample

from generators.templates import (
    GROUP_COUNT_PATTERNS,
    GROUP_AVG_PATTERNS
)

from generators.sql_templates import (
    group_by_count,
    group_by_avg
)


def generate_group_by_queries():

    dataset = []

    # ==========================================
    # COUNT BY ROOM
    # ==========================================

    for pattern in GROUP_COUNT_PATTERNS:

        query = pattern.format(
            table="sensors",
            field="room"
        )

        sql = group_by_count(
            "sensors",
            "room"
        )

        add_sample(
            dataset,
            query,
            sql
        )

    # ==========================================
    # COUNT BY STATUS
    # ==========================================

    for pattern in GROUP_COUNT_PATTERNS:

        query = pattern.format(
            table="devices",
            field="status"
        )

        sql = group_by_count(
            "devices",
            "status"
        )

        add_sample(
            dataset,
            query,
            sql
        )

    # ==========================================
    # AVG TEMPERATURE BY ROOM
    # ==========================================

    for pattern in GROUP_AVG_PATTERNS:

        query = pattern.format(
            value_field="temperature",
            group_field="room"
        )

        sql = group_by_avg(
            "sensors",
            "room",
            "temperature"
        )

        add_sample(
            dataset,
            query,
            sql
        )

    # ==========================================
    # AVG HUMIDITY BY ROOM
    # ==========================================

    for pattern in GROUP_AVG_PATTERNS:

        query = pattern.format(
            value_field="humidity",
            group_field="room"
        )

        sql = group_by_avg(
            "sensors",
            "room",
            "humidity"
        )

        add_sample(
            dataset,
            query,
            sql
        )

    random.shuffle(dataset)

    return dataset