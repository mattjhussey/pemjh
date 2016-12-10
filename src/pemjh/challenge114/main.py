""" Challenge114 """
from pemjh.numbers import get_num_variations


def main(blocks):
    """ challenge114 """
    return get_num_variations(blocks + 1, range(4, blocks + 2), dict())
