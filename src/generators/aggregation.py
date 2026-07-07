import random

from generators.helper import add_sample

from generators.sql_templates import (
    count,
    average,
    maximum,
    minimum,
    summation
)

from generators.templates import (
    COUNT_PATTERNS,
    AVG_PATTERNS,
    MAX_PATTERNS,
    MIN_PATTERNS,
    SUM_PATTERNS
)


NUMERIC_FIELDS = {

    "temperature": "sensors",

    "humidity": "sensors",

    "pressure": "sensors",

    "battery": "devices"

}


def generate_aggregation_queries():

    dataset = []

    # =====================================================
    # COUNT
    # =====================================================

    TABLES = [

        "sensors",

        "devices"

    ]

    for table in TABLES:

        for pattern in COUNT_PATTERNS:

            query = pattern.format(
                table=table
            )

            sql = count(table)

            add_sample(
                dataset,
                query,
                sql
            )

    # =====================================================
    # AVG
    # =====================================================

    for field, table in NUMERIC_FIELDS.items():

        for pattern in AVG_PATTERNS:

            query = pattern.format(
                field=field
            )

            sql = average(
                table,
                field
            )

            add_sample(
                dataset,
                query,
                sql
            )

    # =====================================================
    # MAX
    # =====================================================

    for field, table in NUMERIC_FIELDS.items():

        for pattern in MAX_PATTERNS:

            query = pattern.format(
                field=field
            )

            sql = maximum(
                table,
                field
            )

            add_sample(
                dataset,
                query,
                sql
            )

    # =====================================================
    # MIN
    # =====================================================

    for field, table in NUMERIC_FIELDS.items():

        for pattern in MIN_PATTERNS:

            query = pattern.format(
                field=field
            )

            sql = minimum(
                table,
                field
            )

            add_sample(
                dataset,
                query,
                sql
            )

    # =====================================================
    # SUM
    # =====================================================

    for field, table in NUMERIC_FIELDS.items():

        for pattern in SUM_PATTERNS:

            query = pattern.format(
                field=field
            )

            sql = summation(
                table,
                field
            )

            add_sample(
                dataset,
                query,
                sql
            )

    random.shuffle(dataset)

    return dataset