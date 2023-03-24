""" Challenge082 """
from __future__ import with_statement
from functools import reduce


def combine_columns(column1, column2):
    """ Combine the two rows to find the cheapest route. """
    down_row = []

    # Step through column2
    previous = None
    for column1_value, column2_value in zip(column1, column2):
        possibles = []
        if previous is not None:
            possibles.append(previous + column2_value)
        # The straight route is column1_value, column2_value
        possibles.append(column1_value + column2_value)

        lowest = min(possibles)
        previous = lowest

        down_row.append(lowest)

    new_row = []

    previous = None
    for down_row_value, column2_value in zip(reversed(down_row),
                                             reversed(column2)):
        possibles = []
        if previous is not None:
            possibles.append(previous + column2_value)
        possibles.append(down_row_value)

        lowest = min(possibles)
        previous = lowest

        new_row.append(lowest)

    return list(reversed(new_row))


def main(rows):
    """ challenge082 """
    # Read row data
    rows = [[int(i) for i in row.strip().split(",")] for row in rows]
    # Convert to columns
    columns = [list(row) for row in zip(*rows)]
    # Reduce the columns
    return min(reduce(combine_columns, columns))
