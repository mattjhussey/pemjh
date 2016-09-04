""" Challenge132 """
from pemjh.numbers import sieved_primes


def R(k):
    primes = sieved_primes(160002)
    primes.next()
    primes.next()

    facts = list()

    for p in primes:
        if pow(10, k, 9*p) == 1:
            facts.append(p)
            if len(facts) == 40:
                break

    return facts


def main():
    """ challenge132 """
    return sum(R(10**9)[:40])
