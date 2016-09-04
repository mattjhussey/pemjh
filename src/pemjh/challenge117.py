""" Challenge117 """
from pemjh.numbers import numVariations


def process(blocks):
    n = numVariations(blocks, [2, 3, 4], dict())
    return n


def main():
    """ challenge117 """
    blocks = 50
    return process(blocks)
