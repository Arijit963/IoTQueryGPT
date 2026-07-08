import random

from generators.helper import add_sample

from generators.config import (
    NUMERIC_FIELDS
)

from generators.templates import (
    BETWEEN_PATTERNS
)

from generators.sql_templates import (
    between_query
)


def generate_between_queries():

    dataset = []

    for field, info in NUMERIC_FIELDS.items():

        table = info["table"]

        minimum = info["min"]

        maximum = info["max"]

        step = info["step"]

        ranges = []

        current = minimum

        while current + 20 <= maximum:

            ranges.append(
                (
                    current,
                    current + 20
                )
            )

            current += (
                step * 5
            )

        for lower, upper in ranges:

            for pattern in BETWEEN_PATTERNS:

                query = pattern.format(
                    table=table,
                    field=field,
                    lower=lower,
                    upper=upper
                )

                sql = between_query(
                    table,
                    field,
                    lower,
                    upper
                )

                add_sample(
                    dataset,
                    query,
                    sql
                )

    random.shuffle(dataset)

    return dataset