""" Challenge067 """
from pkgutil import get_data
from pemjh.numbers import get_triangle_route_length


def main():
    """ challenge067 """
    rows = []
    # Read in the file
    triangle_file = get_data(__name__, 'triangle.txt').split('\n')[:-1]
    for line in triangle_file:
        # Create a row
        vals = [int(x) for x in line.split()]
        rows.append(vals)
    return get_triangle_route_length(rows)
