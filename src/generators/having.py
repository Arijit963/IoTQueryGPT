import random

from generators.helper import add_sample

from generators.templates import (
    HAVING_PATTERNS
)

from generators.sql_templates import (
    having_count
)


def generate_having_queries():

    dataset = []

    thresholds = [2, 5, 10, 20]

    for threshold in thresholds:

        for pattern in HAVING_PATTERNS:

            query = pattern.format(
                group_field="rooms",
                threshold=threshold
            )

            sql = having_count(
                "sensors",
                "room",
                threshold
            )

            add_sample(
                dataset,
                query,
                sql
            )

    random.shuffle(dataset)

    return dataset