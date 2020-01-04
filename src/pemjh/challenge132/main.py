""" Challenge132 """
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
from pemjh.numbers import sieved_primes


def R(k):
    primes = sieved_primes(160002)
    next(primes)
    next(primes)

    facts = list()

    while len(facts) != 40:
        p = next(primes)
        if pow(10, k, 9*p) == 1:
            facts.append(p)

    return facts


def main():
    """ challenge132 """
    return sum(R(10**9)[:40])
