import random


# ==========================================================
# Random Utilities
# ==========================================================

def random_choice(items):
    """
    Return a random element from a list.
    """
    return random.choice(items)


# ==========================================================
# Dataset Formatting
# ==========================================================

def make_instruction(query, sql):
    """
    Convert a query-SQL pair into
    instruction tuning format.
    """

    return f"""### Instruction:
Convert the following IoT query into SQL.

### Input:
{query}

### Response:
{sql}
"""


def add_sample(dataset, query, sql):
    """
    Format a sample and append it to the dataset.
    """

    dataset.append(
        make_instruction(query, sql)
    )


# ==========================================================
# Dataset Utilities
# ==========================================================

def shuffle_dataset(dataset):
    """
    Shuffle dataset in-place.
    """

    random.shuffle(dataset)


def save_dataset(dataset, output_file):
    """
    Shuffle and save dataset.
    """

    shuffle_dataset(dataset)

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write("\n".join(dataset))