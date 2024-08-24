""" Challenge129 """
# pylint: disable=invalid-name
from pemjh.numbers import A


def main(limit):
    """ challenge129 """
    maximum = 1
    n = limit + 1
    while maximum < limit:
        n += 2
        if n % 5 != 0:
            an = A(n)

            maximum = max(an, maximum)
    return n
