# ==========================================================
# Basic WHERE Queries
# ==========================================================

def where_numeric(table, field, operator, value):
    return (
        f"SELECT * FROM {table} "
        f"WHERE {field} {operator} {value};"
    )


def where_string(table, field, value):
    return (
        f"SELECT * FROM {table} "
        f"WHERE {field} = '{value}';"
    )


# ==========================================================
# Aggregation Queries
# ==========================================================

def count(table):
    return (
        f"SELECT COUNT(*) FROM {table};"
    )


def average(table, field):
    return (
        f"SELECT AVG({field}) FROM {table};"
    )


def maximum(table, field):
    return (
        f"SELECT MAX({field}) FROM {table};"
    )


def minimum(table, field):
    return (
        f"SELECT MIN({field}) FROM {table};"
    )


def summation(table, field):
    return (
        f"SELECT SUM({field}) FROM {table};"
    )


# ==========================================================
# ORDER BY
# ==========================================================

def order_by(table, field, descending=True, limit=None):

    sql = f"SELECT * FROM {table}"

    sql += f" ORDER BY {field}"

    sql += " DESC" if descending else " ASC"

    if limit is not None:
        sql += f" LIMIT {limit}"

    sql += ";"

    return sql