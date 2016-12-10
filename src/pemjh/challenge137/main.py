""" Challenge137 """
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
from pemjh.function_tools import memoize


@memoize({(0,): 0, (1,): 2, (2,): 15})
def a(n):
    # From A081018
    return 8 * a(n - 1) - 8 * a(n - 2) + a(n - 3)


def main(n):
    """ challenge137 """
    return a(n)
