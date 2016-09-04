""" Challenge110 """
from pemjh.numbers import sievedPrimes, primeIndices


def main():
    """ challenge110 """
    target = 4000000
    primeLimit = 10000

    primes = list(sievedPrimes(primeLimit))[1:]

    # Get suitable primeIndices
    indices = primeIndices((target * 2 - 1), 0, primes, 0)

    return indices
