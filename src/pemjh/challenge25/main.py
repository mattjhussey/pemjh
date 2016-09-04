""" Challenge025 """
from itertools import dropwhile
from pemjh.numbers import fibo


def main():
    """ challenge025 """
    return dropwhile(lambda x: len(str(x[1])) < 1000,
                     enumerate(fibo(), start=1)).next()[0]
