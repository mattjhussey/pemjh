""" Challenge130 """
from pemjh.numbers import sieved_primes, A


def main():
    """ challenge130 """
    limit = 14702  # Optimised value
    primes = set(sieved_primes(limit))

    found = []

    for n in [n for n in xrange(5, limit, 2)
              if (n % 5 != 0) and n not in primes]:
        if (n-1) % A(n) == 0:
            found.append(n)

    return sum(found)
