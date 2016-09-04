""" Challenge114 """
from pemjh.numbers import numVariations


def process(blocks):
    n = numVariations(blocks + 1, range(4, blocks + 2), dict())
    return n


def main():
    """ challenge114 """
    blocks = 50
    return process(blocks)
