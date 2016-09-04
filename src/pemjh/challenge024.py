""" Challenge024 """
from itertools import islice
from pemjh.numbers import permutate


def main():
    """ challenge024 """
    number = "0123456789"
    return int(list(islice(permutate(number), 999999, 1000000))[0])
