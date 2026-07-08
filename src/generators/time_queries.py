import random

from generators.helper import add_sample

from generators.templates import (
    LAST_HOUR_PATTERNS,
    LAST_DAY_PATTERNS,
    TODAY_PATTERNS,
    LAST_WEEK_PATTERNS
)

from generators.sql_templates import (
    last_hour_query,
    last_day_query,
    today_query,
    last_week_query
)


def generate_time_queries():

    dataset = []

    # =====================================================
    # Last Hour
    # =====================================================

    for pattern in LAST_HOUR_PATTERNS:

        add_sample(
            dataset,
            pattern,
            last_hour_query()
        )

    # =====================================================
    # Last Day
    # =====================================================

    for pattern in LAST_DAY_PATTERNS:

        add_sample(
            dataset,
            pattern,
            last_day_query()
        )

    # =====================================================
    # Today
    # =====================================================

    for pattern in TODAY_PATTERNS:

        add_sample(
            dataset,
            pattern,
            today_query()
        )

    # =====================================================
    # Last Week
    # =====================================================

    for pattern in LAST_WEEK_PATTERNS:

        add_sample(
            dataset,
            pattern,
            last_week_query()
        )

    random.shuffle(dataset)

    return dataset