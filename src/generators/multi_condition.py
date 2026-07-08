import random

from generators.helper import add_sample

from generators.config import (
    STATUS,
    ROOMS
)

from generators.templates import (
    VERBS,
    MULTI_CONDITION_PATTERNS
)

from generators.sql_templates import (
    where_and
)


def generate_multi_condition_queries():

    dataset = []

    # =====================================================
    # Device Status + Battery
    # =====================================================

    battery_values = range(20, 101, 10)

    for status in STATUS:

        for battery in battery_values:

            for pattern in MULTI_CONDITION_PATTERNS[:5]:

                query = pattern.format(
                    verb=random.choice(VERBS),
                    status=status,
                    battery=battery
                )

                sql = where_and(
                    "devices",
                    [
                        ("status", "=", status, True),
                        ("battery", ">", battery, False)
                    ]
                )

                add_sample(
                    dataset,
                    query,
                    sql
                )

    # =====================================================
    # Room + Humidity
    # =====================================================

    humidity_values = range(30, 91, 10)

    for room in ROOMS:

        for humidity in humidity_values:

            for pattern in MULTI_CONDITION_PATTERNS[5:]:

                query = pattern.format(
                    verb=random.choice(VERBS),
                    room=room,
                    humidity=humidity
                )

                sql = where_and(
                    "sensors",
                    [
                        ("room", "=", room, True),
                        ("humidity", ">", humidity, False)
                    ]
                )

                add_sample(
                    dataset,
                    query,
                    sql
                )

    random.shuffle(dataset)

    return dataset