""" Challenge187 """
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
from pemjh.numbers import sieved_primes


def semiprimes(n):
    primes = list(sieved_primes(n // 2))[1:]
    nPrimes = len(primes)

    nTwos = 0
    for i in xrange(nPrimes):
        for j in xrange(i, nPrimes):
            if primes[i] * primes[j] >= n:
                break
            nTwos += 1

    return nTwos


def main():
    """ challenge187 """
    return semiprimes(10**8)
