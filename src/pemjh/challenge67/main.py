""" Challenge067 """
from pemjh.numbers import get_triangle_route_length


def main(triangles):
    """ challenge067 """
    rows = []
    for line in triangles:
        # Create a row
        vals = [int(x) for x in line.split()]
        rows.append(vals)
    return get_triangle_route_length(rows)
