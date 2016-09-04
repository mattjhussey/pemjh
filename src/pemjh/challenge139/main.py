""" Challenge139 """
from pemjh.numbers import get_primitive_triples


def main():
    """ challenge139 """
    maximum_size = 100000000

    total = 0
    for a, b, c in get_primitive_triples(maximum_size):

        if c % (b - a) == 0:
            # Fills...
            total += maximum_size // (a + b + c)

    return total
