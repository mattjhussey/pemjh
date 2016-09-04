""" Challenge072 """
from pemjh.numbers import phi


def main():
    """ challenge072 """
    limit = 1000000
    return int(sum(phi(limit)) - 1)
