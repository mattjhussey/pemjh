""" Challenge114 """
from pemjh.numbers import num_variations


def main(blocks):
    """ challenge114 """
    return num_variations(blocks + 1, range(4, blocks + 2), dict())
