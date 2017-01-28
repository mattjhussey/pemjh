""" Challenge015 """
from math import factorial


def get_routes(grid_size):
    """
    >>> get_routes(2)
    6
    """
    # Work out the row
    row = grid_size * 2
    # Get mid point of row
    midpoint = grid_size

    return factorial(row) / (factorial(midpoint)**2)


def main():
    """ challenge015 """
    return get_routes(20)
