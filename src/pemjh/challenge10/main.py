""" Challenge10 """
from math import sqrt


def main(limit):
    """ challenge10 """
    primes = [True] * limit
    for i in range(2, int(sqrt(limit)) + 1):
        if primes[i - 1]:
            for j in range(i**2 - 1, limit, i):
                primes[j] = False

    return sum(i + 1 for i, b in enumerate(primes) if b) - 1
