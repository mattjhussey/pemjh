""" Challenge123 """
from pemjh.numbers import sieved_primes


def getRemainder(p, n):
    return 2 * (n + 1) * p


def main():
    """ challenge123 """
    primes = list(sieved_primes(250000))
    limit = 10**10
    for n in xrange(7038, len(primes), 2):
        p = primes[n]
        r = getRemainder(p, n)
        if r > limit:
            return n + 1
        n += 1
    return
