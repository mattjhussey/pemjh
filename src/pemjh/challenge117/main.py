""" Challenge117 """
from pemjh.numbers import num_variations


def process(blocks):
    n = num_variations(blocks, [2, 3, 4], dict())
    return n


def main():
    """ challenge117 """
    blocks = 50
    return process(blocks)
