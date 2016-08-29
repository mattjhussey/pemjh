""" Challenge002 """
from itertools import takewhile
from pemjh.numbers import fibo


def main(limit):
    """ challenge002 """
    number_range = takewhile(lambda i: i < limit, fibo())
    even_numbers = (i for i in number_range if i % 2 == 0)
    return sum(even_numbers)
