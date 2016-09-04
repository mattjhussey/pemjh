""" Challenge114 """
from pemjh.numbers import num_variations


def process(blocks):
    n = num_variations(blocks + 1, range(4, blocks + 2), dict())
    return n


def main():
    """ challenge114 """
    blocks = 50
    return process(blocks)
